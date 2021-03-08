"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def getLongestCallDuration(calls):
    phoneRecords = {}
    for call in calls:
        currDuration = int(call[3])
        phoneRecords[call[0]] = phoneRecords.get(call[0], 0) + currDuration
        phoneRecords[call[1]] = phoneRecords.get(call[1], 0) + currDuration
    maxDuration = max(phoneRecords.values())
    phoneNum = max(phoneRecords, key=phoneRecords.get)
    print(f"{phoneNum} spent the longest time, {maxDuration} seconds, on the phone during September 2016")

getLongestCallDuration(calls)