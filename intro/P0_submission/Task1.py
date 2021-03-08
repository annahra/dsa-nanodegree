"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def countDistinctTeleNums(texts, calls):
    existingNums = set()
    for text in texts:
        existingNums.add(text[0])
        existingNums.add(text[1])
    for call in calls:
        existingNums.add(call[0])
        existingNums.add(call[1])
    return len(existingNums)

print(f"There are {countDistinctTeleNums(texts,calls)} different telephone numbers in the records.")