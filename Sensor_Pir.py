import RPi.GPIO as GPIO
import time
from tiempo import tiempo as t

class SensorPir:
    def capturar():
        hora = t.capturar()
        pir_sensor = 11
        led_pir = 7

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(led_pir,GPIO.OUT)
        GPIO.setup(pir_sensor, GPIO.IN)

        #archivo = open("Presencia.txt","a")
        
        current_state = 0

        try:
            #while True:
            time.sleep(0.1)
            current_state = GPIO.input(pir_sensor)
            if current_state == 1:
                #print("GPIO pin %s is %s" % (pir_sensor, current_state))
                #archivo.write("Se detecto presencia  " + hora + chr(10) )
                GPIO.output(led_pir,True)
                time.sleep(3)
                GPIO.output(led_pir,False)
                time.sleep(3)
                return hora
            #else:
            #    print("GPIO pin %s is %s" % (pir_sensor, current_state))
        except KeyboardInterrupt:
            pass
        finally:
            GPIO.cleanup()
    
