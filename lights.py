import json
import requests
from pprint import pprint

import matplotlib
import matplotlib.pyplot as plt

from datetime import datetime
from dateutil import parser
#from dateutil import tz
#to_zone = tz.gettz('America/Los_Angeles')

api_token = '0iGsbBGunPVPBNikkJxzzMdBVBCPju'
api_url_base = 'https://api.samsara.com/v1/industrial/data'
startMs = '1550280600000'
endMs = '1550282400000'

r = requests.get(api_url_base + '?access_token=' + api_token + '&startMs=' + startMs + '&endMs=' + endMs)

rJSON = r.json()

data = rJSON['dataInputs'] 
switch1 = data[0]
switch2 = data[1]
light1 = data[2]
light2 = data[3]

# Parse data for switch1
points1 = switch1['points']
dates1 = []
values1 = []

for p in points1:
    # convert unix mili to local time
    unix = p['timeMs']
    datestring = datetime.utcfromtimestamp(unix/1000).strftime('%H:%M')
    date = parser.parse(datestring)
    dates1.append(date)
    values1.append(p['value'])

# Parse data for switch2
points2 = switch2['points']
dates2 = []
values2 = []

for p in points2:
    # convert unix mili to local time
    unix = p['timeMs']
    datestring = datetime.utcfromtimestamp(unix/1000).strftime('%H:%M')
    date = parser.parse(datestring)
    dates2.append(date)
    values2.append(p['value'])



plt.subplot(4, 1, 1)
plt.plot(dates1, values1)
plt.ylabel('On / Off')
plt.xlabel('time')
plt.title('Switch1')

plt.subplot(4, 1, 2)
plt.plot(dates2, values2)
plt.ylabel('On / Off')
plt.xlabel('time')
plt.title('Switch2')





plt.show()
