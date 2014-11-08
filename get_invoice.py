#! /usr/bin/python

import os, sys
import json
import urllib
import urllib2
import hashlib
import hmac
import md5
import httplib
from traceback import format_exc
import base64
from QuoinePayAPISettings import Global
from QuoinePayAPIUtility import TimestampGMT, GetAPIKey

if __name__ == "__main__":

	if len(sys.argv) >= 2:
		invoice_id = str(sys.argv[1])
	else:
		print "Error - invoice id must be provided on command line e.g. ./get_invoice.py 888"
		raise AttributeError,"No invoice id provided in command line parameters"
		
	print "Retrieving data for invoice # " + invoice_id

	gbl = Global()
	user_agent = gbl.UserAgent
        data = "" 
	ctype = gbl.ContentType
	cMD5 = base64.b64encode(md5.new(data).digest())
	print "MD5 :"
	print cMD5
	uri = gbl.GetInvoicesURI + "/" + invoice_id   # "/api/v1/invoices"
	theDate = TimestampGMT()
	str = "%s,%s,%s,%s" % (ctype,cMD5,uri,theDate)

	print "Canonical String :" + str

        key = gbl.ApiKey
        print "API Key : " + key

	hash = hmac.new(bytes(key), bytes(str),hashlib.sha1).digest()

	print "HASH : " + hash
	print "B64 HASH : " + base64.encodestring(hash)

	auth_str = "%s %s:%s" % ('APIAuth',gbl.UserId, base64.b64encode(hash))
        print "Authorization : " + auth_str

	headers = {'User-Agent' : gbl.UserAgent, 'Date': theDate, 'Content-Type': gbl.ContentType, 'Content-MD5': cMD5,  'Authorization': auth_str } 

	url = gbl.BaseTestingURL + gbl.GetInvoicesURI + "/" + invoice_id
        print "URL: " + url 
	req = urllib2.Request(url,None,headers)

	try:
   		f = urllib2.urlopen(req)
   		print f.read()
	except Exception as ex:
   		print format_exc()
