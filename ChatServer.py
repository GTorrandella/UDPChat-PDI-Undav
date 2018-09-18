from socket import *
import GaboProtocol as gp

id = 0                  #Empieza en id=0
dicCLientes={}          #Diccionario de los clientes, contenido --> clave : valor --> Para nuestro caso es --> id : clientAddress.
#Va a ser --> dicCLientes={1:Adress1, 2:Adress2, ...}
def idCLiente():        #Contador para el id, devuelve los id (0,1,2,3,...)
    global id
    id = id+1
    return id

#def parsearMsje (mensaje):
    #para obtener el id!? porque eñ mesje esta formado por 2 cositas

def enviarMsje(id, mensaje):
   serverSocket.sendto(bytes(str(mensaje),'utf-8'), (dicCLientes.get(identificador)))

serverPort = 31000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))     #Escucha todas las IP que tiene (por el '') en el puerto 31000
print ("El servidor esta preparado para recibir")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)    #leeme los 2048 bytes del buffer del socket y la parte de datos del paquete lo pone en message y la dirección del cliente en clientAddress.
    modifiedMessage = message.upper()       #lo pasamos a mayuscula

    # SI la dirección del cliente coincide con su id en el diccionario, es que el tipo está logueado y le manda el mensaje a ese.
    if clientAddress in dicCLientes.values():
        enviarMsje(identificador, modifiedMessage)
        print("Estoy logueado")

    else:                                    #Si no está logueado, hay que loguearlo. Agregamos la id y su adress al dic.
        identificador = idCLiente()                        #Genero mi id del cliente
        dicCLientes[identificador] = clientAddress         #Agregamos eso al dic para que se loguee --> dic[clave] = valor
        serverSocket.sendto(bytes(str(identificador),'utf-8'),clientAddress)  #Le enviamos al cliente su id para que la imprima.
        print("Sin loguear")

#Cuando le enviamos al cliente su id? --> #
