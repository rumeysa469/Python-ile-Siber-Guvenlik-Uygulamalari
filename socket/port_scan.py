########  PORT  TARAMA  ARACI ########## 

import socket  # socket kütüphanemi dahil ediyorum

 #s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)# bütün portlara istek göndermek için bir socket nesnesi ürettik
# isteklerimizi ıpv4 göndermek için af_ınet kullandık ve sock_streamn ile de tcp socketimizi oluşturduk 

ip='10.0.2.5'  # metasploitin apsini girdik
#port = 80

for port in range(1,65535):  # ilk yüz porta istek atması için for döngüsü yazdırıp açık ve kapalı olan portları göreceğiz
	try:
		s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((ip,port))
		print(str(port),"open") # portumuz açık ise open yazdırıyoruz
	except Exception as e:
		#print(str(port),"closed") # portumuz kapalı ise closed yazdırıyoruz
		pass
	finally:
		pass
		s.close()
#sudo nmap -p1-100 -sS 10.0.2.5  terminale bunu yazarak açık olan portları servislerini görebiliriz
