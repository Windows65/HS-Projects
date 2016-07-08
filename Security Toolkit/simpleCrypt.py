# -*- coding: utf-8 -*-
#--NOTE-- This is not meant to encrypt very important information, this is just to keep plain text out of sight.
#Use caution when encrypting.
#Made By (Windows65) east837@gmail.com
def Encrypt(string):
    #Encrypt Codes: 
    #Letters
    aa1 = "!"
    bb1 = "?"
    c1 = "#"
    d1 = "$"
    e1 = "z"
    f1 = "^"
    g1 = "&"
    h1 = "*"
    i1 = "("
    j1 = ")"
    k1 = ";"
    l1 = ":"
    m1 = "]"
    n1 = "["
    o1 = "{"
    p1 = "}"
    q1 = "|"
    r1 = "e"
    s1 = "."
    t1 = ">"
    u1 = "<"
    v1 = "?"
    w1 = "/"
    x1 = ","
    y1 = "~"
    z1 = "`"
    #Nums
    a1 = "p"
    a2 = "h"
    a3 = "d"
    a4 = "w"
    a5 = "x"
    a6 = "y"
    a7 = "m"
    a8 = "v"
    a9 = "c"
    a0 = "o"
    ATe = "-"
    Dote = "_"
    #Decrypt Codes
    #Letters
    aa2 = "a"
    bb2 = "b"
    c2 = "c"
    d2 = "d"
    e2 = "e"
    f2 = "f"
    g2 = "g"
    h2 = "h"
    i2 = "i"
    j2 = "j"
    k2 = "k"
    l2 = "l"
    m2 = "m"
    n2 = "n"
    o2 = "o"
    p2 = "p"
    q2 = "q"
    r2 = "r"
    s2 = "s"
    t2 = "t"
    u2 = "u"
    v2 = "v"
    w2 = "w"
    x2 = "x"
    y2 = "y"
    z2 = "z"
    #Nums
    b1 = "1"
    b2 = "2"
    b3 = "3"
    b4 = "4"
    b5 = "5"
    b6 = "6"
    b7 = "7"
    b8 = "8"
    b9 = "9"
    b0 = "0"
    ATd = "@"
    Dotd = "."
    #Other Chars
    Space = " "    # Non-Encrypted Space Bar
    EncSpace = "+" # Encrypted Space Bar    
    Text = string
    Text = Text.lower()
    Letters = list(Text)
    NewWord = ""
    for x in Letters:
        if x == aa2:
            NewWord = NewWord + aa1
        elif x == bb2:
            NewWord = NewWord + bb1
        elif x == c2:
            NewWord = NewWord + c1
        elif x == d2:
            NewWord = NewWord + d1
        elif x == e2:
            NewWord = NewWord + e1
        elif x == f2:
            NewWord = NewWord + f1
        elif x == g2:
            NewWord = NewWord + g1
        elif x == h2:
            NewWord = NewWord + h1
        elif x == i2:
            NewWord = NewWord + i1
        elif x == j2:
            NewWord = NewWord + j1
        elif x == k2:
            NewWord = NewWord + k1
        elif x == l2:
            NewWord = NewWord + l1
        elif x == m2:
            NewWord = NewWord + m1
        elif x == n2:
            NewWord = NewWord + n1
        elif x == o2:
            NewWord = NewWord + o1
        elif x == p2:
            NewWord = NewWord + p1
        elif x == q2:
            NewWord = NewWord + q1
        elif x == r2:
            NewWord = NewWord + r1
        elif x == s2:
            NewWord = NewWord + s1
        elif x == t2:
            NewWord = NewWord + t1
        elif x == u2:
            NewWord = NewWord + u1
        elif x == v2:
            NewWord = NewWord + v1
        elif x == w2:
            NewWord = NewWord + w1
        elif x == x2:
            NewWord = NewWord + x1
        elif x == y2:
            NewWord = NewWord + y1
        elif x == z2:
            NewWord = NewWord + z1
        elif x == b1:
            NewWord = NewWord + a1
        elif x == b2:
            NewWord = NewWord + a2
        elif x == b3:
            NewWord = NewWord + a3
        elif x == b4:
            NewWord = NewWord + a4
        elif x == b5:
            NewWord = NewWord + a5
        elif x == b6:
            NewWord = NewWord + a6
        elif x == b7:
            NewWord = NewWord + a7
        elif x == b8:
            NewWord = NewWord + a8
        elif x == b9:
            NewWord = NewWord + a9
        elif x == b0:
            NewWord = NewWord + a0
        elif x == Space:
            NewWord = NewWord + EncSpace
        elif x == ATd:
            NewWord = NewWord + ATe
        elif x == Dotd:
            NewWord = NewWord + Dote
        else:
            NewWord = NewWord + "(INVALID)"
    return NewWord
