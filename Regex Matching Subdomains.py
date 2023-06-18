import re

subdomains = ['www.microsoft.com/9023', 'office.microsoft.com', 'skype.msft.com/9023']
msftsubdomains = []

for i in subdomains:
    if re.search('(?<=\.)microsoft.com', i) != None:
        msftsubdomains.append(i)
print(msftsubdomains)
