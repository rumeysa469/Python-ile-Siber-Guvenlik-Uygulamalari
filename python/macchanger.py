import random # random değerleri seçmek için random kütüphanesini ekliyoruz
import subprocess # komut çalıştıracağımız için subprocess kütüphanesini ekliyoruz
import re # regex kütüphanemizi dahil ediyoruz
# ilk önce bir mac adresi üretmek için charlist oluşturuyoruz MAC adresleri hekzadecimal oluyor f e kaadr yazacağız
charList=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

#a= random.choice(charList) # choice() random değerler seçmek için kullanıyoruz 

#print(a)
newMAC= ""
for i in range(12):
	newMAC=newMAC+random.choice(charList)  # 12 karakterli bir mac adresi olusturduk
#print(newMAC)

ifconfigResult =subprocess.check_output("ifconfig eth0", shell=True).decode() 
# buaradki check_output çıktı almak için yazdık
# shell=True ise dönüt alamk için yazdık  byte array geleceği için decode() yazdırdık
#print(ifconfigResult)

#oldMac=re.search("ether (.+)",ifconfigResult).group().split(" ")[1]# search ile ne aradığımızı ve nerde arama yapmak istediğimizi yazıp 
# ve group bilgilerini istediğimizi belirttiğimiz bir oldmac tanımlıyoruz
#print(oldMac)
# ether 08:00:27:1e:36:4a  txqueuelen 1000  (Ethernet) bu kodun çıktısı
#['ether', '08:00:27:1e:36:4a', '', 'txqueuelen', '1000', '', '(Ethernet)'] split edince bu çıktıyı alırız ytani indexlere ayırıyor 0. 1. gibi

oldMac=re.search("ether (.*?)txqueuelen",ifconfigResult).group(1).strip() # burada ise serach kısmına "ether (.*?)txqueuelen" yazdırarak group değerimizi aldık group değerimizin içine 0 yazarsak tamamını 1 yazarsak mac adresimiz ulaşırız
# strip() ederek başındaki boşluklardan kurtulabiliriz
#print(oldMac)

# burada terminalde yaptığımız işleri python ile yapıyoruz
subprocess.check_output("ifconfig eth0 down",shell=True)
subprocess.check_output("ifconfig eth0 hw ether "+newMAC,shell=True)
subprocess.check_output("ifconfig eth0 up",shell=True)

print("Old MAC: ",oldMac)
print("New MAC: ",newMAC)




#08:00:27:1e:36:4a  eth0 mac adresi 
#D70E8F404886  yeni mac adresimiz bu olasun istiyoruz
# bunun için ilk önce eth0 kartımızı kapatmamız lazım yani eth0 düşürmemiz lazım bunun için;
# terminale "sudo ifconfig eth0 down " yazıyoruz ve kartımızı kapatmış olduk
# devamında terminale "sudo ifconfig eth0 hw ether D70E8F404886 " D70E8F404886 bu adres olması istediğimiz adres
# devamında terminale "sudo ifconfig eth0 up " yazarak eth0 kartımızı kaldırıyoruz
# sonrada "ifconfig eth0 " yazarak yeni MAC adresimizi dörüyoruz




