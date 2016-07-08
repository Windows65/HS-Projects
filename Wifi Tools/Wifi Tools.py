#Credit to Pedro Gomes for the origional Wifi Network Detection Script
#The rest of this software was designed by Benjamin East

from datetime import datetime, timedelta
from multiprocessing import Pool
from ctypes.wintypes import *
from ftplib import FTP
from sys import exit
from ctypes import *
import subprocess
import struct
import ctypes
import socket
import time
import sys
import re
import os

global multiScan
global avaMem
global debug


debug = False
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
            print "Enter a remote host to scan: (Try localhost)"
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
--------------------------------------------------------
You are missing the Port Definition File!
Please insert {portDefs.txt} in the same folder the
script is in! If you are missing the contents if the file
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












def customresize(array, new_size):
    return (array._type_*new_size).from_address(addressof(array))

wlanapi = windll.LoadLibrary('wlanapi.dll')
ERROR_SUCCESS = 0
class memoryCheck():
    #Credit to: http://doeidoei.wordpress.com/2009/03/22/python-tip-3-checking-available-ram-with-python/
 
    def __init__(self):
        self.value = self.windowsRam()
 
    def windowsRam(self):
        global avaMem
        """Uses Windows API to check RAM in this OS""" 
        kernel32 = ctypes.windll.kernel32
        c_ulong = ctypes.c_ulong
        class MEMORYSTATUS(ctypes.Structure):
            _fields_ = [
                ("dwLength", c_ulong),
                ("dwMemoryLoad", c_ulong),
                ("dwTotalPhys", c_ulong),
                ("dwAvailPhys", c_ulong),
                ("dwTotalPageFile", c_ulong),
                ("dwAvailPageFile", c_ulong),
                ("dwTotalVirtual", c_ulong),
                ("dwAvailVirtual", c_ulong)
            ]
        memoryStatus = MEMORYSTATUS()
        memoryStatus.dwLength = ctypes.sizeof(MEMORYSTATUS)
        kernel32.GlobalMemoryStatus(ctypes.byref(memoryStatus))
        memz = memoryStatus.dwTotalPhys/1024**2
        #print memz
        #Would have done a direct return but it would not pass the number of memory
        avaMem = memz
    
class GUID(Structure):
    _fields_ = [
        ('Data1', c_ulong),
        ('Data2', c_ushort),
        ('Data3', c_ushort),
        ('Data4', c_ubyte*8),
        ]

WLAN_INTERFACE_STATE = c_uint
(wlan_interface_state_not_ready,
 wlan_interface_state_connected,
 wlan_interface_state_ad_hoc_network_formed,
 wlan_interface_state_disconnecting,
 wlan_interface_state_disconnected,
 wlan_interface_state_associating,
 wlan_interface_state_discovering,
 wlan_interface_state_authenticating) = map(WLAN_INTERFACE_STATE, xrange(0, 8))

class WLAN_INTERFACE_INFO(Structure):
    _fields_ = [
        ("InterfaceGuid", GUID),
        ("strInterfaceDescription", c_wchar * 256),
        ("isState", WLAN_INTERFACE_STATE)
    ]

class WLAN_INTERFACE_INFO_LIST(Structure):
    _fields_ = [
        ("NumberOfItems", DWORD),
        ("Index", DWORD),
        ("InterfaceInfo", WLAN_INTERFACE_INFO * 1)
    ]

WLAN_MAX_PHY_TYPE_NUMBER = 0x8
DOT11_SSID_MAX_LENGTH = 32
WLAN_REASON_CODE = DWORD

DOT11_BSS_TYPE = c_uint
(dot11_BSS_type_infrastructure,
 dot11_BSS_type_independent,
 dot11_BSS_type_any) = map(DOT11_BSS_TYPE, xrange(1, 4))

DOT11_PHY_TYPE = c_uint
dot11_phy_type_unknown      = 0
dot11_phy_type_any          = 0
dot11_phy_type_fhss         = 1
dot11_phy_type_dsss         = 2
dot11_phy_type_irbaseband   = 3
dot11_phy_type_ofdm         = 4
dot11_phy_type_hrdsss       = 5
dot11_phy_type_erp          = 6
dot11_phy_type_ht           = 7
dot11_phy_type_IHV_start    = 0x80000000
dot11_phy_type_IHV_end      = 0xffffffff

