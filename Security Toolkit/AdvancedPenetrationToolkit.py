#--------------------------------------------------------------------------
#----------------------\_______________
#Created By: Ben East   \              \
#--------------------------------------------------\
#Main Program Launch Script For the:               ||
#Advanced Penetration Toolkit                      |||>\_________
#By Benjamin East       .                          |||>/
#Licensed Under The GPL                            ||
#--------------------------------------------------/
#http://www.noWebsite.com  /--------/
#----------------------------/
#--------------------------------------------------------------------------

#All Default Python Modules Used:
#--------------------------------
import subprocess
import time
import sys
import os
#--------------------------------

#All Imported External Modules Used:
#--------------------------------
import colorama
from colorama import init
init()

#--------------------------------

#All of My Modules and Other Modules Used:
#-------------------------------------------
curLocten = os.path.dirname(os.path.abspath(__file__)) + "\lib\\"
import pause
import module_locator
import chooseAttack
from chooseAttack import findAttack
from setuptools.command import easy_install as install
from smsBomber import smsBomberScript
import smsBomber as smsBomb
import httpBrute
dirs = os.listdir(curLocten)
try:
    for x in dirs:
        importLib = curLocten + x + "\\"
        sys.path.append(importLib)
except Exception,e:
    print (str(e))
import aptCrawler
#--------------------------------

#Extra Information:
#-------------------------------------
#path = module_locator.module_path()
global started
started = False
#-------------------------------------
def cls():
    #This clears the Python Shell window with the new lines and console with cls.
    print "\n"*30
    subprocess.call("cls", shell=True)

    #Adds Linux Support:
    #subprocess.call("clear", shell=True)

def easyColor(color):
    if color == "blue":
        subprocess.call("color 09", shell=True)
    if color == "green":
        subprocess.call("color 0a", shell=True)
    if color == "aqua":
        subprocess.call("color 0b", shell=True)
    if color == "red":
        subprocess.call("color 0c", shell=True)
    if color == "purple":
        subprocess.call("color 0d", shell=True)
    if color == "yellow":
        subprocess.call("color 0e", shell=True)
    if color == "white":
        subprocess.call("color 0f", shell=True)
    if color == "gray":
        subprocess.call("color 08", shell=True)
    if color == "reset":
        subprocess.call("color 07", shell=True)

def getInput():
    try:
        inp = raw_input("> ")
        return inp.strip()
    except KeyboardInterrupt:
        pause.pause()
        if "1" in po:
            cls()
            startMenu()
        else:
            cls()
            getInput()
    except Exception,e:
        print "[Error] | > Unable to use the getInput() Function."
        print "[Reason] | > " + str(e)

        
