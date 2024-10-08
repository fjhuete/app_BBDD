from flask import Flask, render_template, abort, request
import funciones, os

app = Flask(__name__)
port = os.getenv("PORT")

@app.route('/', methods=["GET","POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        passwd = request.form.get("passwd")
        login = funciones.login(usuario,passwd)
        if login:
            return render_template("inicio.html")
        else:
            return abort (404)
    else:
        return render_template ("login.html")

@app.route('/dept')
def dept():
    listadept = []
    departamentos = funciones.mostrardeptartamentos()
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
    return render_template("empleados.html",empleados=empleados)

app.run("0.0.0.0",port,debug=True)