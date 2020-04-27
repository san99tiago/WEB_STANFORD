#CODIGO PARA CREAR UNA SESION QUE PERMITA IR GUARDANDO MENSAJES Y MOSTRANDOLOS TODOS
#ADEMAS, QUE LOS VAYA GUARDANDO EN ARCHIVO.TXT EN COMPUTADOR LOCAL
#Se realizara a traves de vetor que almacene info respectiva.
#Tambien trabajaremos  con metodos GET y POST al tiempo, pero los filtraremos para usar...
#...solamente los POST al querer agregar nuevos mensajes (y GET para entrar como tal a la pagina)
#Santiago Garcia Arango, abril 2020



#Simplemente importamos datetime para crear una variable que agregaremos a lass notas (que indiquen dia y hora)
import datetime

#OJO: ahora debemos importar tanto Flask como render_template (para conectar con HTMLs)
#OJO: tambien importamos "request" para poder empezar a utilizar GET y POST como metodos adicionales de conexion
#OJO: session nos permitira tener mas control sobre el servidor como tal de Flask
#OJO: requerimos descargar librerias de flask y flask_session (son diferentes)
from flask import Flask, render_template, request, session
from flask_session import Session


#Creamos web application llamada "app" (basada en Flask), con nombre del archivo actual (__name__)
app = Flask(__name__)

#Como ahora trabajaremos con "flask_session", tendremos que especificar:
#--->SESSION_PERMANENT como False (para indicar que nuestro servidor NO es permanente)
app.config["SESSION_PERMANENT"] = False
#--->SESSION_TYPE como filesystem (para indicar que lo corremos localmente y no con otras sessiones de interfaz)
app.config["SESSION_TYPE"] = "filesystem"

#Inicializamos la session con la app desarrollada y especificada anteriormente
Session(app)


#Creamos vector que nos permitira ir guardando los mensajes que vamos creando!!!
mensajes_santi=[]


#Indicamos funcion asociada a la ruta por defecto "/" (osea si NO tiene nada de ruta adicional)
#Agregamos posibilidad de GET para conexion inicial y POST para agregar notas...
#...pero esto implica que debemos filtrar si es POST o GET en funcion(ver si se agrega o se inicia)
@app.route("/", methods=["GET","POST"])
def index():
    #En caso de que usuario realmente haya hecho el POST (osea que ya tenga mensaje escrito)
    if (request.method == "POST"):

        #Creamos variable para indicar fecha y hora actual y enviarla al html
        fecha_actual = datetime.datetime.now().strftime( "%d/%m/%Y(%I:%M%p)" )

        #Creamos mensaje ingresado junto con la fecha y hora respectiva del mismo
        nuevo_mensaje =  fecha_actual + ": " + request.form.get( "mensaje" )
        
        #Adicionamos este mensaje nuevo al vector de TODOS los mensajes
        mensajes_santi.append( nuevo_mensaje )

        #agregamos mensaje nuevo a TXT LOCAL con info del mensaje que acaba de llegar
        txt = open( "app9_MENSAJES_SANTI.txt", "a")
        txt.write( nuevo_mensaje + "\n")
        txt.close()


        #Generamos la correcta conexion con HMLT especificado y entregamos variable de vector mensajes_santi
        return( render_template("index_09.html" , mensajes_santi=mensajes_santi) )


    #La primera vez que ingresemos (primer GET), debemos indicar tambien render del index_09.html
    return( render_template("index_09.html" , mensajes_santi=mensajes_santi) )

