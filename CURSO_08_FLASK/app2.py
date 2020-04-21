#CODIGO PARA MULTIPLES ROUTES EN FLASK

#Nota: flask NO viene en librerias por defecto, debemos instalarla adicionalmente
#Recomiendo:  >>pip install flask   (hacer esto en terminal en carpeta de Scripts de Python a usar)
from flask import Flask

#Creamos web application llamada "app" (basada en Flask), con nombre del archivo actual (__name__)
app = Flask(__name__)

#Indicamos funcion asociada a la ruta por defecto "/" (osea si NO tiene nada de ruta adicional)
@app.route("/")
def index():
    return( "PRIMERA PAGINA WEB CON FLASK!!!!!")

#Creamos una ruta auxiliar encargada de crear un return diferente segun ruta http:________/santi
@app.route("/santi")
def santi():
    return("HOLA SANTI, TE FELICITO POR LO QUE ESTAS HACIENDO!!!")

#Creamos una ruta auxiliar encargada de crear un return diferente segun ruta http:________/test
@app.route("/test")
def test():
    return("test de la pagina")