import requests
import json
import os
from data import database
from sense_hat import SenseHat

class display:
    r = (255, 0, 0)          # Red
    g = (0, 128, 0)          # Green
    b = (135, 206, 250)     # sky blue

    # Display a cold symbol
    cold = [
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
    ]

    # Display a comfortable symbol
    comfortable = [
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
    ]

    #Display hot symbol
    hot = [
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
    ]
    
    # Function to read Json file
    @staticmethod
    def read_Json(file_Json):
        with open(file_Json,'r') as json_file:
            json_data=json.load(json_file)
            temperature_max=json_data['max_temperature']
            temperature_min=json_data['min_temperature']
        return temperature_max, temperature_min

    # Function to display the temperature in LED matrix
    @staticmethod
    def display(file_Json):
        sense = SenseHat()
        temperature_max, temperature_min = display.read_Json(file_Json)
        sensehat_temp = database.getData()
        if (sensehat_temp < temperature_min):
            sense.show_letter(display.cold)
        elif (sensehat_temp > temperature_min and sensehat_temp < temperature_max):
            sense.set_pixels(display.comfortable)
        elif (sensehat_temp > temperature_max):
            sense.set_pixels(display.hot)
