# Group Activity

**Objective**: To deepen understanding of Snowflake's advanced features, specifically Zero Copy Cloning, the COPY INTO command, the INSERT INTO command, Time Travel, Streams and Tasks, and Data Masking through collaborative research and presentation.


## Zero Copy Cloning
1)How does the feature work in Snowflake
1a) Explanation
	- Zero Copy Cloning in Snowflake allows users to create a clone of a database, schema or table without duplicating the data. This feature makes It possible to create copies of data structures instantaneously and without consuming additional storage
1b) Technical details and underlying mechanisms
	- ZERO Copy Cloning uses metadata and pointers to reference the original dat blocks. Changes are managed with a copy-on-write mechanism, creating new data blocks only when modifications are made.
	- CREATE CLONE my_database_clone CLONE my_database;

2)Identify at least three practical use cases where the feature would be beneficial
2a)Use Case 1
	- Creating clones production databases for development and testing purposes allows develops to work with real data without affecting the production environment
2b)Use Case 2
	- Cloning can be used to create backups at specific point in time, enabling quick recovery in case of data corruption or loss
2c)Use Case 3
	- Data analyst can create clones of data for performing analytics and generating reports without impacting the performance of the live database.
2d)Explain what the feature is advantageous in these scenarios
	- Zero Copy Cloning is advantageous in these scenarios because it allows rapid creation of data copies without consuming additional storage or affecting the performance of the source data. It provides a flexible and efficient way to manage data environments for various purposes

3)Pros and Cons
3a)Advantage 1
	The cloning process is very fast as it relies on metadata operations rather than copying data blocks
3b)Advantage 2
	- Since clones reference the same data blocks as the original. There is no additional storage cost until changes are made
3c)Advantage 3
	- Since close reference the same data blocks as the original, there is no additional storage cost until changes are made
3d)Potential drawbacks or limitations (if any).
3e)Drawback 1
	- Changes to the original data or deletion can impact the close if not managed carefully
3f)Drawback 2
	- While read operations are efficient, write operations can become slower due to the copy-on-write mechanism
3g)Drawback 3
	- Managing multiple clones and their relationships with the original data can become complex


## COPY INTO
1)How does the feature work in Snowflake
1a) Explanation
	- The COPY INTO command in Snowflake is used to load data from an external stage (like Amazon S3. Azure Blob Storage, or Snowflake's internal stage) into Snowflake tables. It can be used to export data from Snowflake tables to external stages
1b) Technical details and underlying mechanisms
	- COPY INTO reads data from specified file formats using parallel processing and can perform transformations and validations during loading.
	- COPY INTO my_table FROM @my_stage/file.csv FILE_FORMAT = (TYPE = 'CSV')

2)Identify at least three practical use cases where the feature would be beneficial
2a)Use Case 1
	- COPY INTO is useful for migrating data from on-prem solutions or other cloud services into Snowflake
2b)Use Case 2
	- Organizations can use COPY INTO to regularly ingest data from external sources into Snowflake for analytics and reporting
2c)Use Case 3
	- Exporting data from Snowflake to external storage using COPY INTO helps in archiving data for compliance and historical analysis
2d)Explain what the feature is advantageous in these scenarios
	- COPY INTO is advantageous in these scenarios because it provides a reliable and efficient way to move data between Snowflake and external storage systems. Its ability to handle large volumes of data and perform transformations during the loading process make it suitable for various data management tasks
3)Pros and Cons
3a)Advantage 1
	- COPY INTO leverages parallel processing to load data quickly and efficiently
3b)Advantage 2
	- The command supports various file formats and can perform data transformations during the loading process
3c)Advantage 3
	- COPY INTO includes error handling and data validation features, ensuring data integrity during the loading process
3d)Potential drawbacks or limitations (if any).
3e)Drawback 1
	- Setting up external stages and configuring the COPY INTO command can be complex, especially for large-scale data operations
3f)Drawback 2
	- Depending on the volume of data and frequency of operations, using external stages and COPY INTO and bring additional costs
3g)Drawback 3
	- The performance and reliability of the COPY INTO command can be affected by the availability and performance of the external storage system


## Time Travel	
Understanding the Feature	How does the feature work in snowflake?
	accessing historical data (data that has been changed or deleted) at any point within a defined period
	restores any data-related objects (tables, shemas, databases) that have been accidently or intentionally deleted
	duplicates and backups data from key points in the past
	analyzes data usage/manipulation over specified periods of time
	
Use Cases	Identify at least three practical use cases where the feature would be beneficial
	query data in the past that has since then been deleted or updated
	create clones of enitre tables, schemas, and databases at or before specific points in the past
	restore tables, schemas, and databases that have been dropped
	Explain why the feature is advantageous in these scenarios
