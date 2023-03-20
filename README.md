# Yelp Sentiment Analysis
Research project for study sentiment analysis using yelp research data

# Data Preprocessing
The original `yelp_academic_dataset_review.json` is too big to be processed directly in memory. The file is so big that a normal text editor cannot open it to inspect samples. Therefore, it is necessary to split the raw data into smaller chunks to facilitate further processing.

## Before preprocessing
You will need the `yelp_academic_dataset_review.json` to be in the correct direct for the script to find it.

### Required python packages
```
pip install mysql-connector-python python-dotenv tqdm linecache2
```

### Required file
Place `yelp_academic_dataset_review.json` under `data_preprocessing/data/`

## Split raw json data into chunks
```
python 
```