def checkModules():
    installList = []
    #Check for Easy_Install
    try:
        from setuptools.command import easy_install as install
        print "Found: easy_install"
    except:
        print "Unable to find: easy_install (Please Install Right Away then Restart this script!)"
        print "Download Link: https://pypi.python.org/pypi/setuptools"
        try:
            subprocess.call('echo ' + "https://pypi.python.org/pypi/setuptools" + '| clip', shell=True)
            print "The Link Was Automatically Copied To Your Clipboard"
        except:
            pass
        raw_input("> ")


    #Check For APT Modules
    try:
        import module_locator
        print "Found: module_locator"
    except:
        print "Unable to find: module_locator.py | ask Windows65 for a new copy!"

    try:
        import chooseAttack
        print "Found: chooseAttack"
    except:
        print "Unable to find: chooseAttack.py | Download a New Copy Of Advanced Penetration Toolkit!"

    try:
        from smsBomber import smsBomberScript
        print "Found: smsBomber"
    except:
        print "Unable to find: smsBomber.py | Download a New Copy Of Advanced Penetration Toolkit!"
        

    #Check For External Modules
    try:
        import colorama
        print "Found: colorama"
    except Exception,e:
        if "No module" in str(e):
            try:
                f = open("C:\Python27\Lib\site-packages\easy-install.pth", "r")
                fnd = False
                for mod in f.readlines():
                    if "color" in mod:
                        fnd = True
                    else:
                        pass
                if fnd == True:
                    print "Found: colorama"
                else:
                    installList.append('colorama')
            except:
                installList.append('colorama')
        else:
            print "[Error] | > " + str(e) + " In the Module Installer."

    try:
        import scapy
        print "Found: scapy"
    except Exception,e:
        if "No module" in str(e):
            try:
                f = open("C:\Python27\Lib\site-packages\easy-install.pth", "r")
                fnd = False
                for mod in f.readlines():
                    if "scapy" in mod:
                        fnd = True
                    else:
                        pass
                if fnd == True:
                    print "Found: scapy"
                else:
                    installList.append('scapy')
            except:
                installList.append('scapy')
        else:
            print "[Error] | > " + str(e) + " In the Module Installer."
    try:
        import eventlet
        print "Found: eventlet"
    except Exception,e:
        if "No module" in str(e):
            try:
                f = open("C:\Python27\Lib\site-packages\easy-install.pth", "r")
                fnd = False
                for mod in f.readlines():
                    if "eventlet" in mod:
                        fnd = True
                    else:
                        pass
                if fnd == True:
                    print "Found: eventlet"
                else:
                    installList.append('eventlet')
            except:
                installList.append('eventlet')
        else:
            print "[Error] | > " + str(e) + " In the Module Installer."

    #Prompt For Instalation
    listLen = len(installList)
    if listLen > 0:
        print "----------------------------------\n\nModules Not Installed:\n----------------------"
        for x in installList:
            print x
        print "----------------------\nWould You Like To Install Now? (y/n)"
        asg = raw_input("> ")
        if "y" in asg:
            print ">------------------------------Install Process Beginning-------------------------------<\n"
            for module in installList:
                
                #Colorama install 
                try:
                    if module.strip() == "colorama":
                        print ">---------------Colorama Install Started---------------<"
                        install.main( "-U colorama".split())
                        print module + " Installed Successfully"
                        print ">---------------Colorama Install Finished---------------<\n"
                except Exception,e:
                    print "[Instalation Error] | > " + str(e)
                    print ("[Note] | > Please Retry In A Few Minutes or Install (%s) Manually...", module.strip())
                    getInput()
                    
                #Scrapy install
                try:
                    if module.strip() == "scapy":
                        print ">---------------Scapy Install Started---------------<"
                        install.main( "-U scapy".split())
                        print module + " Installed Successfully"
                        print ">---------------Scapy Install Finished---------------<\n"
                except Exception,e:
                    print "[Instalation Error] | > " + str(e)
                    print ("[Note] | > Please Retry In A Few Minutes or Install (%s) Manually...", module.strip())
                    getInput()

                #Eventlet install
                try:
                    if module.strip() == "eventlet":
                        print ">---------------Eventlet Install Started---------------<"
                        install.main( "-U eventlet".split())
                        print module + " Installed Successfully"
                        print ">---------------Eventlet Install Finished---------------<\n"
                except Exception,e:
                    print "[Instalation Error] | > " + str(e)
                    print ("[Note] | > Please Retry In A Few Minutes or Install (%s) Manually...", module.strip())
                    getInput()


            print ">--------------------------------Install Process Complete------------------------------<"
            raw_input("Press any key to continue:\n> ")
            cls()
        else:
            print "[Notice] | > You will need to install the list of modules below for this\nscript to work at its best:"
            print "----------------------"
            for x in installList:
                print x
            print "----------------------"
            
    else:
        pass



