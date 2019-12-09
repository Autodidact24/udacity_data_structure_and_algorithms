"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
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

unique_records = set(telephone_numbers_texts + telephone_numbers_calls)

print("There are {0} different telephone numbers in the records.".format(len(unique_records)))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
