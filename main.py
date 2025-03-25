import requests
import duckdb
import pandas as pd

## Connect to db
duckdb = duckdb.connect("local.db")

## Drop table
duckdb.sql("DROP TABLE main.pokemon")

## Call API
response = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=151")

## Put json data into a table
json_data = response.json()
table_data = pd.json_normalize(json_data['results'])

## Create table from dataframe
duckdb.sql("CREATE TABLE main.pokemon AS SELECT * FROM table_data")

## Insert data
duckdb.sql("INSERT INTO main.pokemon SELECT * FROM table_data")

## Show data from table
duckdb.sql("SELECT * FROM main.pokemon").show()