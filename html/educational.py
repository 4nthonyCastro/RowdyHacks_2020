import http.client

conn = http.client.HTTPSConnection("endlessmedicalapi1.p.rapidapi.com")

payload = ""

headers = {
    'x-rapidapi-host': "endlessmedicalapi1.p.rapidapi.com",
    'x-rapidapi-key': "01e835aebfmshbf8a7e95b8b597bp1dd025jsn5bfa92aaecc8",
    'content-type': "application/x-www-form-urlencoded"
    }

conn.request("POST", "/AcceptTermsOfUse?SessionID=%3Crequired%3E&passphrase=%3Crequired%3E", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
