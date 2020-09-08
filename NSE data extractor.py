import requests,json

headers =  {'authority': 'www.nseindia.com',
					   'method': 'GET',
					   'scheme': 'https',
					   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
					   'accept-encoding': 'gzip, deflate, br',
					   'accept-language': 'en-US,en;q=0.9',
					   'cache-control': 'max-age=0',
					   'sec-fetch-mode': 'navigate',
					   'sec-fetch-site': 'none',
					   'sec-fetch-user': '?1',
					   'upgrade-insecure-requests': '1',
					   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
					   }
url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"


api_data = requests.get(url,headers = headers)
data = api_data.json()
stocks= data['data']
print(stocks)