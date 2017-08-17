import socket
from win10toast import ToastNotifier
from threading import Thread
import sys


SERVER_PORT = 4325
SERVER_IP = '127.0.0.1'
BUFFER_SIZE = 8192

def send_data(string_to_send,socket):
	socket.send(bytes(string_to_send,"utf-8"))


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
		client_socket.connect((SERVER_IP, SERVER_PORT)) #connect to the server and get the connection status
		ans = client_socket.recv(BUFFER_SIZE)
		#t1 = Thread(target = toaster.show_toast, args = (str(ans),))
		#t1.start()
		print(ans)
		send_data(uname + "," + password + "," + register ,client_socket) #sending the informaton about the user
		while True:
			pass
	except Exception as e:
		print(e)




main()
