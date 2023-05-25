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


while op != 5:

    os.system("clear")
    print "\t\t============== Bem Vindo ================"
    print "\t\t=== Sistema de Gerenciamento de Redes ==="
    print "\t\t========================================="
    print "\t\t= [1]  Executar Comandos               "
    print "\t\t= [2]  Calcular QOS	  	        "
    print "\t\t= [3]  Bloquear Internet	              "
    print "\t\t= [4]  Bloquear Mouse	              "
    print "\t\t= [5]  Finalizar Programa              "
    print "\t\t========================================="
    op =int(raw_input("Entre com uma opcao:\n# "))
    os.system("clear")
	
    if op == 1:
	UDPSock.sendto(str(op),(addr))
	comando = ""
	while True:
	  if comando == "q" or comando == "Q":
	      break
	  else:
	      
	      
	      print("\t\t--------------------------------------------------")
	      print("\t\tPara voltar ao menu principal digite-> [q] or [Q]")
	      print("\t\tDigite ->clear<- para limpar a tela")
	      print("\t\t--------------------------------------------------")
	      
	      comando = raw_input("entre com um comando:")
	      UDPSock.sendto(comando,(addr))
	      dados,addr = UDPSock.recvfrom(buf)
	      print dados
	 
	      
    elif op == 2:  
	UDPSock.sendto(str(op),(addr))
	qntPing= 0
	endereco = ""
	pings = " "
	while True:
	     
	     if endereco != "q" or pings != "q":
	          endereco = raw_input("Entre com um endereco: ")
		  pings = raw_input("Entre com a Qntdade de Pings: ")
		  recebe = str(endereco+' '+ pings)
		  UDPSock.sendto(recebe,addr)
		  linha,addr = UDPSock.recvfrom(buf)
		  print("\t\t--------------------------------------------------")
		  print("			Calculo do Qos		       ")
		  print("\t\t--------------------------------------------------")
		  print linha
		  time.sleep(0.20)
	     else:
		   break
		  
    elif op==3:
	UDPSock.sendto(str(op),(addr))
	choose = "sim"
	while 1:
	  if choose == "q":
		break
	  else:
		print("\t\t--------------------------------------------------")
		print("\t\tPara voltar ao menu principal digite-> [q] or [Q]")
		print("\t\t--------------------------------------------------")
		choose = raw_input("Deseja Bloquear a Internet?")
		if choose == "sim":
		    os.system("clear")
		    print "--------------------------------"
		    print "	Internet Bloqueada"
		    print "--------------------------------"
		    UDPSock.sendto(choose,addr) 
		    recebe,addr = UDPSock.recvfrom(buf)
		    print recebe
		    
		elif choose == "nao":
		    os.system("clear")
		    print "--------------------------------"
		    print "	Internet Liberada	   "
		    print "--------------------------------"
		    UDPSock.sendto(choose,addr)
		    bloquear, addr = UDPSock.recvfrom(buf)
		    print bloquear
    elif op == 4:
	  UDPSock.sendto(str(op),(addr))
	  option = "sim"
	  while 1:
	    if option == "q" or option == "Q":
		  break
	    else:
		  print("\t\tPara voltar ao menu principal digite-> [q] or [Q]")
		  option = raw_input("Deseja Bloquear a Mouse?")
		  if(option == "sim"):
		      UDPSock.sendto(option,addr)
		      mouse, addr = UDPSock.recvfrom(buf)
		      print ("Mouse Bloqueado!")
		  elif(option == "nao"): 
		      UDPSock.sendto(option,addr)
		      mouse1, addr = UDPSock.recvfrom(buf)
		      print ("Mouse Desbloquedo!")
			  
		      
		    
		  

	
	
  # Close socket
UDPSock.close()
