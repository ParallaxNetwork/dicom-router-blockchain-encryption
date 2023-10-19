import http.client
import json
import configparser
import requests

config = configparser.ConfigParser()
config.read('router.conf')
client_key = config.get('satusehat', 'client_key')
secret_key = config.get('satusehat', 'secret_key')
url = config.get('satusehat', 'url')


def get_token():
  payload = 'client_id='+client_key+'&client_secret='+secret_key
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  try:
    res = requests.post(url=url+"/oauth2/v1/accesstoken?grant_type=client_credentials", data=payload, headers=headers)
    data = res.json()
  except Exception as e: # work on python 3.x
    print(e)
    print("[Error] - Authentication failed")
    return ""
  return data["access_token"]

