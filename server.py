import socket
from threading import Thread

LISTENING_PORT = 4325
unamePass = {}

def send_data(string_to_send,socket):
	socket.send(bytes(string_to_send))

def main():
	listening_socket = socket.socket()
	listening_socket.bind(('0.0.0.0', LISTENING_PORT))
	listening_socket.listen(10)
	while True:
		partner_socket, partner_addr = listening_socket.accept()
		t1 = Thread(target = proccess_socket, args = (partner_socket,))
		t1.start()

def proccess_socket(partner_socket):
	try:
		partner_socket.send(b'connected')
		temp = (str(partner_socket.recv(8192),"utf-8").split(","))
		if temp[0] not in unamePass:
			if temp[3] = '1':
				unamePass[temp[0]] = temp[1]
				partner_socket.send(b'Registered succefully!')
			else:
				partner_socket.send(b'Username does not exist.')
		else:
			if temp[3] = '1':
				partner_socket.send(b'Username already exist.')
			else:
				if temp[1] == unamePass[temp[0]]:
					partner_socket.send(b'Connected succefully!')
				else:
					partner_socket.send(b'Password and username does not match.')

		print(unamePass)
	except Exception as e:
		print(e)

main()