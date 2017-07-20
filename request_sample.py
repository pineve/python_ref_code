import requests as r

uri = "http://www.google.com/search"
param = {'q':'python'}
resp = r.get(uri, param)
print resp.url
print resp.text
