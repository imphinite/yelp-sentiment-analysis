# Use an official MySQL runtime as a parent image
FROM mysql:latest

# Set the root password for MySQL
ENV MYSQL_ROOT_PASSWORD secret

# Create a new database
ENV MYSQL_DATABASE yelp_sentiment_analysis

# Set the character set and collation for the new database
ENV MYSQL_CHARSET utf8mb4
ENV MYSQL_COLLATION utf8mb4_unicode_ci

# Copy raw data into the container
COPY ./data/chunks/chunk_1.json /tmp/

# Copy the initialization SQL script into the container
ADD ./init.sql /docker-entrypoint-initdb.d/
# COPY ./insert_chunks.sql /docker-entrypoint-initdb.d/

# modify CMD to run script after starting MySQL
# CMD ["sh", "-c", "mysql -uroot -p$MYSQL_ROOT_PASSWORD < /docker-entrypoint-initdb.d/init.sql"]


# CMD service mysql start

# Expose port 3306 for MySQL connections
# EXPOSE 3306
