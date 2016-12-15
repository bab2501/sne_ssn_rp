import socket
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


for letter1 in alphabet:
	for letter2 in alphabet:
		for letter3 in alphabet:
			for letter4 in alphabet:
				command = letter1+letter2+letter3+letter4
				#print command+"\r\n"+"\r\n"

				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				#print "Socket Created"
				port = 9220
				ip = "192.168.1.120"

				s.connect ((ip, port))
				#print "Socket Connected to HOST on ip "+ ip

				reply = ''
				while True:
				    message = command+"\r\n"
				    reply += s.recv(1024)
				    if not reply:
					break
				    #break
				    if '220 HP GGW server (version 1.0) ready' in reply:
					s.sendall(message)
					break
				noot= s.recv(65535)
				print noot
