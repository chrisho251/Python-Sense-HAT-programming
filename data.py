import sqlite3 as lite
import sys

# Create class for database
class database:
     
    

    # Create table SENSEHAT_data
    @staticmethod
    def create_db_table():
        connection = lite.connect('sensehat.db')
        with connection.cursor() as cursor:
            # If table SENSEHAT_data has already exist, we will delete it
            cursor.execute("DROP TABLE IF EXISTS SENSEHAT_data")
            # Then create a new table to store the current time, temperature, humidity
            cursor.execute("CREATE TABLE SENSEHAT_data(timestamp DATETIME, temp NUMERIC, hum NUMERIC)")
        connection.commit()
        connection.close()

    # Insert sensor data of temperature and humidity into table SENSEHAT_data
    @staticmethod
    def insertData(temp, hum):
        connection = lite.connect('sensehat.db')
        with connection.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO SENSEHAT_data values(datetime('now'),?,?)",(temp,hum))
            except:
                print('Table does not exist!')    
        connection.commit()
        connection.close()

    # This function is to store the last data of temperature and humidity
    @staticmethod
    def getData():
        connection = lite.connect('sensehat.db')
        with connection.cursor() as cursor:
            try:
                environment_list = list(cursor.execute("SELECT * FROM SENSEHAT_data"))
                temp = environment_list[-1][-2]
                hum = environment_list[-1][-1]
            except:
                print('Table Does not Exist!')
        return environment_list, temp, hum

    