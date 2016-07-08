#!/usr/bin/env python
from datetime import datetime, timedelta
from ftplib import FTP
import subprocess
import socket
import time
import sys
import os
global multiScan
global debug
global smart
import aptCrawler

#NOTES:
#-----------------------------------------------------------------------------------
"""
The origional creator is not responsible for anything you do with this script.
Full credit goes to:
http://eclipsion.com/index.php?/user/5-windows65/
Private message for any questions.

Multiple IP Scan is out of order. Feel free to fix it yourself, its more of a
multiple LAN node scanner, just find out why the list index is our of range and
you it will work. Something so the noobs cnat leech hardcore ;)
"""

#-----------------------------------------------------------------------------------





#SETTINGS:
#-----------------------------------------------------------------------------------
debug = False #Set to true for scan output, false for port found only output (Also Runs Faster Without Printing)
smart = False #Is Changed By Users Choice During Script
#-----------------------------------------------------------------------------------
#END OF SETTINGS

#Do not mess with anything past this point unless you know what you are doing,
#It is possible to mess the script up, if you decide to mess with them it is a
#good idea to make a backup first!
multiScan = False
def pause():
    try:
        raw_input("\n> ")
    except:
        pass
def getInput():
    while True:
        try:
            tell = raw_input("\n> ")
            return tell
        except KeyboardInterrupt:
            raw_input("\n> ")
        except Exception,e:
            raw_input("\n> ")

def printCompleteTime(timea, timeb):
    def curTime(seconds):
        sec = timedelta(seconds=(int(seconds)))
        d = datetime(1,1,1) + sec
        return ("Days: %d | Hours: %d | Minutes: %d | Seconds: %d" % (d.day-1, d.hour, d.minute, d.second))

    start = abs(timea)
    finish = abs(timeb)
    tt = int(start) - int(finish)
    tt = abs(tt)
    timeTaken = curTime(tt)
    return "Completed In: " + timeTaken

def cls():
    print "\n"*50 # Clears IDLE Screen
    subprocess.call('cls', shell=True) # Clears Console Screen

def getIP():
    global multiScan
    try:
        print """
Please select the perfered scan type!
----------------------------------------
>Scan One Host-------------{1}
>Scan A range Of Hosts-----{2} #Not Functioning Properly
>List Hosts Online---------{3}
>Exit Script---------------{CTRL+C}
----------------------------------------"""
        option = raw_input("> ")
        print option
        if option == "1":
            multiScan = False
            cls()
            print "Enter a remote host to scan: "
            remoteServer = getInput()
            if remoteServer.strip() == "":
                cls()
                print "Invalid Option!"
            else:
                return remoteServer
        elif option == "2":
            multiScan = True
            cls()
            print """
                                          Colon Required
                                               \/
Enter a range of hosts to scan: Ex: 192.168.0.0 : 192.168.0.255
--------------------------------------------------------------------
            """
            remoteServer = getInput()
            if remoteServer.strip() == "":
                cls()
                print "[Error] | Invalid Option.. | Retry."
            else:
                return remoteServer
        elif option == "3":
            cls()
            getHosts()
        elif option == "admin":
            print "Nothing here to see..."
            sys.exit(0)
        else:
            cls()
            print "Invalid Option!"
            getIP()
    except Exception, e:
        print "[Error] | " + str(e)
    except KeyboardInterrupt:
        print "You have exited the script, Goodbye!"
        sys.exit(0)

        
def getPortDef(port):
    try:
        defFile =  os.getcwd() + "\\portDefs.txt"
        defs = open(defFile, "r")
    except Exception,e:
        if "No such file or directory" in str(e):
            print """
[Error]:
--------------------------------------------------------
You are missing the Port Definition File!
Please insert {portDefs.txt} in the same folder the
script is in! If you are missing the contents of the file
go to:
http://www.planetlinks.com/tec236/notes-terms/4-10-06/default-tcp-ports-list.html
copy the port list, and paste it into portDefs.txt!
--------------------------------------------------------
"""
            pause()
        else:
            print "Error Opening Port Definition File (portDefs.txt) | " + str(e)
            pause()
            
    for data in defs.readlines():
        data = data.strip()
        portType, porti, desc = data.split("  ")
        if str(port) in data:
            return "[Port Found] | " +  porti + " | " + portType + " | " + desc
    return "[Port Found] | " +  str(port) + " | TCP | Information Not Found!"



