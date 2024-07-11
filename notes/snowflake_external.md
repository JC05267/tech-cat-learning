# External Data in Snowflake
## Stages

Stages are POINTERS to external data.
Do not specifiy schema.

## External Tables
External Tables is still a pointer.
It also allows for sql queries on external data without using internal snowflake storage.
Useful with large datasets that do not need to be fully ingested into Snowflake.
