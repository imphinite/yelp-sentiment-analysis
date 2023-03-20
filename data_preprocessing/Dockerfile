# Use an official MySQL runtime as a parent image
FROM mysql:latest

# Set the root password for MySQL
ENV MYSQL_ROOT_PASSWORD secret

# Create a new database
ENV MYSQL_DATABASE yelp_sentiment_analysis

# Set the character set and collation for the new database
ENV MYSQL_CHARSET utf8mb4
ENV MYSQL_COLLATION utf8mb4_unicode_ci

# Copy the initialization SQL script into the container
ADD ./init.sql /docker-entrypoint-initdb.d/
