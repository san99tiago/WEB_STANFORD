#CODIGO PARA CONECTAR MULTIPLES HTML A TRAVES DE FLASK
#Ver que se conecta con "index_06_A.html" que se encuentra en carpeta "templates"
#Tambien se conecta con "index_06_B.html" que se encuentra en carpeta "templates"
#Lo importante es que ese segundo "index_06_B.html" se crea como "variable" (ver abajo)

#Simplemente importamos datetime para crear una variable "PSEUDO-DINAMICA" que mostraremos en HTML
import datetime

#OJO: ahora debemos importar tanto Flask como render_template (para conectar con HTMLs)
from flask import Flask, render_template


#Creamos web application llamada "app" (basada en Flask), con nombre del archivo actual (__name__)
app = Flask(__name__)

#Ahora tenemos control del puerto a emplear y activamos el debug para facilitar proceso
# Tambien cambiamos el host a nuestro gusto
app.run(port=5000 , debug=True, host='0.0.0.0')


#Indicamos funcion asociada a la ruta por defecto "/" (osea si NO tiene nada de ruta adicional)
@app.route("/")
def index():
    #Creamos variable para indicar fecha y hora actual y enviarla al html
    VARIABLE_DESDE_FLASK = datetime.datetime.now().strftime( "%d %B %Y (%I:%M%p) " )

    #Generamos la correcta conexion con HMLT especificado y entregamos variable de hora
    return( render_template("index_06_A.html", VARIABLE_DESDE_FLASK=VARIABLE_DESDE_FLASK) )

#Indicamos la funcion asociada a la otra ruta que podremos utilizar...
@app.route("/index_06_B")
def otro_index():
    #Creamos variable para indicar fecha y hora actual y enviarla al html
    VARIABLE_DESDE_FLASK = datetime.datetime.now().strftime( "%d %B %Y (%I:%M%p) " )

    #Generamos la correcta conexion con HMLT especificado y entregamos variable de hora
    return( render_template("index_06_B.html", VARIABLE_DESDE_FLASK=VARIABLE_DESDE_FLASK) )
