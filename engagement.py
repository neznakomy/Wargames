# This program should accept the names of 2 opponents (exp: allow any number),
# the engagePeriod (list Periods) and engageCountry/Faction they wish to represent.
# The scenario generator will randomly determine: engageDate; engageStartTime;
# currWeather/duration (up to 12 hours); groundCondition (1 - boggy, 2, wet/heavy
# 3 - soft, 4-6 - dry);  numbers of infantry/type, cavalry/type and artillery;
# startingMorale (1-2 -1, 3-4 0, 5-6 +1); goodLeadership ( (1-2 -1, 3-4 0, 5-6 +1))
# In additon to on-field numbers at the start (Numbers present - 1-6 (,000s))
# Numbers nearby (1-2) to be assessed: a) whether they come (4-6), b) how many hours (1-6)
# 1 engageTurn = 30 engageMinutes
import random
import os
from time import localtime, strftime
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
class Engagement :
    def __init__(self, period, name1, name2) :
        self.period = period
        self.nameOpponent1 = name1
        self.nameOpponent2 = name2
    def upd_time(self, date, time) :
        self.engageDate = date
        self.engageStartTime = time
        return
    def upd_conditions(self, weather, ground) :
        self.currWeather = weather
        self.groundCondition = ground
        return
    def __str__(self):
        return "{} battle between {} and {} on {}".format(self.period, self.nameOpponent1, self.nameOpponent2, self.engageDate)

class Opponent :
    def __init__(self, name, army, general) :
        self.name = name
        self.army = army
        self.general = general
    def upd_troops(self, foot, horse, art, morale, leadership) :
        self.foot_qty = foot
        self.horse_qty = horse
        self.art_qty = art
        self.startingMorale = morale
        self.goodLeadership = leadership
    def upd_num_extras(self, num_extras) :
        self.num_extras = num_extras
    def upd_extras(self, foot, horse, art, morale, leadership, wait) :
        self.extras1 = 'Re-enforcements #1'
        self.extras1_foot_qty = foot
        self.extras1_horse_qty = horse
        self.extras1_art_qty = art
        self.extras1_morale = morale
        self.extras1_leadership = leadership
        self.extras1_turnsaway = wait

def d6():
    return random.randint(1,6)
def d12():
    return random.randint(1,12)
def d28():
    return random.randint(1,28)
def randyear(core_date, var):
    return random.randint(core_date - var, core_date + var)

Periods = ['1 - Medieval', '2 - English Civil War', '3 - Napoleonic']
Weather = {1:'Heavy Rain', 2:'Rain', 3:'Drizzle', 4:'Fine', 5:'Sunny', 6:'Hot'}
Ground = {1:'Boggy', 2:'Heavy', 3:'Soft', 4:'Good', 5:'Dry', 6:'Hard/crusty'}
Morale_d = {1:'Nervous', 2:'Poor', 3:'Average', 4:'Average', 5:'Good', 6:'Excellent'}
Lead_d = {1:'Very Poor', 2:'Poor', 3:'Average', 4:'Average', 5:'Good', 6:'Excellent'}
title = '\nWargame Scenario Generator v0.01'
current_datetime=strftime("%d-%m-%Y %H:%M:%S", localtime())
# not yet used. For expansion ideas
# weather on ground every 60 minutes, adjust ground by number (1- 6 range maintained though)
weather_on_ground = {'Heavy Rain':-1, 'Rain':-0.5, 'Drizzle':-0.25, 'Fine':+0.5, 'Sunny':+1, 'Hot':+1}
ground_on_movement = {'Boggy':0.3, 'Heavy':0.5, 'Soft':0.75, 'Good':1.0, 'Dry':1.0, 'Hard/crusty':0.8}
counters_before_break = {'Nervous':2, 'Poor':4, 'Average':6, 'Good':8, 'Excellent':10}

# Introduction and choice of period and opponents
cls()
print(title,'\t\t',current_datetime, '\n')     # print title
print(Periods[0], Periods[1], Periods[2])
a = int(input('Please enter the period you would like to reenact: '))
if a == 1 : a = Periods[0]
elif a == 2 : a = Periods[1]
elif a == 3 : a = Periods[2]
else: print(a, 'is not an option')
a = a[4:]
b = input('''Please enter the first player's name: ''')
c = input('''Please enter the second player's name: ''')
e = Engagement(a, b, c)            # create the instance of engagement

# generate weather conditions - expansion idea - logical link via data structure
w = Weather[d6()]
g = Ground[d6()]
e.upd_conditions(w, g)             # first update of instance of engagement

# generate chronological detail, starting with the date of the engagement
if e.period  == 'Medieval' :
    core_date = 1390
    var = 30
elif e.period == 'English Civil War' :
    core_date = 1646
    var = 4
elif e.period == 'Napoleonic' :
    core_date = 1810
    var = 5
year = str(randyear(core_date, var))
day = str(d28())
month = d12()
if month < 10 : month = '0' + str(month)
else : month = str(month)
d = day + '/' + month + '/' + year
# now determine the start time for the engagement
roll = d12()
if roll >= 5 and roll < 12: t = str(roll) + 'am'
else : t = str(roll) + 'pm'
e.upd_time(d, t)
cls()
print(title,'\t\t',current_datetime,'\n')     # print title
print(e)
print('Weather situation is', e.currWeather, 'and the ground is', e.groundCondition)
print('The action will commence at', e.engageStartTime, '(battle clock)')
print('* Remember that each turn is the equivalent of 30 minutes elapsed,')
print('so after the first turn, the battle clock will move on to', str(roll) + '.30' + e.engageStartTime[-2::] + '\n')

