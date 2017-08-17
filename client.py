import socket
from win10toast import ToastNotifier
from threading import Thread
import sys


SERVER_PORT = 4325
SERVER_IP = '127.0.0.1'
BUFFER_SIZE = 8192

def main():
	try:
		uname = sys.argv[1]
		password = sys.argv[2]
		register = sys.argv[3]
	except:
		print('Open the program in this formula:')
		print('program username password register(1 or 0)')
		exit()
	#toaster = ToastNotifier()
	client_socket = socket.socket()
	try:
		client_socket.connect((SERVER_IP, SERVER_PORT))
		ans = client_socket.recv(BUFFER_SIZE)
		#t1 = Thread(target = toaster.show_toast, args = (str(ans),))
		#t1.start()
		print(ans)
		client_socket.sendall(bytes(uname,"utf-8") + b"," + bytes(password,"utf-8") + b"," + bytes(register,"utf-8"))
		while True:
			pass
	except Exception as e:
		print(e)

main()