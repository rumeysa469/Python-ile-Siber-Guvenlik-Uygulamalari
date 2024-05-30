
import socket  # socket kütüphanemi dahil ediyorum

 #s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)# bütün portlara istek göndermek için bir socket nesnesi ürettik
# isteklerimizi ıpv4 göndermek için af_ınet kullandık ve sock_streamn ile de tcp socketimizi oluşturduk 

ip='10.0.2.5'  # metasploitin apsini girdik
#port = 80

for port in range(1,100):  # ilk yüz porta istek atması için for döngüsü yazdırıp açık ve kapalı olan portları göreceğiz
	try:
		s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.settimeout(5.0)
		s.connect((ip,port))
# bize dönen mesajları almak için recv kullanıyoruz
		response=s.recv(1024)


		print(str(port),"open :  banner: ",response.decode()) # portumuz açık ise open yazdırıyoruz
		# banner değerlerini de yazdırıyoruz	
	except socket.timeout as t:  # timeout olan değerleri yakalamak için bir exception yazıyoruz
		if(port==80): # port 80 ise 
			httpMessage="GET/HTTP/1.0\r\n\r\n"  # bir http mesajı oluştuuruyoruz
			s.send(httpMessage.encode())  # mesajı göndermek için send ve encode yi kullanıyoruz
			httpRcv=s.recv(1024)  # mesajı almak için recv yapıyoruz 
			print(str(port),"open :  banner: ",httpRcv.decode())  # burada da ekrana yazdırıyoruz
		else:  # farklı bir şey gelirse diye de use different method yazdırıyoruz başka yöntem deneyiniz
			print(str(port),": use different method")
	except Exception as e:
		#print(str(port),"closed : reason : ",str(e)) # portumuz kapalı ise closed yazdırıyoruz
		pass
	finally:
		s.close()

