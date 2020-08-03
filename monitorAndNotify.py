from data import database
from environment import environment
from sense_hat import SenseHat
from readAndDisplay import display

# Main 
## Take the CPU environment
temp, hum = environment.get_temp_hum()
## Insert sensor data to SQLite database
database.insertData(temp,hum)
## Display the temperature in LED matrix
display.display('config.json')
