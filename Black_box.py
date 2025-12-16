import requests

methods = ["get", "post", "options", "put", "Track", "Trace"]
header = {'Host': 'abc.com','X-Forwarded-Host': 'abc.com','Forwarded': 'bing.com','X-Host': 'google.com','X-HTTP-Host-Override': 'test.com'}


url = input("Enter the domain: ")
print("1.Methods check")
print("2.Security Headers check")
print("3.Host Header Check")
print("4.Exit")




def function1(url):    
    for i in methods:
        y = requests.request(i,url, allow_redirects = True)
        print("The status code for "+url+ " with method "+i+ " is ",y.status_code)
        print()

def function2(url):
    y = requests.get(url, allow_redirects = True)
            #y.status_code == int(200):
    z = y.headers
    print("The status code for "+url+ " with method is",y.status_code)
    for key, value in z.items():        #As headers are key value pairs
        print(f"{key}: {value}")        #We have to print as a key value
            
def function3(url):
    print("Host header check")
    try:
        for q in header:
            a = requests.get(url, allow_redirects=True, headers=header, timeout=10)
            print("The host header check for "+ q ,a.status_code)
    except requests.exceptions.Timeout:
        print("The request timed out.")
    except requests.exceptions.ConnectionError:
        print("Network problem — couldn’t connect to server.")
    except requests.exceptions.HTTPError as err:
        print("HTTP error:", err)
    except requests.exceptions.RequestException as e:
        print("Something went wrong:", e)


while True:
    options = int(input("Enter the option: "))
  
    if options == 1:   
        function1(url)
    elif options == 2:
        function2(url)
    elif options == 3: 
        function3(url)
    else:
        break

    
