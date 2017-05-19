# Py-keylogger

<p>A Simple Keylogger for Linux written in Python using the pyxhook module which is an implementation of pyhook module (for Windows OS). </p>

<h3>Changes:</h3>

+ reduced CPU utilization ( removed "mouse move" hook )
+ organized output (grouped chars with the same "window context", showing the process name and the time).

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

<h3>Requirements:</h3> 

+ python 2.7
+ python-xlib

<h2>Installation:</h2>
<h6>Get the code</h6>

```
git clone https://github.com/mkcn/py-keylogger.git
```
<h6>Set the directory</h6>

```
cd py-keylogger
```
<p>Default log file: file.log (set in "kl.py")</p>

<h6>Run the keylogger</h6>

```
python kl.py 
```
<h6>Run in background</h6>
```
nohup python kl.py -r > output &
```

<h6>Auto start (Ubuntu)</h6>
<p>"Startup applications" → "Add"</p>

+ name 	: "py-key"
+ Command : "python ~/py-keylogger/kl.py"
+ Exit : 'Control_L'  then '+' to exit
			        
            
<h2>Credits:</h2>Visit the <a href="https://github.com/hiamandeep/py-keylogger.git">original project</a>

