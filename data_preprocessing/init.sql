USE yelp_sentiment_analysis;

CREATE TABLE reviews (
    id INT NOT NULL AUTO_INCREMENT,
    review_id CHAR(22) NOT NULL,
    user_id CHAR(22) NOT NULL,
    business_id CHAR(22) NOT NULL,
    stars FLOAT DEFAULT 0,
    useful INT DEFAULT 0,
    funny INT DEFAULT 0,
    cool INT DEFAULT 0,
    text TEXT,
    date DATETIME,
    PRIMARY KEY (id)
);

SET autocommit=0;

-- import data from JSON files
LOAD DATA INFILE '/tmp/chunk_1.json' INTO TABLE reviews;

COMMIT;

SET autocommit=1;
