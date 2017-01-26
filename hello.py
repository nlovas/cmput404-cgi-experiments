#!/usr/bin/env python

#^this line is called the "shebang"

import os
import json
import cgi
import Cookie

form = cgi.FieldStorage() #can handle POST too

username = form.getvalue('user')
password = form.getvalue('password')

C = Cookie.SimpleCookie()
C.load(os.environ['HTTP_COOKIE'])


print "Content-Type: text/html"
if username == "bob" and password == "1234":
	print "Set-Cookie: loggedin=true"

print
print "<HTML><BODY>"
print "<H1>Hello world!</H1>"
print "your magic tracking number is:" 
print form.getvalue('magic_tracking_number')

print "<p>your browser is"
if "Firefox" in os.environ['HTTP_USER_AGENT']:
	print "Firefox!"
elif "Chrome" in os.environ['HTTP_USER_AGENT']:
	print "Chrome!"
else:
	print os.environ['HTTP_USER_AGENT'] #do a curl -A Firefox localhost:8000/hello.py to pretend ur using firefox when curling

print "<form method = 'POST'><input name = 'user'><input name = 'password' type='password'>"
print "<input type = 'submit'></form>"



print "<P>Username: " + str(username)
print "<p>Password: " + str(password)

if(username == "bob" and password == "1234"):
	print "<p>login successful"

if 'loggedin' in C:
	print "<p>Loggedin: " + str(C['loggedin'].value)
else:
	print "<p>no cookie"
#print json.dumps(dict(os.environ), indent = 2, sort_keys = True)


