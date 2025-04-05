import requests

header = { 'Authorization': 'ApeKey placekeyhere' }
mode = {'mode': 'time'}
urlHack = open('urlPath.txt', 'r')
baseUrl = requests.get('https://api.monkeytype.com/results', headers=header) # to add params include [, params=mode ]
responce = baseUrl.json()

i = 0
average_wpm = 0
while i < 10:
   average_wpm = average_wpm + responce['data'][i]['wpm']
   i += 1

print("User: " + str(responce['data'][0]['name']))
print("Last test WPM: " + str(responce['data'][0]['wpm']))
print("Average WPM: " + str(round(average_wpm / 10)))

# This is for retriveing the most recent typing test results from MonkeyType (https://monkeytype.com/) using 
# their API (https://api.monkeytype.com/docs#tag/results/operation/results.get)
