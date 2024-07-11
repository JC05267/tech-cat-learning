# Group Activity

**Objective**: To deepen understanding of Snowflake's advanced features, specifically Zero Copy Cloning, the COPY INTO command, the INSERT INTO command, Time Travel, Streams and Tasks, and Data Masking through collaborative research and presentation.

## 1. Zero Copy Cloning

**Understanding Zero Copy Cloning**:

- How does Zero Copy Cloning work in Snowflake?
- Technical details and underlying mechanisms.

**Use Cases for Zero Copy Cloning**:

- Identify at least three practical use cases where Zero Copy Cloning would be beneficial.
- Explain why Zero Copy Cloning is advantageous in these scenarios.

**Pros and Cons**:

- List some of the advantages of using Zero Copy Cloning.
- Potential drawbacks or limitations.

| **Feature**                   | **Details**                                                  |
| ----------------------------- | ------------------------------------------------------------ |
| **Understanding the Feature** | How does the feature work in Snowflake?                      |
|                               | - Explanation                                                |
|                               | - Technical details and underlying mechanisms                |
| **Use Cases**                 | Identify at least three practical use cases where the feature would be beneficial. |
|                               | - Use Case 1                                                 |
|                               | - Use Case 2                                                 |
|                               | - Use Case 3                                                 |
|                               | Explain why the feature is advantageous in these scenarios.  |
| **Pros and Cons**             | List some of the advantages of using the feature.            |
|                               | - Advantage 1                                                |
|                               | - Advantage 2                                                |
|                               | - Advantage 3                                                |
|                               | Potential drawbacks or limitations (if any).                 |
|                               | - Drawback 1                                                 |
|                               | - Drawback 2                                                 |
|                               | - Drawback 3                                                 |

## 2. COPY INTO

**Understanding COPY INTO Command**:

- How does the COPY INTO command work?
- Syntax and common parameters.

**Use Cases for COPY INTO**:

- Identify scenarios where the COPY INTO command is the preferred method for loading data.
- Discuss specific examples and benefits.

**Comparison with INSERT INTO**:

- List the differences between COPY INTO and INSERT INTO.
- When should each command be used?

**Pros and Cons**:

- Advantages and disadvantages of using COPY INTO for bulk loading.
- Performance considerations.

| **Feature**                   | **Details**                                                  |
| ----------------------------- | ------------------------------------------------------------ |
| **Understanding the Feature** | How does the feature work in Snowflake?                      |
|                               | - Explanation                                                |
|                               | - Technical details and underlying mechanisms                |
| **Use Cases**                 | Identify at least three practical use cases where the feature would be beneficial. |
|                               | - Use Case 1                                                 |
|                               | - Use Case 2                                                 |
|                               | - Use Case 3                                                 |
|                               | Explain why the feature is advantageous in these scenarios.  |
| **Pros and Cons**             | List some of the advantages of using the feature.            |
|                               | - Advantage 1                                                |
|                               | - Advantage 2                                                |
|                               | - Advantage 3                                                |
|                               | Potential drawbacks or limitations (if any).                 |
|                               | - Drawback 1                                                 |
|                               | - Drawback 2                                                 |
|                               | - Drawback 3                                                 |

## 3. Time Travel

**Understanding Time Travel**:

- What is Time Travel in Snowflake and how does it work?
- Technical details and underlying mechanisms.

**Use Cases for Time Travel**:

- Identify at least three practical use cases where Time Travel would be beneficial.
- Explain why Time Travel is advantageous in these scenarios.

**Pros and Cons**:

- List some of the advantages of using Time Travel.
- Potential drawbacks or limitations.

| **Feature**                   | **Details**                                                  |
| ----------------------------- | ------------------------------------------------------------ |
| **Understanding the Feature** | How does the feature work in Snowflake?                      |
|                               | - Explanation                                                |
|                               | - Technical details and underlying mechanisms                |
| **Use Cases**                 | Identify at least three practical use cases where the feature would be beneficial. |
|                               | - Use Case 1                                                 |
|                               | - Use Case 2                                                 |
|                               | - Use Case 3                                                 |
|                               | Explain why the feature is advantageous in these scenarios.  |
| **Pros and Cons**             | List some of the advantages of using the feature.            |
|                               | - Advantage 1                                                |
|                               | - Advantage 2                                                |
|                               | - Advantage 3                                                |
|                               | Potential drawbacks or limitations (if any).                 |
|                               | - Drawback 1                                                 |
|                               | - Drawback 2                                                 |
|                               | - Drawback 3                                                 |

## 4. Streams and Tasks

**Understanding Streams**:

- How do Streams work in Snowflake?
- Technical details and common use cases.

**Understanding Tasks**:

- How do Tasks work in Snowflake?
- Syntax and scheduling options.

**Use Cases for Streams and Tasks**:

- Identify scenarios where Streams and Tasks would be beneficial.
- Discuss specific examples and benefits.

**Pros and Cons**:

- Advantages and disadvantages of using Streams and Tasks.
- Performance considerations and potential pitfalls.

| **Feature**                   | **Details**                                                  |
| ----------------------------- | ------------------------------------------------------------ |
| **Understanding the Feature** | How does the feature work in Snowflake?                      |
|                               | - Explanation                                                |
|                               | - Technical details and underlying mechanisms                |
| **Use Cases**                 | Identify at least three practical use cases where the feature would be beneficial. |
|                               | - Use Case 1                                                 |
|                               | - Use Case 2                                                 |
|                               | - Use Case 3                                                 |
|                               | Explain why the feature is advantageous in these scenarios.  |
| **Pros and Cons**             | List some of the advantages of using the feature.            |
|                               | - Advantage 1                                                |
|                               | - Advantage 2                                                |
|                               | - Advantage 3                                                |
|                               | Potential drawbacks or limitations (if any).                 |
|                               | - Drawback 1                                                 |
|                               | - Drawback 2                                                 |
|                               | - Drawback 3                                                 |

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
