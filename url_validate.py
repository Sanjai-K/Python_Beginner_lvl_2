#Python code to validate URL

from urlparse import urlparse
url = urlparse('https://www.google.com/search')
protocol = url.scheme
domain = url.netloc
path = url.path

if(protocol == "https"):
    port = 443
if(protocol == "http"):
    port = 8080

print "Protocol :",protocol
print "Port :",port
print "Domain :",domain
print "Path :",path
