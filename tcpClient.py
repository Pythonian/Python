import socket

def Main():
	host = '127.0.0.1'
	port = 5000

	# Create socket object
	s = socket.socket()
	# Connect to the server
	s.connect((host, port))

	# Get message from user
	message = input("-> ")
	while message != 'q':
		s.send(message.encode('utf-8'))
		# Receive data from the server
		data = s.recv(1024).decode('utf-8')
		print("Received from server: " + data)
		message = input("-> ")
	s.close()

if __name__ == '__main__':
	Main()

