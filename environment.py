import os
from sense_hat import SenseHat
from data import database

class environment:

    # Get CPU temperature
    @staticmethod
    def get_cpu_temp():
        res = os.popen("vcgencmd measure_temp").readline()
        return float(res.replace("temp=","").replace("'C\n",""))

    
    @staticmethod
    def get_temp_hum():
        # Initialize the sensehat object
        sense = SenseHat()
        # Get the temperature
        t1 = sense.get_temperature_from_humidity()
        t2 = sense.get_temperature_from_pressure()
        # Get the CPU temperature
        t_cpu = environment.get_cpu_temp()
        # Get humidity
        h = sense.get_humidity()
        #p = sense.get_pressure()
        # Calculates the real temperature compesating CPU heating.
        t = (t1 + t2) / 2
        t_corr = t - ((t_cpu - t) / 1.5)
        if environment.check_valid_data(t,h)==False:
            return environment.get_temp_hum
        return round(t_corr), round(h)
    
    # This function is to check the temperature and humidity at the beginning where it equals to 0
    @staticmethod
    def check_valid_data(temp, hum):
        if temp==0 or hum==0:
            return False
        return True

