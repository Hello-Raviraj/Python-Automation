import requests
url = "http://testphp.vulnweb.com/"
#directory = dir_brute.txt
f = open("dir_brute.txt" , "r")
b = f.read().splitlines()
f.close()
for i in b:
    new_url = url + i 
    x = requests.get(new_url)
    #print(x.request.url)
    print("The request is ", x.request.url, "and its status code is ", x.status_code )