DOT11_AUTH_ALGORITHM = c_uint
DOT11_AUTH_ALGO_80211_OPEN         = 1
DOT11_AUTH_ALGO_80211_SHARED_KEY   = 2
DOT11_AUTH_ALGO_WPA                = 3
DOT11_AUTH_ALGO_WPA_PSK            = 4
DOT11_AUTH_ALGO_WPA_NONE           = 5
DOT11_AUTH_ALGO_RSNA               = 6
DOT11_AUTH_ALGO_RSNA_PSK           = 7
DOT11_AUTH_ALGO_IHV_START          = 0x80000000
DOT11_AUTH_ALGO_IHV_END            = 0xffffffff

DOT11_CIPHER_ALGORITHM = c_uint
DOT11_CIPHER_ALGO_NONE            = 0x00
DOT11_CIPHER_ALGO_WEP40           = 0x01
DOT11_CIPHER_ALGO_TKIP            = 0x02
DOT11_CIPHER_ALGO_CCMP            = 0x04
DOT11_CIPHER_ALGO_WEP104          = 0x05
DOT11_CIPHER_ALGO_WPA_USE_GROUP   = 0x100
DOT11_CIPHER_ALGO_RSN_USE_GROUP   = 0x100
DOT11_CIPHER_ALGO_WEP             = 0x101
DOT11_CIPHER_ALGO_IHV_START       = 0x80000000
DOT11_CIPHER_ALGO_IHV_END         = 0xffffffff

WLAN_AVAILABLE_NETWORK_CONNECTED = 1
WLAN_AVAILABLE_NETWORK_HAS_PROFILE = 2

WLAN_AVAILABLE_NETWORK_INCLUDE_ALL_ADHOC_PROFILES = 0x00000001
WLAN_AVAILABLE_NETWORK_INCLUDE_ALL_MANUAL_HIDDEN_PROFILES = 0x00000002

class DOT11_SSID(Structure):
    _fields_ = [
        ("SSIDLength", c_ulong),
        ("SSID", c_char * DOT11_SSID_MAX_LENGTH)
    ]


class WLAN_AVAILABLE_NETWORK(Structure):
    _fields_ = [
        ("ProfileName", c_wchar * 256),
        ("dot11Ssid", DOT11_SSID),
        ("dot11BssType", DOT11_BSS_TYPE),
        ("NumberOfBssids", c_ulong),
        ("NetworkConnectable", c_bool),
        ("wlanNotConnectableReason", WLAN_REASON_CODE),
        ("NumberOfPhyTypes", c_ulong),
        ("dot11PhyTypes", DOT11_PHY_TYPE * WLAN_MAX_PHY_TYPE_NUMBER),
        ("MorePhyTypes", c_bool),
        ("wlanSignalQuality", c_ulong),
        ("SecurityEnabled", c_bool),
        ("dot11DefaultAuthAlgorithm", DOT11_AUTH_ALGORITHM),
        ("dot11DefaultCipherAlgorithm", DOT11_CIPHER_ALGORITHM),
        ("Flags", DWORD),
        ("Reserved", DWORD)
    ]

class WLAN_AVAILABLE_NETWORK_LIST(Structure):
    _fields_ = [
        ("NumberOfItems", DWORD),
        ("Index", DWORD),
        ("Network", WLAN_AVAILABLE_NETWORK * 1)
    ]


DOT11_MAC_ADDRESS = c_ubyte * 6

DOT11_CIPHER_ALGORITHM = c_uint
DOT11_CIPHER_ALGO_NONE            = 0x00
DOT11_CIPHER_ALGO_WEP40           = 0x01
DOT11_CIPHER_ALGO_TKIP            = 0x02

DOT11_PHY_TYPE = c_uint
DOT11_PHY_TYPE_UNKNOWN  = 0
DOT11_PHY_TYPE_ANY         = 0
DOT11_PHY_TYPE_FHSS        = 1
DOT11_PHY_TYPE_DSSS        = 2
DOT11_PHY_TYPE_IRBASEBAND  = 3
DOT11_PHY_TYPE_OFDM        = 4
DOT11_PHY_TYPE_HRDSSS      = 5
DOT11_PHY_TYPE_ERP         = 6
DOT11_PHY_TYPE_HT          = 7
DOT11_PHY_TYPE_IHV_START   = 0X80000000
DOT11_PHY_TYPE_IHV_END     = 0XFFFFFFFF

class WLAN_RATE_SET(Structure):
    _fields_ = [
        ("uRateSetLength", c_ulong),
        ("usRateSet", c_ushort * 126)
    ]

