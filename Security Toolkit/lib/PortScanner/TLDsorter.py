import os



def getPortDef():
    dlist = []
    try:
        defFile =  os.getcwd() + "\\user_pass.txt"
        defs = open(defFile, "r")
    except Exception,e:
        print "Error Opening Port Definition File (domains.txt) | " + str(e)
        pause()


    stripList = " ,"
    ul = []
    pl = []
    for data in defs.readlines():
        num, usr, ps = data.split()
        for item in list(stripList):
            usr = usr.strip(item)
            ps = ps.strip(item)
        
        print usr + " | " + ps
        ul.append(usr)
        pl.append(ps)
    print ul
    print pl
    return dlist


bigList = getPortDef()

for tld in bigList:
    print tld