def scanPorts(remoteServer, beginPort, endPort):
    global multiScan
    global debug
    global smart
    quickPortScan = ["80", "443", "22", "21", "8080", "25", "4567", "1723", "53", "23", "3389", "110", "135", "143", "445", "5000", "111", "69", "13", "1027"]
    customDelay = False
    if multiScan == False:
        openPorts = [] 
        cls()
        tldList = open("domains.txt", "r")
        urlThngs = tldList.readlines()
        for urlDetect in urlThngs:
            if urlDetect.strip() in remoteServer.strip():
                delay = 0.8
                print "{Notice} | HTTP Detected! | Scanning Slower For Better Accuracy."
                break
            elif customDelay == True:
                print "Delay Between Port Scans (Default = 0.01)"
                try:
                    delay = float(getInput())
                except Exception, e:
                    print "[Input Error] | > " + str(e)
                    
                break
            elif "localhost" in remoteServer.strip():
                delay = 0.00000009
                print "{Notice} | localhost Detected! | You Now Have Higher Speed Scanning Capibilities."
                break
            
            else:
                delay = 0.01
        try:
            remoteServerIP  = socket.gethostbyname(remoteServer)
        except Exception,e:
            if "getaddrinfo failed" in str(e):
                print "[ERROR] | Unable to connect to host. | Please Check your Typing And Try Again!"
                newIP = getIP()
                scanPorts(newIP, beginPort, endPort)
        t1 = time.time()
    
        try:
            if smart == True:
                print "-" * 73
                print "Please wait, scanning the most common ports on host " + remoteServerIP
                print "-" * 73
                for port in quickPortScan:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(delay)
                    result = sock.connect_ex((remoteServerIP, int(port)))
                    sock.settimeout(None)
                    if result == 0:
                        printPort = getPortDef(port) #Make this varialbe: print str(port)  if you do not want the port description
                        print printPort
                        openPorts.append(printPort)
                    else:
                        if debug == True:
                            print "{Scanned} | " + remoteServerIP + " : " + str(port)
                        else:
                            pass
                    sock.close()
            else:
                print "-" * 73
                print "Please wait, scanning ports (" + beginPort + " - " + endPort + ") on the remote host " + remoteServerIP
                print "-" * 73
                for port in range(int(beginPort),int(endPort) + 1):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(delay)
                    result = sock.connect_ex((remoteServerIP, port))
                    sock.settimeout(None)
                    if result == 0:
                        printPort = getPortDef(port) #Make this varialbe: print str(port)  if you do not want the port description
                        print printPort
                        openPorts.append(printPort)
                    else:
                        if debug == True:
                            print "{Scanned} | " + remoteServerIP + " : " + str(port)
                        else:
                            pass
                    sock.close()
        except KeyboardInterrupt:
            print """
----------------------------------------------
Port Scan Stopped
--------------------------------------
Main Menu-------(Any Key)
--------------------------------------
            """
            pauseChs = getInput()
            cls()
            getScanType()
        
        except socket.gaierror:
            print 'Hostname could not be resolved. Exiting'
            sys.exit()
        except socket.error:
            print "Couldn't connect to server"
            sys.exit()
        t2 = time.time()
        cls()
        attackPorts = []
        thePorts = []
        portCounter = 0
        print "Open Ports: \n" + "-"*75
        for port in openPorts:
            portCounter = portCounter + 1
            print port
            attackPorts.append(port)
            for word in port.split(" | "):
                if word.isdigit() == True:
                    thePorts.append(word.strip())
                    break
                else:
                    pass
                
        if len(attackPorts) != 0:  
            print "Attack All Ports. | Type: (all)"
            print "-"*75 + "\n"
            print printCompleteTime(t2, t1)
            print "-"*70
            print "Choose a port to attack from (Multiple Supported.) | Ex: [80,443,22,8080]\nLeave blank for None."
            attackPrts = getInput()
            attackPrts.strip()
            if "all" in attackPrts:
                #print thePorts
                pentestPort(thePorts, remoteServerIP)
            else:
                pentestPort(attackPrts, remoteServerIP)
            cls()
            getScanType()
        else:
            print "No ports detected!"
            print "-"*75 + "\n"
            print printCompleteTime(t2, t1)
            print "-"*70
            getInput()
            cls()
            getScanType()




    elif multiScan == True:
        remoteServer = remoteServer.strip()
        founds = 0
        openPorts = []
        cls()
        delay = 0.01
        try:
            
            try:
                if ":" in remoteServer:
                    ip1, ip2 = remoteServer.split(":")
                else:
                     print "[Error] | Please Use : to seporate the two IP's."
                     print "Retype the IP's: (192.168.1.1 : 192.168.255.255)"
                     getScanType()
            except Exception, e:
                if "object has no" in str(e):
                    print "Tried: " + splitChar + " | " + str(e)
                else:
                    print "[Error] | " + str(e)
            except KeyboardInterrupt:
                pass
            print remoteServer
            ip1 = ip1.strip()
            ip2 = ip2.strip()
            numz1 = ip1.split(".")
            numz2 = ip2.split(".")
            one, two, three, four = ip1.split(".")
            newSub = one + "." + two + "."
            chkBig = []
            
            chkBig.append(numz1[3])
            chkBig.append(numz2[3])
            bigger = max(chkBig)
            if max(chkBig) == chkBig[0]: 
                biggest = chkBig[0]
                smaller = chkBig[1]
            elif max(chkBig) == chkBig[1]:
                biggest = chkBig[1]
                smaller = chkBig[0]
            
            else:
                print "Fatal Error, Restarting!"
                pause()
                getScanType()

            chkBig2 = []
            
            chkBig2.append(numz1[2])
            chkBig2.append(numz2[2])
            bigger = max(chkBig2)
            if max(chkBig2) == chkBig2[0]: 
                biggest2 = chkBig2[0]
                smaller2 = chkBig2[1]
            elif max(chkBig2) == chkBig2[1]:
                biggest2 = chkBig2[1]
                smaller2 = chkBig2[0]
            
            else:
                print "Fatal Error, Restarting!"
                pause()
                getScanType()
                
        except Exception,e:
            if "list index out of range" in str(e):
                print "[Error] | IP addresses not within range. | " + str(e)
                newIP = getIP()
                scanPorts(newIP, beginPort, endPort)
            else:
                print str(e)
                print "{ERROR} | Unable to get the range of hosts. | Please Check your Typing And Try Again!"
                newIP = getIP()
                scanPorts(newIP, beginPort, endPort)

        print "Please wait, scanning ports (" + beginPort + " - " + endPort + ") on the each host between " + ip1 + " - " + i2p
        print str(newSub) + str(newIP2) + str(newIP), int(port)
        print "-" * 93
        t1 = time.time()
        try:
            if smart == True:
                for newIP2 in range(int(smaller2), int(biggest2)):
                    for newIP in range(int(smaller), int(biggest)):
                        
                        #print "\nScanning IP: " + str(newSub) + str(newIP) + "\n" + "-"*75

                        openPorts.append("Results For: | " + str(newSub) + str(newIP) + " | Ports: (" + str(smaller) + "-" + str(biggest) + ")\n" + "-"*75)
                        for port in range(79,81):#quickPortScan:
                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            sock.settimeout(delay)
                            result = sock.connect_ex((str(newSub) + str(newIP2) + str(newIP), int(port)))
                            sock.settimeout(None)
                            if result == 0:
                                printPort = getPortDef(port) #Make this varialbe: print str(port)  if you do not want the port description
                                print printPort
                                openPorts.append(printPort)
                                founds = founds + 1
                            else:
                                if debug == True:
                                    print "{Scanned} | " + str(newSub) + str(newIP) + " : " + str(port)
                                else:
                                    pass
                            sock.close()
                        if founds == 0:
                            #print "No Ports Open on this IP: \n" + "-"*75
                            openPorts.append("No Ports Open on this IP:")
                            openPorts.append("-"*75 + "\n\n")
                        else:
                            openPorts.append("-"*75 + "\n\n")
                        founds = 0
                        
                        print "\n"

                
            else:
                for newIP in range(int(smaller), int(biggest)):
                    print "\nScanning IP: " + str(newSub) + str(remoteServerIP) + "\n" + "-"*75

                    openPorts.append("Results For: | " + str(newSub) + str(newIP) + " | Ports: (" + str(smaller) + "-" + str(biggest) + ")\n" + "-"*75)
                    for port in range(int(beginPort),int(endPort) + 1):
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(delay)
                        result = sock.connect_ex((str(newSub) + str(newIP), port))
                        sock.settimeout(None)
                        if result == 0:
                            printPort = getPortDef(port) #Make this varialbe: print str(port)  if you do not want the port description
                            print printPort
                            
                            openPorts.append(printPort)
                            
                            founds = founds + 1
                        else:
                            if debug == True:
                                print "{Scanned} | " + str(newSub) + str(newIP) + " : " + str(port)
                            else:
                                pass
                        sock.close()
                    if founds == 0:
                        print "No Ports Open on this IP: \n" + "-"*75
                        openPorts.append("No Ports Open on this IP:")
                        openPorts.append("-"*75 + "\n\n")
                    else:
                        openPorts.append("-"*75 + "\n\n")
                    founds = 0
                    
                    print "\n"
        except KeyboardInterrupt:
            print """
----------------------------------------------
Port Scan Stopped
--------------------------------------
Main Menu-------(Any Key)
--------------------------------------
            """
            pauseChs = getInput()
            cls()
            getScanType()
        
        except socket.gaierror:
            print '[Connection Error] | Unable to resolve host name | Restarting Script!'
            getScanType()
        except socket.error:
            print "[Connection Error] | Unable to connect to the host (Possibally Blocked) | Restarting Script!"
            getScanType()
            
        t2 = time.time()
        cls()
        attackPorts = []
        thePorts = []
        portCounter = 0
        print "Open Ports: \n" + "-"*75
        for port in openPorts:
            portCounter = portCounter + 1
            print port
            attackPorts.append(port)
            for word in port.split(" | "):
                if word.isdigit() == True:
                    thePorts.append(word.strip())
                    break
                else:
                    pass
                
        if len(attackPorts) != 0:  
            print "Attack All Ports. | Type: (all)"
            print "-"*75 + "\n"
            print printCompleteTime(t2, t1)
            print "-"*70
            print "Choose a port to attack from (Multiple Supported.) | Ex: [80,443,22,8080]\nLeave blank for None."
            attackPrts = getInput()
            attackPrts.strip()
            if "all" in attackPrts:
                print thePorts
                pentestPort(thePorts, remoteServerIP)
            elif attackPrts == "":
                getScanType()
            else:
                pentestPort(attackPrts, remoteServerIP)
            cls()
            getScanType()
        else:
            print "No ports detected!"
            print "-"*75 + "\n"
            print printCompleteTime(t2, t1)
            print "-"*70
            getInput()
            cls()
            getScanType()

    else:
        print "global Varialbe {multiScan} is not set to True or False, this is fatal, Goodbye!"
        pause()
        getScanType()
