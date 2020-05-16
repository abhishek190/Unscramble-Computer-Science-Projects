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
thisdict={}
for x in texts:
 thisdict[x[0]]=1
 thisdict[x[1]]=1
for x in calls:
 thisdict[x[0]]=1
 thisdict[x[1]]=1
count=0
for x in thisdict.values():
    if x==1:
      count+=1
print("There are %d different telephone numbers in the records." %count)
