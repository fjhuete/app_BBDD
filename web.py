from flask import Flask, render_template, abort, request
from pymongo.mongo_client import MongoClient
import funciones, os

app = Flask(__name__)
port = os.getenv("PORT")

@app.route('/', methods=["GET","POST"])
def login():
    if request.method == "POST":
        host = "192.168.122.166"
        port = "27017"

        usuario = request.form.get("usuario")
        passwd = request.form.get("passwd")

        uri = f"mongodb://{usuario}:{passwd}@{host}:{port}/scott?directConnection=true&authSource=scott&appName=mongosh+2.2.4"
    
        cliente = MongoClient(uri)

        db = cliente.scott
        emp = db.emp
        dept = db.dept

        departamentos = []
        cursor_dept = dept.find({})
        for documento in cursor_dept:
            departamentos.append(documento)

        empleados = []
        cursor_emp = emp.find({})
        for documento in cursor_emp:
            empleados.append(documento)

        if cliente:
            return render_template("inicio.html",depts=departamentos, emps=empleados)
        else:
            return abort (404)
    else:
        return render_template ("login.html")

##############################################################################

""" @app.route('/dept')
def dept():
    listadept = []
    departamentos = funciones.mostrardeptartamentos(usuario,passwd)
    for dept in departamentos:
        listadept.append(dept)
    print(listadept)
    return render_template("dept.html",departamentos=listadept)

@app.route('/emp')
def emp():
    return render_template("emp.html")

@app.route('/departamento', methods=["POST"])
def empleados_departamento():
    deptno = request.form.get("deptno")
    empleados = funciones.buscar_empleados(deptno)
    return render_template("departamento.html",empleados=empleados)

@app.route('/empleados', methods=["POST"])
def empleados_salario():
    min = request.form.get("minimo")
    max = request.form.get("maximo")
    empleados = funciones.rango_salario(min,max)
    return render_template("empleados.html",empleados=empleados) """

###############################################################################################

app.run("0.0.0.0",port,debug=True)