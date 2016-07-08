[7/14/14]
I have worked as hard as I can to make a fast, clean, and reliable script to fit any situation you may come across.
Most if not all errors you will come across are taken care of hopefully, I have tested the script to the fullest extent.
The main thing you will have to watch out for is how your input certian things, here is a small tutorial:


How to use this script:
I have built this script to be as simple and comprehendable as possible,

When you first launch the script you should see:

Please select the perfered scan type!
----------------------------------------
>Scan One Host-------------{1}
>Scan A range Of Hosts-----{2}
----------------------------------------

> 

To choose an option insert the option number specified on the right of the option 
you want and press enter. 

If you choose option 1 it is pretty simple from there on out.

If you choose option two there is a bit extra work to do, let me explain:
You will be greeted with this view:


                                          Colon Required
                                               \/
Enter a range of hosts to scan: Ex: 192.168.0.0 : 192.168.999.999
--------------------------------------------------------------------
            

> 

This option scans a range of IP addresses inputed into the script,
It is required that you put a colon between the two addresses so the 
script will know when the new IP starts, the addresses Have to be in the
regular IP format for the script to correctly read them. You will receive
an out of range error if it is too short or two long. You can put spaces 
if you like for it to like for it to look neater, it takes them out when it processess the 
ip's. It only gets the range of the last number in the IP, anything before that is not
supported.



When it comes to the speed of the scan I had to find the happy medium between accuracy and speed,
for a web scan the timeout is set to 0.1 and for anything else it is set to 0.01. You may change
these values based on these speeds though they are mainly effected by the servers connection speed.



If you would like to see which port it is currently on change "debug = False" to "debug = True"
If you turn it on it may slow the total process down, if you leave it off it will still
display open ports as it finds them. It just looks better without it. Also, if you do have it
on, it will display all open ports and the IP they belong to at the end of the scan.

Also, be careful with CTRL + C, sometimes it will return NoneType and you will have to 
restart the script.

If the port definition file is not with the script it will give you a big error and 
tell you how to easily fix it. It is a very cool feature to have in a port scanner!
the port definition file Must be in the format that the origional file came with when
you received this script, {port  type  desc}, a URL to the origional resource is provided
in the Error dialog if you get the error.


Here is an example run I have ran on my network:
######################################################################################################################################################

STAGE 1:
===================================================================================================
Please select the perfered scan type!
----------------------------------------
>Scan One Host-------------{1}
>Scan A range Of Hosts-----{2}
>List Hosts Online---------{3}
----------------------------------------

> 1
===================================================================================================



STAGE 2:
===================================================================================================
Enter a remote host to scan: 

> localhost
===================================================================================================



STAGE 3:
===================================================================================================
What type of scan do you want to do?:
--------------------------------------------
Small Scan:---------------------(1)
Scan Commonly Used:-------------(2)
Full Scan:----------------------(3)
Custom Scan:--------------------(4)
--------------------------------------------


> 3
===================================================================================================



STAGE 4:
===================================================================================================
Open Ports: 
---------------------------------------------------------------------------
[Port Found] | 80 | TCP | World Wide Web (HTTP)
[Port Found] | 135 | TCP | DCE endpoint resolution
[Port Found] | 443 | TCP | HTTP protocol over TLS/SSL (Mostly Mail Services)
[Port Found] | 445 | TCP | Microsoft-DS
[Port Found] | 5$5$ | TCP | Information Not Found!
[Port Found] | 2$1$3 | TCP | Information Not Found!
[Port Found] | 27$15 | TCP | Information Not Found!
[Port Found] | 4$152 | TCP | Information Not Found!
[Port Found] | $9153 | TCP | Information Not Found!
[Port Found] | 49$5$ | TCP | Information Not Found!
[Port Found] | 491$5 | TCP | Information Not Found!
[Port Found] | 4$156 | TCP | Information Not Found!
[Port Found] | $9173 | TCP | Information Not Found!
[Port Found] | 596$4 | TCP | Information Not Found!
[Port Found] | $1$1$ | TCP | Information Not Found!
[Port Found] | $2$45 | TCP | Information Not Found!
[Port Found] | 6$4$7 | TCP | Information Not Found!
[Port Found] | $24$$ | TCP | Information Not Found!
Attack All Ports. | Type: (all)
---------------------------------------------------------------------------

Completed In: Days: 0 | Hours: 0 | Minutes: 0 | Seconds: 10
----------------------------------------------------------------------
Choose a port to attack from (Multiple Supported.) | Ex: [80,443,22,8080]
Leave blank for None.

> 
===================================================================================================



STAGE 5:
===================================================================================================
Beggining Port connection on | 127.0.0.1
---------------------------------------------------------------------------

80
80 | >  Response: | ÀÂÈïzþh ?Úì? 5??À3Ú?çWs??fÇ?%??ú9e0)wc(Y?/u"?`QNçlí:ã8Iæ?ÄeRA~WÝjSè9tU??À1?ÇÌ?Ø)F$E?

---------------------------------------------------------------------------

> 
===================================================================================================




-RESETS TO MAIN MENU-

######################################################################################################################################################

I hope you like the script, I did the best I can, if you have any questions regarding
this script or future projects feel free to message me on Fiverr or perferabally email
me at east837@gmail.com. I check my Email every day and it gives us more freedom in our conversations.

Thank you for using my service, Please let me know what you think, did I do a good job? I am always looking
for improvments!
-Windows65
-Paradox Technologies

