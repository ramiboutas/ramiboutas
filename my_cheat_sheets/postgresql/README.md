## PostgreSQL



### Info

* Default user: `postgres`
* Password:
* Port: `5432`
* Configuration file: `/etc/postgresql/<VERSION>/main/postgresql.conf`

### Connect to postgres

```
sudo -i -u postgres
psql
```
* Alternative: `sudo -u postgres psql`

### Usefull command once inside postgres

* To quit `\q`

* Show all the databases `\l`

* Connect to a db: `\c mydb;`

###  Configuring a db for django:
```
CREATE DATABASE mydb;
CREATE USER myuser WITH PASSWORD 'mypass';
ALTER ROLE myuser SET client_endcoding TO 'utf-8';
ALTER ROLE myuser SET timezone TO 'UTC';
ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
```




### Most Important SQL Statements:

Command  |  Waht is does?
--|--
SELECT  | extracts data from a database
UPDATE | updates data in a database
DELETE | deletes data from a database
INSERT INTO | inserts new data into a database
CREATE DATABASE | creates a new database
ALTER DATABASE | modifies a database
CREATE TABLE | creates a new table
ALTER TABLE | modifies a table
DROP TABLE | deletes a table
CREATE INDEX | creates an index (search key)
DROP INDEX | deletes an index  |
