# py-keylogger
A Simple Keylogger for Linux application written in Python 
using the pyxhook module which is an implementation of pyhook module (for Windows OS). 

<h3>Changes:</h3>
-reduced CPU utilization ( removed "mouse move" hook )
-organized output (group with the same "window name" and "process name" plus time).
	---------------------------------------------------------------------------
	# 2016-02-09 11:36:41 : Mirko Conti - Mozilla Firefox [ Navigator ]
	---------------------------------------------------------------------------
	 e x a m p l e space o f space t e x t

	---------------------------------------------------------------------------
	# 2016-02-09 11:38:05 : *pyxhook.py (~/Documents/py-key) - gedit [ gedit ]
	---------------------------------------------------------------------------
	 space c o d e space Shift_L percent space 2 Control_L
 
<h3>Requires:</h3> 
python 2.7
python-xlib

<h3>Installation original project:</h3>
<a href="http://www.techinfected.net/2015/10/how-to-make-simple-basic-keylogger-in-python-for-linux.html">Visit this LINK</a>

<h3>Installation ubuntu:</h3>
1) get the code
git clone https://github.com/mkcn/py-keylogger.git
3) go in the directory
cd py-keylogger
2)if need change the name of the log file (relative path or absolute path) in the "py-keylogger.py" file
3) run the keylogger
python keylogger.py 
4) auto start , manually go in "Startup applications" → "Add"
   		name 	: "py-key"
   		Command : "python ~/py-keylogger/py-keylogger.py"
			
