-- A script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- Creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Uses a database
USE hbtn_0d_usa;
-- Creates a table
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL
state_id NOT NULL,
name VARCHAR(256) NOT FULL
PRIMARY KEY(id)
FOREIGN KEY(state_id) REFERENCES states(id))