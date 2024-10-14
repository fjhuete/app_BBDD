import pymongo,json,pprint
from pymongo.mongo_client import MongoClient

host = "192.168.122.166"
port = "27017"

def conexion(usuario,passwd):
    uri = f"mongodb://{usuario}:{passwd}@{host}:{port}/?directConnection=true&authSource=scott&appName=mongosh+2.2.4"
    cliente = MongoClient(uri)
    return cliente

def login(usuario,passwd):
    cliente = conexion(usuario,passwd)
    try:
        cliente.admin.command('ping')
        return cliente
    except Exception as e:
        print(e)
        return False

def mostrardeptartamentos(usuario,passwd):
    cliente = conexion(usuario,passwd)
    db = cliente.scott
    dept = db.dept
    cursor = dept.find({})
    return cursor

def mostrarempleados(usuario,passwd):
    empleados = []
    cliente = conexion(usuario,passwd)
    db = cliente.scott
    emp = db.emp
    cursor_emp = emp.find({})
    for documento in cursor_emp:
        empleados.append(documento)
    return empleados

def buscar_empleados(deptno,usuario,passwd):
    lista = []
    cliente = conexion(usuario,passwd)
    db = cliente.scott
    emp = db.emp
    if int(deptno) == 0:
        cursor = mostrarempleados(usuario,passwd)
        for documento in cursor:
            lista.append(documento)
    else:
        cursor = emp.find({"deptno": int(deptno)})
        for documento in cursor:
            lista.append(documento)
    return lista

def rango_salario(min,max,usuario,passwd):
    lista = []
    cliente = conexion(usuario,passwd)
    db = cliente.scott
    emp = db.emp
    consulta = {"$match": {"sal": {"$gt": int(min), "$lt": int(max)}}}
    orden = {"$sort": {"sal": -1}}
    agregacion = [consulta,orden]
    cursor = emp.aggregate(agregacion)
    for documento in cursor:
        lista.append(documento)
    return lista