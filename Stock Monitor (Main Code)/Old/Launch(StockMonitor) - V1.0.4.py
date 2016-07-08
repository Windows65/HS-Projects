from yahoo_finance import Share
from datetime import datetime
from plotly.graph_objs import *
import plotly.tools as tls
import plotly.plotly as py
import numpy as np
import datetime 
import time
global shareAmount
global shareName
global buyPrice
global stream
import subprocess
import sys
import os

def getStreamID():
    return tls.get_credentials_file()['stream_ids']

def initDatabase():
    #>-------------------:DatabaseInit:-------------------<
    try:
        f = open("stockData.txt", "r")
        f.read()
        f.close()
    except KeyboardInterrupt:
        return "Canceled by user."
    except:
        f = open("stockData.txt", "w")
        f.write("Stock Calculator:\n>" + "-"*50 + "<")
        f.close()
    #>---------------:DatabaseInit_Complete:---------------<


def saveToDatabase(data):
    f = open("stockData.txt", "a")
    f.write("\n" + data)
    f.close()


def cls():
    print "\n"*50
    subprocess.call('cls',shell=True)
    return


def getPrice(share, formated):
    global buyPrice  
    global shareName
    getOpen = share.get_open()
    sharePrice = str(round(float(share.get_price()),2))
    timeSearched = getTime()
    if sharePrice > buyPrice: #lesthn
        if "-" in str(str(round(float(sharePrice) - buyPrice,2))):
            profitPerShare = "$" + str(round(float(sharePrice) - buyPrice,2))
        else:
            profitPerShare = "$+" + str(round(float(sharePrice) - buyPrice,2))
        
        
    if formated == "true":
        dataFormatted = str("[Share Update] | Share: " + str(shareName) + " | Price: $" + sharePrice + " | Profit: " + str(profitPerShare) + " | " + "Time: " + timeSearched)
        return dataFormatted
    elif formated == "false":
        return sharePrice
    else:
        print "[PriceError] | Is format set to true or false? Check the code."

def getTime():
    today = datetime.date.today()
    date = today.strftime('%b/%d/%y')
    return date + "(" + datetime.datetime.now().strftime("%I:%M.%S %p") + ")"


def sellProfit():
    global shareAmount
    global shareName
    global stream
    global buyPrice
    currentPrice = getPrice(Share(shareName), "false")
    totalBuyPrice = round(float(buyPrice) * float(shareAmount)),2
    totalSellPrice = round(float(currentPrice) * float(shareAmount)),2
    moneyEarned = totalBuyPrice - totalSellPrice
    return "[Buy Price] | $" + str(totalBuyPrice) + "\n[Sell Price(Now)] | $" +  str(totalSellPrice) + "\n[Total Sell Profit] | $" + str(moneyEarned)
    

def main():
    start = 1
    prevPrice = 0
    cls()
    global shareName
    global stream
    global buyPrice
    global shareAmount
    
    buyPrice = 3.42
    shareAmount = 5845
    shareName = raw_input("Enter The Share You Would Like To Monitor:\n" + "--"*25 + "\n> ").strip() #YHOO
    alertPrice = buyPrice * 1.50
    cls()
    waitTime = 1
    initDatabase()
    print ">--------------------:Monitoring_Share_[" + shareName + "]:--------------------<"
    while True:
        try:
            share = Share(shareName)
            price = getPrice(share, "false")
            if price == alertPrice:
                print "[ALERT] | Sell Now: (50% Profit) | >-[Alert]-<>-[Alert]-<>-[Alert]-<>-[Alert]-<>-[Alert]-<>-[Alert]-<>-[Alert]-<>-[Alert]-<"
            if price == prevPrice:
                pass
            else:
                info = getPrice(share, "true")
                saveToDatabase(info)
                print info
                
            prevPrice = price
            xValue = getTime()
            yValue = price
            time.sleep(0.3)
            
        except Exception, e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            if "'str' and 'NoneType'" in str(e):
                raw_input("-"*75 + "\n[Error] | Unable to find the share: [" + shareName + "] | Press (Enter) To Go Back To Main Menu.\n" + "> ")
                main()
            elif "Query failed with error" in str(e):
                saveToDatabase("[Error] | > " + str(e))
            else:
                print "[Error] " + str(exc_tb.tb_lineno) + " | > " + str(e)
        except KeyboardInterrupt:
            print "\n" + "-"*69 + "\n" + sellProfit()
            chs = raw_input("[User] | Monitoring of [" + shareName + "] Paused.\n" + "-"*40 + "<\n> Continue Monitoring------(1)\n> Main Menu----------------(2)\n>" + "-"*40 + "<\n> ")
            if "1" in chs:
                pass
            else:
                main()
            
if __name__ == "__main__":
    main()
