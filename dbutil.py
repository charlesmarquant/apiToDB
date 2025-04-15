import pymysql

## Load the database configuration from a file 
def read_config():
     
    config = {}
    with open("/Users/carlito/Desktop/python/apiToDB/db_config.txt", "r") as file:
        for line in file:
            key, value = line.strip().split("=")
            config[key] = value
    return config

## Connect to the database 
def connect_to_mysql():
    
    dbconf = read_config()
    try:
        connection = pymysql.connect(
            charset=dbconf["charset"],
            connect_timeout=int(dbconf["timeout"]),
            cursorclass=pymysql.cursors.DictCursor,
            db=dbconf["db"],
            host=dbconf["host"],
            password=dbconf["password"],
            read_timeout=int(dbconf["timeout"]),
            port=int(dbconf["port"]),
            user=dbconf["user"],
            write_timeout=int(dbconf["timeout"])
        )
        if connection.open:
            print("Successfully connected to the database")
            return connection
    except pymysql.connect.Error as err:
        print(f"Error: {err}")
        return None
    
## Insert data into the database
def insert_to_mysql(connection, sql):
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()
            print("Data inserted successfully")
    except pymysql.MySQLError as err:
        print(f"Error: {err}")
        connection.rollback()