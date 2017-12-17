import  json
from urllib.request import  urlopen
import urllib3

with urlopen('https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json') as response:
    data_online =response.read()


data=json.loads(data_online)

# print(json.dumps(data,indent=2))
print(data['list']['resources'])


