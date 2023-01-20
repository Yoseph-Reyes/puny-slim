from flask_sqlalchemy import SQLAlchemy
import datetime, os

db = SQLAlchemy()

def setup_db(app):
    dbdir = "sqlite:///"+os.path.abspath(os.getcwd())+'\db\database.db' #Ruta de la base de datos\
    app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

def db_drop_and_create_all(app):
    with app.app_context():
       # db.drop_all()
        db.create_all()

class usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # plays nice with all major database engines
    nombre = db.Column(db.String(20), unique= True, nullable = False) 
    PassW = db.Column(db.String(80), nullable = False)
    admin = db.Column(db.Integer, default = 0, nullable = False)
    status = db.Column(db.Integer, default = 1, nullable = False) 

class historial(db.Model):
    __tablename__ ="historial"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # plays nice with all major database engines
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    id_gp = db.Column(db.Integer,db.ForeignKey('gpruebas.id'))
    id_ws = db.Column(db.Integer,db.ForeignKey('webs.id'))
    id_user = db.Column(db.Integer,db.ForeignKey('usuario.id')) 
    
class GPrueba(db.Model):
    __tablename__ = "gpruebas"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # plays nice with all major database engines
    url = db.Column(db.String(100)) 
    param = db.Column(db.String(600)) 
    para = db.Column(db.String(600))
    #id_gp = db.Column(db.Integer,db.ForeignKey('historial.id_gp')) 

class WebS(db.Model):
    __tablename__ = "webs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # plays nice with all major database engines
    url = db.Column(db.String(100)) 
    


'''import sqlite3 as sql


def insertUser(username,password):
    con = sql.connect("db/base.db")
    cur = con.cursor()
    cur.execute("INSERT INTO usuario (nombre,PassW) VALUES (?,?)", (username,password))
    con.commit()

    con.close()
    return ("exito")


def retrieveUsers(user,passw):
	con = sql.connect("db/base.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM usuario where nombre = '"+user+"' and PassW = '"+passw+"'")
	login = cur.fetchone()
	con.close()
    
	return login'''

