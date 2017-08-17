import socket
from threading import Thread
from hashlib import md5	

LISTENING_PORT = 4325
unamePass = {}

def main():
	listening_socket = socket.socket()
	listening_socket.bind(('0.0.0.0', LISTENING_PORT))
	listening_socket.listen(10)
	while True:
		partner_socket, partner_addr = listening_socket.accept()
		t1 = Thread(target = proccess_socket, args = (partner_socket,))
		t1.start()

def send_data(string_to_send,socket):
	'''The function sending the string to the client'''
	socket.send(bytes(string_to_send,"utf-8"))

def read_users():
	'''The funcion reading the usernames and the passwords from the users.dat file.'''
	global unamePass
	try:
		file = open('users.dat', 'r')
		data = file.read()
		unamePass = json.loads(data)
		file.close()
	except Exception as e:
		print(e)

def register_user(uname, password):
	global unamePass
	file = open('users.dat', 'rb+')
	file.seek(-1, 2)
	file.truncate()
	m = md5(password.encode("utf-8"))
	unamePass[uname] = m.hexdigest()
	file.write(', "' + uname + '":"' + unamePass[uname] + '"}')
	file.close()


def proccess_socket(partner_socket):
	try:
		partner_socket.send(b'connected')
		temp = (str(partner_socket.recv(8192),"utf-8").split(","))
		print('message: ' + str(temp))
		if temp[0] not in unamePass:  #checking if the username does not exist.
			if temp[2] == '1':  #checking if the user want to register.
				register_user(temp[0], temp[1])
				send_data('Registered succefully!', partner_socket)
			else:
				send_data('Username does not exist.', partner_socket)
		else:  #the username exist
			if temp[2] == '1':  #the user want to register
				send_data('Username already exist.', partner_socket)
			else:
				if temp[1] == unamePass[temp[0]]:  #checking if the password is equals to the password that sent.
					send_data('Connected succefully!', partner_socket)
				else:  #the password is wrong.
					send_data('Password and username does not match.', partner_socket)

		print(unamePass)
	except Exception as e:
		print(e)

main()