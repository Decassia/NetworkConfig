# Programa Servidor
# Joanna de Cassia Valadares - 12/03/2012

from socket import *
import commands

host = "0.0.0.0"
port = 5555
buf = 2048
addr = (host,port)

print 'Esperando Conexao...'
UDPSock = socket(AF_INET,SOCK_DGRAM)
UDPSock.bind(addr)
qntPing = 5
joanna = ' '
op = 1
while 1:
    
	    data,addr = UDPSock.recvfrom(buf)
	    cmd1 = commands.getoutput(data)
	    var = open("arquivo2.txt","w")
	    texto = var.write(cmd1) 
	    var = open("arquivo2.txt","r")
	    linhas = var.read()
	    UDPSock.sendto(linhas,addr)
	    print 'Conexao vinda de:', addr

	    var.close()
	 

# Close socket
UDPSock.close()