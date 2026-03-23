import os
import pymysql

def test_connection():
    print("Testing connection to the database...")
    db_host = os.environ.get("DB_HOST")
    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")
    db_name = os.environ.get("DB_NAME")

    try:
        connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        print("SUCCESS: The Python server is connected to MySQL!")
        connection.close()

    except Exception as e:
        print("ERROR: Failed to connect to the database.")
        print(f"Details: {e}")
        exit(1)

if __name__ == "__main__":
    test_connection()
