import socket
domainname = "google.com"
_getDomainName = socket.gethostbyname(domainname)
print("Domain name {} bind IP {}".format(domainname, _getDomainName))
