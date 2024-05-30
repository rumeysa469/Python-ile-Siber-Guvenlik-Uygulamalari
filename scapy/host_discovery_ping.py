from scapy.all import *

ip = IP() # ip adonda pakaetimizi oluşturduk
icmp = ICMP() # icmp adında paketimizi oluşturduk

pingPckt= ip/icmp # pingPckt adında ikisini birleştirdiğimiz paketimizi de oluşturuduk

ipList=[] # açık olan cihazları eklemek için liste oluşturduk

addr = "10.0.2." # burada ıp miz için bir adres tanımlıyoruz
for i in range(15): # addr değerinin yanına .123 şeklinde 256 ya kadar gitmesi için for döngüsü yazdık
	pingPckt[IP].dst= addr+str(i)  # burada pingPckt nin IP headers ındaki dst değerini addr+str(i) olarak atarız 

	#print(pingPckt[IP].dst)  # ekrana yazdırıyoruz
	# şimdi paket göndermek için dönen değeri alması için bir response değeri oluşturduk
	response = sr1(pingPckt,timeout=0.5,verbose=False)# pingPckt paketini gönderiyoruz
	#print(response) 
	if (response): # burada bize cevap veren cihazların açık olup olmadıklarını anlayabiliyoruz bunun için cevap aldığımız çıhazından is up açık olduğunu söyleyebiliriz
		#print(pingPckt[IP].dst,"İS UP ")
		ipList.append(pingPckt[IP].dst) # listeye ekleme yapıyoruz
	else:
		pass 
print(ipList)