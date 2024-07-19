# Apache Software

## Apache Spark
- analytics engine for large-scale data processing. 
- interface for programming clusters with implicit data parallelism and fault tolerance. 
- in memory so it is fast 

## Apache Hadoop
- framework for distributed storage and processing of large datasets using the MapReduce programming model. 
- Two main components: 
    1. Hadoop Distributed File System (HDFS) (storage)
    2. MapReduce engine (processing)

## Apache Pig
- high-level platform for creating programs that run on Hadoop
- high-level scripting language, Pig Latin
    - for expressing data analysis programs: translated into MapReduce jobs to be executed by Hadoop

## Apache Hue
- SQL Assistant for Databases & Data Warehouses 
- web-based interface that allows users to interact with Hadoop and its ecosystem components like Hive, Pig, and HDFS
- simplifies process of querying, exploring, and visualizing data

## Apache Tez
- application framework that allows for building efficient and flexible data processing applications on Hadoop YARN. 
- improves on the MapReduce paradigm by providing a more complex and sophisticated DAG (Directed Acyclic Graph) execution engine

## Apache Hive
- data warehouse infrastructure built on top of Hadoop
- a metastore and for many pruposes a SQL wrapper around map-reduce
- it provides data summarization, query, and analysis using a SQL-like language HiveQL
- Hive is particularly well-suited for batch processing of large datasets

## Apache Trino (See Presto)
- (formerly known as Presto) 
- distributed SQL query engine for big data 
- it allows users to query data where it lives, including Hive, Cassandra, relational databases, and proprietary data stores
- Trino is known for its low-latency query performance

## Apache Phoenix
- relational database layer over HBase (Hadoop's NoSQL store)
- SQL -> HBase -> results
- enables low-latency queries over HBase data by leveraging the SQL query language
- allows for efficient data access in a familiar SQL manner

## Apache Storm
- distributed real-time computation system for processing large streams of data
- It is designed to be scalable, fault-tolerant, and easy to set up and operate 
- well-suited for tasks like continuous computation, stream processing, and real-time analytics

## Apache Drill
- Apache Drill is a low-latency distributed query engine for large-scale datasets
- supports structured and semi-structured/nested data 
- supports SQL queries and allows for schema-free data exploration
- easy to analyze data without predefined schemas

## Apache Presto (Renamed Trino)
- distributed SQL query engine for big data that enables querying data where it lives
- it supports querying various data sources like Hive, Cassandra, relational databases, and more with low latency
- (AWS Athena is based on Presto)

## Apache Zeppelin 
- web-based notebook for interactive data analytics
- python, sql, scala, R and more - with its interpreeter is allows for almost any language/data-processing backend
- integrates with Spark, Flink, JDBC
