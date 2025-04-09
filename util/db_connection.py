import mysql.connector

def get_connection(props):
    try:
        connection = mysql.connector.connect(
            host=props.get("host"),
            user=props.get("user"),
            password=props.get("password"),
            database=props.get("database")
        )
        if connection.is_connected():
            print("Database connection established successfully!")
        return connection
    except mysql.connector.Error as e:
        raise Exception(f"Error connecting to the database: {e}")