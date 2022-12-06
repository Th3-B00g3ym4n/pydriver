import requests
import sys
import resp

class response:
  content = str()
  status = str()

class data:
  payload = {}
  headers = {}

def send(url):
  global p
  with requests.session() as s:

    if not data.payload:
      print("ERROR: NO PAYLOAD")
      sys.exit()
    else:
      
      if not data.headers:
        p = s.post(url, data=data.payload)
      
      else:  
        p = s.post(url, data=data.payload, headers=data.headers)

      t = p.content
      s = p.status_code

      response.content = t
      response.status = s

      
__version__ = 'dev'

