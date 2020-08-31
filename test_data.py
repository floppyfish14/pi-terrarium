#!/usr/bin/env python3
import Adafruit_DHT
from time import sleep

def main():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(11,4)
        fahrenheit = ((int(temperature) * (9/5)) + 32)
        print(fahrenheit)
        print(temperature)
        sleep(5)
main()
