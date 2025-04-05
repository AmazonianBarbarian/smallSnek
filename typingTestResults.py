import requests

header = { 'Authorization': 'ApeKey placekeyhere' }
mode = {'mode': 'time'}
urlHack = open('urlPath.txt', 'r')
baseUrl = requests.get('https://api.monkeytype.com/results', headers=header) # to add params include [, params=mode ]
responce = baseUrl.json()

print("User: " + str(responce['data'][0]['name']))
print("Words Per Minute: " + str(responce['data'][0]['wpm'])) 

# This is for retriveing the most recent typing test results from MonkeyType (https://monkeytype.com/) using 
# their API (https://api.monkeytype.com/docs#tag/results/operation/results.get)