class WLAN_BSS_ENTRY(Structure):
    _fields_ = [
        ("dot11Ssid",DOT11_SSID),
        ("uPhyId",c_ulong),
        ("dot11Bssid", DOT11_MAC_ADDRESS),
        ("dot11BssType", DOT11_BSS_TYPE),
        ("dot11BssPhyType", DOT11_PHY_TYPE),
        ("lRssi", c_long),
        ("uLinkQuality", c_ulong),
        ("bInRegDomain", c_bool),
        ("usBeaconPeriod",c_ushort),
        ("ullTimestamp", c_ulonglong),
        ("ullHostTimestamp",c_ulonglong),
        ("usCapabilityInformation",c_ushort),
        ("ulChCenterFrequency", c_ulong),
        ("wlanRateSet",WLAN_RATE_SET),
        ("ulIeOffset", c_ulong),
        ("ulIeSize", c_ulong)]

class WLAN_BSS_LIST(Structure):
    _fields_ = [
        ("TotalSize", DWORD),
        ("NumberOfItems", DWORD),
        ("NetworkBSS", WLAN_BSS_ENTRY * 1)
    ]

class WLAN_AVAILABLE_NETWORK_LIST_BSS(Structure):
    _fields_ = [
        ("TotalSize", DWORD),
        ("NumberOfItems", DWORD),
        ("Network", WLAN_BSS_ENTRY * 1)
    ]

WlanOpenHandle = wlanapi.WlanOpenHandle
WlanOpenHandle.argtypes = (DWORD, c_void_p, POINTER(DWORD), POINTER(HANDLE))
WlanOpenHandle.restype = DWORD

WlanCloseHandle = wlanapi.WlanCloseHandle
WlanCloseHandle.argtypes = (HANDLE, c_void_p)
WlanCloseHandle.restype = DWORD

WlanEnumInterfaces = wlanapi.WlanEnumInterfaces
WlanEnumInterfaces.argtypes = (HANDLE, c_void_p,
                               POINTER(POINTER(WLAN_INTERFACE_INFO_LIST)))
WlanEnumInterfaces.restype = DWORD

WlanGetAvailableNetworkList = wlanapi.WlanGetAvailableNetworkList
WlanGetAvailableNetworkList.argtypes = (HANDLE, POINTER(GUID), DWORD, c_void_p,
                                        POINTER(POINTER(WLAN_AVAILABLE_NETWORK_LIST)))
WlanGetAvailableNetworkList.restype = DWORD

WlanGetNetworkBssList = wlanapi.WlanGetNetworkBssList
WlanGetNetworkBssList.argtypes = (HANDLE, POINTER(GUID),POINTER(GUID),POINTER(GUID), c_bool, c_void_p,
                                  POINTER(POINTER(WLAN_BSS_LIST)))
WlanGetNetworkBssList.restype = DWORD


WlanFreeMemory = wlanapi.WlanFreeMemory
WlanFreeMemory.argtypes = [c_void_p]


WlanScan = wlanapi.WlanScan
WlanScan.argtypes = (HANDLE, POINTER(GUID),c_void_p,c_void_p, c_void_p)
WlanScan.restype = DWORD




def get_interface():

    NegotiatedVersion = DWORD()
    ClientHandle = HANDLE()
    ret = WlanOpenHandle(1, None, byref(NegotiatedVersion), byref(ClientHandle))
    if ret != ERROR_SUCCESS:
        exit(FormatError(ret))
        # find all wireless network interfaces
    pInterfaceList = pointer(WLAN_INTERFACE_INFO_LIST())
    ret = WlanEnumInterfaces(ClientHandle, None, byref(pInterfaceList))
    if ret != ERROR_SUCCESS:
        exit(FormatError(ret))
    try:
        ifaces = customresize(pInterfaceList.contents.InterfaceInfo,
                              pInterfaceList.contents.NumberOfItems)
        # find each available network for each interface
        for iface in ifaces:
            #print "Interface: %s" % (iface.strInterfaceDescription)
            interface = iface.strInterfaceDescription

    finally:
        WlanFreeMemory(pInterfaceList)
        return interface

class MAC_BSSID_POWER:
    """Classe para os valores retirados"""
    def __init__(self, mac, bssid):

        self.mac = str(mac)
        self.bssid = str(bssid)
        self.valores = []

    def addPower(self,power):
        self.valores.append(int(power))

    def getBssid(self):
        return self.bssid
    def getPowers(self):
        return self.valores
    def getMac(self):
        return self.mac


