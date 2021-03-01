import RPi.GPIO as GPIO
from librerias import dht11
import time
from tiempo import tiempo as t

class SensorTemperatura:
    def capturar():
        # initialize GPIO
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)

        # read data using pin 14
        instance = dht11.DHT11(pin=15)
        hora = t.capturar()
        try:
            while True:
                result = instance.read()
                if result.is_valid():
                    #print("Temperature: %-3.1f C" % result.temperature)
                    #print("Humidity: %-3.1f %%" % result.humidity)
                    '''
                    result.temperature = temperatura
                    result.humidity = humedad
                    print(temperatura, humedad)'''
                    return result.temperature, result.humidity,hora
                time.sleep(2)

        except KeyboardInterrupt:
            pass
        finally:
            #print("Cleanup")
            GPIO.cleanup()
