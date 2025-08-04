import requests
url = "https://ecourts.gov.in"
payload = {'username'=='test', 'password'=='abc123'}
x = requests.post(url , data=payload)
print(x.status_code)
