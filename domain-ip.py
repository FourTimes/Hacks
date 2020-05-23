import socket
import sys

if len(sys.argv) == 1:
    domainname = int(sys.argv[1])
else:
    domainname = "google.com"
print(socket.gethostbyname(domainname))
