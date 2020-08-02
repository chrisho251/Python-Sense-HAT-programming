import sqlite3 as lite
import sys

# Create class for database
class database:

    #Initialize connection
    @staticmethod
    def connection():
        connect = lite.connect('sensehat.db')
        return connect

    # Create table SENSEHAT_data
    connect = database.connection()
    @staticmethod
    def create_db_table():
        with connect:
            # Set up the cursor
            cursor = connect.cursor()
            # If table SENSEHAT_data has already exist, we will delete it
            cursor.execute("DROP TALBE IF EXISTS SENSEHAT_data")
            # Then create a new table to store the current time, temperature, humidity
            cursor.execute("CREATE TABLE SENSEHAT_data(timestamp DATETIME, temp NUMERIC, hum NUMERIC)")
            connect.close()

    # Insert sensor data of temperature and humidity into talbe SENSEHAT_data
    @staticmethod
    def insertData(temp, hum):
        connect = database.connection()
        with connect:
            cursor = connect.cursor()
            cursor.execute("INSERT INTO SENSEHAT_data values(datetime('now'),?,?)",(temp,hum))
            connect.commit()
            connect.close()