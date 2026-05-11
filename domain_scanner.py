import socket


def domain_scanner():
    print("---Domain Scanner by Beato---")

    while True:
        try:
            domain = input(
                "Enter a url/hostname here or type 'exit' to close :")

            if domain == "exit":
                print("Exiting program...")
                break

            elif domain != "exit":
                print("Scanning url [{}]".format(domain))

            ip_add = socket.gethostbyname(domain)
            ports = [80, 443, 8080]
            print("The IP address for {} is {}".format(domain, ip_add))

            for port in ports:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                result = s.connect_ex((ip_add, port))
                if result == 0:
                    print("[+] Port {} is open, service is active".format(port))
                else:
                 print("[-] Port {} is closed, service is inactive".format(port))
            s.close()
        except socket.gaierror:
            print("Unable to connect to url")


domain_scanner()
input("Press Enter to Exit")
