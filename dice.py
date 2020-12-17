import random

def d6():
    return random.randint(1,6)

rolls = int(input('How many dice do you need to roll? '))
while rolls > 0 :
    print(d6())
    rolls -= 1
