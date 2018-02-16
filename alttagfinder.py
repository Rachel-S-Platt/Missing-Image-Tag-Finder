from bs4 import BeautifulSoup
from collections import defaultdict
import argparse
import time
import urllib2
import OSC

html_page = urllib2.urlopen("https://www.lingscars.com/")

send_address = '127.0.0.1', 6448

# OSC basic client
c = OSC.OSCClient()
c.connect( send_address )
while 1:
    missingalttags = OSC.OSCMessage()
    missingalttags.setAddress("/wek/inputs")

    soup = BeautifulSoup(html_page, 'html.parser')

    soupimgwithoutalt= soup.find_all('img', alt=False)
   # print(soupimgwithoutalt)

    missingalt= float(len(soupimgwithoutalt))
    #print(missingalt)

    missingalttags.append(missingalt)
    c.send(missingalttags)
    print "Sent number of missing alt tags"

    time.sleep(1) 
    


