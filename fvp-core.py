#code written by duck_master since 2 january 2021
#licensed under MIT license
#based on Final Version Perfected, invented by willbradshaw on 27 november 2020
#as described in https://www.lesswrong.com/posts/xfcKYznQ6B9yuxB28/final-version-perfected-an-underused-execution-algorithm
#TODO: make into PyPI package or shell script

#libraries
import random       #for randomizing reminder list

#functions for reading/normalizing input
#TODO: implement already having stars
#TODO: implement try-catch in case of bad filepath
def read_reminders_from_file(reminders_pathname):
    '''Reads in a list of reminders from a file.
    str -> [str]'''
    with open(reminders_pathname, mode = 'r') as f:
        reminders = f.readlines()                       #read from reminders_pathname and normalize
        reminders = [rr.strip('\n') for rr in reminders]
        return reminders

def read_reminders_from_console():
    '''Reads in a list of reminders from text input.
    (To finish the list, the user should type nothing and enter.)
    None, str input -> [str]'''
    print('Enter your reminders here. (Type nothing and enter to stop.)')
    reminders = []                                              #type in reminders
    while True:
            newreminder = input('What is a reminder of yours? ')
            if newreminder != '':
                    reminders.append(newreminder)
            else:
                    break
    return reminders

#function to add stars to reminder file lines
#TODO: implement
#def add_stars_to_reminderlines(reminderlines, items_to_star):
#    '''TODO: implement.
#    This function should add stars to the marked items given by the indices in the second column.
#    [str], [(str, int)] -> [str]
#    '''
#    pass

#read in reminders
if input('Do you want to read in your reminders from a file? ') in ['yes', 'Yes']:
    reminders_pathname = input('What is the file path? ')
    reminders = read_reminders_from_file(reminders_pathname)
else:
    reminders = read_reminders_from_console()

#running FVP on idea list
print('\nNow, let\'s FVP your reminders!')
#keep track of indices (to make file-writing easy)
reminders_shuffled = [(reminders[index], index) for index in range(len(reminders))]
random.shuffle(reminders_shuffled)      #to remove bias from idea order; TODO: allow option to keep original order
bestideas = [reminders_shuffled[0]]
for i in range(1, len(reminders_shuffled)):
	response = input(f'Would you rather do "{reminders_shuffled[i][0]}" rather than "{bestideas[-1][0]}"? ')
	if response in ['yes', 'Yes']:
		bestideas.append(reminders_shuffled[i])

#output
print('\nHere are your marked reminders, in order of importance:')
for idea in list(bestideas.__reversed__()):
    print(f'- {idea[0]}')

#for file writes
##if reminders_pathname != '':
##    if input('Write to file? ') in ['yes', 'Yes']:
##        with open(reminders_pathname, 'r') as f:
##            reminderfile_contents = f.readlines()
##        with open(reminders_pathname, 'w') as f:
##            f.writelines(add_stars_to_reminderlines(reminderfile_contents, bestideas))

if input('\nQuit? ') in ['yes', 'Yes']:
    exit()
