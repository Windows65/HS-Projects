import sys
import AdvancedPenetrationToolkit

def pause():
    print """
>----------------------------------------------------<
|> Main Menu:----------------------{1}
|> Exit Script:--------------------{2}
|> Continue Script:----------------{Any Other Key}
>----------------------------------------------------<"""
    try:
        chs = raw_input("> ")
        if "1" in chs:
            AdvancedPenetrationToolkit.cls()
            return AdvancedPenetrationToolkit.startMenu()
        elif "2" in chs:
            sys.exit("Goodbye!\n>-------------------------------------------")
        else:
            return
    except KeyboardInterrupt:
        pause()
    
