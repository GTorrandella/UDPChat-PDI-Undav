from socket import *
import GaboProtocol as gp

serverName = 'localhost'
serverPort = 31000

def InitSocket():
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    return clientSocket

def CloseSocket(socket):
    socket.close()
    
def main():
    
    clientSocket = InitSocket()
    #Mandamos un mensaje para que el usuario se loguee y su id se agregue al diccionario del server (o sea que entre al else del serverUDP):
    messagePrueba = "Prueba"
    clientSocket.sendto(bytes(messagePrueba,'utf-8'),(serverName, serverPort))  # Le mandamos al servidor el mensaje y lo demás al buffer del socket del servidor.
                                                                                # Con bytes() --> Pasamos el mensaje a bytes.
    identificador, serverAddress = clientSocket.recvfrom(2048) #OBtengo el id leyendo lo que me mandó el servidor.
    print("Identificador cliente: " + str(int(identificador)))  # Si pongo solo print(identificador) me imprime b'1' indicando que son bytes.
    
    #Ahora ingresamos el Id del cliente receptor y el mensaje que se le enviará:
    idAEnviar = input('ID a enviar:')    # TINE QUE SER NO BLOAQUEANTE, no tiene que esperar todoo el tiempo la rta del servidor.
    message = input('Mensaje:')
    
    #Mandamos el mensaje de arriba, ahora como ya estaría logueado entraría al IF del servidor:
    gp.SendMessage(clientSocket, message)
    
    #print (modifiedMessage)
    CloseSocket(clientSocket)
    
main()