from flask import Flask, render_template, request, redirect, url_for
from test import *
from cEngine import *
import copy
import shutil


c1,c2=initWP()
main_combat=Combate(c1,c2)
it=100
# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir la ruta y la función para mostrar "Hola Mundo"
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/settings")
def settings():
    data={
        "entr":main_combat.rand,
        "dblood":main_combat.dblood,
        "darmor":main_combat.darmor,
        "it":it
    }
    return render_template("settings.html",data=data)

@app.route("/combat1")
def test1():
    # Renderizar la plantilla de la nueva página
    data = {
        "fue": c1.fisico['fue'],
        "agi": c1.fisico['agi'],
        "peso": c1.fisico['peso'],
        "res": c1.fisico['res'],
        "cons": c1.fisico['cons'],
        "arm": c1.fisico['arm'],
        "tecnica": c1.tecnica,
        "refle": c1.mental['ref'],
        "exp": c1.mental['exp'],
        "estilo": c1.mental['est'],
        "vis": c1.mental['vis'],
        "int": c1.nofisico['int'],
        "ast": c1.nofisico['ast'],
        "sab": c1.nofisico['sab'],
        "pac": c1.nofisico['pac'],
        "aut": c1.nofisico['aut'],
        "mor": c1.psico['mor'],
        "conf": c1.psico['conf'],
        "cone": c1.psico['cone'],
        "ada": c1.psico['ada'],
        "conc": c1.psico['conc'],
        "c": 1,
    }

    return render_template("combat1.html",data=data)

@app.route("/combat2")
def test2():
    # Renderizar la plantilla de la nueva página
    data = {
        "fue": c2.fisico['fue'],
        "agi": c2.fisico['agi'],
        "peso": c2.fisico['peso'],
        "res": c2.fisico['res'],
        "cons": c2.fisico['cons'],
        "arm": c2.fisico['arm'],
        "tecnica": c2.tecnica,
        "refle": c2.mental['ref'],
        "exp": c2.mental['exp'],
        "estilo": c2.mental['est'],
        "vis": c2.mental['vis'],
        "int": c2.nofisico['int'],
        "ast": c2.nofisico['ast'],
        "sab": c2.nofisico['sab'],
        "pac": c2.nofisico['pac'],
        "aut": c2.nofisico['aut'],
        "mor": c2.psico['mor'],
        "conf": c2.psico['conf'],
        "cone": c2.psico['cone'],
        "ada": c2.psico['ada'],
        "conc": c2.psico['conc'],
        "c": 2,
    }
    return render_template("combat1.html",data=data)

@app.route("/error")
def error_template():
    # Renderizar la plantilla de la nueva página
    return render_template("error.html")



@app.route("/check1", methods=["POST"])
def check1():
    checkbox_value = request.form.get("checkboxValue")
    if checkbox_value=="true":
        c1.setRandom()
        print('setRandom')
    else:
        print("FALSE")
    c1.printf()
    return ""

@app.route("/update", methods=["POST"])
def update():
    fue = int(request.form.get("fue"))
    agil = int(request.form.get("agi"))
    peso = int(request.form.get("peso"))
    res = int(request.form.get("res"))
    const = int(request.form.get("cons"))
    armor = int(request.form.get("arm"))

    refle = int(request.form.get("refle"))
    exp = int(request.form.get("exp"))
    estil = int(request.form.get("estilo"))
    vision = int(request.form.get("vis"))
    tecnica= request.form.get("tecnica")

    inte = int(request.form.get("int"))
    ast = int(request.form.get("ast"))
    sab = int(request.form.get("sab"))
    pac = int(request.form.get("pac"))
    aut = int(request.form.get("aut"))

    mor = int(request.form.get("mor"))
    conf = int(request.form.get("conf"))
    cone = int(request.form.get("cone"))
    ada = int(request.form.get("ada"))
    conc = int(request.form.get("conc"))
    c_id= request.form.get("c")
    if c_id=="1":
        print("updated 1")
        c1.setFisico(fue, agil, peso, res, const, armor)
        c1.setMental(refle, exp, estil, vision, tecnica)
        c1.setNofisico(inte, sab, ast, pac, aut)
        c1.setPsico(mor, conf, cone, ada, conc)
    if c_id=="2":
        print("updated 2")
        c2.setFisico(fue, agil, peso, res, const, armor)
        c2.setMental(refle, exp, estil, vision, tecnica)
        c2.setNofisico(inte, sab, ast, pac, aut)
        c2.setPsico(mor, conf, cone, ada, conc)

    return ""

@app.route("/check2", methods=["POST"])
def check2():
    checkbox_value = request.form.get("checkboxValue")
    if checkbox_value=="true":
        c2.setRandom()
        print('setRandom')
    else:
        print("FALSE")
    c2.printf()
    return ""

@app.route("/settings_update",  methods=["POST"])
def settings_update():
    entr= int(request.form.get("entr"))
    dblood= int(request.form.get("dblood"))
    darmor= int(request.form.get("darmor"))
    main_combat.rand=entr
    main_combat.dblood=dblood
    main_combat.darmor=darmor
    it=int(request.form.get("it"))
    print("Settings updated")
    return ""

@app.route("/run")
def run_test():
    shutil.rmtree('static/resultados')
    c1_copy = copy.deepcopy(c1)  # Crear una copia independiente de c1
    c2_copy = copy.deepcopy(c2)
    main_combat.setCs(c1_copy,c2_copy)
    
    run(main_combat,it)
    print("CORRIDA EXITOSA")
    
    return render_template("run.html")



# Iniciar el servidor de desarrollo
if __name__ == "__main__":
    app.run()
