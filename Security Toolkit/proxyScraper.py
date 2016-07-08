#Created Fully By igo on www.cashcapacity.com
#Implemented and lightly edited By windows65

from eventlet.green import urllib2
import eventlet
import re

def getProxies(url):
  src = urllib2.urlopen(url).read().split("\n")

  css = False
  classes = {}
  ips = []
  proxies = []
  
  for i in xrange(len(src)):
    line = src[i]
    
    # Start of style
    if "<td><span><style>" in line:
      css = True
      continue
    
    # Handle the CSS
    if css == True:
      # End of style
      if "</style>" in line:
        css = False
      
      if "display:none" in line:
        classes[line[1:5]] = "none"
        
      if "display:inline" in line:
        classes[line[1:5]] = "inline"
    
    # IP line
    if len(classes) > 0 and css == False:
      ip = line
      linePort = src[i + 2]
      lineCountry = src[i + 4]
      lineResponseTime = src[i + 7]
      lineConnectionTime = src[i + 11]
      lineType = src[i + 16]
      lineAnonymity = src[i + 17]
      
      # Replace class declarations with style ones
      for class_ in classes:
        ip = ip.replace("class=\"%s\"" % (class_), "style=\"display:%s\"" % (classes[class_]))
      
      # Remove all unecessary poop :)
      ip = re.sub(r"<(div|span) style=\"display:none\">[\.0-9]+</(div|span)>", r"", ip)
      ip = re.sub(r"class=\"[0-9]+\"", r"", ip)
      ip = re.sub(r"[^0123456789\.]", r"", ip)
      
      # Port
      port = linePort.replace("</td>", "")
      
      # Country
      country = lineCountry.split("")[1].split("<")[0]
      
      # Response Time Percents
      responseTime = lineResponseTime.split(":")[1].split("%")[0]
      
      # Connection Time Percents
      connectionTime = lineConnectionTime.split(":")[1].split("%")[0]
      
      # Connection Type
      type = lineType.split(">")[1].split("<")[0]
      
      # Anonymity
      anonymity = lineAnonymity.split(">")[1].split("<")[0]
      
      proxies.append({"ip":ip, "port":port, "country":country, "responseTime":responseTime, "connectionTime":connectionTime, "type":type, "anonymity":anonymity})
      
      classes = {}

  return url, proxies

proxies = []

pool = eventlet.GreenPool(12)
for url, proxyList in pool.imap(getProxies, ["http://proxylist.hidemyass.com/" + str(i + 1) for i in xrange(12)]):
  for proxy in proxyList:
    proxies.append(proxy)

for proxy in proxies:
  print "%s:%s" % (proxy["ip"], proxy["port"])
  
print "\nGot %s proxies!" % (len(proxies))
