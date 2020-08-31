import requests
from lxml.html import fromstring


realip = requests.get("https://ifconfig.me")
realip = str(realip.text)

site1 = requests.get("https://free-proxy-list.net")
parser = fromstring(site1.text)
for i in parser.xpath("//tbody/tr"):
#	print(i.xpath(f'{proxynum}:{portnum}'))
	proxynum = i.xpath(".//td[1]/text()")
	portnum = i.xpath(".//td[2]/text()")
	proxyfull = f"{proxynum}:{portnum}"
	showport = str(portnum)
	showport = showport.replace("'","").replace("]","").replace("[","")
#	print(f"{proxynum}:{portnum}")
	proxyfull = proxyfull.replace("]", "").replace("[", "").replace("'", "")
#	print(proxyfull)
	try:
		if proxyfull != realip :
			response = requests.get("https://ifconfig.me",proxies={"http": proxyfull, "https": proxyfull}, timeout=2)
			print(f"{response.text}:{showport}")
		else:
			a = 1
	except:
		print("Sama")
