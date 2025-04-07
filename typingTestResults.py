import requests
import requests
import datetime
import time
import os

header = { 'Authorization': f'ApeKey {os.environ['APE_KEY']}' }
mode = {'mode': 'time'}
baseUrl = requests.get('https://api.monkeytype.com/results', headers=header) # to add params include [, params=mode ]
responce = baseUrl.json()
timeTillUse = datetime.datetime.fromtimestamp(int(baseUrl.headers['x-ratelimit-reset'])).strftime('%Y-%m-%d %H:%M:%S UTC')

if int(baseUrl.headers['x-ratelimit-remaining']) > 5:
    i = 1
    average_wpm = 0
    while i < len(responce['data']):
       average_wpm = average_wpm + responce['data'][i]['wpm']
       i += 1

    print("User: " + str(responce['data'][0]['name']))
    print("Last test WPM: " + str(responce['data'][0]['wpm']))
    print("Average WPM: " + str(round(average_wpm / i)))
else:
    print("Rate limit exceeded, stop testing")
    print("May be used again on: " + timeTillUse)

# This is for retriveing the most recent typing test results from MonkeyType (https://monkeytype.com/) using 
# their API (https://api.monkeytype.com/docs#tag/results/operation/results.get)
