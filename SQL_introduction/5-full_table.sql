-- Select the table name and creation statement from the information schema

SELECT
   TABLE_NAME AS 'Table',
   CREATE_TABLE AS 'Create Table'
FROM
   information_schema.tables
WHERE
   tables_schema = DATABASE()
   AND table_name = 'first_table';