def get_BSSI():

    BSSI_Values={}

    NegotiatedVersion = DWORD()
    ClientHandle = HANDLE()
    ret = WlanOpenHandle(1, None, byref(NegotiatedVersion), byref(ClientHandle))
    if ret != ERROR_SUCCESS:
        exit(FormatError(ret))
        # find all wireless network interfaces
    pInterfaceList = pointer(WLAN_INTERFACE_INFO_LIST())
    ret = WlanEnumInterfaces(ClientHandle, None, byref(pInterfaceList))
    if ret != ERROR_SUCCESS:
        exit(FormatError(ret))
    try:
        ifaces = customresize(pInterfaceList.contents.InterfaceInfo,
                              pInterfaceList.contents.NumberOfItems)
        # find each available network for each interface
        for iface in ifaces:
            # print "Interface: %s" % (iface.strInterfaceDescription)

            pAvailableNetworkList2 = pointer(WLAN_BSS_LIST())


            ret2 = WlanGetNetworkBssList(ClientHandle,
                                         byref(iface.InterfaceGuid),
                                         None,
                                         None,True,None,
                                         byref(pAvailableNetworkList2))
            if ret2 != ERROR_SUCCESS:
                exit(FormatError(ret2))
            try:
                retScan = WlanScan(ClientHandle,byref(iface.InterfaceGuid),None,None,None)
                if retScan != ERROR_SUCCESS:
                    exit(FormatError(retScan))
                avail_net_list2 = pAvailableNetworkList2.contents
                networks2 = customresize(avail_net_list2.NetworkBSS,
                                         avail_net_list2.NumberOfItems)
                wifiList = []
                string = ""
                for network in networks2:

                    SSID = str(network.dot11Ssid.SSID[:network.dot11Ssid.SSIDLength])
                    BSSID = ':'.join('%02x' % b for b in network.dot11Bssid).upper()
                    signal_strength = str(network.lRssi)
                    signal_strength = signal_strength.replace("-", "%")


                    #print 'SSID: ({0:2s})  MAC: <{1:3s}> Signal Quality: [{2:4s}]'.format(SSID, BSSID, signal_strength)

                    
                    wifiList.append('SSID: ({0:2s}) | MAC: ({1:3s}) | Signal Quality: [{2:4s}]'.format(SSID, BSSID, signal_strength))
                    BSSI_Values[BSSID] = [SSID,signal_strength]

            finally:
                WlanFreeMemory(pAvailableNetworkList2)
                WlanCloseHandle(ClientHandle,None)
    finally:
        WlanFreeMemory(pInterfaceList)
    #return BSSI_Values
    return wifiList


def get_BSSI_times_and_total_seconds(times,seconds):

    BSSI_to_return = {}

    for i in range(0,seconds*times):
        time_to_sleep = float(1.0/times)
        time.sleep(time_to_sleep)
        got_bssi_temp = get_BSSI()

        for bssi in got_bssi_temp:
            if not BSSI_to_return.get(bssi):
                BSSI_to_return[bssi] = MAC_BSSID_POWER(bssi,got_bssi_temp[bssi][0])
                BSSI_to_return[bssi].addPower( got_bssi_temp[bssi][1] )

                #BSSI_to_return[bssi] = [got_bssi_temp[bssi][1]]

            else:
                BSSI_to_return[bssi].addPower( got_bssi_temp[bssi][1] )
                #BSSI_to_return[bssi].append(got_bssi_temp[bssi][1])
        print "Medicao "+str(i)+" de "+str(seconds*times)
    print BSSI_to_return
    return BSSI_to_return

def pentestPort(ports,server):
    cls()
    print "Beggining Port connection on | " + server + " | -No Security Test is Performed as of Now\n" + "-"*75
    if len(ports) == 0:
        cls()
        Choose()
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
                try:
                    br = mechanize.Browser()
                    br.set_handle_robots(False)
                    br.set_debug_http(True)
                    br.set_debug_redirects(True)
                    br.set_debug_responses(True)
                    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
                    br.open("www." + server + ".com", timeout=10.0)
                    br._factory.is_html = True
                    for link in br.links():
                        print link
                except Exception, e:
                    print "[Error] | " + str(e)
                except KeyboardInterrupt:
                    print "Port[" + port + "] | Connection Stopped."
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
                    Choose()
        print "-"*75
        getInput()
        cls()
        Choose()
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
                    Choose()
            getInput()
            cls()
            Choose()




