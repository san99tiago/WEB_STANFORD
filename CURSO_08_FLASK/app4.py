#CODIGO PARA CONECTAR HTMLs EXISTENTES A TRAVES DE FLASK
#Ver que se conecta con "index_04.html" que se encuentra en carpeta "templates"

#OJO: ahora debemos importar tanto Flask como render_template (para conectar con HTMLs)
from flask import Flask, render_template

#Creamos web application llamada "app" (basada en Flask), con nombre del archivo actual (__name__)
app = Flask(__name__)

#Indicamos funcion asociada a la ruta por defecto "/" (osea si NO tiene nada de ruta adicional)
@app.route("/")
def index():
    # Con esta funcion interna de flask vamos a renderizar un html desde flask (conectarlo)
    return( render_template("index_04.html") )
