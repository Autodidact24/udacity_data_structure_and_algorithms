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

callers = [number[0] for number in calls]
receivers = [number[1] for number in calls]
texters = [text[0] for text in texts]
text_receivers = [text[1] for text in texts]

telemarketers = []
for num in callers:
    if num not in receivers + texters + text_receivers + telemarketers:
        telemarketers.append(num)
    
print("These numbers could be telemarketers: ")
for num in sorted(telemarketers, key=str.lower):
    print(num)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""