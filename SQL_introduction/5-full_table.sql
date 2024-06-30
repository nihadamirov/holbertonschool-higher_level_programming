<<<<<<< HEAD
-- Prints the full description of the table first_table.
SHOW CREATE TABLE `first_table`;
=======
-- Select the table name and creation statement from the information schema

SELECT
   TABLE_NAME AS 'Table',
   CREATE_TABLE AS 'Create Table'
FROM
   information_schema.tables
WHERE
   tables_schema = DATABASE()
   AND table_name = 'first_table';
>>>>>>> 6871f21c26ab738af24c9a73a2ba7c37514572e1
