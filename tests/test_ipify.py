import os
import sys

import requests
import re


from ipify import get_ip
print(get_ip())


user_agents = []
user_agents.append("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0")
user_agents.append("Mozilla/5.0 Gecko/20100101 Firefox/49.0"
user_agents.append("Mozilla/5.0 Firefox/49.0")
user_agents.append("Mozilla/5.0")

#~ ip = requests.get('https://api.ipify.org').text
#~ print('My public IP address is:', ip)
#~ print(requests.get('http://checkip.dyndns.org').text)



#~ http://ipinfo.io/ip
#~ requests.get('http://ipinfo.io')
#~ {
  #~ "ip": "88.181.70.50",
  #~ "hostname": "mar67-1-88-181-70-50.fbx.proxad.net",
  #~ "city": "Marlenheim",
  #~ "region": "Bas-Rhin",
  #~ "country": "FR",
  #~ "loc": "48.6092,7.4964",
  #~ "org": "AS12322 Free SAS",
  #~ "postal": "67520"
#~ }
