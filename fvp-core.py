#code written by duck_master from 2 january 2021
#licensed under MIT license
#based on Final Version Perfected, a method invented by willbradshaw on 27 november 2020
#as described in https://www.lesswrong.com/posts/xfcKYznQ6B9yuxB28/final-version-perfected-an-underused-execution-algorithm
#TODO: make into shell script and/or PyPI package

#libraries
import random

#reading in the idea list from user input
#TODO: implement file reads
#TODO: implement already having stars 
print('Enter your reminders here. (Type in nothing and enter to stop.)')
reminders = []
while True:
    newreminder = input('What is a reminder of yours? ')
    if newreminder != '':
        reminders.append(newreminder)
    else:
        break

#running FVP on idea list
print('\nNow that we\'ve finished listing your reminders, let\'s FVP them!')
reminders_shuffled = reminders
random.shuffle(reminders_shuffled)      #to remove bias from idea order; TODO: allow option to keep original order
bestideas = [reminders_shuffled[0]]
for i in range(1, len(reminders_shuffled)):
	response = input(f'Would you rather do "{reminders_shuffled[i]}" rather than "{bestideas[-1]}"? ')
	if response in ['yes', 'Yes']:
		bestideas.append(reminders_shuffled[i])

#output
#TODO: implement file writes
print('\nHere are your marked reminders, in order of importance:')
bestideas.reverse()
for idea in bestideas:
    print(f'- {idea}')
if input('\nQuit? ') in ['yes', 'Yes']:
    exit()
