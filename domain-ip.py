import socket
domainname = "google.com"
_getDomainName = socket.gethosbyname(domainname)
print("Domain name {} bind IP {}".format(domainname, _getDomainName))
