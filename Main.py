from Sensor_Pir import SensorPir as sP
from Sensor_Ultrasonico import SensorUltrasonico as sU
from Sensor_TemperaturayHumedad import SensorTemperatura as sT

from ConexionMysql import Conexion as Cmysql
from ConexionMongo import ConexionMongo as Cmongo
from SaveonArchivos import SaveArchivos as sA
#from Sensor_TemperaturayHumedad import SensorTemperatura as sT

class main:
        while True:
            distancia, horaultrasonico = sU.capturar()
            horapir = sP.capturar()
            temperatura, humedad, horatemperatura = sT.capturar()
            if horapir != None:
                print("Se detecto movimiento")
                #insert on mysql
                Cmysql.insertUltrasonico(distancia,horaultrasonico)
                Cmysql.insertPir(horapir)
                Cmysql.insertTemperatura(temperatura,humedad,horatemperatura)
                #insert on mongo
                Cmongo.insertUltrasonico(distancia,horaultrasonico)
                Cmongo.insertPir(horapir)
                Cmongo.insertTemperatura(temperatura,humedad,horatemperatura)
                #insert on archivos
                sA.insertUltrasonico(distancia,horaultrasonico)
                sA.insertPir(horapir)
                sA.insertTemperatura(temperatura,humedad,horatemperatura)
                print("-----Insertados correctamente-------")
            Cmysql.commit()
            #sT.capturar()
        
