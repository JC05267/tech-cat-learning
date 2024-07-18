# Mini Project

## DDL
```SQL
CREATE OR REPLACE TRANSIENT TABLE techcatalyst_de.jc.SONGS_DIM (
    song_id VARCHAR,
    title VARCHAR,
    artist_id VARCHAR,
    year INT,
    duration FLOAT
);

CREATE OR REPLACE TRANSIENT TABLE techcatalyst_de.jc.USER_DIM (
    user_id INT,
    first_name VARCHAR,
    last_name VARCHAR,
    gender VARCHAR,
    level VARCHAR
);

CREATE OR REPLACE TRANSIENT TABLE techcatalyst_de.jc.TIME_DIM (
    datetime TIMESTAMP,
    start_time TIME,    
    hour INT, 
    day INT, 
    week INT, 
    month INT, 
    year INT, 
    weekday VARCHAR
);

CREATE OR REPLACE TRANSIENT TABLE techcatalyst_de.jc.ARTIST_DIM (
    artist_id VARCHAR,
    name VARCHAR,
    location VARCHAR,
    lattitude FLOAT,
    longitude FLOAT
);
```

## Diagram
![png](./diagram.png)

## Data Lake and Data Warehouse Purpose
### Data Lake
Our data lake provides a central place to dump all of the json (semi-structured) data that Sparkify produces.
Because S3 is schema-less, it allows our logs and other data to change over time, while still being written to the same place.
We can also leverage tools like Athena to get a quick understanding of the general shape of this data.

### Data Warehouse
The data warehouse converts the semi-structured data in our data lake to structured data.
Coupled with the star schema in our data warehouse allows for easy querying. 
Moreover, snowflake is optimized for large analytics meaning Sparkify will be able to scale their company without fear of running out of room.

## Database Schema Design/ ETL Pipeline design justification
Our schema is a basic star schema which allows for easy and fast analysis.
The goal is to minimize complex joins and allow analysts easy access to all the data.

The ETL pipeline design focuses on simplicity and accessibility.
The data lake will allow Sparkify to trivially build new services on top of their data because the raw data is still available. 
Moreover, with a continued loading, analysts will have access to all the data that flows into the data lake.
This will make gleaning insights from their data much easier.

## Process Summary
The basic process is well described in the diagram.
We load the raw json data from the initial s3 bucket.
Then in databricks, we perform the necessary logic and create our data lake.
It was at this point we discovered that the newer version of spark appears to be writing additional metadata that snowflake and glue are unprepared to handle.
As such, using glue was untenable without extensive filtering of file paths.
We were able to load the data into snowflake after ignoring the errors related to the improperly read files.
From there we performed some basic data validation.