Pros and Cons	List some of the advantages of using this feature
	able to restore data and tables that you may have deleted accidently or someone deleted eprpousfully
	
	
Potential drawbacks or limitations (if any)
after a defined period of time has passed, the data gets moved into Snowflake Fail-Safe and you can no longer use these actions (standard period is 1 day)

## Streams and Tasks	
Understanding the Feature	How does the feature work in snowflake?
	objects that enable continuous and periodic processing of data
	a stream logically takes an initial snapshot of every row in the source object ( table, external table, or the underlying tables for a view) by initializing a point in time (called an offset) as the current transactional version of the object
	tasks define a reacurring schedule for executing a SQL statement
	tasks can use streams to process stream content on a schedule
	think of streams like a bookmark, indicated a point in time in the pages of a book (the source object), can be thrown away and can insert multiple bookmarks into thfferent places in the book
Use Cases	Identify at least three practical use cases where the feature would be beneficial
	tasks can generate periodic reports by inserting or merging rows into a report table or perform other periodic work
	can be used together to create ETL piplines
	a task reads the streams every few minutes to update the aggregate table which is read by a real-time dashboard
	Explain why the feature is advantageous in these scenarios
Pros and Cons	List some of the advantages of using this feature
	a stream can be dropped and other streams created at the same or different points of time (you can do this consecutively or at different times using Time Travel)
	
	
Potential drawbacks or limitations (if any)
a stream itself does not contain any table data
table schema evolution is not supported by tasks

## 5. Data Masking & Row Access Policies

**Understanding Data Masking & Row Access Policies**:

- What is Data Masking/Row Access Policies in Snowflake and how does it work?
    - snowflake allows policy administrators to implement different masks for different roles
    - we can selectively mask plain-text data in table and view columns *at query time*
    - for example, users with the 'ANALYST' role might only be able to see the last 4 digits of a person's phone number while a SUPPORT role can see everything, including sensitive information like social security information.
- Technical details and implementation strategies.
```sql
-- Dynamic Data Masking
CREATE MASKING POLICY employee_ssn_mask AS (val string) RETURNS string ->
  CASE
    WHEN CURRENT_ROLE() IN ('PAYROLL') THEN val
    ELSE '******'
  END;

-- External Tokenisation
  CREATE MASKING POLICY employee_ssn_detokenize AS (val string) RETURNS string ->
  CASE
    WHEN CURRENT_ROLE() IN ('PAYROLL') THEN ssn_unprotect(VAL)
    ELSE val -- sees tokenized data
  END;
```


**Use Cases for Data Masking**:

- Identify at least three practical use cases where Data Masking/Row Access Policies would be beneficial.
- Explain why Data Masking/Row Access Policies  is advantageous in these scenarios.

1. protect personally identifiable information
2. anonymization of data
3. safely distribute data

In all cases, we can hide potentially sensitive information to people who should not see it.

**Pros and Cons**:

- List some of the advantages of using Data Masking.
1. Easy of use - one policy can apply to thousands of columns across databases and schemas
2. Easy to restrict data access
3. Mask before sharing
4. Easily change policies without needing to remask thousands of columns
- Potential drawbacks or limitations.
1. Role that view unmasked data can insert into a different column where policies are not applied allowing non-authorized users to view data (on the new column)



## 6.  UDF and Stored Procedures 

#### UDFs and Stored Procedures

**Understanding UDFs and Stored Procedures**
- Stored Procedure: perform administrative operations by executing SQL statements. Can, but does not have to return a value.
- User defined function (UDF): Calculate and return a value. A function always returns a value.
- can by in java, javascript, python, scala, sql

```sql
CREATE OR REPLACE PROCEDURE MyStoredProcedure(from_table string, to_table string, count int)
  returns string
  language python
  runtime_version = '3.8'
  packages = ('snowflake-snowpark-python')
  handler = 'run'
as
$$
def run(session, from_table, to_table, count):
  session.table(from_table).limit(count).write.save_as_table(to_table)
  return "SUCCESS"
$$;


-- Call Stored Procedure
CALL MyStoredProcedure('tbl1', 'tbl2');

-- UDF written in python
CREATE OR REPLACE FUNCTION addone(i int)
RETURNS INT
LANGUAGE PYTHON
RUNTIME_VERSION = '3.8'
HANDLER = 'addone_py'
as
$$
def addone_py(i):
  return i+1
$$;


SELECT addone(1);
```

**Use Cases For Stored Procedures**
- performing DDL or DML operations
  - Deleting data over n-days old, etc
  - UPDATE statements

**Use Cases for UDFs**
- function that is part of a sql statement

**Pros and Cons**
- can call UDF's inline (in sql); cannot do that with stored procedures
- udfs are more rigid
- can invoke functions from a stored procedure; cannot invoke procedure from function
