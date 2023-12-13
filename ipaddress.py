#importing the socket library
import socket
#getting the hostname
hostname = socket.gethostname()
#Now getting the ip adress
ip =socket. gethostbyname(hostname)
#prints the ip adress
print("Your ip address is : " + ip)