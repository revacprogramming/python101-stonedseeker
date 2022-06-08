# Network Programming
# https://www.py4e.com/lessons/network

<<<<<<< HEAD
=======
# Network Programming
# https://www.py4e.com/lessons/network

>>>>>>> 81ea93cf55ff3b4a15b73c140f5184a6f0bd29f9
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org',80))  
# # 
#from cgitb import html


# GET http://www.dr-chuck.com/page2.html

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
    
mysock.close()
