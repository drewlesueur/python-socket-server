import socket
import select
import time

#http://forums.devshed.com/python-programming-11/a-few-socket-questions-75012.html
#http://davidf.sjsoft.com/mirrors/mcmillan-inc/sock1.html
#try assyncore

#create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port



port = 5555
serversocket.bind((socket.gethostname(), port)) #this is the one you want
#serversocket.bind(("127.0.0.1", port))
"""
	to connect if you have a router
	type ipconfig in dos and get your routers ip address
	eg: 192.168.1.105
"""


#become a server socket
serversocket.listen(5)


serversocket.setblocking(0)
#serversocket.settimeout(10000);

#serversocket.setblocking(0)
#serversocket.settimeout(.01);

def handle_data(data):
	if data[0:len("<policy-file-request/>")] == "<policy-file-request/>":
		print socko.send('<?xml version=\"1.0\"?><cross-domain-policy><allow-access-from domain="*" to-ports= "*" /></cross-domain-policy>')
		print "sent policy file"
		closesocket(socko)
	else:
		print "you said" + data


connections = []
conn_info = [];
counter = 0;
print "going to listen on port " + str(port)


def closesocket(socko):
	socko.close()
	connections.remove(socko) #remove is pretty cool if it works!
	socko = None

while 1: 
	
	"""counter = counter + 1
	if counter == 1000:
		counter = 0
		print "reset"
		for y in range(0,len(connections)):
			print conn_info[y] """

	time.sleep(.001) #change this in the future for speed
	ready_to_read, ready_to_write, in_error = select.select([serversocket],[],[],0) #should I change that 0 to .001
	
	#print len(ready_to_read)
	
	for sock in ready_to_read:
		print "test"		
		(clientsocket, address) = sock.accept()
		#print clientsocket
		#print address
		print "putting " + address[0] + " onto connections";
			
		conn_info.append(address)
		
		clientsocket.setblocking(0)
		connections.append(clientsocket)
		print len(connections)
		
		
	if len(connections) > 0:
		to_read, to_write, to_error = select.select(connections,connections,connections,0)
		for socko in to_read:
			#i needed this try block only for google chrome! wierd.
			try:
				data = socko.recv(1024) #1024 potential problem causer
			except socket.error, msg:
				closesocket(socko)
				break
				
			print data
			if not data:
				print "no data"
				closesocket(socko)
				break
			try:
				#print "this is the first" + data[0]
				#for flash policy stuff
				#socko.send(data)
				for sockwrite in to_write:
					print "test"
					ret = handle_data(data)
					if ret != None:
						sockwrite.send(ret)
					
				#print socko.send("HTTP/1.0 200 OK\r\n")
				#print socko.send("Content-Type: text/html\r\n")
				#socko.send("Content-Length: 16\r\n\r\nThis is the text")
				print "i sent output"
			except socket.error, msg:
				closesocket(socko)
		
		for socko in to_error:
			print socko + " had an error"
    
