import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from tqdm import tqdm
from utils.db_connection import conn

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))


def lemmatize_text(raw_text):
    # Create an instance of the WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()

    # Lemmatize
    text = raw_text.lower()
    text = ''.join([char for char in text if char.isalnum() or char.isspace()])
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)


def bulk_save_result(cnx, data):
    # Create cursor
    cursor = cnx.cursor()
    
    query = """
        INSERT INTO lemmatized_reviews (review_id, lemmatized_text)
        VALUES (%s, %s)
    """

    cursor.executemany(query, data)

    # Commit changes to database
    cnx.commit()

    cursor.close()


def bulk_retrieve(cnx, bulk_size=1000, offset=0):
    cursor = cnx.cursor()

    # Query
    query = """
        SELECT id, text FROM reviews
        LIMIT %s
        OFFSET %s
    """
    # Execute the SQL query
    cursor.execute(query, (bulk_size, offset))

    # Retrieve the results
    results = cursor.fetchall()

    cursor.close()

    return results

def get_count(cnx):
    cursor = cnx.cursor()

    query = """
        SHOW TABLE STATUS LIKE 'reviews';
    """
    # Execute the SQL query
    cursor.execute(query)

    # Fetch the result
    count = cursor.fetchone()[4]

    cursor.close()

    return count


def run():
    db = conn()

    # Get total records
    total_records = get_count(db)

    pbar = tqdm(total=total_records)

    # Process data in bulks
    bulk_size = 1000
    offset = 0

    # # loop_ctrl for debugging
    # loop_ctrl = 0

    # For each bulk_size data
    while offset < total_records:
        # Retrieve raw data
        raw_data = bulk_retrieve(db, bulk_size, offset)

        result = []
        for row in raw_data:
            review_id = row[0]
            review_text = row[1]

            # Lemmatize text
            lemmatized_text = lemmatize_text(review_text)

            # Create lemmatized record for insert
            lemmatized_record = (review_id, lemmatized_text)
            result.append(lemmatized_record)

        # Bulk insert
        bulk_save_result(db, result)

        # Update offset
        offset = offset + bulk_size

        pbar.update(bulk_size)

        # loop_ctrl += 1
        # if (loop_ctrl > 2):
        #     break
    
    # Close conn
    db.close()


if __name__ == "__main__":
    run()
