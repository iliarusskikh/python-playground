#application programming interface
#rest  - web requests
#post - write new data post/drinks
#put - replace/update data put/drinks/102
#get
#delete

import requests
import json

response = requests.get('http://api.stackexchange.com/2.2/questions?order=desc&sor=activity&site=stackoverflow')

print(response)
#print(response.json())
for data in (response.json()['items']):
    if data['answer_count']==0:
        print(data['title'])
        print(data['link'])
        print()



