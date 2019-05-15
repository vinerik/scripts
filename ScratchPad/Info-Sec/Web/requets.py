# Script to port json data
import requests
_url = "http://www.website.com"
_json = {"data":"asdasdsf"}

r=requests.post(_url, json=_json)
print (r.text)
