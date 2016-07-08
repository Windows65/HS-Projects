
#Imports:
#--------------------------------------
from yahoo_finance import Share
from datetime import datetime
import numpy as np
import subprocess
import itertools
import operator
import datetime
import smtplib
import locale
import time
import sys
import os
#--------------------------------------


#Globals:
#--------------------------------------
global currentBallance
global beforePrice
global shareAmount
global shareName
global buyPrice
global stream
#--------------------------------------





#--------------------------------------------------[Information Gathering]--------------------------------------------------

def initDatabase():
    #>-------------------:DatabaseInit:-------------------<
    files = ["stockData.txt","profitMon.txt", "ballance.txt"]
    createFiles = []
    for fi in files:
        try:
            f = open(fi, "r")
            f.read()
            f.close()
        except KeyboardInterrupt:
            return "Database Init Canceled by user."
        except:
            createFiles.append(fi)

    for fi in createFiles:
        try:
            f = open(fi, "w")
            f.write("")
            f.close()
        except KeyboardInterrupt:
            return "Canceled by user."
        except:
            pass
    #>---------------:DatabaseInit_Complete:---------------<
def saveToDatabase(data, fil):
    if fil == 1:
        f = open("stockData.txt", "a")
        f.write("\n" + data)
        f.close()
    elif fil == 2:
        f = open("profitMon.txt", "a")
        f.write("\n" + data)
        f.close()
    else:
        print "[Error] | saveToDatabase() | Unknown File"
def cls():
    print "\n"*50
    subprocess.call('cls',shell=True)
    return
def parse(p):
    p = str(p)
    stuff = "+-$"
    posOrMin = ""
    for everything in stuff.split():
        if "-" in p:
            posOrMin = "-"
        elif "+" in p:
            posOrMin = "+"
        price = p.replace(everything,"")
    return price + "|" +  posOrMin
def getSaleSuggestion():
    f = open("stockData.txt", "r")
    for price in f.readlines():
        price = parse(price)
        price.append(values)
        num
    f.close()
def getPrice(share, formated, status):
    global buyPrice  
    global shareName
    global beforePrice
    getOpen = share.get_open()
    sharePrice = str(round(float(share.get_price()),2))
    timeSearched = getTime()
    if sharePrice > buyPrice: #lesthn
        if "-" in str(str(round(float(sharePrice) - buyPrice,2))):
            profitPerShare = "$" + str(round(float(sharePrice) - buyPrice,2))
        else:
            profitPerShare = "$+" + str(round(float(sharePrice) - buyPrice,2))

    #Deals with the missing 0 error:
    item = str(buyPrice)
    itms = list("-$+")
    for i in itms:
        item.strip(i)
    if len(item) < len(str(beforePrice)):
        buyPrice = int(str(buyPrice) + "0")

        
    saveToDatabase(str(profitPerShare), 2)
    if formated == "true":
        if status.strip() == "":
            status = "N/A"
        dataFormatted = str("[Share Update] | Share: " + str(shareName) + " | Price: $" + sharePrice + " | Profit: " + str(profitPerShare) + " | Status: " + str(status) + " | " + "Time: " + timeSearched)
        return dataFormatted
    elif formated == "false":
        return sharePrice
    else:
        print "[PriceError] | Is format set to true or false? Check the code."
def getTime():
    today = datetime.date.today()
    date = today.strftime('%b/%d/%y')
    return date + "(" + datetime.datetime.now().strftime("%I:%M.%S %p") + ")"
def sendMessage(msg):
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login( 'east837@gmail.com', 'windows8016' )
    server.sendmail( 'east837@gmail.com', '2566030294@vtext.com', str(msg))
    server.close()
    print "Text Sent To Benjamin East. Waiting 30 Seconds to Prevent Spam. | [Text Number]: " + str(textNum) + " of " + str(textNumLimit)
    time.sleep(30)
    if textNum == textNumLimit:
        print "The Text Send Limit Has Been Reached."
        textNum = textNum + 1
    textNum = textNum + 1
    
def sellProfit():
    global shareAmount
    global shareName
    global stream
    global buyPrice
    currentPrice = getPrice(Share(shareName), "false", None)
    totalBuyPrice = round(float(buyPrice) * float(shareAmount),2)
    totalSellPrice = round(float(currentPrice) * float(shareAmount),2)
    moneyEarned = totalSellPrice - totalBuyPrice
    return "[Share Name] | (" + shareName + ")\n>" + "---"*5 + "<\n[Buy Price] | $" + str(formNum(totalBuyPrice)) + "\n[Sell Price(Now)] | $" +  str(formNum(totalSellPrice)) + "\n[Total Sell Profit] | $" + str(formNum(moneyEarned))

#--------------------------------------------------[Information Gathering Complete]--------------------------------------------------


