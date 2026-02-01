import requests
I = input("Enter the domain with https://:- ")
response = requests.get(I, allow_redirects = True)
session_id = response.cookies.get("JSESSION")  
x = int(session_id)
print(x.bit_length())
if x == 128:  
    print("Session ID is 128 bits.")
else:
    print("Session ID is not 128 bits.")

