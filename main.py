import requests
import json
print("welcome to nibble")
print("enter nibble in github user/repo format (expecting main branch)")
nibble = input("> ")
print("searching the cookie jar...")
nibblefile = requests.get("https://raw.githubusercontent.com/{}/main/nibble.json".format(nibble))
nibblefile = nibblefile.text
nibblefile = json.loads(nibblefile)
print("running {} by {}, c to cancel: ".format(nibblefile["name"], nibblefile["author"]), end='')
if input().lower() == "c":
    exit()
cookie = requests.get("https://raw.githubusercontent.com/{}/main/nibble.py".format(nibble))
cookie = cookie.text
x = open("nibble.py", "w")
x.write(cookie)
x.close()
print("nibble saved as nibble.py")