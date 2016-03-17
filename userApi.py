from sailthru.sailthru_client import SailthruClient

api_key = "replace-with-your-api-key"
api_secret = "replace-with-your-api-secret"
api_url = "http://api.sailthru.com" # optional

sc = SailthruClient(api_key, api_secret, api_url)

# GET /user
response = sc.api_get('user', {'email': 'foo@foobar.com'})

print "is_ok: " + str(response.is_ok())
print "body: " + str(response.get_body())
print "response: " + str(response.get_response())
print "status_code: " + str(response.get_status_code())
print "error: " + str(response.get_error())