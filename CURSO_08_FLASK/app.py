#Ahora comenzaremos a trabajar con FLASK!!!!
#Esta herramienta es un framework que nos facilita el trabajo para desarrollo de paginas web.
#El objetivo de este es facilitar el monitoreo y manejo de "requests" y "responses"

#Nota: flask NO viene en librerias por defecto, debemos instalarla adicionalmente
#Recomiendo:  >>pip install flask   (hacer esto en terminal en carpeta de Scripts de Python a usar)
from flask import Flask

#Creamos web application llamada "app" (basada en Flask), con nombre del archivo actual (__name__)
app = Flask(__name__)

#Indicamos funcion asociada a la ruta por defecto "/" (osea si NO tiene nada de ruta adicional)
@app.route("/")
def index():
    return( "PRIMERA PAGINA WEB CON FLASK!!!!!")

