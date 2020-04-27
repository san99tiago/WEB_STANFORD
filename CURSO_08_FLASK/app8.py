#CODIGO PARA PROCESAR HTML PRINCIPAL, CREAR UN POST REQUEST Y PROCESAR ESTA INFO
#Santiago Garcia Arango, abril 2020
#Nos permite entonces conectar el backend con mayor versatilidad e interactividad

#Simplemente importamos datetime para crear una variable "PSEUDO-DINAMICA" que mostraremos en HTML
import datetime

#OJO: ahora debemos importar tanto Flask como render_template (para conectar con HTMLs)
#OJO: tambien importamos "request" para poder empezar a utilizar POST como metodo adicional de conexion
from flask import Flask, render_template, request


#Creamos web application llamada "app" (basada en Flask), con nombre del archivo actual (__name__)
app = Flask(__name__)

#Ahora tenemos control del puerto a emplear y activamos el debug para facilitar proceso
app.run(port=5000 , debug=True)


#Indicamos funcion asociada a la ruta por defecto "/" (osea si NO tiene nada de ruta adicional)
@app.route("/")
def index():
    #Creamos variable para indicar fecha y hora actual y enviarla al html
    VARIABLE_DESDE_FLASK = datetime.datetime.now().strftime( "%d %B %Y (%I:%M%p) " )

    #Generamos la correcta conexion con HMLT especificado y entregamos variable de hora
    return( render_template("index_08_A.html", VARIABLE_DESDE_FLASK=VARIABLE_DESDE_FLASK) )


#Creamos forma de procesar un "request" tipo "POST" desde HTML
#Esta funcion nos permitira procesar el POST y llevarlos a otra "url" personalizada con su info
#NOTA: al indicar metodo POST... solamente permite acceso a traves de llamar al POST, de lo contrario...
#...NO permitira acceder. (Esto permite entonces diferenciar entre POST y GET y filtrarlos respectivamente)
@app.route("/index_08_B" , methods=["POST"])
def otro_index():
    #Creamos variable para indicar fecha y hora actual y enviarla al html
    VARIABLE_DESDE_FLASK = datetime.datetime.now().strftime( "%d %B %Y (%I:%M%p) " )

    #Realizamos un request para obtener info asociada a "form" con nombre "nombre"
    #De tal forma que logramos obtener nombre de usuario, desde HTML y lo procesamos aqui
    nombre = request.form.get( key="nombre" )
    nombre = nombre.upper()

    #Realizamos un request para obtener info asociada a "form" con nombre "edad"
    #De tal forma que logramos obtener edad de usuario, desde HTML y lo procesamos aqui
    edad = request.form.get( key="edad" )

    #Generamos la correcta conexion con HMLT especificado y entregamos variable de hora
    #Ahora ademas de generar conexion con HTML, entregamos el nombre obtenido desde "index_08_A.html"
    return( render_template("index_08_B.html", nombre=nombre, edad=edad, VARIABLE_DESDE_FLASK=VARIABLE_DESDE_FLASK) )
