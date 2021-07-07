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
    Notes: * indicates important reminders; filtered by no. of stars.
    ! indicates completed reminders; these are ignored.
    str -> [str]'''
    with open(reminders_pathname, mode = 'r') as f:
        rlines = f.readlines()                       #read from reminders_pathname and normalize
        rlines = [rr.strip('\n') for rr in reminders]
        return reminder

def read_reminders_from_console():
    '''Reads in a list of reminders from text input.
    (To finish the list, the user should type nothing and enter.)
    None, str input -> [str]'''
    print('Enter your reminders here. (Type nothing and enter to stop.)')
    reminders = []                                              #type in reminders
    while True:
            newreminder = input('What is one of your reminders? ')
            if newreminder != '':
                    reminders.append(newreminder)
            else:
                    break
    return reminders

#function to add stars to reminder file lines
def add_stars_to_reminderlines(reminderlines, items_to_star):
    '''This function should add stars to the marked items given by the indices in the second column.
    [str], [(str, int)] -> [str]
    '''
    result = reminderlines
    for (item, index) in items_to_star:
        result[index] = '*' + result[index]
    return result

#function to normalize reminders
def normalize_reminderlines(reminderlines):
    '''Normalizes reminderlines.
    Deletes lines starting with -.
    Filters lines not starting with *, if any exists, and eliminates beginning *.
    [str] -> [str].'''
    result = reminderlines
    result = list(filter((lambda s: s[0] != '-'), result)) #detes lines starting with -
    imp = list(filter((lambda s: s[0] = '*'), result)) #selects lines starting with *
    if len(imp) > 0:
        result = list(map((lambda s: s[1:]), imp))
    return result

#main code
#read in reminders
if input('Do you want to read in your reminders from a file? ') in ['yes', 'Yes']:
    reminders_pathname = input('What is the file path? ')
    reminders = read_reminders_from_file(reminders_pathname)
else:
    reminders = read_reminders_from_console()
#normalize reminders
reminders = normalize_reminderlines(reminders)

#running FVP on idea list
print('\nNow, let\'s sort your reminders!')
#keep track of indices (to make file-writing easy)
reminders_shuffled = [(reminders[index], index) for index in range(len(reminders))]
random.shuffle(reminders_shuffled)      #to remove bias from idea order; TODO: allow option to keep original order
bestideas = [reminders_shuffled[0]]
for i in range(1, len(reminders_shuffled)):
	response = input(f'Would you rather do "{reminders_shuffled[i][0]}" rather than "{bestideas[-1][0]}"? ')
	if response in ['yes', 'Yes']:
		bestideas.append(reminders_shuffled[i])

#output
print(f'\nYou should do {list(bestideas.__reversed__())[0][0]}.')

#for file writes
if reminders_pathname != '':
    if input('Write to file? ') in ['yes', 'Yes']:
        with open(reminders_pathname, 'r') as f:
            reminderfile_contents = f.readlines()
        with open(reminders_pathname, 'w') as f:
            f.writelines(add_stars_to_reminderlines(reminderfile_contents, bestideas))

if input('\nQuit? ') in ['yes', 'Yes']:
    exit()
