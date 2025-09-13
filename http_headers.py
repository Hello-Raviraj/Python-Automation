import requests
url = ["https://abc.com"]
website = "https://ecourts.gov.in"
x = requests.get(website)           #send the request to the websote
y = x.headers                       #grab the headers
for key, value in y.items():        #As headers are key value pairs
    #for key, value in i.items():
    print(f"{key}: {value}")        #We have to print as a key value
