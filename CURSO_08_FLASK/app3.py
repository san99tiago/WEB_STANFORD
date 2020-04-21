#CODIGO PARA MULTIPLES ROUTES EN FLASK PERSONALIZADAS SEGUN RUTA INGRESADA

#Nota: flask NO viene en librerias por defecto, debemos instalarla adicionalmente (pip install flask)
from flask import Flask

#Creamos web application llamada "app" (basada en Flask), con nombre del archivo actual (__name__)
app = Flask(__name__)

#Indicamos funcion asociada a la ruta por defecto "/" (osea si NO tiene nada de ruta adicional)
@app.route("/")
def index():
    return( "PRIMERA PAGINA WEB CON FLASK!!!!!")

#Creamos ahora una ruta PERSONALIZADA donde se puede ingresar LO QUE SEA!!!!
#Ahora, el servidor nos muestra un saludo, seguno lo ingresado respectivamente
@app.route("/<string:nombre>")
def saludar(nombre):
    nombre = nombre.upper()
    return("BUENOS DIAS, " + nombre + " <3")