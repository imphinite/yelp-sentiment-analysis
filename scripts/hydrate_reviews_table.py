import sys
import os
import subprocess
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from tqdm import tqdm
from utils.db_connection import conn


current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Set path to directory containing JSON data chunks
data_dir = os.path.join(parent_dir, "data_preprocessing/data/chunks")

# Define function to import data from a JSON file into MySQL
def import_data(filename, cnx, batch_size=2):
    result = subprocess.run(['wc', '-l', filename], capture_output=True, text=True)
    total_lines = int(result.stdout.split()[0])

    # Open JSON file
    with open(filename, "r") as f:
        # Prepare rows for insertion
        rows = []
        count = 0

        # Loop through data and insert into MySQL
        pbar = tqdm(total=total_lines, desc="Importing data from " + filename)
        for line in f:
            # Parse JSON data
            d = json.loads(line)

            row = (
                d["review_id"],
                d["user_id"],
                d["business_id"],
                d["stars"],
                d.get("useful", 0),
                d.get("funny", 0),
                d.get("cool", 0),
                d.get("text", ""),
                d.get("date", "")
            )
            rows.append(row)
            count += 1


            # Insert into database if batch is full
            if (count % batch_size == 0):
                # Create cursor
                cursor = cnx.cursor()

                # Insert rows in batches of 1000(default)
                for i in range(0, len(rows), batch_size):
                    batch = rows[i:i+batch_size]
                    query = "INSERT INTO reviews (review_id, user_id, business_id, stars, useful, funny, cool, text, date) VALUES %s"
                    cursor.executemany(query, batch[1:-1])
                

                pbar.update(len(rows))

                rows = []

                 
    # Commit changes to database
    cnx.commit()

    # Close cursor
    cursor.close()


def run():
    db = conn()

    # Loop through JSON data chunks and import data into MySQL
    for i in range(1, 15):
        filename = os.path.join(data_dir, f"chunk_{i}.json")
        if os.path.exists(filename):
            import_data(filename, db)

    # Close conn
    db.close()


if __name__ == '__main__':
    run()
