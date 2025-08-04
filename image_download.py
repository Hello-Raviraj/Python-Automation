#compiler underatands step by step Like below

import requests
url = "https://httpbin.org/image/png"
x =  requests.get(url)  #send the request to the url
if x.status_code == 200:
    f = open("downlaoded_image.png", "wb")   #create a file with name which is available to modify
    f.write(x.content)                       #write the response of x variable in the file   
    f.close()                                #clsoe the file once done
    print("success")
else:
    print("not successful")
