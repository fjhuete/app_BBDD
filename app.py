from flask import Flask, render_template, abort, request, session
from pymongo.mongo_client import MongoClient
import funciones, os

app = Flask(__name__)
port = os.getenv("PORT")
app.secret_key = 'e$fksEci$2t9sFVsi="f0$cbTy'

@app.route('/', methods=["GET","POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        passwd = request.form.get("passwd")
        cliente = funciones.conexion(usuario,passwd)
        if cliente:
            session['usuario'] = usuario
            session['passwd'] = passwd
            return render_template("inicio2.html")
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")
    
@app.route('/dept')
def dept():
    listadept = []
    usuario = session['usuario']
    passwd = session['passwd']
    departamentos = funciones.mostrardeptartamentos(usuario,passwd)
    for dept in departamentos:
        listadept.append(dept)
    print(listadept)
    return render_template("depts.html",depts=listadept)

@app.route('/emp')
def emp():
    listaemp = []
    usuario = session['usuario']
    passwd = session['passwd']
    empleados = funciones.mostrarempleados(usuario,passwd)
    for emp in empleados:
        listaemp.append(emp)
    print(listaemp)
    return render_template("emps.html",emps=listaemp)

@app.route('/departamento', methods=["POST"])
def empleados_departamento():
    usuario = session['usuario']
    passwd = session['passwd']
    deptno = request.form.get("deptno")
    empleados = funciones.buscar_empleados(deptno,usuario,passwd)
    return render_template("departamento.html",empleados=empleados)

@app.route('/empleados', methods=["POST"])
def empleados_salario():
    min = request.form.get("minimo")
    max = request.form.get("maximo")
    empleados = funciones.rango_salario(min,max)
    return render_template("empleados.html",empleados=empleados)

@app.route('/logout')
def logout():
    session.clear()
    return render_template("login.html")
        
app.run("0.0.0.0",port,debug=True)