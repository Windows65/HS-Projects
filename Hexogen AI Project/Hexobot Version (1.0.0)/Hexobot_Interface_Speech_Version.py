import pyttsx
import cleverbot
import pythoncom
import datetime
global curTime
global humanResponse
import admin
import time
#import HexoBrain
curTime = datetime.datetime.now().time()
if not admin.isUserAdmin(): #Needed to bypass win10's crappy admin system
    print "Running as Administrator..."
    admin.runAsAdmin()
from dragonfly.all import Grammar, CompoundRule, Rule
from pygsr import Pygsr



#Variables:
#-----------------------------
global name
name = "Benjamin"











def getResponse(): #I need to use this function only as the gateway to the bot. Build another function as the brain.
    class Question(CompoundRule):
        spec = "i have a question" 
        def _process_recognition(self, node, extras):
            Speak("What's your question?")
 
    class Weather(CompoundRule):
        spec = "what is the weather like" 
        def _process_recognition(self, node, extras): 
             Speak("It's currently around 80 degrees, it seems to have been warm all day.")

    class Thanks(CompoundRule):
        spec = "thanks" 
        def _process_recognition(self, node, extras): 
             Speak("Any time Mr. East")
             
    class Nothing(CompoundRule):
        spec = "nothing right now" 
        def _process_recognition(self, node, extras): 
             Speak("Awesome, just say my name if you need me.")

    class Bye(CompoundRule):
        spec = "okay bye" 
        def _process_recognition(self, node, extras): 
             Speak("Goodbye!")
             
    class Mom(CompoundRule):
        spec = "say hi to mom" 
        def _process_recognition(self, node, extras): 
             Speak("Hello Ms. East, Welcome! Please make your self at home.")


             


    class Snap(CompoundRule):
        spec = "say hi to everyone" 
        def _process_recognition(self, node, extrs): 
             Speak("Hey everyone, I am Hexo Bot!")
    
    class Hey(CompoundRule):
        spec = "hey" 
        def _process_recognition(self, node, extras): 
             Speak("Hey Ben!")

    class Security(CompoundRule):
        spec = "turn the security system on" 
        def _process_recognition(self, node, extras): 
             Speak("System armed in sectors A through D, I will notify you before offensive action is taken.")

    class Goodnight(CompoundRule):
        spec = "goodnight"

        
        def _process_recognition(self, node, extras): 
             Speak("Sleep well Benjamin, the systems are armed, you should sleep with comfort.")
             
    grammar = Grammar("HexoBrain")            
    grammar.add_rule(Question())
    grammar.add_rule(Weather())    
    grammar.add_rule(Thanks())
    grammar.add_rule(Nothing())
    grammar.add_rule(Bye())
    grammar.add_rule(Mom())
    grammar.add_rule(Snap())
    grammar.add_rule(Hey())
    grammar.add_rule(Security())
    grammar.add_rule(Goodnight())
    grammar.load()                                      

    while True:
        pythoncom.PumpWaitingMessages()
        time.sleep(0.1)                                    # Load the grammar.



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
    #Speak(getResponse(humanResponse))
    
Speak("Good {0} {1}.".format(genGreeting(), name))
getResponse()

















