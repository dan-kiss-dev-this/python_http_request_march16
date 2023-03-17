import requests
import json

response = requests.get(
    'http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

# to see the data type of the response and convert it into an object python can work with see below
# print(type(response))
# print(response.json()['items'])

for data in response.json()['items']:
    if data['is_answered']:
        # below we are grabbing the title attribute
        print(data['title'])
        print(data['link'])
    else:
        print("skipped")
    print("---")
