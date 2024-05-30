from scapy.all import * # diyerek tüm paketleri dahil ediyoruz

pckt_list=[] #  random oluşturduğumuz paketleri liste haline getirmek için ilste olusturduk
for i in range(10):
	# burada random src(kaynak) ve dst(hedef) değerleri oluşturuyoruz
	srcMac = RandMAC()
	dstMac = RandMAC()
	srcIp = RandIP()
	dstIp = RandIP()

	ether= Ether(src=srcMac,dst=dstMac) # ether headers ımızı oluşturup src ve dst lerine random olan mac src ve dstkoyuyoruz
	ip=IP(src=srcIp,dst=dstIp) # ip adında headers ımızı oluşturuyoruz src ve dst lerine random olan ip src ve dst leri koyuyoruz
	pckt=ether/ip # ether ve ip headers lerimizi pckt adındaki paketle birleştiriyoruz
	pckt_list.append(pckt) # ürettiğm pckt paketlerini pckt_list listesine ekliyorum
	print(srcMac,":",srcIp,">>",dstMac,":",dstIp)
	# aldığımız random src ve dst leri daha düzgün göstermek adına böyle yazdık

sendp(pckt_list,iface="eth0",verbose=False)
#sendp: Scapy'deki bu fonksiyon, katman-2 (veri bağlantı katmanı) paketlerini gönderir.
#pckt_list: Gönderilecek paketlerin bulunduğu liste. Bu liste, daha önce oluşturduğunuz ve append() ile eklediğiniz paketlerden oluşur.
#iface="eth0": Paketlerin gönderileceği ağ arayüzünü belirtir. Bu örnekte, "eth0" Ethernet arayüzü kullanılmıştır.
#verbose=False: Bu parametre, işlemler sırasında detaylı çıktının (verbose output) gösterilip gösterilmeyeceğini belirler. False olarak ayarlandığında, işlem sırasında detaylı bilgi yazdırılmaz.
