import AdvancedPenetrationToolkit
def findAttack(choice):
    if choice == "passwordAttacks":
        print """
Available Password Attacks:
/------------------------------\\
|(1): SMTP Brute Force
|(2): Web Brute Force
|(3): Local Brute Force
\\------------------------------/
"""
        chosenAttack = AdvancedPenetrationToolkit.getInput()
        chosenAttack = "pass"+chosenAttack
        return chosenAttack
    
    elif choice == "exploitAttacks":
        print """
Available Exploitation Attacks:
/------------------------------\\
|(1): Windows Backdoor Generator
|(2): Python Code Injection
|(3): Exploitation Code Generator
\\------------------------------/
"""
        chosenAttack = AdvancedPenetrationToolkit.getInput()
        chosenAttack = "exploit"+chosenAttack
        return chosenAttack
    
    elif choice == "malwareGenerators":
        print """
Available Malware Generators:
/------------------------------\\
|(1): Trojan Generator
|(2): Virus Generator
|(3): Worm Generator
\\------------------------------/
"""
        chosenAttack = AdvancedPenetrationToolkit.getInput()
        chosenAttack = "malware"+chosenAttack
        return chosenAttack
    
    elif choice == "ddosAttacks":
        print """
Available DDoS/DoS Attacks:
/------------------------------\\
|(1): TCP DDoS/DoS
|(2): UDP DDoS/DoS
|(3): HTTP DDoS/DoS
\\------------------------------/
"""
        chosenAttack = AdvancedPenetrationToolkit.getInput()
        chosenAttack = "ddos"+chosenAttack
        return chosenAttack
    
    elif choice == "spamAttacks":
        print """
Available Spam Attacks:
/------------------------------\\
|(1): SMS Bomber
|(2): Email Spam Generator
|(3): Skype Spammer
\\------------------------------/
"""
        chosenAttack = AdvancedPenetrationToolkit.getInput()
        chosenAttack = "spam"+chosenAttack
        return chosenAttack
    
    elif choice == "webAttacks":
        print """
Available Web Attacks:
/------------------------------\\
|(1): SQL-Injection Test
|(2): Cross Site Scripting (XSS)
|(3): Custom Code Injection
|(4): Port Scanner
|(5): Web Crawler
\\------------------------------/
"""
        chosenAttack = AdvancedPenetrationToolkit.getInput()
        chosenAttack = "web"+chosenAttack
        return chosenAttack
    
    elif choice == "Analysis":
        print """
Available System Analysis Tools:
/------------------------------\\
|(1): Packet Sniffer
|(2): Registry Viewer
|(3): File Sniffer
\\------------------------------/
"""
        chosenAttack = AdvancedPenetrationToolkit.getInput()
        chosenAttack = "analysis"+chosenAttack
        return chosenAttack
    
    elif choice == "spoofingAttacks":
        print """
Available Spoofing Attacks:
/------------------------------\\
|(1): ARP/DNS Spoofing
|(2): MAC Spoofing
|(3): IP Spoofing
\\------------------------------/
"""
        chosenAttack = AdvancedPenetrationToolkit.getInput()
        chosenAttack = "spoof"+chosenAttack
        return chosenAttack
    
    elif choice == "ratAttacks":
        print """
Available Remote Access Tools:
/------------------------------\\
|(1): File Theft
|(2): Key Logger
|(3): BotNet
\\------------------------------/
"""
        chosenAttack = AdvancedPenetrationToolkit.getInput()
        chosenAttack = "rat"+chosenAttack
        return chosenAttack
    


    elif choice == "help":
        print """
Available Help Options Attacks:
/------------------------------\\
|(1): What Tool Should I Use?
|(2): How Can This Be Used?
|(3): How Do I Contact the Creator?
|(4): How Do I Submit My Own Tools?
|(5): Need to know more? Choose this!
\\------------------------------/
"""
        chosenAttack = AdvancedPenetrationToolkit.getInput()
        chosenAttack = "help"+chosenAttack
        return chosenAttack



    elif choice == "userTemplates":
        print """
Available User Templates:
/------------------------------\\
|(1): Add Penetration Tool Here!
|(2): Add Penetration Tool Here!
|(3): Add Penetration Tool Here!
|(4): Add Penetration Tool Here!
|(5): Add Penetration Tool Here!
\\------------------------------/
"""
        chosenAttack = AdvancedPenetrationToolkit.getInput()
        chosenAttack = "user"+chosenAttack
        return chosenAttack
    

    


        
    else:
        return "Attack Not Found"
    
    


if __name__ == '__main__':
    findAttack(finalChoice)