def manageBallance(do, amount):
    global shareName
    try:
        if do == "change":
            f = open("ballance.txt", "w")
            f.write(str(amount))
            f.close()
        elif do == "get":
            f = open("ballance.txt", "a")
            a = f.read()
            f.close()
            return a
        else:
            return "[Unknown Command] | manageBallance()"
    except Exception, e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print "[Error] | manageBallance() | LN: " + str(fname) + " | > " + str(e) 
    except KeyboardInterrupt:
        print "\n" + "-"*69 + "\n" + sellProfit()
        chs = raw_input("[User] | Ballance Managment Paused.\n" + "-"*40 + "<\n> Continue------(1)\n> Main Menu----------------(2)\n>" + "-"*40 + "<\n> ")
        if "2" in chs:
            main()
        else:
            pass



def formNum(x):
    x, dec = str(x).split(".")
    x = int(x)
    dec = "." + str(dec)
    if type(x) not in [type(0), type(0L)]:
        raise TypeError("Parameter must be an integer.")
    if x < 0:
        return '-' + intWithCommas(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)
    return str("%d%s" % (x, result)) + dec


def sellShares():
    global currentBallance
    global shareAmount
    global shareName
    global stream
    global buyPrice
    currentPrice = getPrice(Share(shareName), "false")
    totalBuyPrice = round(float(buyPrice) * float(shareAmount),2)
    totalSellPrice = round(float(currentPrice) * float(shareAmount),2)
    moneyEarned = totalSellPrice - totalBuyPrice
    oldBallance = currentBallance
    currentBallance = currentBallance + moneyEarned
    print "[Broker] | Old Ballance: " +  str(formNum(oldBallance)) + " | New Ballance: " + str(formNum(currentBallance)) + " | Money Differance: " + str(formNum(moneyEarned))

def most_common(lst):
  groups = itertools.groupby(sorted(lst))
  def _auxfun((item, iterable)):
    return len(list(iterable)), -lst.index(item)
  return max(groups, key=_auxfun)[0]



#NEXT Add A Function To Buy Stocks With The Money Made.

def main():
    global shareName
    global stream
    global buyPrice
    global shareAmount
    global currentBallance
    global beforePrice
    cls()
    start = 1
    prevPrice = 0
    textNum = 1
    textNumLimit = 6
    buyPrice = 21.43
    beforePrice = buyPrice
    shareAmount = 10000
    shareName = raw_input("Enter The Share You Would Like To Monitor:\n" + "--"*25 + "\n> ").strip() #YHOO
    alertPrice = buyPrice * 1.20
    cls()
    waitTime = 1 #Until Starts
    initDatabase()
    UpDownValues = [""]
    
    print ">" + "-"*52 + ":Monitoring_Share_[" + shareName + "]:" + "-"*52 + "<"
    while True:
        try:
            status = most_common(UpDownValues)
            share = Share(shareName)
            price = getPrice(share, "false", None)
            if price == prevPrice:
                pass
            else:
                info = getPrice(share, "true", status)
                saveToDatabase(info, 1)
                print info

            if price > prevPrice:
                UpDownValues.append("UP")
            elif price < prevPrice:
                UpDownValues.append("DOWN")
            if len(UpDownValues) > 15: #Risk Threshold to pull out
                UpDownValues.pop()
            
            if float(price) >= float(alertPrice):
                if str(status) == "DOWN":
                    sellShares()
                elif str(status) == "UP":
                    print "Waiting to sell for now."
                if textNum <= textNumLimit:
                    #sendMessage("Current Status:\n" + str(sellProfit()) + "\n>" + "---"*5 + "<\nBen's Monitor.")
                    pass
                else:
                    pass
                
            prevPrice = price
            xValue = getTime()
            yValue = price
            time.sleep(0.3) #Default: (0.3)
            
        except Exception, e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            if "'str' and 'NoneType'" in str(e):
                raw_input("-"*75 + "\nCurrent Share Status:\n[Error] | Unable to find the share: [" + shareName + "] | Press (Enter) To Go Back To Main Menu.\n" + "> ")
                main()
            elif "object has no attribute" in str(e):
                pass
            elif "Query failed with error" in str(e):
                pass
            else:
                print "[Error] " + str(exc_tb.tb_lineno) + " | > " + str(e)
        except KeyboardInterrupt:
            print "\n" + "-"*69 + "\n" + sellProfit()
            chs = raw_input("[User] | Monitoring of [" + shareName + "] Paused.\n" + "-"*40 + "<\n> Continue Monitoring------(1)\n> Main Menu----------------(2)\n>" + "-"*40 + "<\n> ")
            if "2" in chs:
                main()
            else:
                pass

if __name__ == "__main__":
    main()
