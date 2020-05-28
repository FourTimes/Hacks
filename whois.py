import whois

DomainInfo = whois.query('google.com')
Result = DomainInfo.__dict__

for R, L in Result.items():
    if R == "name_servers":
        for a in L:
            print(R.ljust(15), a[:])
    else:
        print(R.ljust(15), L)
