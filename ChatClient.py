from socket import *
serverName = 'localhost'
serverPort = 31000
clientSocket = socket(AF_INET, SOCK_DGRAM)

#Mandamos un mensaje para que el usuario se loguee y su id se agregue al diccionario del server (o sea que entre al else del serverUDP):
messagePrueba = "Prueba"
clientSocket.sendto(bytes(messagePrueba,'utf-8'),(serverName, serverPort))  # Le mandamos al servidor el mensaje y lo demás al buffer del socket del servidor.
                                                                            # Con bytes() --> Pasamos el mensaje a bytes.
identificador, serverAddress = clientSocket.recvfrom(2048) #OBtengo el id leyendo lo que me mandó el servidor.
print (identificador)

#Ahora ingresamos el Id del cliente receptor y el mensaje que se le enviará:
idAEnviar = input('ID a enviar:')    # TINE QUE SER NO BLOAQUEANTE, no tiene que esperar todoo el tiempo la rta del servidor.
message = input('Mensaje:')

#Mandamos el mensaje de arriba, ahora como ya estaría logueado entraría al IF del servidor:
clientSocket.sendto(bytes(message,'utf-8'),(serverName, serverPort))

#print (modifiedMessage)
clientSocket.close()
