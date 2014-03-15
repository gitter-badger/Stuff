#!/usr/bin/python
import sys
from os.path import expanduser
import os
import json
import urllib
 
dir = os.path.join(expanduser("~"),"fbusers/")
 
if not len(sys.argv)==2:
  sys.stderr.write("Specify user\n")
  sys.stderr.write("Available users: "+(" ".join(os.listdir(dir)))+"\n") 
  exit(1)
  
with open(dir+sys.argv[1]+".txt") as file:
 token=file.read()
 
if sys.stdin.isatty():
  sys.stderr.write("Things seem correct. Pipe in the status\n")
  exit(1)
  
status=sys.stdin.read().strip()

if len(status) <1:
  sys.stderr.write("No input\n")
  exit(1)
  
request={"message":status,"access_token":token}
con=urllib.urlopen("https://graph.facebook.com/me/feed",data=urllib.urlencode(request))
jd=json.load(con)
con.close()

if "error" in jd:
  sys.stderr.write("Error: %s\n" % jd["error"]["message"]) 
  exit(1)
  
if not "id" in jd:
  sys.stderr.write("No id returned from server\n") 
  exit(1)
  
print "https://fb.com/"+jd["id"]
