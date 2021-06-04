import requests
import json

url = "https://bandev.uk/api/lux/commands.json"

data = json.loads(requests.get(url).text)

readme = open("/home/runner/work/Lux/Lux/README.md", "r").read()

a = readme.split("<ul id='EDTCMDS'>")
a1 = a[1]
a2 = a1.split("</ul>")[0]
commands = a2.split("<li>")

i = 0

newcommands = ""


for command in data["commands"]:
  newcommands += "<li>"+"<code>"+command["examples"][0]+"</code><p>"+command["description"]+"</p>"+"</li>"
  
text = a[0] + "<ul id='EDTCMDS'>"+newcommands+"</ul>" + a[2]

print(text)
