from yahoo_finance import Share
from datetime import datetime
from plotly.graph_objs import *
import plotly.tools as tls
import plotly.plotly as py
import numpy as np
import datetime 
import time
global shareName
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
    initGraph()


def saveToDatabase(data):
    f = open("stockData.txt", "a")
    f.write("\n" + data)
    f.close()


def cls():
    print "\n"*50
    subprocess.call('cls',shell=True)
    return


def getPrice(share, formated):
    global shareName
    getOpen = share.get_open()
    sharePrice = share.get_price()
    timeSearched = getTime()
    if formated == "true":
        dataFormatted = str("[Share Update] | Share: " + shareName + " | Price: " + sharePrice + " | Time: " + timeSearched)
        saveToDatabase(formated)
        return dataFormatted
    elif formated == "false":
        return sharePrice
    else:
        print "[PriceError] | Is format set to true or false? Check the code."

def getTime():
    today = datetime.date.today()
    date = today.strftime('%b/%d/%y')
    return date + "(" + datetime.datetime.now().strftime("%I:%M.%S %p") + ")"


#Indevidual Graphing Processes:
def closeGraphConnection():
    global stream
    stream.close() 
def initGraph():
    global shareName
    global stream
    strm_ids = tls.get_credentials_file()['stream_ids']
    strm = Stream(token=strm_ids[0],maxpoints=100)
    trace1 = Scatter(x=[], y=[], mode='lines+markers', strm = strm)
    data = Data([trace1])
    layout = Layout(title='Live Stock Price(' + shareName + ")")
    fig = Figure(data=data, layout=layout)
    unique_url = py.plot(fig, filename='s7_first-stream')
    stream = py.Stream(strm_ids[0])
    stream.open()
    print "[Notice] | Graph Stream Initilization Complete."
    
def graph(price):
    global stream
    xValue = getTime()
    yValue = price
    stream.write(dict(x=xValue, y=yValue))
    time.sleep(1)




def main():
    cls()
    global shareName
    global stream
    shareName = raw_input("Enter The Share You Would Like To Monitor:\n" + "--"*25 + "\n> ").strip() #YHOO
    #strm_ids = tls.get_credentials_file()['stream_ids']
    #strm = Stream(token=strm_ids[0],maxpoints=100)
    #trace1 = Scatter(x=[], y=[], mode='lines+markers', strm = strm)
    #data = Data([trace1])
    #layout = Layout(title='Live Stock Price(' + shareName + ")")
    #fig = Figure(data=data, layout=layout)
    #unique_url = py.plot(fig, filename='s7_first-stream')
    #stream = py.Stream(strm_ids[0])
    #stream.open()

    cls()
    waitTime = 1
    initDatabase()
    time.sleep(5)
    print ">--------------------:Monitoring_Share_[" + shareName + "]:--------------------<"
    while True:
        try:
            share = Share(shareName)
            price = getPrice(share, "false")
            print getPrice(share, "true")
            
            xValue = getTime()
            yValue = price
            #stream.write(dict(x=xValue, y=yValue))
            time.sleep(1)
            
        except Exception, e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            if "'str' and 'NoneType'" in str(e):
                stream.close()
                raw_input("-"*75 + "\n[Error] | Unable to find the share: [" + shareName + "] | Press (Enter) To Go Back To Main Menu.\n" + "> ")
                main()
            else:
                print "[Error] " + str(exc_tb.tb_lineno) + " | > " + str(e)
        except KeyboardInterrupt:
            chs = raw_input("[User] | Monitoring of [" + shareName + "] Paused.\n>" + "-"*40 + "<\n> Continue Monitoring------(1)\n> Main Menu----------------(2)\n>" + "-"*40 + "<\n> ")
            if "1" in chs:
                pass
            else:
                stream.close() 
                main()
            
if __name__ == "__main__":
    main()
