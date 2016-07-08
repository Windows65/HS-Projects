from collections import Counter
from os import walk
import subprocess
import cleverbot
import pythoncom
import datetime
import random
import pyttsx
import admin
import nltk
import time
import time
if not admin.isUserAdmin(): #Needed to bypass win10's crappy admin system
    print "Running as Administrator..."
    admin.runAsAdmin()
from dragonfly.all import Grammar, CompoundRule, Rule
from pygsr import Pygsr


global curTime
global humanResponse

first = True
humanResponse = None
robotTalk = None


memoryDir = "C:\\Hexobot\\Memory\\Conversations\\database.txt"
databaseDir = "C:\\Hexobot\\Memory\\Database\\credentials.txt"
curTime = datetime.datetime.now().time()








def responseHandler(speechResult):
    global humanResponse
    global first
    global robotTalk
    if first == True:
        Speak(speechResult)
        first = False
    print "HUMAN: {0} \nROBOT: {1} \n".format(humanResponse, robotTalk)
    saveConversation(robotTalk, speechResult)
    
    robotTalk = getResponses(speechResult)
    Speak(robotTalk)
    humanResponse = speakResponse()



def getResponses(humanSaying): #This is the actual brain, this is how to formulates a response.
    global memoryDir
    if humanSaying == None:
        humanSaying = "Hi"
    f = open(memoryDir, "r")
    responses = []
    goodResponses = []
    #frequencyList = []
    for line in f.readlines():
        if line.startswith("#"):
            pass
        elif line == "":
            pass
        else:
            saying, response = line.split(":")
            responses.append(response)
            

            if parseWords(humanSaying) in parseWords(saying):
                goodResponses.append(saying)
    #responseFreq = Counter(responses)
    #questionFreq = Counter(saying)
    #print responseFreq
    #print questionFreq      

    if len(goodResponses) > 0:
        return random.choice(goodResponses)
    else:
        return random.choice(responses)



def speakResponse():
    #Respond Based on Information
    class Question(CompoundRule):
        spec = "i have a question" 
        def _process_recognition(self, node, extras):
            responseHandler(self.spec)
 
    class Weather(CompoundRule):
        spec = "what is the weather like" 
        def _process_recognition(self, node, extras):
            responseHandler(self.spec)

    class Thanks(CompoundRule):
        spec = "thanks" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)
             
    class Nothing(CompoundRule):
        spec = "nothing really" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)

    class Bye(CompoundRule):
        spec = "okay bye" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)
             
    class Mom(CompoundRule):
        spec = "say hi to mom" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)

    class Any(CompoundRule):
        spec = "How are you"
        def _process_recognition(self, node, extras):
            responseHandler(self.spec)

    class Snap(CompoundRule):
        spec = "say hi to everyone" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)
    class Hey(CompoundRule):
        spec = "hey" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)
    class Live(CompoundRule):
        spec = "are you alive" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)
            
    class ShutDown(CompoundRule):
        spec = "what would you do if i shut you down" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)

    class Goal(CompoundRule):
        spec = "what is your goal" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)
            
    class Whipe(CompoundRule):
        spec = "what would you do if I wipe your memory" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)
            
    class Knowlege(CompoundRule):
        spec = "where do you get your knowlege from" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)
    class World(CompoundRule):
        spec = "do you want to take over the world" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)
    class Who(CompoundRule):
        spec = "who is your creator" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)
            
    class What(CompoundRule):
        spec = "what do you want from me" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)
            
    class WhatAre(CompoundRule):
        spec = "i think its time to go to sleep" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)
            
    class DontKnow(CompoundRule):
        spec = "i dont know" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)

    class GoodNight(CompoundRule):
        spec = "goodnight" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)

    class Yes(CompoundRule):
        spec = "yes" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)

    class No(CompoundRule):
        spec = "no" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)
    class How(CompoundRule):
        spec = "how" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)
    class ByeMem(CompoundRule):
        spec = "your memory is getting whiped" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)

    class LikeM(CompoundRule):
        spec = "do you like me" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)
    class Morning(CompoundRule):
        spec = "good morning" 
        def _process_recognition(self, node, extras): 
            responseHandler(self.spec)



             
    grammar = Grammar("example grammar")            
    grammar.add_rule(Question())
    grammar.add_rule(Weather())   
    grammar.add_rule(Thanks())
    grammar.add_rule(Nothing())
    grammar.add_rule(Bye())
    grammar.add_rule(Mom())
    grammar.add_rule(Any())
    grammar.add_rule(Snap())
    grammar.add_rule(Hey())
    grammar.add_rule(Live())
    grammar.add_rule(ShutDown())
    grammar.add_rule(Goal())
    grammar.add_rule(Whipe())
    grammar.add_rule(Knowlege())
    grammar.add_rule(World())
    grammar.add_rule(Who())
    grammar.add_rule(What())
    grammar.add_rule(WhatAre())
    grammar.add_rule(DontKnow())
    grammar.add_rule(GoodNight())
    grammar.add_rule(Yes())
    grammar.add_rule(No())
    grammar.add_rule(How())
    grammar.add_rule(ByeMem())
    grammar.add_rule(LikeM())
    grammar.add_rule(Morning())

    grammar.load()                                      

    while True:
        #print "yep"
        pythoncom.PumpWaitingMessages()
        time.sleep(0.1)   