# Now we go onto the opponents and their army details
first_opponent = True
x = 2
for i in range(x):
    if first_opponent is True :
        a = e.nameOpponent1
    else:
        a = e.nameOpponent2
    print(a, 'army details:')
    b = input('Please enter country or faction: ')
    c = input('''Please enter the contemporary general's name: ''')
    if first_opponent is True :
        o1 = Opponent(a, b, c)
        first_opponent = False
    else: o2 = Opponent(a, b, c)
print('\nSummary:')
print(o1.name, 'and', o1.general, 'will lead the', o1.army, 'army')
print(o2.name, 'and', o2.general, 'will lead the', o2.army, 'army')

# now onto the basic army for each opponent
o1f = d6() * 200 * 2         # range 300-1800 x 2
o1h = d6() * 75 * 2          # range 100-600
o1a = d6() // 2          # range 0-3
o1m = Morale_d[d6()]
o1l = Lead_d[d6()]
o1.upd_troops(o1f, o1h, o1a, o1m, o1l)
o2f = d6() * 200 * 2         # as above
o2h = d6() * 75 * 2
o2a = d6() // 2
o2m = Morale_d[d6()]
o2l = Lead_d[d6()]
o2.upd_troops(o2f, o2h, o2a, o2m, o2l)
print('\nSummary of', o1.army, 'army make-up and status for :', o1.name)
print('Foot: ', o1.foot_qty, '(', int(o1.foot_qty / 25), 'figures )    ',
 'Horse: ', o1.horse_qty, '(', int(o1.horse_qty / 25), 'figures )    '
 'Guns: ', o1.art_qty)
print('Morale: ', o1.startingMorale)
print('Leadership: ', o1.goodLeadership)
print('\nSummary of', o2.army, 'make-up and status for :', o2.name)
print('Foot: ', o2.foot_qty, '(', int(o2.foot_qty / 25), 'figures )    ',
 'Horse: ', o2.horse_qty, '(', int(o2.horse_qty / 25), 'figures )    '
 'Guns: ', o1.art_qty)
print('Morale: ', o2.startingMorale)
print('Leadership: ', o2.goodLeadership)
print()
# finally the reenforcements section
if (o1.foot_qty + o1.horse_qty) > (o2.foot_qty + o2.horse_qty) :
    o1r = 0
    o2r = 1
elif (o1.foot_qty + o1.horse_qty) < (o2.foot_qty + o2.horse_qty) :
    o1r = 1
    o2r = 0
else :
    o1r = 1     # d6() // 4
    o2r = 1     # d6() // 4
o1.upd_num_extras(o1r)
o2.upd_num_extras(o2r)
print(o1.army, 'have news of', o1.num_extras, 'set(s) of re-reenforcements nearby')
print(o2.army, 'have news of', o2.num_extras, 'set(s) of re-reenforcements nearby')
known_by = d6()
if o1r == 1:
    o1ef1 = d6() * 300        # range 125-750
    o1eh1 = d6() * 100         # range 75-450
    o1ea1 = d6() // 6         # range 0-1
    o1em1 = Morale_d[d6()]
    o1el1 = Lead_d[d6()]
    o1et1 = 'This group is ' + str(d6() * 1) + ' hours away'
    o1.upd_extras(o1ef1, o1eh1, o1ea1, o1em1, o1el1, o1et1)
    print('\nSummary of', o1.army, o1.extras1, 'make-up and status for :', o1.name)
    print('Foot: ', o1.extras1_foot_qty, '(', int(o1.extras1_foot_qty / 25), 'figures )    ',
          'Horse: ', o1.extras1_horse_qty, '(', int(o1.extras1_horse_qty / 25), 'figures )    '
          'Guns: ', o1.extras1_art_qty)
    print('Morale: ', o1.extras1_morale)
    print('Leadership: ', o1.extras1_leadership)
    print('Distance away: ', o1.extras1_turnsaway)
    if known_by <= 3 :
        print('The opposing general IS AWARE of this')
    else :
        print('The opposing general IS NOT AWARE of this')
if o2r == 1:
    o2ef1 = d6() * 300         # as above
    o2eh1 = d6() * 100
    o2ea1 = d6() // 6
    o2em1 = Morale_d[d6()]
    o2el1 = Lead_d[d6()]
    o2et1 = 'This group is ' + str(d6() * 1) + ' hours away'
    o2.upd_extras(o2ef1, o2eh1, o2ea1, o2em1, o2el1, o2et1)
    print('\nSummary of', o2.army, o2.extras1, 'make-up and status for :', o2.name)
    print('Foot: ', o2.extras1_foot_qty, '(', int(o2.extras1_foot_qty / 25), 'figures )    ',
          'Horse: ', o2.extras1_horse_qty, '(', int(o2.extras1_horse_qty / 25), 'figures )    '
          'Guns: ', o2.extras1_art_qty)
    print('Morale: ', o2.extras1_morale)
    print('Leadership: ', o2.extras1_leadership)
    print('Distance away: ', o2.extras1_turnsaway)
    if known_by <= 3 :
        print('The opposing general IS AWARE of this')
    else :
        print('The opposing general IS NOT AWARE of this')
# final printed advice
print('\nYou now have up to 30 actual minutes to survey the field, write your battle plans')
print('deploy your troops and provide them with their initial orders for the first turn.')
# program ends
