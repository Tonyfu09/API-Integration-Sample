# import lib
import requests
import pprint
import secrets
from urllib import request,parse
import json
from pprint import pprint as pp
from requests import Session

#url = 'https://neutrinoapi.net/ip-info'
#params = {
#  'user-id': 'd3API',
#  'api-key': 'lB8S9T3fRS0Sf84T6w7m53I6YmEVWnkOjRfNc7qPAFs6kgs8',
#  'ip': '8.8.8.8'
#}

#postdata = parse.urlencode(params).encode()
#req = request.Request(url, data=postdata)
#response = request.urlopen(req)
#result = json.loads(response.read().decode("utf-8"))

#pp(result)

# Create the class for the feature
class virustotalAPI:
    def __init__(self, apikey):
      self.apiurl = 'https://www.virustotal.com/vtapi/v2'
      self.headers = { 'Accepts': 'application/json', 'api-key': apikey}
      self.session = Session()
      self.session.headers.update(self.headers)

    def getFileReport(self, txtFile):
      url = self.apiurl + '/file/report'
      txtFile = {'resource' : txtFile}
      r = self.session.post(url, headers=self.headers, params=txtFile)
      data = r.json()
      return data
      
# use the feature on the class with userid and apikey parmas
virustotalAPI = virustotalAPI(secrets.apikey)
#neturinoAPI = neturinoAPI (secrets.userid,secrets.apikey)
pp(virustotalAPI.getFileScan('4d1740485713a2ab3a4f5822a01f645fe8387f92'))
