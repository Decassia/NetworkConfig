# Programa Cliente
# Joanna de Cassia Valadares - 12/03/2012


from socket import *
import os
import commands
import time

# Set the socket parameters
#host = "localhost"

host = raw_input("Entre com um ip: ")
port = 5555
buf = 2048
addr = (host,port)

# Create socket
UDPSock = socket(AF_INET,SOCK_DGRAM)


op = 0	
op1 = 0


while op != 3:
	
	os.system("clear")
	print "\t\t============== Bem Vindo ================"
	print "\t\t=== Sistema de Gerenciamento de Redes ==="
	print "\t\t========================================="
	print "\t\t= [1]  Executar Comandos                ="
	print "\t\t= [2]  Calcular QOS	  	           ="
	print "\t\t= [3]  Finalizar Programa               ="
	print "\t\t========================================="
	op =int(raw_input("Entre com uma opcao:\n# "))
	os.system("clear")
	if op == 1:
	    data = ""
	    while True:
	      if data == "q" or data == "Q":
		  break
	      else:
		
		  print("\t\t==============================================================")
		  print("\t\tPara voltar ao menu principal digite-> [q] or [Q]")
		  print("\t\tDigite ->clear<- para limpar a tela")
		  print("\t\tPara executar arquivos em PDF digite XPDF <nome do arquivo>")
		  print("\t\t==============================================================")
		
		  data = raw_input("Entre com um comando # ")
		  UDPSock.sendto(data,(addr))
		  dados,addr = UDPSock.recvfrom(buf)
		  print dados
		  
		      
		 
# Close socket
UDPSock.close()