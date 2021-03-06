import httplib, urllib
import json

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace the accessKey string value with your valid access key.
accessKey = 'enter key here'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your access keys.
# For example, if you obtained your access keys from the westus region, replace
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial access keys are generated in the westcentralus region, so if you are using
# a free trial access key, you should not need to change this region.
uri = 'eastasia.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/sentiment'

def GetSentiment (documents):
	"Gets the sentiments for a set of documents and returns the information."

	headers = {'Ocp-Apim-Subscription-Key': "key"}
	conn = httplib.HTTPSConnection (uri)
	body = json.dumps (documents)
	conn.request ("POST", path, body, headers)
	response = conn.getresponse ()
	return response.read()

documents = {'documents': [
	{ 'id': '1', 'language': 'en', 'text': 'beautiful.' },

]}

print 'Please wait a moment for the results to appear.\n'

result = GetSentiment(documents)
print result
print result
resp_dict = json.loads(result)
print resp_dict
x = resp_dict["documents"][0]["score"]
print x
print (json.dumps(json.loads(result), indent=2))
print x
if x<5:
	print "good word"
else:
	print "bad word"


