#! /usr/bin/python

import hashlib
import hmac
import md5
import base64
from QuoinePayAPISettings import *
from QuoinePayAPIUtility import *

gbl = Global()
key = gbl.ApiKey
print "API Key : " + key
ctype = gbl.ContentType
cMD5 = md5.new("").hexdigest()
print "MD5 :" + cMD5
uri = gbl.GetInvoicesURI
print "URI for request :" + uri
date = TimestampGMT()
print "Timestamp :" + date

str = "%s,%s,%s,%s" % (ctype,cMD5,uri,date)
print "Canonical string : " + str

hash = hmac.new(bytes(key), bytes(str),hashlib.sha1).digest()
print "Hash Digest: " + hash
print "\nB64 Encoded Hash : " + base64.encodestring(hash)
