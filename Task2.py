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
my_dictCall={}
for x in calls:
 try:
   my_dictCall[x[0]]+=int(x[3])
 except:
   my_dictCall[x[0]]=int(x[3])
for x in calls:
 try:
   my_dictCall[x[1]]+=int(x[3])
 except:
   my_dictCall[x[1]]=int(x[3])
no=None
value=0
for x,y in my_dictCall.items():
    if no==None or value<y:
      no=x
      value=y
    else:
      continue
print("%s spent the longest time, %d seconds, on the phone during September 2016."%(no,value))
