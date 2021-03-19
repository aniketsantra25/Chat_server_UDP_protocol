import socket
import time
import threading
import sys


def reciever(ip, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((ip, port))
	while True:
		r = s.recvfrom(1024)
		print("\t\t\tRecieved Message : ",r[0].decode())
		time.sleep(0.3)

def sender(ip2, port2):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	while True:
		text = input()
		s.sendto(text.encode(), (ip2,port2))
		print("Your Message: " , text)
		time.sleep(0.2)

ip = input("Enter Reciever's IP address : ")
port = int(input("Enter Reciever's port number : "))

ip2 = input("Enter Sender's IP address : ")
port2 = int(input("Enter Sender's port number : "))

x1 = threading.Thread(target=sender, args=(ip2, port2))
x2 = threading.Thread(target=reciever, args=(ip, port))

x1.start()
x2.start()
                
