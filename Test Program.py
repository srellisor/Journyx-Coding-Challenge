import json
import re
from urllib import request
import urllib

#Message recieves our users input
message = input()

#List of variables
output = []
count = 0
links = ["Links:"]

#Find gets any urls from our users input and places them into a list
def Find(string): 
  
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)       
    return [x[0] for x in url] 

#Find url title using urllib
def findTitle(url):
    webpage = urllib.request.urlopen(url).read()
    title = str(webpage).split('<title>')[1].split('</title>')[0]
    return title

#If there's an occurance of a mention findall mentions and place them into a list
if "@" in message:
    for text in [message]:
        mention_list = "Mentions:",re.findall(r'@(\w+)', text)
        #Insert list into the output list
        output.append(mention_list)

#If there's an occurance of a emoticon findall emoticons and place them into a list
if "(" in message:
    for text in [message]:
        emoticon_list = "Emoticons:",re.findall(r"\(([A-Za-z0-9_]{0,15})\)", text)
        #Insert list into the output list
        output.append(emoticon_list)
        
#If the message has http in it we run find then seperate the list into elements
if "http" in message:
    html_list = Find(message)
    #Inside the while loop we run the findTitle function for each list element
    while count < len(html_list):
        url_title = (findTitle(html_list[count]))
        #Combine the url and title into an element and insert it links list
        link = "url: " + html_list[count] + ", tile: " + url_title
        links.append(link)
        count += 1
    #Insert links list into our output list
    output.append(links)
        
#Split the user input into individual words get a count then subtract the
#occurances of mentions, emoticons and links
word_count = "Words:", len(message.split()) - message.count("@") - message.count("(") - message.count("http")
output.append(word_count)
#Take our output list and convert it into json
json_output = json.dumps(output)

print (json_output)