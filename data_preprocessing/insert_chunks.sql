USE yelp_sentiment_analysis;

SET autocommit=0;

START TRANSACTION;

-- loop through all 14 chunks of data
SET @i = 1;
WHILE @i <= 14 DO
    SET @file_path = CONCAT('/tmp/chunk_', @i, '.json');

    -- insert data from current chunk file
    LOAD DATA INFILE @file_path
    INTO TABLE reviews
    FIELDS TERMINATED BY ',' 
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;

    SET @i = @i + 1;
END WHILE;

COMMIT;
