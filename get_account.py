#! /usr/bin/python

import os, sys
import json
import urllib
import urllib2
import hashlib
import hmac
import md5
import httplib
import base64
from QuoinePayAPISettings import *
from QuoinePayAPIUtility import TimestampGMT, GetAPIKey

if __name__ == "__main__":

	gbl = Global()

	user_agent = gbl.UserAgent
	data = ""
	ctype = gbl.ContentType
	cMD5 = base64.b64encode(md5.new(data).digest())
	print "MD5 :" +  cMD5
	uri = gbl.GetAccountURI
	theDate = TimestampGMT()
	str = "%s,%s,%s,%s" % (ctype,cMD5,uri,theDate)

	print "Canonical String :" + str

        key = gbl.ApiKey
        print "API Key : " + key

	hash = hmac.new(bytes(key), bytes(str),hashlib.sha1).digest()

	print "HASH : " + hash
	print "B64 HASH : " + base64.encodestring(hash)

	auth_str = "%s %s:%s" % ('APIAuth', gbl.UserId, base64.b64encode(hash))
        print "Authorization : " + auth_str

	headers = {'User-Agent' : gbl.UserAgent,'Date': theDate, 'Content-Type': gbl.ContentType, 'Content-MD5': cMD5,  'Authorization': auth_str } 

	url = gbl.BaseTestingURL + gbl.GetAccountURI
	req = urllib2.Request(url,None,headers)

	try:
   		f = urllib2.urlopen(req)
   		print f.read()
	except Exception as ex:
   		print ex
   		print ex.args
