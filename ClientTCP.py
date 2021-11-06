import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345)) #connecting with server
playload="Hey server"

try:
    while True:
        client_socket.send(playload.encode('utf-8'))
        request = client_socket.recv(1024)
        print(str(request))
        more= input("Press Enter to continue (digit x to exit): ")
        if more.lower()!="exit": # if the input is different of exit
            playload=input("Write a message: ") #send menssage for server
        else:
            break
except KeyboardInterrupt:
    print("")
client_socket.close()