import requests
url = "http://httpbin.io/headers"
header = {'User-Agent': 'Pentest'}
x = requests.get(url ,headers=header)
print(x.status_code)
print(x.text)
y = x.headers
for key, value in y.items():
    
    print(f'{key}:{value}')
