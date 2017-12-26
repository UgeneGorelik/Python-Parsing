#downloading content using request lib and parsing usiing json lib

import  json
from urllib.request import  urlopen
import urllib3

with urlopen('https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json') as response:
    data_online =response.read()

data=json.loads(data_online)
print(data['list']['resources'])


