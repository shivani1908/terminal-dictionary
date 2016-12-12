import urllib
import json

var = raw_input("Enter input: ")
url = "http://api.duckduckgo.com/?q=%s&format=json&pretty=1" %var

uh = urllib.urlopen(url)
data = uh.read()
count = 0
js = json.loads(str(data))

#print json.dumps(js, indent=4)

count = len(js["RelatedTopics"])

if count==0:
    print "no meaning for such a word exists!!"

elif count==1:
    print  js["RelatedTopics"][0]["Text"]

else:
    count = 3 if count >= 3 else count
    print "The word %s may refer to: " %var
    for i in range(0, 3):
        meaning = js["RelatedTopics"][i]["Text"]
        print str((i+1)) + ": " + meaning