def dLoop():
    for i in range(0,999999999):
        cls()
        getInput()



def pentestPort(ports,server):
    cls()
    print "Beggining Port connection on | " + server + "\n" + "-"*75
    if len(ports) == 0:
        cls()
        getScanType()
    try:
        for port in ports.split(","):
            port = str(port).strip()
            #Port Specific Attacks:
            #----------------------------------------------------------------------------------------------------------------------------------------------------------------------


            #--------------------------------------------------------------------------------------------------------------------------
            if port == "21":
                userlist = ["admin","root","test","uploader","josh","bill","mike","agata","ftp","oracle","marketing",]
                passwdlist = ['oracle', 'root', 'abc123', 'password', '123456', 'admin', 'test', 'uploader', '123qwe', 'test', 'password', 'password', 'john', 'bill', 'abc123', 'mike', 'password', 'agata', 'ftp', 'admin', 'ftp123', 'ftpuser', 'password', 'marketing']
                print "FTP Detected, \nTrying Common User/Pass Combinations on the FTP File Server: \n" + "-"*65
                for user in userlist:
                    for passwd in passwdlist:
                        try:
                            print "[Trying Login] | >" + user + " - " + passwd
                            ftp = FTP(server)   # connect to host, default port
                            ftp.login()               # user anonymous, passwd anonymous@
                            print "[Login Found:] \n" + "-"*50 + "Server: " + server + ":21" + "\nUsername: " + user + "\nPassword: " + passwd + "-"*50
                            ftp.retrlines('LIST')     # list directory contents
                        except Exception, e:
                            e = str(e)
                            if "Login incorrect" in e:
                                pass
                            else:
                                print "[Error] | >" + e
                                getInput()
                        except KeyboardInterrupt:
                            pass
                print "-"*65
                getInput()
            #--------------------------------------------------------------------------------------------------------------------------
                

            #--------------------------------------------------------------------------------------------------------------------------
            elif port == "80" or port == "8080":
                aptCrawler.scraperChoose(url, "1")

            #--------------------------------------------------------------------------------------------------------------------------


            #--------------------------------------------------------------------------------------------------------------------------
            elif port == "111":
                cls()
                try:
                    port = int(port)
                    buffSize = 1024
                    payload = "echo"#raw_input("-"*70 + "\nWhat Do you want to send to (" + str(port) + ")?\n> ")
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(5) #10 is normal
                    s.connect((server, port))
                    s.send(payload)
                    data = s.recv(buffSize)
                    s.close()
                    print "Port[" + str(port) + "] | >  Response: | " + data.strip("\n") + "\n"
                except Exception, e:
                    e = str(e)
                    if "machine actively refused it" in e:
                        print str(port) + " | > Access Denied."
                    elif "timed out" in e:
                        print str(port) + " | > It Took Too Long For The Server To Respond... "
                    elif "forcibly closed" in e:
                        print str(port) + " | > The Server has closed the connection. "
                    else:
                        print str(port) + "Unknown Error: | > " + e
                except KeyboardInterrupt:
                    print "Port[" + port + "] | Connection Stopped."
            #--------------------------------------------------------------------------------------------------------------------------

                
            #--------------------------------------------------------------------------------------------------------------------------
            elif port == "443" or port == "587" or port == "25":
                userlist = ["admin","root","test","uploader","josh","bill","mike","agata","ftp","oracle","marketing",]
                passwdlist = ['oracle', 'root', 'abc123', 'password', '123456', 'admin', 'test', 'uploader', '123qwe', 'test', 'password', 'password', 'john', 'bill', 'abc123', 'mike', 'password', 'agata', 'ftp', 'admin', 'ftp123', 'ftpuser', 'password', 'marketing']
                print "SMTP Detected, \nValidating The Server is Reachable: \n" + "-"*65
                for user in userlist:
                    for passwd in passwdlist:
                        try:
                            print "[Trying Login] | >" + user + " - " + passwd
                            ftp = FTP(server)   # connect to host, default port
                            ftp.login()               # user anonymous, passwd anonymous@
                            print "[Login Found:] \n" + "-"*50 + "Server: " + server + ":21" + "\nUsername: " + user + "\nPassword: " + passwd + "-"*50
                            ftp.retrlines('LIST')     # list directory contents
                        except Exception, e:
                            e = str(e)
                            if "Login incorrect" in e:
                                pass
                            else:
                                print "[Error] | >" + e
                                getInput()
                        except KeyboardInterrupt:
                            pass
                import smtplib
                server = smtplib.SMTP('smtp.gmail.com', port)
                server.login("youremailusername", "password")
                msg = "\nHello!"
                server.sendmail("you@gmail.com", "target@example.com", msg)
                #--------------------------------------------------------------------------------------------------------------------------









            #----------------------------------------------------------------------------------------------------------------------------------------------------------------------
            else:
                try:
                    print "\n" + port
                    port = int(port)
                    buffSize = 1024
                    payload = "echo"#raw_input("-"*70 + "What Do you want to send to (" + str(port) + ")?\n> ")
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(5) #10 default
                    s.connect((server, port))
                    s.send(payload)
                    data = s.recv(buffSize)
                    s.close()
                    print "Port[" + str(port) + "] | >  Response: | " + data.strip("\n") + "\n"
                except Exception, e:
                    e = str(e)
                    if "machine actively refused it" in e:
                        print str(port) + " | > Access Denied."
                    elif "timed out" in e:
                        print str(port) + " | > It Took Too Long For The Server To Respond... "
                    elif "forcibly closed" in e:
                        print str(port) + " | > The Server has closed the connection. "
                    else:
                        print str(port) + "Unknown Error: | > " + e
                except KeyboardInterrupt:
                    print """
            ----------------------------------------------
            Connection Attempt Canceled.
            --------------------------------------
            Continue Scan-------(Any Key)
            --------------------------------------
                    """
                    getInput()
                    cls()
                    getScanType()
        print "-"*75
        getInput()
        cls()
        getScanType()
    except Exception, e:
        if "no att" in str(e):
            for port in ports:
                try:
                    port = int(port)
                    buffSize = 1024
                    payload = "User-agent Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1"
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(10)
                    s.connect((server, port))
                    s.send(payload)
                    data = s.recv(buffSize)
                    s.close()
                    print "Port[" + str(port) + "] | >  Response: | " + data.strip("\n") + "\n"
                except Exception, e:
                    e = str(e)
                    if "machine actively refused it" in e:
                        print "Port[" + str(port) + "] | > Access Denied."
                    elif "timed out" in e:
                        print "Port[" + str(port) + "] | > It Took Too Long For The Server To Respond... "
                    elif "forcibly closed" in e:
                        print "Port[" + str(port) + "] | > The Server has closed the connection. "
                    else:
                        print "Port[" + str(port) + "] Unknown Error: | > " + e
                except KeyboardInterrupt:
                    print """
            ----------------------------------------------
            Connection Attempt Canceled.
            --------------------------------------
            Continue Scan-------(Any Key)
            --------------------------------------
                    """
                    getInput()
                    cls()
                    getScanType()
            getInput()
            cls()
            getScanType()





