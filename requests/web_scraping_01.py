import requests
from bs4 import BeautifulSoup

url ="https://stackoverflow.com/questions/tagged/python-requests"  # kazıma yapacağımız web sayfasının url sini giriyoruz
sayac=0
for i in range(1,11):
	url2="https://stackoverflow.com/questions/tagged/python-requests?tab=newest&page="+str(i)+"&pagesize=50"
	response= requests.get(url2)  # isteğimizi gönderiyoruz
	
	parser= BeautifulSoup(response.text,"html.parser") # beatifulsoup a html kodumuzu tanıtmamız gerekiyor yani senin ayriştirman gereken kod bu üstünde çalışacağın kod bu demek adına tanıtıyoruz
	#spans=parser.find_all("span",{"class":"-link--channel-name pl6"}) # burada html kodumuzun içindeki tüm span ları bulması için spans adında bir değere atıyoruz
	questions=parser.find_all("div",{"class":"s-post-summary"})  # buradaki div aradığımız verinin nerede olduğunu belirtemek için kullandık yani divin içine bakıyoruz

	for q in questions:
		#print(q) # .text ekleyince içindeki verileri de yazdırıyoruz
		title=q.find("h3",{"class":"s-post-summary--content-title"}) # burada title olduğu yeri ve classımızı söylüyoruz
		print(title.text.strip()) # strip ederek boşluklardan kurtuluyoruz ve title yazdırıyoruz
		
		content = q.find("div",{"class":"s-post-summary--content-excerpt"})  # burası contentimiz yazan metin gibi düşünebiliriz
		print(content.text.strip()) # buraad contentimizi yazdırıyoruz
		
		time=q.find("span",{"class":"relativetime"})
		print(time["title"]) # time içindeki title alıyoruz

		sayac=sayac+1
		print("content count : ",str(sayac))

		print("--------------------------------------------------------")
	#print(response.text) # yazdırıyoruz
