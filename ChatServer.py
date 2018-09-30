from socket import *
import select
import GaboProtocol as gp

serverName = 'localhost'
serverPort = 31000

id = 0                  #Empieza en id=0
dicClients={}          #Diccionario de los clientes, contenido --> clave : valor --> Para nuestro caso es --> id : clientAddress.
#Va a ser --> dicClients={1:Adress1, 2:Adress2, ...}
def idCLiente():
    """Generates ID for each new user"""        #Contador para el id, devuelve los id (0,1,2,3,...)
    global id
    id = id+1
    return id

def separateReceptorId(message):
    """Separates the receptor's ID from the rest of the message"""
    return message.split(" ", 1) 

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))     #Escucha todas las IP que tiene (por el '') en el puerto 31000
print ("El servidor esta preparado para recibir")
while 1:
    
    print("Esperando")
    socketsReady = select.select([serverSocket], [], [])
    print("Trabajando")
    msg, clientAddress = gp.recvMessage(serverSocket)
    
    # SI la dirección del cliente coincide con su id en el diccionario, es que el tipo está logueado y le manda el mensaje a ese.
    if clientAddress in dicClients.values():
        id, msg = separateReceptorId(str(msg))
        if id in dicClients.keys():
            print(dicClients[id])
            gp.sendMessage(socket, msg, dicClients[id])
        
    else:                                    #Si no está logueado, hay que loguearlo. Agregamos la id y su adress al dic.
        id = idCLiente()                        #Genero mi id del cliente
        dicClients[id] = clientAddress         #Agregamos eso al dic para que se loguee --> dic[clave] = valor
        gp.sendMessage(serverSocket, "Your ID is: " + str(id), clientAddress) #Le enviamos al cliente su id para que la imprima.
        print("Sin loguear")