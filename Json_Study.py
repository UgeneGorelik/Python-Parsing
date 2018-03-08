#example on using and parsing Json files

import  json

#declare string in json format
people_string='''
    {
        "people": [
        {
            "name": "avi",
            "age": "13",
            "license" : true
        },
        {
            "name": "avi",
            "age": "15" ,
            "license" : false  
        }
    ]
   } 
'''
#load string to be as json file
data =json.loads(people_string)

#as its like dict you can use it and print it like dict
print(type(data['people']))

#delete field in dict
for person in data['people']:
    del person['age']

#create string from json object ident uset for beautifying the string and sort keys sorts the keys
new_string=json.dumps(data,indent=2,sort_keys=True)

# print(new_string)

#open existing json file
with open('states.json') as f:
    data=json.load(f)

for state in data['states']:
    print(state['name'])

for state in data['states']:
    del state['area_codes']

#return to file after beautifying it using ident
with open('new_states.json','w') as f:
    json.dump(data,f, indent=2)

