#CODIGO PARA CONECTAR HTML A TRAVES DE FLASK Y ENTREGAR VARIABLE Y VECTOR VARIABLES  A HTML
#Ver que se conecta con "index_05.html" que se encuentra en carpeta "templates"

#Simplemente importamos datetime para crear una variable "PSEUDO-DINAMICA" que mostraremos en HTML
import datetime

#Importamos libreria random para poder generar condiciones aleatorias y mostrar cambios facil
import random

#Crearemos nombres completos aleatorios, para correcta pagina web dinamica
NOMBRES = ["Santiago","Monica","Mariana","Jaime","Gabriel","Miguel","Juan","Elkin","Juanita","Silvia","Leonor","Miguel","Manuela","Hans","Jose",
            "Mauricio","Guillermo","Diana","Melissa","Camila","Juliana","Valentina","Laura","Sebastian","Maria","Isabela","Daniela","Lorena",
            "Lorenzo","Camilo","Eliana","Elizabeth","Martin","Jairon","Amparo","Jorge","Adriana","Oscar","Kim","Tatiana","Kelly","Doris","Ana"]
APELLIDOS = ["Mercedee","Sosa","Garcia","Arango","Ortega","Molina","Smith","Saldarriaga","Gutierrez","Palacio","Medina","Gomez","Arango","Diaz",
            "Hill","Donadio","Copello","Rendon","Ruiz","Guerra","Perico","Hernandez","Lopez","Giraldo","Echeverry","Dominguez","Murillo","Sol",
            "Upegui","Bustamante","Ramirez","Castanno","Posada","Alvarez","Madrir","Restrepo","Areiza","Blandon","Perez","Correa","Mendez",
            "Isaza","Renteria","Rodas","Barrreneche","Berrio","Castro","Castellano","Ceballos","Toretto","Toricelli","Idarra","Zapata","Yepes",
            "Villamil","Contreras","Arauco","Beltran","Rios","Velazques","Llano","Escobar","Cardenas","Bonaparte","Wolf","Padilla","Mendoza"]


#OJO: ahora debemos importar tanto Flask como render_template (para conectar con HTMLs)
from flask import Flask, render_template


#Creamos web application llamada "app" (basada en Flask), con nombre del archivo actual (__name__)
app = Flask(__name__)

#Indicamos funcion asociada a la ruta por defecto "/" (osea si NO tiene nada de ruta adicional)
@app.route("/")
def index():
    #Creamos variable para indicar fecha y hora actual y enviarla al html
    VARIABLE_DESDE_FLASK = datetime.datetime.now().strftime( "%d %B %Y (%I:%M%p) " )

    #Creamos una cantidad de nombres aleatoria entre 3 y 20 (para mostrarlos)
    VARIABLE_CANTIDAD_NOMBRES = random.randint(3,20)
    #Creamos vector nombres, para poder almacenar en este, la cantidad aleatoria de todos estos nombres
    VECTOR_NOMBRES = []
    for _ in range(VARIABLE_CANTIDAD_NOMBRES):
        #Creamos la cantidad de nombres aleatorias elegidas y cada uno con un nombre y 2 apellidos
        VECTOR_NOMBRES.append( random.choice(NOMBRES) + " " + random.choice(APELLIDOS) + " " + random.choice(APELLIDOS) + "." )

    #Con esta funcion interna de flask vamos a renderizar un html desde flask (conectarlo)
    #Tambien vamos a agregar las variables a integrar con el HTML, de tal forma que se puedan incluir en HTML correctas
    #En este caso incluimos la fecha actual, la cantidad de nomrbes a generar aleatorios y el vector de nombres aleatorios
    return( render_template("index_05.html", VARIABLE_DESDE_FLASK=VARIABLE_DESDE_FLASK, VARIABLE_CANTIDAD_NOMBRES=VARIABLE_CANTIDAD_NOMBRES, VECTOR_NOMBRES=VECTOR_NOMBRES) )
