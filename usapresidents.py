#Problem description
#Find out if there are any duplicate urls used in the
#json placeholder photo data
from pprint import pprint
import requests

#url = 'https://jsonplaceholder.typicode.com/photos'
url = "https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json"

#get the data about the photos
response = requests.get(url)
#pprint(response.json())

#read that data into a variable  
json_data = response.json()


#print(json_data["RelatedTopics"][0]["Text"])


for element in json_data["RelatedTopics"]:
#    pprint((element["Text"].split())[0:3])
    pprint(element["Text"])
    obj = element["Text"]

pprint(obj)
pprint("Taylor" in obj)





#create a list for storing the url of each photo
#url_list = json_data['RelatedTopics']
#for item in json_data['RelatedTopics'][0]:
    #add the url for each photo to the url_list
    #url_list.append(item["text"])
#    print(item["Text"])
#print (len(url_list))

#new_url_list = set(url_list)
#print(len(new_url_list))
#How many items are in the url list (Should be 5000 since we have 5000 photos in our dataset)?


#How many items are there if we turn that list into a set?


