# Siege Scenario generator
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

import random
def d6():
    return random.randint(1,6)

relief_d = {1:'no hope of relief of the siege by land',
            2:'some hope of relief by land after 2 weeks',
            3:'some hope of relief by land after 10 days',
            4:'a good chance of relief by land in 5 days',
            5:'news that relief will arrive by land in 3 days',
            6:'news that relief by land will be here in 36 hours'}
population_list = [3000, 6000, 9000, 12000, 15000, 18000]
weekly_food_list = [10000, 15000, 20000, 25000, 30000, 40000]
disease_d = {1:'dysentery',
             2:'cholera',
             3:'scarlet fever',
             4:'typhus',
             5:'pneumonia',
             6:'plague'}
has_port = d6()
has_port_str = '\nThe besieged town does have a port,'
ship_due = d6()
ships_d = {1:'Nicodemus',
           2:'Leopard',
           3:'Providence',
           4:'Greyhound',
           5:'Swallow',
           6:'Unicorn'}
days_to_arrive = d6() * 2
disease_present = d6()
petards_present = d6()
can_sally = d6()

cls()
# general scenario
print('\nYou are the Military Governor of a besieged town. There is', relief_d[d6()])
print('\nThe local population including an influx of local countryfolk is', population_list[d6() - 1])
print('Your garrison and the townsfolk have enough provisions for 1 week for', weekly_food_list[d6() - 1], 'people.')
# port access and relief ship arrival news
if has_port > 4 :
    if ship_due > 4 :
        print(has_port_str, 'and a relief ship,', str(ships_d[d6()] + ','), 'carrying 750 men and provisions is due in', days_to_arrive, 'day(s).')
    else :
        print(has_port_str, 'however no relief ship is due for the forseeable future.')
else :
    print('\nThe besieged town is land-locked and has no port to get relief that way.')
# disease
if disease_present > 2 :
    print('\nThe bad news is that disease has just broken out in the town with around', str(d6())+'0%', 'of those')
    print('in the town likely to be impacted by an outbreak of', disease_d[d6()], 'with cases rising by 10% per week.')
else :
    print('\nFortunately there do not appear to be any issues as regards disease within the town.')

# disease
disease_present = d6()
if disease_present > 2 :
    print('\nYou have learned that disease has broken out amongst the troops besieging the town with', str(d6())+'0%', 'of those')
    print('troops likely to be impacted by an outbreak of', disease_d[d6()], 'with cases rising by 15% per week.')
else :
    print('\nThere is no news of disease outside the town.')
print('\nOn the plus side for the besieging force, they have', petards_present, 'petard(s) for trying to create a breach.')
if can_sally > 3 :
    print('\nYour garrison, commanders and their men, are willing to sally forth and try their chances of breaking out.')
else:
    print('\nYour commanding officers advise you that your men would be nervous about attempting to break out.')
print('\nNow is the time to consider your plan for preventing this strategic town falling into enemy hands.')
print('\nNote: the maximum number of turns per day shall be TWELVE, with conflict ending no later than 7pm.')
