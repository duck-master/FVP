#code written by duck_master from 2 january 2021
#licensed under MIT license
#based on Final Version Perfected, a method invented by willbradshaw on 27 november 2020
#as described in https://www.lesswrong.com/posts/xfcKYznQ6B9yuxB28/final-version-perfected-an-underused-execution-algorithm
#TODO: make into PyPI package or shell script

#libraries
import random

#reading in the idea list from user input
#TODO: implement already having stars

#read in reminders
if input('Do you want to read in your reminders from a file? ') in ['yes', 'Yes']:
    reminders_pathname = input('What is the file pathname? ')   #read in reminders from filename
    with open(reminders_pathname, mode = 'r') as f:
        reminders_rawlist = f.readlines()                       #read from reminders_pathname and normalize
        reminders_rawlist = [rr.strip('\n') for rr in reminders_rawlist]
    reminder_lists = {}
    currlist = 'default'                                        #unlisted reminders go into "default" reminder list
    for rr in reminders_rawlist:                                #sort reminders into lists; there might be a more Pythonic way but idk
        if rr[:2] == '==' and rr[-2:] == '==':
            currlist = rr[2:-2]
        elif currlist not in reminder_lists:                    #to prevent KeyErrors
            reminder_lists[currlist] = [rr]
        else:
            reminder_lists[currlist].append(rr)
else:
    print('Enter your reminders here. (Type in nothing and enter to stop.)')
    reminders = []                                              #type in reminders
    while True:
            newreminder = input('What is a reminder of yours? ')
            if newreminder != '':
                    reminders.append(newreminder)
            else:
                    break
    reminder_lists = {'default': reminders}

#select main list
if len(reminder_lists) == 1:                                    #if there's only one list, select this
    reminders = reminder_lists[list(reminder_lists)[0]]
else:
    list_to_select = input('What reminder list would you like to FVP? ')
    if list_to_select not in reminder_lists:
        list_to_select = list(reminder_lists)[0]
    reminders = reminder_lists[list_to_select]

#running FVP on idea list
print('\nNow, let\'s FVP your reminders!')
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
