
# RTFM
# import module
# Test a basic request
# API Key b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c
# /v1/cryptocurrency/info api request

import traceback
import requests
import secrets

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': secrets.API_KEY,
}

r = requests.get(url, headers=headers)
statuscode = r.status_code
print(statuscode)
