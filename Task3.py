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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
#part A
mylist={}
for x in calls:
    z=None
    if x[0][0]=='(':
        for i in x[0]:
            if i=='(':
                continue
            if i==')':
                break
            if z==None:
             z=i
             continue
            z=z+i
        mylist[z]=1
        continue
    if x[0][0]=='7' or x[0][0]=='8' or x[0][0]=='9':
        j=1
        for i in x[0]:
            if z==None:
             z=i
             continue
            z=z+i
            j=j+1
            if j==4:
             break
        mylist[z]=1
    if x[0][0]=='1':
     z='140'
     mylist[z]=1
print("The numbers called by people in Bangalore have codes:")
for x in sorted(mylist.keys()):
    print(x)
#part b
count1=0
count2=0
counter=float(0)
for x in calls:
    if x[0].startswith("(080)"):
        count1+=1
    if x[1].startswith("(080)") and x[0].startswith("(080)"):
        count2+=1

counter=str(round((count2/count1)*100,2))
print("%s percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore." %counter)
