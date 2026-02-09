##create warehouse
CREATE WAREHOUSE hotel_wh
WITH WAREHOUSE_SIZE = 'XSMALL'
AUTO_SUSPEND = 60
AUTO_RESUME = TRUE;

USE WAREHOUSE hotel_wh;

##CREATE DB and SCHEMA
CREATE DATABASE hotel_db;
USE DATABASE hotel_db;

CREATE SCHEMA raw;
CREATE SCHEMA analytics;

##CREATE TABLE
CREATE TABLE analytics.hotels_cleaned (
    hotel_id STRING,
    hotel_name STRING,
    city STRING,
    date DATE,
    price NUMBER,
    availability BOOLEAN
);

##CREATE S# STORAGE INTEGRATION
USE ROLE ACCOUNTADMIN;

CREATE OR REPLACE STORAGE INTEGRATION s3_int_hotels
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = S3
ENABLED = TRUE
STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::699155485535:role/snowflake_s3_role'
STORAGE_ALLOWED_LOCATIONS = ('s3://hotel-etl-portfolio-ds/curated/');

##CHECKING INTEGRATION DETAILS
DESC INTEGRATION s3_int_hotels;


##CREATING FILE FORMAT
 USE DATABASE hotel_db;
USE SCHEMA analytics;

CREATE OR REPLACE FILE FORMAT ff_hotels_csv
TYPE = CSV
SKIP_HEADER = 1
FIELD_OPTIONALLY_ENCLOSED_BY = '"'
EMPTY_FIELD_AS_NULL = TRUE;

##CREATING EXTERNAL STAGE(SNOWFLAKE --> S3)
CREATE OR REPLACE STAGE stg_hotels_curated
URL = 's3://hotel-etl-portfolio-ds/curated/mock_hotels_cleaned/'
STORAGE_INTEGRATION = s3_int_hotels
FILE_FORMAT = ff_hotels_csv;

LIST @stg_hotels_curated;

## LOADING DATA INTO SNOWFLAKE TABLE
TRUNCATE TABLE analytics.hotels_cleaned;

COPY INTO analytics.hotels_cleaned
FROM @stg_hotels_curated
FILES = ('cleaned_hotels.csv')
ON_ERROR = 'ABORT_STATEMENT';

SELECT COUNT(*) FROM analytics.hotels_cleaned;
SELECT * FROM analytics.hotels_cleaned LIMIT 10;


