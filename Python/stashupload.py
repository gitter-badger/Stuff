import urllib2
import json
import sys

def base36encode(number, alphabet='0123456789abcdefghijklmnopqrstuvwxyz'):
    base36 = ''
    sign = ''
    if number < 0:
        sign = '-'
        number = -number
    if 0 <= number < len(alphabet):
        return sign + alphabet[number]
    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36
    return sign + base36
    
if len(sys.argv) < 3:
  exit("specify image to upload")
  
boundary="----s4t8dp5yd5yd5yh5y"
data="--"+boundary+"\r\n"
data+="Content-Disposition: form-data; name=\"test\"; filename=\"test.png\"\r\n"
data+="Content-Type: image/jpg\r\n\r\n"

with open(sys.argv[2],"rb") as f:
  data+=f.read()
data+="\r\n--"+boundary+"--"
size=str(len(data))
raw_input("Size: "+str(size))
headers={"Content-Type":"multipart/form-data; boundary="+boundary}
resp=urllib2.urlopen(urllib2.Request("https://www.deviantart.com/api/oauth2/stash/submit?access_token="+sys.argv[1],data,headers)).read()
print resp
resp=json.loads(resp)
if "stashid" in resp:
  print "https://sta.sh/0"+base36encode(resp["stashid"])
  