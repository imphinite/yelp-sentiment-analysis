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
python scripts/split_data.py
```

## Create docker image and run docker container (Skip if you already have a MySQL instance running)
```
cd data_preprocessing && docker build -t mysql-yelp .
```

```
docker run -p 3306:3306 --name mysql-yelp-container -d mysql-yelp
```

This will host a MySQL instance on port 3306.

## Prepare env
```
cp .env.example .env
```

By default, the docker image provided will use localhost:3306 uroot psecret, and database is yelp_sentiment_analysis.

## Hydrate reviews table using the splitted data
```
python scripts/hydrate_reviews_table.py
```

## Lemmatize the reviews
```
python scripts/lemmatize_reviews_text.py
```