def Decrypt(string):
    #Encrypt Codes: 
    #Letters
    aa1 = "!"
    bb1 = "?"
    c1 = "#"
    d1 = "$"
    e1 = "z"
    f1 = "^"
    g1 = "&"
    h1 = "*"
    i1 = "("
    j1 = ")"
    k1 = ";"
    l1 = ":"
    m1 = "]"
    n1 = "["
    o1 = "{"
    p1 = "}"
    q1 = "|"
    r1 = "e"
    s1 = "."
    t1 = ">"
    u1 = "<"
    v1 = "?"
    w1 = "/"
    x1 = ","
    y1 = "~"
    z1 = "`"
    #Nums
    a1 = "p"
    a2 = "h"
    a3 = "d"
    a4 = "w"
    a5 = "x"
    a6 = "y"
    a7 = "m"
    a8 = "v"
    a9 = "c"
    a0 = "o"
    ATe = "-"
    Dote = "_"
    #Decrypt Codes
    #Letters
    aa2 = "a"
    bb2 = "b"
    c2 = "c"
    d2 = "d"
    e2 = "e"
    f2 = "f"
    g2 = "g"
    h2 = "h"
    i2 = "i"
    j2 = "j"
    k2 = "k"
    l2 = "l"
    m2 = "m"
    n2 = "n"
    o2 = "o"
    p2 = "p"
    q2 = "q"
    r2 = "r"
    s2 = "s"
    t2 = "t"
    u2 = "u"
    v2 = "v"
    w2 = "w"
    x2 = "x"
    y2 = "y"
    z2 = "z"
    #Nums
    b1 = "1"
    b2 = "2"
    b3 = "3"
    b4 = "4"
    b5 = "5"
    b6 = "6"
    b7 = "7"
    b8 = "8"
    b9 = "9"
    b0 = "0"
    ATd = "@"
    Dotd = "."
    #Other Chars
    Space = " "    # Non-Encrypted Space Bar
    EncSpace = "+" # Encrypted Space Bar    
    Text = string
    Text = Text.lower()
    Letters = list(Text)
    NewWord = ""
    for x in Letters:
        if x == aa1:
            NewWord = NewWord + aa2
        elif x == bb1:
            NewWord = NewWord + bb2
        elif x == c1:
            NewWord = NewWord + c2
        elif x == d1:
            NewWord = NewWord + d2
        elif x == e1:
            NewWord = NewWord + e2
        elif x == f1:
            NewWord = NewWord + f2
        elif x == g1:
            NewWord = NewWord + g2
        elif x == h1:
            NewWord = NewWord + h2
        elif x == i1:
            NewWord = NewWord + i2
        elif x == j1:
            NewWord = NewWord + j2
        elif x == k1:
            NewWord = NewWord + k2
        elif x == l1:
            NewWord = NewWord + l2
        elif x == m1:
            NewWord = NewWord + m2
        elif x == n1:
            NewWord = NewWord + n2
        elif x == o1:
            NewWord = NewWord + o2
        elif x == p1:
            NewWord = NewWord + p2
        elif x == q1:
            NewWord = NewWord + q2
        elif x == r1:
            NewWord = NewWord + r2
        elif x == s1:
            NewWord = NewWord + s2
        elif x == t1:
            NewWord = NewWord + t2
        elif x == u1:
            NewWord = NewWord + u2
        elif x == v1:
            NewWord = NewWord + v2
        elif x == w1:
            NewWord = NewWord + w2
        elif x == x1:
            NewWord = NewWord + x2
        elif x == y1:
            NewWord = NewWord + y2
        elif x == z1:
            NewWord = NewWord + z2
        elif x == a1:
            NewWord = NewWord + b1
        elif x == a2:
            NewWord = NewWord + b2
        elif x == a3:
            NewWord = NewWord + b3
        elif x == a4:
            NewWord = NewWord + b4
        elif x == a5:
            NewWord = NewWord + b5
        elif x == a6:
            NewWord = NewWord + b6
        elif x == a7:
            NewWord = NewWord + b7
        elif x == a8:
            NewWord = NewWord + b8
        elif x == a9:
            NewWord = NewWord + b9
        elif x == a0:
            NewWord = NewWord + b0
        elif x == EncSpace:
            NewWord = NewWord + Space
        elif x == ATe:
            NewWord = NewWord + ATd
        elif x == Dote:
            NewWord = NewWord + Dotd
        else:
            NewWord = NewWord + "(INVALID)"
    return NewWord

def choose(cryptType,string):
        if cryptType == "Encrypt":
            return Encrypt(string)
        elif cryptType == "Decrypt":
            return Decrypt(string)
        else:
            return "Error: Check Your Method Name, It Must Be \"Encrypt\" Or \"Decrypt\""



def lo():
    Manuel = False
    if Manuel == True:
        print "CryptType:"
        print "---------------"
        print "Encrypt---(1)"
        print "Decrypt---(2)"
        print "---------------"
        ct = raw_input("> ")
        string = raw_input("\nString To Crypt:\n> ")
        if ct == "1":
            print Encrypt(string)
        if ct == "2":
            print Decrypt(string)
            choose(cryptType,string)
    else:
        print "What type of crypt? (e/d)"
        ct = raw_input("> ")
        ct.strip()
        ct.lower()
        string = raw_input("\nString To Crypt:\n> ")
        if ct == "e":
            print Encrypt(string)
        elif ct == "d":
            Decrypt(string)
            #choose(cryptType,string)
        else:
            pass

Manuel = False
#Manuel = True
if Manuel == True:
    lo()
else:
    pass
