#Cñases Externas
from flask import Flask, render_template,request, session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import secrets, random
###  Clases propias ###
from db.models import setup_db,db_drop_and_create_all,usuario,GPrueba,WebS,db
from WebScrap.app import webs
from GPruebas.app import pre
import os
app = Flask(__name__)

setup_db(app)  
db_drop_and_create_all(app)

app.secret_key = os.environ["SECRET_KEY"]

####  RUTAS  ####
@app.route('/registro',methods=['GET','POST']) #REGISTRO DE USUARIOS#
def registro():
    if request.method== 'POST':

        user =  request.form['usuario']
        if request.form['pass'] == request.form['repass'] :
            passw = generate_password_hash(request.form['pass'],method="sha256")
            registro = usuario(nombre=user,PassW=passw,status = 1, admin = 0)
            db.session.add(registro)
            db.session.commit()
            flash ("Usuario creado correctamente")
        else:
            flash ("Error en la creación del Usuario")
            return render_template("creacion-user.html")  
        return redirect("/")

    return render_template("creacion-user.html")

@app.route('/',methods=['GET','POST']) #Login DE USUARIOS#
def login():
    if request.method== 'POST':
        user =  usuario.query.filter_by(nombre = request.form['user']).first()
        session['admin'] = int(user.admin if user else 0) 
        #print (user.admin)
        if user and check_password_hash( user.PassW, request.form['passw']) and user.admin == 0 and user.status == 1:
            session['user'] = user.nombre
            session['id'] = user.id
            admin = session['admin']
            print ("no admin")
            return redirect(url_for("inicio", admin = admin))
        elif user and check_password_hash( user.PassW, request.form['passw']) and user.admin == 1 and user.status == 1:
            session['user'] = user.nombre
            session['id'] = user.id
            admin = session['admin']
            return redirect(url_for("inicio", admin = admin) )
        elif user and check_password_hash( user.PassW, request.form['passw']) and user.status == 0:
            flash ("Usuario Inhabilitado")    
            return redirect("/")
        else:
            flash ("Usuario invalido")    
            return redirect("/")
    return render_template('login.html')


@app.route("/admin", methods= ['GET','POST'])
def admin():
    if not session.get('user'):
        return redirect("/")
    user = usuario.query.all()
    lista = list()
    for i in user:
        lista.append([i.id,i.nombre,i.admin,i.status])

    return render_template('administrador.html', lista = lista)


@app.route("/inh/<int:id>")
def inh(id):
    if not session.get('user'):
        return redirect("/")
    user = usuario.query.filter_by(id = id).first()
    if user.status == 1:
        user.status = 0
    else:
        user.status = 1    
    db.session.commit()
    print (str(id) + " bloqueada")
    return redirect(url_for("admin"))

@app.route("/prom/<int:id>")
def prom(id):
    if not session.get('user'):
        return redirect("/")
    user = usuario.query.filter_by(id = id).first()
    user.admin = 1
    db.session.commit()
    print (str(id) + " promovido")
    return redirect(url_for("admin"))

@app.route("/hist/<int:id>")
def hist(id):
    if not session.get('user'):
        return redirect("/")
    ide = int(id)
    print (ide)
    return redirect(url_for("historial", ide = ide))


@app.route('/usuario', methods= ['GET','POST'])
def user():
    if not session.get('user'):
        return redirect("/")
    if request.method == 'POST':
        user = usuario.query.filter_by(nombre = session['user']).first()
        
        if request.form['usuario'] and not request.form['pass']:
            user.nombre = request.form['usuario']
            db.session.commit()
            session.pop('user', None)
            session['user'] = str(user.nombre)
            flash ("Nombre de usuario cambiado exitosamente weee")
            return redirect("/inicio")

        elif  not request.form['usuario'] and request.form['pass'] == request.form["repass"]:
            if  user and check_password_hash( user.PassW, request.form['opass']): 
                user.nombre = session['user']
                user.PassW = generate_password_hash(request.form['pass'],'sha256')
                db.session.commit()
                session.pop('user', None)
                session['user'] = str(user.nombre)
                flash ("Contraseña del usuario cambiado exitosamente weey")
                return redirect("/inicio")
            else:
                flash("error PTM")   
                return render_template('gestion-user.html') 

        elif  request.form['usuario'] and request.form['pass'] == request.form["repass"]:
            if  user and check_password_hash( user.PassW, request.form['opass']): 
                user.nombre = user.form['usuario']
                user.PassW = generate_password_hash(request.form['pass'],'sha256')
                db.session.commit()
                session.pop('user', None)
                session['user'] = str(user.nombre)
                flash ("Datos del usuario cambiados exitosamente weey")
                return redirect("/inicio")
            else:
                flash("error PTM")   
                return render_template('gestion-user.html') 
        else:
            flash("error PTM")  

    return render_template('gestion-user.html')


@app.route("/logout")
def logout():
    session.pop('user', None)
    session.pop('id', None)
    session.pop("admin", None)
    return redirect("/")

@app.route('/inicio',methods=['GET','POST']) #Pagina Principal#
def inicio():
    if not session.get('user'):
        flash("Se debe Iniciar Sesión")
        return redirect("/")
    return render_template('index.html') 

