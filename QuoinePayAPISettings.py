#! /usr/bin/python 

from QuoinePayAPIUtility import *

class Global():

	UserAgent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
	ContentType =  "application/json"
 
	ApiKey = 'aJmCpekM3DNIeUEnMQjAd0DITWLxSBxYdUBJeR3gJxZbExHOZR3OxuvVkTqUImK7P0RPJ+5Zg7Pt+H/2ks/byA=='

	UserId = "59"

	# URLs for API calls - test, production
	BaseProductionURL = "https://pay.quoine.com"
	BaseTestingURL = "https://pay-stag.quoine.com"

	# URI parts for calling API - to be added to BaseXXXXURL per call
	GetAPIKeyURI   = "/api/v1/api_secret_key/"			# [GET] 				
	NewInvoiceURI  = "/api/v1/invoices"				# [POST] 				
	GetInvoiceURI  = "/api/v1/invoices" 				# [GET]				
	GetInvoicesURI = "/api/v1/invoices" 				# [GET]				
	GetAccountURI  = "/api/v1/account"				# [GET] 				
	SetPaymentsCallbackURI = "/api/v1/payments_callback_url"	# [POST] 	

	def GetApiSecretKey(self):
		key = ""
		if self.ApiKey == "Dynamic":
			resp = QuoinePayAPIUtility.GetAPIKey()
			print resp
			print resp['api_secret_key']
			key = resp['api_secret_key']
		else:
			key = self.ApiKey
		return key

if __name__ == "__main__":
  gbl = Global()
  print "API Key: " + gbl.GetApiSecretKey()
