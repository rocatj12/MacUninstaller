import os
import subprocess
import time
import argparse
import sys
import glob
import shutil


print('')
print('#################################################################')
print('#                                                               #')
print('#                    Uninstaller for MacOS                      #')
print('#                    Written by Agent Roca                      #')
print('#                       Version 1.0.0                           #')
print('#                                                               #')
print('#             *************************************             #')
print('#        Run "python MacUninstaller.py -h" for usage/help       #')
print('#             *************************************             #')
print('#                                                               #')
print('#################################################################')
print('')


##############################################################################
                                 # Functions #
##############################################################################

def delete(item): # Item is an absolute pathname
    # Check if item is in trash, delete if there, before deleting item specified to avoid conflicts
    if item in os.listdir(path='~/.Trash/'): # Iterate over the list of items in "~/.Trash/"
        if os.path.isdir('~/.Trash/' + item): # Check if the item match in ~/.Trash is directory or file, act accordingly
            shutil.rmtree('~/.Trash/' + item) # Item is directory, delete recursively
        else:
            os.remove('~/.Trash/' + item) # Item is file, delete

    # Proceed with removing specified item to ~/.Trash
    if os.path.isdir(item):
        shutil.rmtree
    else:
        os.remove(item)


##############################################################################
                        # Set up command line arguments #
##############################################################################

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--application', help='Application Name [How it appears in "/Applications/", without the ".app"]', metavar='')
parser.add_argument('-m', '--mode', help='Intensity of Scan [ 1:Light, (2):Standard, 3:Intense] (Default = 2)', metavar='')
args = parser.parse_args()
APP_TO_REMOVE = args.application
mode = args.mode

if APP_TO_REMOVE[-4:] == '.app':
    APP_TO_REMOVE = APP_TO_REMOVE.replace('.app', '')

# Error check cause someone might be silly
if '/' in str(APP_TO_REMOVE): # Yeeting it if there is a '/' in the application name
    print('Not valid application name')
    print('Exiting...')
    exit()
if mode == None: # Setting default mode to Mode 2
    mode = 2
if mode < 1 or mode > 3: # What were ya thinking
    print('Not valid mode')
    print('Exiting...')
    exit()


##############################################################################
                            # Start Removal Process
##############################################################################

# Variables (somewhat of a bad practice, I know)
raw_input = raw_input # Ignore this stupid line, python 2 is being a b!tch
items_to_remove = ''
cwd = ''

#################################### Mode 1 ##################################
# Remove from main applications directory
cwd = '/Applications/'
print('Searching and removing...')
print('CWD: "' + cwd + '"')

os.chdir(cwd) # Change working directory to "/Applications"

for item in os.listdir(path='.'): # List all items in current directory "."
    if APP_TO_REMOVE in item: # If item specified exists
        delete(os.path.abspath(item)) # Delete it, passing in the absolute path
    else: # It is not exist under the specified name in the cwd
        print('Application does not exist...')

        if mode >= 2: # If Mode 2, continuing on to more scans
            print('Continuing with Level 2 to find leftovers')
        else: # Only Mode 1 was specified, exiting program
            print('Level 1 Removal Complete')
            exit()

cwd = '' # Just emptying out the variable to be reused and avoid conflicts


#################################### Mode 2 ##################################
# Remove files and directories from known support locations
# Starting at user's HOME Application Support
cwd = '~/Library/Application Support/"'
print('Searching and removing...')
print('CWD: "' + cwd + '"')

os.chdir(cwd) # Change working directory to "~/Library/Application Support/"

if os.path.exists(APP_TO_REMOVE): # If there is a directory that exists in the cwd with a title that matches the item specified
    print('Application Support data was found...')
    print()
    print('List of items found that match:')

    items_to_remove = glob.glob(item) # Create list matches to the item specified
    for item in items_to_remove: # Print to screen all items that were found as a match
        print(os.path.abspath(item))

    can_remove = raw_input('Remove? [Y/n]: ') # Confirm that operator would like to delete these items (Yes is the default)
    if can_remove.rstrip() == '' or 'Y' or 'y': # If operator approved, continuing
        print('Removing...')

        for item in items_to_remove: # Scanning over that list again and deleting the matching items
            delete(os.path.abspath(item))
    elif can_remove.rstrip() == 'n' or 'N': # If operator declined, exiting
        print('Exiting...')
        exit()
    else: # Error? Exiting, don't want to make assumptions in this situation
        print("Unexpected error [Could not verify user choice]")
        exit()

else: # No application support was found in cwd ("~/Library/Application Support")
    print('No application support found in "' + cwd + '"') 
    if mode == 3:
        print('Continuing to Level 3 for advanced scan')
    else:
        print('Level 2 Removal Complete')
        exit()

cwd = ''# Emptying out the variable to be reused and avoid conflicts
items_to_remove = '' # Emptying out the variable to be reused and avoid conflicts

# Switching to ROOT Application Support, scanning again
cwd = '/Library/Application Support'
print('Searching and removing...')
print('CWD: "' + cwd + '"')

os.chdir(cwd) # Chainging cwd to "/Library/Application Support"

if os.path.exists(APP_TO_REMOVE):
    print('Application Support data was found...')
    print()
    print('List of items found that match')

    items_to_remove = glob.glob(item)
    for item in items_to_remove:
        print(os.path.abspath(item))
    
    can_remove = raw_input('Remove? [Y/n]: ')
    if can_remove == '' or 'Y' or 'y':
        print('Removing...')

        for item in items_to_remove:
            delete(os.path.abspath(item))
    elif can_remove == 'n' or 'N':
        print('Exiting...')
        exit()
    else:
        print('Unexpected error [Could not verify user choice]')
        exit()

else: # No application support was found in cwd ("/Library/Application Support")
    print('No application support found in "' + cwd + '"')

cwd = ''
items_to_remove = ''

# Switching to User Launch Agents
cwd = '~/Library/LaunchAgents'
print('Searching and removing...')
print('CWD: "' + cwd + '"')

os.chdir(cwd)

items_to_remove = glob.glob('*' + APP_TO_REMOVE + '*')
for item in items_to_remove:
    delete(os.path.abspath(item))

cwd = ''
items_to_remove = ''

# Switching to ROOT Launch Agents
cwd = '/Library/LaunchAgents'
print('Searching and removing...')
print('CWD: "' + cwd + '"')

os.chdir(cwd)

items_to_remove = glob.glob('*' + APP_TO_REMOVE + '*') # using the * because it is usually surrounded by other things
for item in items_to_remove:
    delete(os.path.abspath(item))

cwd = ''
items_to_remove = ''


# Switching to Application Scripts
cwd = '~/Library/Application Scripts'
print('Searching and removing...')
print('CWD: "' + cwd + '"')

os.chdir(cwd)

items_to_remove = glob.glob('*' + APP_TO_REMOVE + '*')
for item in items_to_remove:
    delete(os.path.abspath(item))

cwd = ''
items_to_remove = ''





#################################### Mode 3 ##################################

# os.chdir(os.path.expanduser("~"))
# print('Starting System Scan...')
# os.system('mdfind ' + APP_TO_REMOVEOVE_stripped)
# raw_input('Remove the found leftovers? [Y/n]: ')


