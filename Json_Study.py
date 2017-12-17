import json


contacts= '''
    
    {
  "people": [
    {
      "name": "john",
      "abbreviation": "j",
      "phones": ["205", "251"]
    },
      {
          "name": "alex",
          "abbreviation": "j",
          "phones": ["205", "251"]
      }
  ]
}
'''
data=json.loads(contacts)
print(data)

for man in data['people']:
     print(man['name'])

new_str=json.dumps(data,sort_keys=True)

print(new_str)