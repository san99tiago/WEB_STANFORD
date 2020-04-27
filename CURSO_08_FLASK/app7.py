#CODIGO PARA CONEXION A MULTIPLES PAGINAS HTML Y AHORA TENDREMOS UN LAYOUT COMUN BASE
#Esto lo que busca es conectar "index_07_A.html" y "index_07_B.html" con un LAYOUT COMUN...
#...de tal forma que ambos tendran un mismo "layout_07.html" principal, y solamente la diferencias...
#...puntuales iran en el archhivo especifico de index_07_A.html" y "index_07_B.html".
#Esto es fundamental, porque podremos crear un layout principal complejo, y solamente hacer...
#...los cambios en los respectivos archivos puntuales, SIN tener tanto codigo en cada HTML heredado.
#NOTA: este "layout_07.html" se encuentra tambien en los archivos de carpeta templates!!!

#Simplemente importamos datetime para crear una variable "PSEUDO-DINAMICA" que mostraremos en HTML
import datetime

#OJO: ahora debemos importar tanto Flask como render_template (para conectar con HTMLs)
from flask import Flask, render_template


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
    return( render_template("index_07_A.html", VARIABLE_DESDE_FLASK=VARIABLE_DESDE_FLASK) )

#Indicamos la funcion asociada a la otra ruta que podremos utilizar...
@app.route("/index_07_B")
def otro_index():
    #Creamos variable para indicar fecha y hora actual y enviarla al html
    VARIABLE_DESDE_FLASK = datetime.datetime.now().strftime( "%d %B %Y (%I:%M%p) " )

    #Generamos la correcta conexion con HMLT especificado y entregamos variable de hora
    return( render_template("index_07_B.html", VARIABLE_DESDE_FLASK=VARIABLE_DESDE_FLASK) )
