import sys
import os
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import linecache
from tqdm import tqdm
from utils import paths
from utils.db_connection import conn


# Define function to import data from a JSON file into MySQL
def import_data(filename, cnx, batch_size=1000):    
    total_lines = len(linecache.getlines(filename))

    # Open JSON file
    with open(filename, "r", encoding='utf-8') as f:
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
                d.get("stars", 0.0),
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
                    query = """
                        INSERT INTO reviews (review_id, user_id, business_id, stars, useful, funny, cool, text, date)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    
                    cursor.executemany(query, batch)

                    break

                pbar.update(len(rows))

                rows = []

    # Commit changes to database
    cnx.commit()

    # Close cursor
    cursor.close()


def run():
    db = conn()

    # Loop through JSON data chunks and import data into MySQL
    for i in range(2, 15):
        filename = os.path.join(paths.data_chunks_dir, f"chunk_{i}.json")
        if os.path.exists(filename):
            import_data(filename, db)

    # Close conn
    db.close()


if __name__ == '__main__':
    run()
