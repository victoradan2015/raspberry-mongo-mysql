from pymongo import MongoClient

class ConexionMongo:
    Mongo_uri = 'mongodb://localhost'
    client = MongoClient(Mongo_uri)
    db = client['datosPractica1']

    def insertUltrasonico(distancia,hora):
        insertarUltrasonico = ConexionMongo.db['datosUltrasonico']
        insertarUltrasonico.insert_one({"Distancia":distancia,"Hora": hora})
        
    def insertPir(hora):
        insertarPir = ConexionMongo.db['datosPir']
        insertarPir.insert_one({"Prasencia":hora})
        
    def insertTemperatura(temperatura,humedad,hora):
        insertarTemperatura =ConexionMongo.db['datosTemperatura']
        insertarTemperatura.insert_one({"Temperatura": temperatura, "Humedad": humedad, "Hora":hora})
        
#print(client.list_database_names())
