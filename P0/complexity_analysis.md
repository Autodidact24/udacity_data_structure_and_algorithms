# Step 3 - Calculate Big O

Once you have completed your solution for each problem, perform a run time analysis (Worst Case Big-O Notation) of your solution. Document this for each problem and include this in your submission.

## Task 0

```python
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

first_text = texts[0]
print("First record of texts, {0} texts {1} at time {2}".format(first_text[0], first_text[1], first_text[2]))

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

last_call = calls[-1]
print("Last record of calls, {0} calls {1} at time {2}, lasting {3}".format(last_call[0], last_call[1], last_call[2], last_call[3]))
```

This task requires you to fetch the information associated with the first and the last call. This has a Worst Case Big-O complexity of O(1).
Given the index of the elements we are interested in i.e 0 and -1, and a fixed length list, we can fetch the elements O(1) irrespective of the size of the list.


## Task 1

```python
import csv
from itertools import chain

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

telephone_numbers_texts = list(chain.from_iterable((text[0], text[1]) for text in texts))
telephone_numbers_calls = list(chain.from_iterable((call[0], call[1]) for call in calls))

unique_records = list(chain.from_iterable((telephone_numbers_texts, telephone_numbers_calls)))

print("There are {0} different telephone numbers in the records.".format(len(set(unique_records))))
```
This task requires us to go through all the telephone numbers in the input files. This solution would have a complexity of O(n).


## Task 2

```python
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def time_tracker(telephone_number, duration, tracker):
    if telephone_number not in tracker.keys():
        tracker[telephone_number] = duration
    else:
        tracker[telephone_number] += duration
    
    return tracker

tracker = {}
for call in calls:
    caller, receiver, duration = call[0], call[1], int(call[3])
    time_tracker(call[0], duration, tracker)
    time_tracker(call[1], duration, tracker)

longest_time = max(tracker, key=tracker.get)

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(longest_time, tracker[longest_time]))
```
This solution would also require us to go through all the numbers in the input files. This also has a complexity of O(n).


## Task 3

```python
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Part A

def get_prefix(n):
    if n.startswith('('):
        prefix = n[:n.index(')')+1]
    elif n.startswith('140'):
        prefix = 140
    else:
        prefix = n[:4]
    return prefix


recievers = []
print("The numbers called by people in Bangalore have codes: ")
for call in calls:
    if call[0].startswith('(080)'):
        print(get_prefix(call[1]))
        recievers.append(get_prefix(call[1]))


# Part B

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(recievers.count('(080)')/len(recievers), 2)))
```
This requires iterating over the complete input file which has a complexity of O(n). Lexicographically sorting the `receivers` list has a complexity of O(log n).
Hence, the whole process has a complexity of O(n log n).


## Task 4

```python
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
    
print("These numbers could be telemarketers: {}".format(sorted(telemarketers, key=str.lower)))
```
Other than the overheads in creating all the lists, we just iterate over our input files. This would also have a complexity of O(n).
Lexicographically sorting the `telemarketers` list has a complexity of O(log n).
Hence, the whole process has a complexity of O(n log n).