def WifiScan():
    #Credit to origional owner for the script that gathers Wifi information!
    #I have lightly edited it for my purposes, excelent code.
    import time
    wifiLogFile = open("wifiDetectionLog.log", "w")
    try:
        delay = raw_input("Update Frequency(Sec/Dec): > ")
        try:
            delay = float(delay)
        except Exception,e:
            print "Input Error: {" + str(e) + "}"
            Choose()
    except KeyboardInterrupt:
        Choose()
    except Exception,e:
        print "Error: " + str(e)
        raw_input("> ")
        WifiScan()
    WifiScan = get_BSSI()
    while True:
        try:
            oldWifiScan = WifiScan
            WifiScan = get_BSSI()
            print "\n"*50
            #wifiogFile.write("\n")
            subprocess.call("cls", shell=True)
            for detection in WifiScan:
                print detection
                wifiLogFile.write(detection + "\n")
            time.sleep(delay)
        except Exception,e:
            print "Error: " + str(e)
            raw_input("> ")
            Choose()
        except KeyboardInterrupt:
            print "Monitering Paused:\nPress x To Exit | Number To Change Speed | (Any Other Key To Continue Scan!)"
            try:
                asgf = raw_input("> ")
            except KeyboardInterrupt:
                wifiLogFile.close()
                Choose()
            if asgf == "x":
                print "\n"*30
                subprocess.call("cls", shell=True)
                wifiLogFile.close()
                Choose()
            try:
                delay = float(asgf)
            except:
                pass
            else:
                pass
            





def viewComputers():
    import socket
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
        import os
        path = os.path.dirname(os.path.realpath(__file__))
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
                    print "Failed to get: " + Con + "'s IP. Reason: {" + str(e) + "}"
                    
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
            viewComputers()
        
    try:
        print ">" + "-"*75
        raw_input("> ")
    except KeyboardInterrupt:
        print "Redoing Scan..."
        viewComputers()
    Choose()









def wakeComputer(mac, ip):
    if len(mac) == 12:
        pass
    elif len(mac) == 12 + 5:
        sep = mac[2]
        mac = mac.replace(sep, '')
    else:
        print 'Incorrect MAC address format\n Correct Format Example: (XX-XX-XX-XX-XX-XX)'
        raw_input("> ")
        Choose()
    data = ''.join(['FFFFFFFFFFFF', mac * 20])
    send_data = '' 
    for i in range(0, len(data), 2):
        send_data = ''.join([send_data,
        struct.pack('B', int(data[i: i + 2], 16))])
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(send_data, ('<broadcast>', 7))
    print "Data Sent: (Checking For Responsivness)"
    response = 0
    try:
        while True:
            print "Pinging: " + ip
            response = subprocess.call("ping -l 1 -n 1 -w 1000 -4 " + ip, shell=True)
            if response == 1:
                pass
            else:
                break
    except Exception,e:
        print "Error: " + (str(e))
    except KeyboardInterrupt:
        print "\nYou Have Pause The Connection:\nPress x To Exit | (Press Any Other Key To Continue!)"
        try:
            asgf = raw_input("> ")
        except KeyboardInterrupt:
            Choose()
        if asgf == "x":
            print "\n"*50
            subprocess.call("cls", shell=True)
            Choose()
        else:
            wakeComputer(mac, ip)
    try:
        print "Computer Found!"
        raw_input("> ")
        Choose() 
    except:
        Choose()    




def getMAC(IP):
    listOfMacs = []
    IP = IP.strip()
    import socket
    computers = subprocess.call("getmac /NH -s " + IP + " > getMac.tmp", shell=True)
    f = open('getMac.tmp', 'r')
    for lin in f.readlines():
        if "-" in lin:
            mac = lin.split("   ")
            #print mac[0]
            listOfMacs.append(mac[0])
        else:
            pass
    f.close()
    import os
    path = os.path.dirname(os.path.realpath(__file__))
    subprocess.call("DEL /F /S /Q /A " + path + "\\getMac.tmp", shell=True)
    return listOfMacs[0]

    Choose()


