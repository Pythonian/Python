import socket

def Main():
	host = '127.0.0.1'
	port = 5000
	# Create a TCP socket
	s = socket.socket()
	s.bind((host, port))
	
	# Listen to one connection at a time
	s.listen(1)
	client, address = s.accept()
	print("Connection from: " + str(address))
	
	# Have the server run indefinitely
	while True:
		# Receive data from client
		data = client.recv(1024).decode('utf-8')
		# If no data, break out from the loop
		if not data:
			break
		print("From connected user: " +  data)
		data = data.upper()
		print("Sending: " + data)
		# Send data back to client, encoding it back to raw byte
		client.send(data.encode('utf-8'))
	client.close()

if __name__ == '__main__':
	Main()