def getHosts():
    try:
        computers = subprocess.call("net view > netCon.tmp", shell=True)
        f = open('netCon.tmp', 'r')
        f.readline();f.readline();f.readline()
        conn = []
        host = f.readline()
        while host[0] == '\\':
            conn.append(host[2:host.find(' ')])
            host = f.readline()
        f.close()
        
        path = defFile =  os.getcwd()
        subprocess.call("DEL /F /S /Q /A " + path + "\\netCon.tmp", shell=True)
        #print conn
        print "Scanning Network for Active Computers:\n>" + "-"*75
        for Con in conn:
            try:
                conIp = socket.gethostbyname(Con)
                #mac = getMAC(Con)
                print Con + " | " + conIp + " | "# + str(mac)
            except Exception,e:
                if "getaddrinfo failed" in str(e):
                    print "Failed to get: " + Con + "'s IP. | Reason: {" + str(e) + "}"
    except Exception,e:
        print "Error: " + (str(e))
    except KeyboardInterrupt:
        print "\nInformation Gathering Paused:\nPress x To Exit | (Press Any Other Key To Restart Scan!)"
        try:
            asgf = raw_input("> ")
        except KeyboardInterrupt:
            Choose()
            
        if asgf == "x":
            print "\n"*50
            subprocess.call("cls", shell=True)
            Choose()
        else:
            print "\n"*50
            subprocess.call("cls", shell=True)
            getHosts()
        
    try:
        print ">" + "-"*75
        getInput()
        cls()
        getScanType()
    except KeyboardInterrupt:
        print "Redoing Scan..."
        getHosts()
    Choose()





        
