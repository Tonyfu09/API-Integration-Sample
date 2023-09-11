
#Reference https://www.youtube.com/watch?v=p71SWzjeqtk
#API Document https://coinmarketcap.com/api/documentation/v1

import requests
import secrets
import pprint
from requests import Session
from pprint import pprint as pp

#url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
#headers = {
#  'Accepts': 'application/json',
#  'X-CMC_PRO_API_KEY': secrets.API_KEY,
#}
#r = requests.get(url, headers=headers)

# Build up a class so we can easily make the REST API calls
class CMC:
    def __init__(self, token):
      self.apiurl = 'https://pro-api.coinmarketcap.com'
      self.headers = {  'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': token}
      self.session = Session()
      self.session.headers.update(self.headers)
    def getAllCoins(self):
      url = self.apiurl + '/v1/cryptocurrency/map'
      r = self.session.get(url)
      data = r.json()['data']
      return data
    def getCoinsPrice(self, symbol):
      url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
      parameter = {'symbol' : symbol}
      r = self.session.get(url, params=parameter)
      data = r.json()['data']
      return data

cmc = CMC(secrets.API_KEY)
pp(cmc.getAllCoins())
pp(cmc.getCoinsPrice('BTC'))

#print all the data
#from pprint import pprint as pp
#pp(r.json())
