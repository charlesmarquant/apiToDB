import requests
import dbutil
import pandas as pd

## Connect to MySQL database
connect_db = dbutil.connect_to_mysql()

print(connect_db)

## Call API
response = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=151")


## Put json data into a table
json_data = response.json()
print(json_data)
table_data = pd.json_normalize(data=json_data['results'],meta=['name', 'url'])


## Insert data
for index, row in table_data.iterrows():
    name = row[0]
    url = row[1]
    sql = f"INSERT INTO stgPokemon (pokemonName, pokemonUrl) VALUES ('{name}', '{url}') ON DUPLICATE KEY UPDATE pokemonUrl = '{url}'"
    print(sql)
    dbutil.insert_to_mysql(connect_db, sql)

