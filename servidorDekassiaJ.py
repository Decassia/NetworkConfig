# Programa Servidor
# Joanna de Cassia Valadares - 12/03/2012

from socket import *
import commands,os
#from Qos import *
def qos(endereco,qntPing):
    joanna = ' '

    #endereco = raw_input("Entre com um endereco: ")
    cmd = commands.getoutput("ping -c %s %s | awk -F = {'print $4'} | awk {'print $1'}|awk 'NF>0'>a.txt" %(qntPing,endereco))				
    cmd1 = commands.getoutput("ping -c%s %s|grep ttl| awk -F = {'print $3 * 2'}|awk 'NF>0' > t.txt " %(qntPing,endereco))
    cmd = open("a.txt","r")
    pega = cmd.readlines()
    linhas = pega
    cmd1 = open("t.txt","r")
    pegaVazao = cmd1.readlines()
    lines = pegaVazao


    #print linhas

    i =0
    tempo = 0.0
    time= 0.0 
    jitter = 0.0
    j = 1
    perda = 0.0

    while i <= qntPing:
	for linha in linhas:
	    time = float(linha)
	    tempo += time
	  
	for l in linhas:
	    jitter +=time - float(linhas[j-1])
	    j+1
	    if(jitter < 0):
	      jitter *(-1)
	    
	    
	for line in lines:
	    pegaVazao = float(line)
	    perda = pegaVazao * int(qntPing)
		    
      
	break
	
    #print jitter

    #atraso   
    atraso = tempo/2
    totalAtraso = atraso/qntPing
    #print 'O valor do atraso eh:',totalAtraso
    #Jitter
    totalJitter = jitter/qntPing
    #print 'O valor do Jitter eh:', totalJitter

    #Vazao
    totalPerda = perda/tempo
    #print 'A vazao(perda) eh:', totalPerda
    
    qos = 'Atraso: '+ str(totalAtraso)+'\n'  + 'Jitter:'+ str(totalJitter)+'\n' +  'Perda: ' + str(totalPerda)

    cmd.close()
    cmd1.close()

    return qos
    

      
host = "0.0.0.0"
port = 5555
buf = 2048
addr = (host,port)

print 'Esperando Conexao...'
UDPSock = socket(AF_INET,SOCK_DGRAM)
UDPSock.bind(addr)
qntPing = 5
joanna = ' '
dekassia = ''
decassia = ''
data = ''
endereco = ''
op,addr = UDPSock.recvfrom(buf)
while True:
    
     if len(op) == 1:
	 if int(op) == 1:
	  print op
	  while 1:
	    data,addr = UDPSock.recvfrom(buf)
	    cmd1 = commands.getoutput(data)
	    var = open("arquivo2.txt","w")
	    texto = var.write(cmd1) 
	    var = open("arquivo2.txt","r")
	    linhas = var.read()
	    UDPSock.sendto(linhas,addr)

	    var.close()
	   
	 elif int(op) == 2:
	    print op
	    endereco,addr = UDPSock.recvfrom(buf)
	    print endereco
	    cmd = qos(endereco.split(' ')[0],int(endereco.split(' ')[1]))
	    UDPSock.sendto(cmd,addr)
	    
	 elif int(op) == 3:
	      print op
	      choose,addr = UDPSock.recvfrom(buf)
	      if choose == "sim":
	          commands.getoutput("iptables -A OUTPUT -p udp --dport 80  -j DROP")
	          commands.getoutput("iptables -A OUTPUT -p tcp --dport 80  -j DROP")
	          commands.getoutput("iptables -A OUTPUT  -p udp --dport 3128  -j DROP")
	          commands.getoutput("iptables -A OUTPUT  q-p tcp --dport 3128  -j DROP")
	          chains = commands.getoutput("iptables -L")
	          UDPSock.sendto(chains,addr)
	      elif choose == "nao":
	          commands.getoutput("iptables -D OUTPUT -p udp --dport 80  -j DROP")
	          commands.getoutput("iptables -D OUTPUT -p tcp --dport 80  -j DROP")
	          commands.getoutput("iptables -D OUTPUT -p udp --dport 3128  -j DROP")
	          commands.getoutput("iptables -D OUTPUT -p tcp --dport 3128  -j DROP")
	          chain = commands.getoutput("iptables -L")
	          UDPSock.sendto(chain,addr)
	     
	      
	 elif int(op) == 4:
		  print op
		  option,addr = UDPSock.recvfrom(buf)
		  print option
		  mouse = commands.getoutput( "xinput list | grep slave |grep pointer| awk -F 'id=' {'print $2'} | awk -F ' ' {'print $1'}")
		  if option == "sim":
		      for i in mouse:
			  pegaMouse = commands.getoutput("xinput set-int-prop "+ i + " \"Device Enabled\" 8 0")
		      
		  elif option == "nao":
		       for i in mouse:
			   pegaMouse = commands.getoutput("xinput set-int-prop "+ i + " \"Device Enabled\" 8 1")
		      
		 
	   
		  UDPSock.sendto(pegaMouse,addr)
     op = 0
# Close socket
UDPSock.close()