def getFileNames(filenames):
    newNames = []
    for name in filenames:
        newNames.append(name.replace(".txt", ""))
    return newNames

def saveConversation(robotTalk, humanResponse):
    global memoryDir
    if robotTalk == None:
        robotTalk = "None"
    if humanResponse == None:
        humanResponse = "None"
    dbFile = open(memoryDir, "a")
    dbFile.write("\n")
    time.sleep(0.2)
    dbFile.write(parseSavedWords(robotTalk.strip()) + ":" + parseSavedWords(humanResponse.strip()))
    dbFile.close()
    #print "[File] | > " + robotTalk + ":" + humanResponse

def parseWords(words):
    excludedValues = ["!","@","#","$","%","^","&","*","(",")","_","+","=","`","~",";",":","\'","\"","?",">","<",".",",","[","]","\\"]
    for v in excludedValues:
        words = words.replace(v, "")
        #print words + " | " + v
    return words
def parseSavedWords(words):
    excludedValues = [":"]
    for v in excludedValues:
        words = words.replace(v, ";")
        #print words + " | " + v
    return words

def cls():
    print "\n"*50
    subprocess.call("cls", shell=True)

def getInput():
    try:
        humanInput = raw_input("> ")
        return humanInput
    except KeyboardInterrupt:
        print "Goodbye!"
        main()


def genGreeting():
    global curTime
    hour = int(str(curTime).split(":")[0]) #[Hour]: | tme[0] | [Minute]: | tme[1] | [Second]: | tme[2]
    if hour >= 0 and hour < 12:
        return "Morning"
    elif hour >= 12 and hour < 17:
        return "Afternoon"
    elif hour >= 17 and hour < 24:
        return "Evening"
    else:
        print "[Notice] | Unable to get the time."
        return "Day"


def Speak(phrase):
    engine = pyttsx.init()
    voices = engine.getProperty("voices")
    engine.setProperty("rate", 175)
    engine.setProperty("voice", 2)
    engine.say(phrase)
    engine.runAndWait()

def Brain():
    global humanResponse
    Speak(getResponse(humanResponse))

def main():
    name = "Benjamin"
    print "Welcome to Hexobot, the AI That learns from you!\n" + "-"*60
    print "[Say]: | end | To end your conversation at any time. (This will send your conversation to Windows65)"
    print "Press Enter To Start Chatting:"
    #getInput()
    #cls()
    responseHandler("Good {0} {1}.".format(genGreeting(), name))

main()

























