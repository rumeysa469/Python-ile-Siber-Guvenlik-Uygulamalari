import nmap  # nmap kütüphanesi eklendi

scanner = nmap.PortScanner()

ip = '10.0.2.5'


# sudo nmap 10.0.2.5 yazdığımızda açık olan portları açık olan servisleri gösteriyor
scanner.scan(ip,'0-100','-sV')
#burada -sS yazınca SYN taraması yapıyoruz -sV yazınca version taraması yapıp bilgileri alıyoruz
#print(scanner.scaninfo())
# scan modülü ile kali terminalde yaptığımızı bu işlemi scriptimiz üzerinde de göstereceğiz
#print(scanner[ip]) bu kod ile de tüm bilgilere ulaşabilirim
#print('host', ip,':',scanner[ip].state())

#ben bir hostun ayakta olup olmadığını 
#print(scanner[ip].state()) kodu ile kontrol edebilirim

#print('protocols',scanner[ip].all_protocols()) # burada hangi protokolü kullanıyoruz onu söylüyor
#print('open ports : ',scanner[ip]['tcp'].keys()) # burada tcp deki açık portların kullanıldığını öğreniyoruz
#print(scanner[ip]['tcp'][21])  # 21 keyine sahip portun içindeki verileri bastırıyoruz

for port in scanner[ip]['tcp'].keys(): # burada tcp deki portların hepsini görmek için bir for döngüsü yazıyoruz
	#print(scanner[ip]['tcp'][port])
	# burada bilgileri daha net ve temiz şekilde görmek için bunu yaptık
	name = scanner[ip]['tcp'][port]['name']
	product = scanner[ip]['tcp'][port]['product']
	version = scanner[ip]['tcp'][port]['version']
	print(port,name,product,version)

#### nmap -p 0-100 -sV 10.0.2.5 bu şkilde nmap taraması yapılıyor

