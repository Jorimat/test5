def recommend_test():
    return 'Recommendations test...'


import csv
import re

def read_events(fileIn):
    events = []
    with open(fileIn) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if re.search('#', row[0]) is None: # Remove lines with pound sign
                events.append(row)    
    return events    



import collections

def recommend_pop(fileIn, nrec=5):
    
    # Read fileIn
    events = read_events(fileIn)
    
    # Get most popular ones
    articles = [ev[1] for ev in events] 
    counts = collections.Counter(articles)
    pop = counts.most_common(nrec)
    
    return pop



def events2string(fileIn):
    
    # Read fileIn
    events = read_events(fileIn)
    

    
    return str(events)
