import datetime, random

def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA

print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
  The birthday paradox shows us that in a group of N people, the odds
  that two of them have matching birthdays is surprisingly large.
  This program does a Monte Carlo simulation (that is, repeated random
  simulations) to explore this concept. 
 (It's not actually a paradox, it's just a surprising result.)
 ''')

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')

while True:
    print('How many birthdays shall I generate?')
    response = input("> ")
    if response.isdecimal() and int(response) > 0:
        numBDays = int(response)
        break
print()

print(f'Here are {numBDays} birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

match = getMatch(birthdays)
print('In this simulation, ', end='')
if match is not None:
    monthName = MONTHS[match.month - 1]
    dateText = f'{monthName} {match.day}'
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')
print('Let\'s run another 100,000 simulations.')
simMatch = 0  # How many simulations had matching birthdays in them.

for i in range(100000):
    if i % 1000 == 0:  # Change the frequency to every 1,000 simulations
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) is not None:
        simMatch += 1
print('100,000 simulations run.')

probability = round(simMatch / 100000 * 100, 2)
print(f'Out of 100,000 simulations of {numBDays} people, there was a')
print(f'matching birthday in that group {simMatch} times. This means')
print(f'that {numBDays} people have a {probability}% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')
