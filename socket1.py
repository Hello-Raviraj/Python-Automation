import socket
domain = []
while True:
    x = input("Enter the domain: ")
    
    if x == "exit":
        break
    domain.append(x)
print(f"the list is :{domain}")
        
y = int(input("Enter the starting port: "))
z = int(input("Enter the last port: "))
q = input("Do you want to save to save the output: ")
if q == "yes":
    a = input("Enter the name of the file: ")
        
for j in domain:
    print(f"{j}")
    for i in range(y, z):
        sock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #create socket
        sock.settimeout(2)                                          #set timeout

        result = sock.connect_ex((j,i))                             #connection made here

        if result == 0:
            with open(a, 'w') as f:                                 #write output in file
                print(f"The port {i} is open for {j}", file=f)
        else:
            print(f"The port {i} is closed for {j}")
#i = i + 1
        
