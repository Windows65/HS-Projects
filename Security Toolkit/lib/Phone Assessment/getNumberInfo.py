import urllib
import os
import sys
import re
from bs4 import BeautifulSoup
import bs4 as bs
import urlparse
import mechanize
import Cookie
import cookielib
import subprocess
import urllib2
import unicodedata
import time
import random
import datetime
from datetime import datetime, timedelta


def scrapeURL(url):
    checkPhn = True
    html = urllib.urlopen(url).read()
    soup = bs.BeautifulSoup(html)
    texts = soup.findAll(text=True)
    start = time.time()
    slocation =  os.path.dirname(os.path.abspath(__file__)) + "\\Pages\\"
    finalstring = os.path.join(slocation, "URLScrape_" + ".txt")
    fid = open(finalstring, 'w')
    
    def visible(element):
        #AdvancedSettings = raw_input("Advanced Settings? (y/n)> ")
        newElement = unicodedata.normalize('NFKD', element).encode('utf8')
        mailf = open("scrapedEmails.txt", "w")
        byechars = "<>(){}[]|,\%-=+!@#^&*;:\'\"\\/"
        delStrings = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ]
        finalTxt = [""]
        new = newElement
        lastTest = byechars[-1:]
        newElemenet = newElement.split('\n')
        linkDetect = ["www.","http:","https:",".com",".net",".org",".edu"]
        detectionAmount = 0
        detectionSensitivity = 2 #The higher the number the more factors there are in finding a link, do not go over the size of linkDetect
        mailDetect = ["@gmail","@hotmail","@yahoo","@msn","@icloud","@vtext"] #Deals with .com in detection loop
        counterz = 0
        try:
            for goaway in list(byechars):
                
                if "http" in new:
                    if goaway == "/" or goaway == ":":
                        pass
                    else:
                        new = new.replace(goaway, '')
                        counterz = counterz + 1
                else:
                    new = new.replace(goaway, '')
                    counterz = counterz + 1
                new = new.strip()
                new = re.sub(r'\s+', ' ', new)
                if len(new) > 1500:
                   print "Too Long To Print! (Will still be in log file!)"
                   finalTxt.append(new) # Print This!!!!!!!!!!!!
                else:
                    pass
                    
                                        
        except Exception,e:
            fid.close()
            mailf.close()
            print "Error: " + str(e)
            raw_input("> ")
        except KeyboardInterrupt:
            print """
----------------------------------------------
Script Paused
--------------------------------------
Main Scrape Menu------(1)
Continue Script-------(Any Key)
--------------------------------------
"""
            pauseChs = raw_input("> ")
            if pauseChs == "1":
                fid.close()
                mailf.close()
                scraperChoose()
            else:
                pass

    try:
        visible_texts = filter(visible, texts)
        print visible_texts
        finish = time.time()
        start = abs(start)
        finish = abs(finish)
        tt = (int(start)) - (int(finish))
        tt = abs(tt)
        timeTaken = curTime(tt)
        print "Completed In: " + timeTaken
    except Exception,e:
        print "Error: " + str(e)
        raw_input("> ")
    except KeyboardInterrupt:
        print """
----------------------------------------------
Script Paused
--------------------------------------
Main Scrape Menu------(1)
Continue Script-------(Any Key)
--------------------------------------
"""
        pauseChs = raw_input("> ")
        if pauseChs == "1":
            fid.close()
            scraperChoose()
        else:
            pass





































def getNumberInfo():
    print "Format: xxx-xxx-xxx"
    number = raw_input("Phone Number For Information Assessment:\n> ")
    url = "www.reverse-phone--directory.net/trace-results.html?phone=" + number
    print url
    scrapeURL(url)






















getNumberInfo()
