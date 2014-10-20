#! /usr/bin/python

import json
import urllib
import urllib2
from QuoinePayAPISettings import Global

gbl = Global()

user_agent = gbl.UserAgent
headers = {'User-Agent' : user_agent, 'Content-Type': gbl.ContentType }

# replace following parameters with email, password from Quoine Pay web site
data = '{"email": "example@gmail.com","password": "example"}'

url = gbl.BaseURL + gbl.GetAPIKeyURI 
print url
skey = ""

try:
   req = urllib2.Request(url, data, headers)
   f = urllib2.urlopen(req)
   skey = f.read()
except Exception, ex:
   #prints the HTTP error code that was given
   print ex
   print str(ex)
finally:
   print skey
