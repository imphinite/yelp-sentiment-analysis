USE yelp_sentiment_analysis;

CREATE TABLE reviews (
    id INT NOT NULL AUTO_INCREMENT,
    review_id CHAR(22) UNIQUE NOT NULL,
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

CREATE TABLE lemmatized_reviews (
    id INT NOT NULL AUTO_INCREMENT,
    review_id INTEGER REFERENCES reviews (id),
    lemmatized_text TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);
