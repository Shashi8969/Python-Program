import socket 
socket_server = socket.socket() 
server_host = socket.gethostname() 
ip = socket.gethostbyname(server_host) 
sport = 8080 
print("~~~ WELCOME TO THE CHAT APPLICATION ~~~") 
server_host = '192.168.1.5' 
name = input('Enter your name: ') 
socket_server.connect((server_host, sport)) 
socket_server.send(name.encode()) 
server_name = socket_server.recv(1024) 
server_name = server_name.decode() 
print(server_name,' has connected...')
while True: 
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message) 
    while True: 
        message = (socket_server.recv(1024)).decode() 
        print(server_name, ":", message)                     
        message = input("Me : ")                      
        socket_server.send(message.encode())     
