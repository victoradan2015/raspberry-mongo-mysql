import pymysql

class Conexion:
    connection = pymysql.connect(
        host="localhost",
        user="admin",
        password="admin",
        db="datosPractica1"
        )

    cursor = connection.cursor()

    def insertUltrasonico(distancia,hora):
        #print(distancia + hora)
        #round(distancia,2)
        sql="insert into datosUltrasonico(Distancia,Hora) VALUES('{}','{}')".format(distancia,hora)
        Conexion.cursor.execute(sql)
        
    def insertPir(hora):
        sql = "insert into datosPir(Presencia) VALUES('{}')".format(hora)
        Conexion.cursor.execute(sql)
        
    def insertTemperatura(temperatura,humedad,hora):
        sql = "insert into datosTemperatura(Temperatura,Humedad,Hora) VALUES ('{}','{}','{}')".format(temperatura,humedad,hora)
        Conexion.cursor.execute(sql)

        
    def commit():
        Conexion.connection.commit()

    
