import socket
from win10toast import ToastNotifier
from threading import Thread
import sys


SERVER_PORT = 4325
SERVER_IP = '127.0.0.1'
BUFFER_SIZE = 8192

def send_data(string_to_send,socket):
	'''The function sending the string to the server'''
	socket.send(bytes(string_to_send,"utf-8"))

def check_connected_status(ans):
	'''The function checking the connection status and printing it'''
	if ans == "Registered succefully!":
		print("Registered and connected")
		return True
	elif ans == "Username does not exist." or ans == "Password and username does not match.":
		print("connected unsuccefully username or password is wrong")
		return False
	elif ans == "Username already exist.":
		print("username exists try to remember your password")
		return False
	else:
		print("connected sucssesfully")
		return True



def main():
	try:
		uname = sys.argv[1] #get username from the user via args
		password = sys.argv[2] #get the password from the user via args
		register = sys.argv[3] #get if you are already registered or not via args
	except:
		print('Open the program in this formula:')
		print('program username password register(1 or 0)')
		exit()
	#toaster = ToastNotifier()
	client_socket = socket.socket()
	try:
		client_socket.connect((SERVER_IP, SERVER_PORT))  #connect to the server and get the connection status
		ans = client_socket.recv(BUFFER_SIZE)
		#t1 = Thread(target = toaster.show_toast, args = (str(ans),))
		#t1.start()
		print(ans)
		send_data(uname + "," + password + "," + register ,client_socket) #sending the informaton about the user
		ans = client_socket.recv(BUFFER_SIZE)
		if not check_connected_status(str(ans,"utf-8")):
			client_socket.close()
			exit()
		while True:
			pass
	except Exception as e:
		print(e)





main()