#As I Create New Attacks They Will Be Added In This Section!-----------------------------
def runAttack(choice):
    #>passwordAttacks
    if choice == "pass1":
        print choice

    elif choice == "pass2":
        httpBrute.httpBruteForce()
        startMenu()

    elif choice == "pass3":
        print choice


    #>exploitAttacks
    elif choice == "exploit1":
        print choice

    elif choice == "exploit2":
        print choice

    elif choice == "exploit3":
        print choice


    #>malwareGenerators
    elif choice == "malware1":
        print choice

    elif choice == "malware2":
        print choice

    elif choice == "malware3":
        print choice




    #>ddosAttacks
    elif choice == "ddos1":
        print choice

    elif choice == "ddos2":
        print choice

    elif choice == "ddos3":
        print choice




    #>spamAttacks
    elif choice == "spam1":
        cls()
        smsBomb.smsBomberScript()
        startMenu()

    elif choice == "spam2":
        print choice

    elif choice == "spam3":
        print choice


    #>webAttacks
    elif choice == "web1":
        print choice

    elif choice == "web2":
        print choice

    elif choice == "web3":
        print choice

    elif choice == "web4":
        cls()
        portScan.chooseScan()
        startMenu()

    elif choice == "web5":
        cls()
        aptCrawler.scraperChoose()
        startMenu()

    #>Analysis
    elif choice == "analysis1":
        print choice

    elif choice == "analysis2":
        print choice

    elif choice == "analysis3":
        print choice


    #>spoofingAttacks
    elif choice == "spoof1":
        print choice

    elif choice == "spoof2":
        print choice

    elif choice == "spoof3":
        print choice


    #>ratAttacks
    elif choice == "rat1":
        print choice

    elif choice == "rat2":
        print choice

    elif choice == "rat3":
        print choice


    #>mainHelp
    elif choice == "help1":
        print """
In order to know what tool you should use, go to Google and ask
how to do what you want to do. Once you are done, you should have
more of an idea of what to do.

For Example:
I want to hack a gmail account, so
I eventually learn that it is a Brute force attack on the SMTP protocol.
I then know to use Gmail Brute Force.
        """
        getInput()

    elif choice == "help2":
        print """
This whole program is a set of tools built for power
and simplicity. My goal is to make high quality progams.
You can use this toolkit to do many things that you could get in trouble for
Be careful with how you use these tools, I am not responsible for
any of your actions.
        """
        getInput()

    elif choice == "help3":
        print """
You can contact through the forum you got this tool from
or by Email if provided through the forum.
        """

    elif choice == "help4":
        print """
To have your penetration tool added to this toolkit
for the rest of the world to use, you will need to give me your email,
the code, a POC, and detailed description of what the code is used for.
I do not accept anything other than .py files which will be
heavily analysed before running.
        """
        getInput()
        
    elif choice == "help5":
        print """
For more information or questions regarding this toolkit contact me
through the forum/place you got this tool from. You may send
another form of communication through that messaging system
and we will talk from there.

Thank you.
        """
        getInput()
#End Of My Tools!


#Add Your Tools Here!-------------------------------
    #>userTemplates
    elif choice == "user1":
        print choice

    elif choice == "user2":
        print choice

    elif choice == "user3":
        print choice

    elif choice == "user4":
        print choice

    elif choice == "user5":
        print choice
#End Of Personal Tool List

    else:
        print "Going back to main menu: "
        startMenu()



def startMenu():
    global started
    if started == False:

        easyColor("green")
        print """
Welcome To the Advanced Penetration Toolkit by Benjamin East.
This is not meant for malicious usage though I cannot control your
Behavior, I just ask that you use this as responsibility,
Thank you. 

(By Continuing or Altering this File You Agree That I Am Not
Responsible For Anything You Do With These Tools!)
------------------------------------------------------------------------
Press any key to continue to the start menu:
    """
        getInput()
        easyColor("reset")
        cls()


        print "Checking For Missing Modules!\n----------------------------------"
        checkModules()
        print "----------------------------------\nDone Checking Modules!"
        time.sleep(0.3)
    cls()
    easyColor("reset")
    started = True
    print"""
{I suggest going to help first!}
>----------------------------\\
Choose A Category To Proceed: \\
>------------------------------------------\\
{1}: {Password Attacks} -------------------|
{2}: {Exploitation} -----------------------|
{3}: {Malware Generators} -----------------|
{4}: {DoS/DDoS Attacks} -------------------|
{5}: {Spam Attacks} -----------------------|
{6}: {Web Attacks} ------------------------|
{7}: {System Analysis} --------------------|
{8}: {Spoofing} ---------------------------|
{9}: {Remote Administration} --------------|
{10}:{User Templates} ---------------------|
{11}:{Help} -------------------------------|
>------------------------------------------/

Input The Number of Your Selection and Press Enter:"""

    chosenAttackMethod = getInput()
    try:
        execChoice = 0
                                              #List Access Numbers:
        finalChoice = ["Filler",              #0 (This is so I can go by the number the user chooses) Skips 0
                       "passwordAttacks",     #1
                       "exploitAttacks",      #2
                       "malwareGenerators",   #3
                       "ddosAttacks",         #4
                       "spamAttacks",         #5
                       "webAttacks",          #6
                       "Analysis",            #7
                       "spoofingAttacks",     #8
                       "ratAttacks",          #9
                       "userTemplates",       #10
                       "help"]                #11
        runAttack(chooseAttack.findAttack(finalChoice[int(chosenAttackMethod.strip())]))
        cls()
        startMenu()
    except Exception,e:
        print "Error: " + (str(e))
        getInput()
        startMenu()
    except KeyboardInterrupt:
        pause.pause()

#Start The Script At startMenu():
if __name__ == "__main__":
    startMenu()
