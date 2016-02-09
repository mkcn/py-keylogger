# Py-keylogger

<p>A Simple Keylogger for Linux application written in Python 
using the pyxhook module which is an implementation of pyhook module (for Windows OS). </p>

<h3>Changes:</h3>

+ reduced CPU utilization ( removed "mouse move" hook )
+ organized output (group with the same "window name" and "process name" plus time).

```
	---------------------------------------------------------------------------
	# 2016-02-09 11:36:41 : Mirko Conti - Mozilla Firefox [ Navigator ]
	---------------------------------------------------------------------------
	 e x a m p l e space o f space t e x t

	---------------------------------------------------------------------------
	# 2016-02-09 11:38:05 : *pyxhook.py (~/Documents/py-key) - gedit [ gedit ]
	---------------------------------------------------------------------------
	 space c o d e space Shift_L percent space 2 Control_L
```

<h3>Requires:</h3> 

+ python 2.7
+ python-xlib

<h2>Installation ubuntu:</h2>
<h6>Get the code</h6>

```
git clone https://github.com/mkcn/py-keylogger.git
```
<h6>Go in the directory</h6>

```
cd py-keylogger
```
<h6>If need change the name of the log file (relative path or absolute path) in the "py-keylogger.py" file</h6>

<h6>Run the keylogger</h6>

```
python keylogger.py 
```
<h6>Auto start , manually go in "Startup applications" → "Add"</h6>

+ name 	: "py-key"
+ Command : "python ~/py-keylogger/py-keylogger.py"

			
            
            
<h2>Installation original project:</h2><a href="http://www.techinfected.net/2015/10/how-to-make-simple-basic-keylogger-in-python-for-linux.html">Visit this LINK</a>

