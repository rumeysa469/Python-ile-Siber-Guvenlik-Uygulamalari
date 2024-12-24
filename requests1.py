import requests

url = 'http://10.0.2.5/dvwa/login.php' # buradaki url ise headers daki POST dan alınan url dir
#headers= {'user-agent': 'btk-akademi/1.1.1'}

data={'username':'admin' , 'password': 'password', 'Login': 'Login'} #buradaki bu bilgileri metasploit ile dvwa ya bağlanıp sağ tık yapıp 
# inspect(q) ya tıklayıp loginde ki repuests tıklayıp bu bilgilere eriştik 

try:
	r = requests.post(url, data=data ,allow_redirects=True) # burada get(url) ile girdiğimiz url ye istekte bulunuyoruz
	# buradaki url post türünden olduğu için get yerine post yazıyoruz
# buradaki allow_redirects=False yönlendirmeyi kapatması demek gibi düşünebilişriz http diyince https olan sayfaya yönlendirmeyi engelliyor ve baska hata kodu veriyor
# buradaki timeout benim istek atacağım sitenin hızını belirlemek gibi düşünebilirim eğer cok küçük değerler girersem olmayabilir
	print(r.status_code) # buradaki status code dediğimiz şey bizim aldığımız hata yada uyarı oluyor normal 505 4040 gibi aldığımız hata kodları yani 
# burada da 200 hata kodunu aldık github sitesine istek yolladık o da bize cevap olaark 200 hata kodunu yolladı 
	print(r.text) # burada contentini yazdırıyoruz https olunca çalıştırıp html kodlarını görebiliyoruz
#print(r.headers) 
	#print(r.headers.get('Date')) # burada .get() kullanark istediğimiz değeri alaviliriz
	
except Exception as e:
	print(e)
	pass

	# REQUESTS KÜTÜPHANESİ ÜZERİNDEN GİRİŞ YAPILDI

