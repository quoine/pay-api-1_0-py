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
import random
from QuoinePayAPISettings import Global
from QuoinePayAPIUtility import TimestampGMT, GetAPIKey

if __name__ == "__main__":

        gbl = Global()
	user_agent = gbl.UserAgent
	# generate some random data for testing
	random_price = round(random.random()*100,3)
	random_customer = str(int(random.random()*1000000))
	random_name = 'Invoice #2014/10/1234/' + str(int(random.random()*10000))
	data = '{ "price": "' + str(random_price) + '", "name": "' + random_name + '","data": "Payment of ' + str(random_price) + ' for services to Customer # ' + random_customer +' " }'
	print "New Invoice ->"
	print "+ price : " + json.loads(data)['price']
	print "+ name  : " + json.loads(data)['name']
	print "+ date  : " + json.loads(data)['data'] + "\n"
	ctype = gbl.ContentType
	cMD5 = base64.b64encode(md5.new(data).digest())
	print "MD5 :" + cMD5
	uri = gbl.NewInvoiceURI
	theDate = TimestampGMT()

	str = "%s,%s,%s,%s" % (ctype,cMD5,uri,theDate)
	print "Canonical String :" + str

        key = gbl.ApiKey
        print "API Key : " + key

	hash = hmac.new(bytes(key), bytes(str),hashlib.sha1).digest()

	print "HASH : " + hash
	print "B64 HASH : " + base64.encodestring(hash)

	auth_str = "%s %s:%s" % ('APIAuth', gbl.UserId, base64.b64encode(hash))
	print auth_str
        print "Authorization : " + auth_str

	headers = {'User-Agent' : gbl.UserAgent,'Date': theDate, 'Content-Type': gbl.ContentType, 'Content-MD5': cMD5,  'Authorization': auth_str } 

	url = gbl.BaseTestingURL + uri
        print "URL :: " + url
	req = urllib2.Request(url,data,headers)

	try:
   		f = urllib2.urlopen(req)
   		resp = f.read()
		print resp 
		inv = json.loads(resp)
		print repr(inv)
		#print "New Invoice status : " + inv["invoice_status"]
		#print "System status : " + inv["system_status"]
		#print "BTC Balance : " + inv["btc_balance"]
		#print "Bitcoin Address : " + inv["bitcoin_address"]
		#print "Invoice expiry : " + inv["invoice_expiry"]
	except Exception as ex:
   		print ex
   		print ex.args