@app.route('/historial')
def historial():
    if not session.get('user'):
        return redirect("/")
    lista = list()
    ide = 0
    if request.args:
        ide = request.args['ide']
    if not ide == 0: 
        his_web = db.engine.execute('select historial.id,date,webs.url from webs inner join historial on historial.id_ws = webs.id inner join usuario on usuario.id = historial.id_user where usuario.id ='+str(ide)+';')
        row_web = his_web.fetchall()
        his_pb = db.engine.execute('select historial.id, date, gpruebas.url, gpruebas.param, gpruebas.para from gpruebas inner join historial on historial.id_gp = gpruebas.id inner join usuario on usuario.id = historial.id_user where usuario.id ='+str(ide)+';')
        row_pb = his_pb.fetchall()
        
        for row in row_web:
            lista_web = [row['id'],"Web Scrap",row['date'],row['url']]
            lista.append(lista_web)

        for row in row_pb:
            lista_pb = [row['id'],"Prueba Automatizada",row['date'],row['url'],row['param'],row['para']]
            lista.append(lista_pb)
        lista.sort(reverse=True)
    else:
        his_web = db.engine.execute('select historial.id,date,webs.url from webs inner join historial on historial.id_ws = webs.id inner join usuario on usuario.id = historial.id_user where usuario.nombre ="'+session['user']+'";')
        row_web = his_web.fetchall()
        his_pb = db.engine.execute('select historial.id, date, gpruebas.url, gpruebas.param , gpruebas.para from gpruebas inner join historial on historial.id_gp = gpruebas.id inner join usuario on usuario.id = historial.id_user where usuario.nombre ="'+session['user']+'";')
        row_pb = his_pb.fetchall()
        
        for row in row_web:
            lista_web = [row['id'],"Web Scrap",row['date'],row['url']]
            lista.append(lista_web)

        for row in row_pb:
            lista_pb = [row['id'],"Prueba Automatizada",row['date'],row['url'],row['param'],row['para']]
            lista.append(lista_pb)
        lista.sort(reverse=True)

    resultados = lista

    return render_template ('historial.html', resultados = resultados)

@app.route('/web/<path:url>')
def web(url):
    if url: 
        return redirect(url_for("resultado", url = url))
    return redirect("historial")


@app.route('/pb/<path:param>')
def pb(param):
    if param:
        path = os.getcwd()
        text_file = open(path+"/"+param, "r",encoding="utf-8")
        data = text_file.read()
        text_file.close()
        dato = data.split("\n")
        print(dato)
        return redirect(url_for("pruebas", datos = dato))
    return redirect("historial")


@app.route('/pruebas',methods=['GET','POST'])
def pruebas():
    lista = (["","",""])
    val = 0
    lista3 = request.args.getlist("datos")
    if not session.get('user'):
        return redirect("/")
    if request.method == 'POST':
        param = request.form.to_dict()
        my_list = []
        for i in param.values():
            my_list.append(i)
        print (param)
        funPrueba = pre(param)     
        if funPrueba == "Exito":           
            registro = GPrueba(url=request.form['url'],param="GPruebas/Parametros/"+request.form['name']+".txt",para=str(my_list))
            db.session.add(registro)
            db.session.commit()
            regis = GPrueba.query.filter_by(url = request.form['url']).order_by(GPrueba.id.desc()).first()            
            db.engine.execute('insert into historial (date,id_gp,id_ws,id_user) values(DATE("now"),'+str(regis.id)+',NULL,'+str(session['id'])+');')
            db.session.commit()
            flash ("Ejecutando Prueba, esta se vera en otra pantalla")
            return render_template('gpruebas.html', lista = lista, val = val)
        else: 
            flash ("Error en el sistema")
            return render_template('gpruebas.html', lista = lista, val = val)

    if session.get("lista"): #Entrada por Exportacion
        val = 0
        lista2 = session.get("lista")
        session.pop("lista",None)
        return render_template('gpruebas2.html',lista = lista2, val = val)

    if not lista3 is None: #Entrada por Historial
        print (lista3)
        if lista3:
            val = int(lista3[0]) 
        else:
            val = 0    
        #val = 0 if not lista3 else int(lista3[0])
        return render_template('gpruebas.html',lista = lista3, val = val)    
    else:
        return render_template('gpruebas.html', lista = lista, val = val)    
   

@app.route('/scrapper', methods=['GET','POST'])
def scrapper():
    if not session.get('user'):
        return redirect("/")
    return render_template('web-scrapper.html') 

@app.route('/resultado', methods=['GET','POST'])
def resultado():
    if not session.get('user'):
        return redirect("/")
    if request.method== 'POST':
        web =  request.form['webs']
        resp  = webs(web)
    elif request.args:
        web = request.args['url']
        resp  = webs(web)   

    if resp:
        registro = WebS(url=web)
        db.session.add(registro)
        db.session.commit()
        regis = WebS.query.filter_by(url = web).order_by(WebS.id.desc()).first()
        db.engine.execute('insert into historial (date,id_gp,id_ws,id_user) values(DATE("now"),NULL,'+str(regis.id)+','+str(session['id'])+');')
        db.session.commit()
       
        return render_template('resultado.html',result = resp, web = web) 
    flash("No se ha introducido una URL")    
    return redirect("scrapper")


@app.route('/res', methods=['GET','POST'])
def res():
    if request.method== 'POST':
        x = int(len(request.form.to_dict()))
        param = request.form.to_dict()
        lista = list()
        lista2 = list()
        for values  in param.values():
                lista.append(values)
        print (lista)
 
        session["lista"] = lista
        return redirect(url_for("pruebas", lista = lista))
    return redirect("scrapper")

if __name__ == "__main__":
    
    app.debug = True
    app.run(debug=True)
