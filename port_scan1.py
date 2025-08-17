import subprocess
y = []
while True:
    domain = input("Enter the domain: ")
    
    if domain == "run":
        break
    y.append(domain)

x = []
while True:
    scan_type = input("Enter ports: ")
    
    if scan_type == "run":
        break
    x.append(scan_type)
    
print(f"the list is :{x}")
print(f"the list is :{y}")
output = input("Do you want to save the output in file: ")
cmd1 = ["nmap", "-vv", "-p", ",".join(x),] + y

if output == "yes":
    filename = input("Enter the name of the file: ")    
    cmd2 = ["nmap", "-vv", "-p", ",".join(x), "-oN", filename] + y
    z = subprocess.run(cmd2, capture_output=True, text=True)
    print("Running command:", " ".join(cmd2))
    #print(z.stdout)
else:
    z = subprocess.run(cmd1, capture_output=True, text=True) 
    print("Running command:", " ".join(cmd1))
    print(z.stdout)
   
        








    #if scan_type = " " 
    ##print(" ".join(cmd))  
    #
    #print(x.stdout)



