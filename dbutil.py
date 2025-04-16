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
    
    db_conf = read_config()
    try:
        connection = pymysql.connect(
            charset=db_conf["charset"],
            connect_timeout=int(db_conf["timeout"]),
            cursorclass=pymysql.cursors.DictCursor,
            db=db_conf["db"],
            host=db_conf["host"],
            password=db_conf["password"],
            read_timeout=int(db_conf["timeout"]),
            port=int(db_conf["port"]),
            user=db_conf["user"],
            write_timeout=int(db_conf["timeout"])
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