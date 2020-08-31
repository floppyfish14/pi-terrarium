#!/usr/bin/env python
import os

# Setup django environment to input data into models.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Terrarium.settings")
import django
django.setup()

from tempsensor.models import Temperature
from humidity.models import Humidity

# Import neeeded modules for sensors and other.
import Adafruit_DHT
import datetime
import pytz

# Put "from" imports here. Just to be OCD, lol.
from time import localtime, sleep

def run_fan():
    # Put code to turn fan on for a certain time period here. 
    # Use subprocess for timing purposes.
    print("{} Ran Fan!".format(datetime.datetime.now()))

def humidify():
    # Put code to run humidifier here.
    # Use subprocess for timing purposes.
    print("{} Humidified!".format(datetime.datetime.now()))

def water_level():
    # Put code to monitor water level here. Important, so we dont run the pump if it's dry. 
    # Should be fine with 60 seconds to run.
    print("{} Checked Water Level!".format(datetime.datetime.now()))

def humidity_temp():

    # Monitors Temperature and Humidity. Puts data imto django models for website.
    while True:
        PACER = localtime().tm_sec
        now = datetime.datetime.now(pytz.timezone('US/Eastern'))
        humidity, temperature = Adafruit_DHT.read_retry(11,4)
        fahrenheit = (int(temperature) * (9/5) + 32)

        q = Temperature.objects.create(reading_time=now, Temp_F=fahrenheit)
        q.save()
        r = Humidity.objects.create(reading_time=now, Humidity_Percent=humidity)
        r.save()
        """ run only once, at the top of every minute """
        if fahrenheit > 78:
             run_fan()
             humidify()
        elif humidity < 88:
             humidify()
        water_level()
        sleep(60 - PACER)
        

def main():

    # Create a way to run through all functions without hanging on one for the whole time program runs.
    
    #First Check Humidity and Temperature
    humidity_temp()
main()
