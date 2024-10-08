import pymongo,json,pprint
from pymongo.mongo_client import MongoClient

host = "192.168.122.166"
port = "27017"

uri = f"mongodb://scott:tiger@{host}:{port}/?directConnection=true&authSource=scott&appName=mongosh+2.2.4"


cliente = MongoClient(uri)
db = cliente.scott
emp = db.emp
dept = db.dept
usuarios = db.usuarios

def probarconexion():
    try:
        cliente.admin.command('ping')
        print("Conexión exitosa a la base de datos.")
    except Exception as e:
        print(e)

def cerrarcliente():
    cliente.close()

def login(user,passwd):
    lista = []
    login = False
    cursor = usuarios.find({"usuario":user})
    for documento in cursor:
        lista.append(documento)
    print(lista)
    for usuario in lista:
        if usuario["passwd"] == passwd:
            login = True
    return login

def mostrardeptartamentos():
    cursor = dept.find({})
    return cursor

def mostrarempleados():
    cursor = emp.find({})
    return cursor

def buscar_empleados(deptno):
    lista = []
    if int(deptno) == 0:
        cursor = mostrarempleados()
        for documento in cursor:
            lista.append(documento)
    else:
        cursor = emp.find({"deptno": int(deptno)})
        for documento in cursor:
            lista.append(documento)
    return lista

def rango_salario(min,max):
    lista = []
    consulta = {"$match": {"sal": {"$gt": int(min), "$lt": int(max)}}}
    orden = {"$sort": {"sal": -1}}
    agregacion = [consulta,orden]
    cursor = emp.aggregate(agregacion)
    for documento in cursor:
        lista.append(documento)
    return lista