def scanPorts(remoteServer, beginPort, endPort):
    global multiScan
    global debug

    customDelay = False
    if multiScan == False:
        openPorts = [] 
        cls()
        tldList = open("domains.txt", "r")
        urlThngs = tldList.readlines()
        for urlDetect in urlThngs:
            if urlDetect.strip() in remoteServer.strip():
                delay = 0.1
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
                delay = 0.0000000009
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
        print "-" * 73
        print "Please wait, scanning ports (" + beginPort + " - " + endPort + ") on the remote host " + remoteServerIP
        print "-" * 73
        t1 = time.time()
    
        try:
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
            Choose()
        
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
            print "Attack All Ports. | Type: (all) - This functionality was never completed" #This functionality was never completed"
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
            Choose()
        else:
            print "No ports detected!"
            print "-"*75 + "\n"
            print printCompleteTime(t2, t1)
            print "-"*70
            getInput()
            cls()
            Choose()

    elif multiScan == True:
        print remoteServer
        founds = 0
        openPorts = []
        cls()
        delay = 0.01
        splits = "-:|~"
        try:
            for splitChar in list(splits):
                try:
                    remoteHosts = remoteServer.split(splitChar)
                    print remoteHosts
                except Exception, e:
                    if "object has no" in str(e):
                        print "Tried: " + splitChar + " | " + str(e)
                    else:
                        print "[Error] | " + str(e)
                except KeyboardInterrupt:
                    pass
            print remoteServer
            ip1 = remoteHosts[0].strip()
            ip2 = remoteHosts[1].strip()
            numz1 = ip1.split(".")
            numz2 = ip2.split(".")
            one, two, three, four = ip1.split(".")
            newSub = one + "." + two + "." + three + "."
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
                Choose()             
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

        print "Please wait, scanning ports (" + beginPort + " - " + endPort + ") on the each host between " + ip1 + " - " + ip2
        print "-" * 93
        t1 = time.time()
        try:
            for remoteServerIP in range(int(smaller), int(biggest)):
                print "\nScanning IP: " + str(newSub) + str(remoteServerIP) + "\n" + "-"*75

                openPorts.append("Results For: | " + str(newSub) + str(remoteServerIP) + " | Ports: (" + str(smaller) + "-" + str(biggest) + ")\n" + "-"*75)
                for port in range(int(beginPort),int(endPort) + 1):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(delay)
                    result = sock.connect_ex((str(newSub) + str(remoteServerIP), port))
                    sock.settimeout(None)
                    if result == 0:
                        printPort = getPortDef(port) #Make this varialbe: print str(port)  if you do not want the port description
                        print printPort
                        
                        openPorts.append(printPort)
                        
                        founds = founds + 1
                    else:
                        if debug == True:
                            print "{Scanned} | " + str(newSub) + str(remoteServerIP) + " : " + str(port)
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
            Choose()
        
        except socket.gaierror:
            print '[Connection Error] | Unable to resolve host name | Restarting Script!'
            Choose()
        except socket.error:
            print "[Connection Error] | Unable to connect to the host (Possibally Blocked) | Restarting Script!"
            Choose()
            
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
            elif attackPrts == "":
                Choose()
            else:
                pentestPort(attackPrts, remoteServerIP)
            cls()
            Choose()
        else:
            print "No ports detected!"
            print "-"*75 + "\n"
            print printCompleteTime(t2, t1)
            print "-"*70
            getInput()
            cls()
            Choose()

    else:
        print "global Varialbe {multiScan} is not set to True or False, this is fatal, Goodbye!"
        pause()
        Choose()
    
def Choose():
    print """
--------------------------------------------
Wifi Scanner:---------------------(1)
Computer Viewer:------------------(2)
Wake Computers:-------------------(3)
Get MAC From IP(LAN):-------------(4)
Scan LAN Ports:-------------------(5)
--------------------------------------------"""
    try:
        choice = raw_input("> ")
    except KeyboardInterrupt:
        Choose()
        
    if choice == "1":
        WifiScan()
        
    elif choice == "2":
        viewComputers()
        
    elif choice == "3":
        try:
            print "MAC To Wake Up: "
            mac = raw_input("> ")
            print "Computers IP:"
            ip = raw_input("> ")
        except KeyboardInterrupt:
            Choose()
        wakeComputer(mac,ip)
        
    elif choice == "4":
        print "IP: "
        ip = raw_input("> ")
        getMAC(ip)
        Choose()
        
    elif choice == "5":
        remoteServer = getIP()
        cls()
        print """What type of scan do you want to do?:
-------------------------------------------
Small Scan:---------------------(1)
Scan Commonly Used:-------------(2)
Full Scan:----------------------(3)
Custom Scan:--------------------(4)
--------------------------------------------"""
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
            
                
        else:
            cls()
            print "Input Error: " + scanType
            Choose()
        cls()
        scanPorts(remoteServer, scanFrom, scanTo)






#Other Added Commands:
    elif choice == "cls":
        subprocess.call('cls', shell=True)
        print "\n"*50
        Choose()

        
    else:
        Choose()

Choose()