def getScanType():
    global smart
    remoteServer = getIP()
    cls()
    print """What type of scan do you want to do?:
--------------------------------------------
Small Scan:---------------------(1)
Scan Commonly Used:-------------(2)
Full Scan:----------------------(3)
Custom Scan:--------------------(4)
Smart Scan----------------------{5}
--------------------------------------------
"""
    try:
        scanType = getInput()
        scanType = scanType.strip()
        scanTo = "1025"
        scanFrom = "0"
    except KeyboardInterrupt:
        Choose()
        
    if scanType == "1":
        scanTo = "500"
        
    elif scanType == "2":
        scanTo = "1025"
        
    elif scanType == "3":
        scanTo = "65535"
        
    elif scanType == "4":
        print "For Default, Leave blank!\n" + "-"*50
        print "Scan From (Default 1): "
        scanFrom = getInput()
        print "Scan To (Default 1025):"
        scanTo = getInput()
        chars = "!@#$%^&*()-_=+\|]}[{\'\";:/?.>,<`~\\ " #If you mistype this will automaticle correct it for you!
        for bye in chars.split():
            scanFrom.strip(bye)
            scanTo.strip(bye)
        if len(scanTo) > 6:
            scanTo = "1025"
        else:
            pass
        if len(scanFrom) > 6:
            scanTo = "1"
        else:
            pass
        scanTo = scanTo.strip()
        if scanTo == "":
            scanTo = "1025"
        else:
            pass
        if scanFrom == "":
            scanFrom = "1"
            
        else:
            pass
    elif scanType == "5":
        smart = True
    else:
        cls()
        print "Input Error: " + scanType
        getScanType()
    cls()
    scanPorts(remoteServer, scanFrom, scanTo)
getScanType()
