# Random Events (work in progress / untested)
# Each army to roll ONE d6 after each turn.  If 6 rolled, roll another d6.
# If greater than 3, then get a random positive event.  If less than 4, get a
# random negative event.

import random
def d6():
    return random.randint(1,6)
disease_d = {1:'dysentery',
             2:'cholera',
             3:'scarlet fever',
             4:'typhus',
             5:'pneumonia',
             6:'plague'}
infile = open("siege_events.txt", "r")
event_check = d6()

if event_check == 6 :
    pos_or_neg = d6()
    specific_event = str(d6()) # need as a string to validate against values[1]
    if pos_or_neg < 4 :        # negative event
        event_type = 'Negative'
    if pos_or_neg > 3 :        # positive event
        event_type = 'Positive'
    for aline in infile:
        values = aline.split(",")
        if values[0] == event_type and values[1] == specific_event :
            print('Random event!', values[2])
            repeatable_event = values[3]
            if repeatable_event == 'N' :
                print('If this event has occurred already please ignore - i.e. no random event')
                print('* if any further disease outbreak, then it is', disease_d[d6()])
            break
else :
    print("No random event this turn for you!")
infile.close()
