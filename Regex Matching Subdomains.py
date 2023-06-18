import re

subdomains = ['www.microsoft.com/9023', 'office.microsoft.com', 'skype.msft.com/9023']
malicioussubdomains = []

for i in subdomains:
    if re.search('(?<=\.)microsoft.com', i) != None:
        malicioussubdomains.append(i)
print(malicioussubdomains)