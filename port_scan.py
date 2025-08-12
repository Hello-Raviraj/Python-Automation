import subprocess
domain = input("Enter the domain: ")
while True:
    print("select the scan type : \n1: port 80 \n2: port 443 \n3: port 21 \n4: exit")
    scan_type = int(input("Select scan port: "))

    if scan_type == 1:
        cmd = ["nmap", "-p", "80", domain]
    
    elif scan_type == 2:
        cmd = ["nmap" ,"-p" ,"443", domain]
    
    elif scan_type == 3:
        cmd = ["nmap" ,"-p" ,"21", domain]
    else:
        break
    print(" ".join(cmd))  
    x = subprocess.run(cmd, capture_output=True, text=True)  
    print(x.stdout)
