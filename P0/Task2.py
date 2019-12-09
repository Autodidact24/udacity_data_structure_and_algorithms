"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
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


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

