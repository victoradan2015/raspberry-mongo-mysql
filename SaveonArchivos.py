class SaveArchivos:
    def insertUltrasonico(distancia,hora):
        archivo = open("datosGuardados/distancia.txt","a")
        archivo.write( "Distancia: %.2f cm  " % distancia + hora +chr(10))
        print( "Distancia: %.2f cm" % distancia)
        
        
    def insertPir(hora):
        archivo = open("datosGuardados/presencia.txt","a")
        archivo.write("Se detecto presencia a las" + hora + chr(10) )
        print("Presencia detectada a las: " + str(hora))
        
    def insertTemperatura(temperatura,humedad,hora):
        #print("Temperature: %-3.1f C" % result.temperature)
        #print("Humidity: %-3.1f %%" % result.humidity)
        #("GPIO pin %s is %s" % (pir_sensor, current_state))
        
        archivo = open("datosGuardados/temperaturayhumedad.txt","a")
        #archivo.write(temperatura)
        #archivo.write(humedad)
        datosTemperatura= "Humedad: "+ str(humedad) + "% Temperatura: "+ str(temperatura) + "C. Hora:" + str(hora)
        print(datosTemperatura)
        archivo.write(datosTemperatura + chr(10))
        #archivo.write("Humedad: %s  Temperatura: s%  Hora: s%" % (humedad,temperatura,hora))