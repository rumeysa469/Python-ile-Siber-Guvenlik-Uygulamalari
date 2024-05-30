from scapy.all import*
eth = Ether() # ether diye paketimizi tanımlıyoruz
arp= ARP()  # arp diye paketimizi tanımlıyoruz

eth.dst= "ff:ff:ff:ff:ff:ff" # ethernetin dst sini ff olarak ayarlıyoruz
arp.pdst ="10.0.2.1/24"
bcPckt= eth/arp # broadcast imiz için bcPckt adında bir paket oluşturuyoruz
# buraya da eth ve arp paketlerimizi birleştiriyoruz


bcPckt.show() # paketimiizn içeriğini gösteriyor 
ans,unans=srp(bcPckt,timeout=5)
#ans.summary()  # cevap aldıklarımızı yazdırdık
print("#"*30)
#unans.summary()  # cevap alamadıklarımızı yazdırdık

for snd,rcv in ans:
	#rcv.show() # cevap aldıklarımızı yani rcv olanları gösterdik
	# kaynağın MAC adresini bastırmak için bize ethernet paketinin src ve arp paketinin psrc si gerekli
	print(rcv.psrc," : ",rcv.src)