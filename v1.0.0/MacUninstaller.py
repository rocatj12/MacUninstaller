import os
import subprocess
import time
import argparse
import sys
import glob

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

# Functions

def delete(item):
    command = 'sudo mv ' + str(item) + ' ~/.Trash'
    os.system(command)
    try:
        pass
    except OSError: # Another copy of the dir in question is already in trash
        # item_in_trash = '~/.Trash/' + str(item)
        # os.removedirs(item_in_trash) # So empty that item out of trash so dir in question can go there
        #print('"' + '" is already in the trash, remove it first and retry') # we're gonna need a work around
        pass


# Set up command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--application', help='Application Name [How it appears in "/Applications/"]', metavar='')
parser.add_argument('-m', '--mode', help='Intensity of Scan [ 1:Light, (2):Standard, 3:Intense]', metavar='')
args = parser.parse_args()
app_to_rem = args.application
app_to_rem_stripped = app_to_rem.replace('.app', '')
mode = args.mode


# Error check cause someone might be silly
if '/' in str(app_to_rem):
    print('Not valid application name')
    print('Exiting...')
    exit()
if mode == None:
    mode = 2
if mode < 1:
    print('Not valid mode')
    print('Exiting...')
    exit()


# Start removal process

# Mode 1
# Remove from main applications directory
os.chdir('/Users/roca/Desktop/')
for item in glob.glob('*'):
    if app_to_rem_stripped in item:
        # delete(item)
        pass
    else:
        print('Application does not exist...')
        if mode >= 2:
            print('Continuing with Level 2 to find leftovers')
        else:
            print('Level 1 Removal Complete')
            exit()


# Mode 1 & 2
# Remove files and directories from known support locations
os.chdir('/Library/Application Support/')
if os.path.exists(app_to_rem_stripped):
    print('Application support was found...')
    raw_input = raw_input # Ignore this stupid line, python is being a bitch
    can_remove = raw_input('Remove? [Y/n]: ')
    if can_remove.rstrip() == '' or 'Y' or 'y':
        print('Removing...')
        for item in glob.glob('*'):
            # delete(item)
            pass
        os.chdir(os.path.expanduser("~/Library"))
        for item in glob.glob('*'):
            # delete(item)
            pass
    elif can_remove.rstrip() == 'n':
        print('Exiting...')
        exit()
else:
    print('No application support found')
    if mode >= 3:
        print('Continuing to Level 3 for advanced scan')
    else:
        print('Level 2 Removal Complete')
        exit()

# Mode 1 & 1 & 3

# os.chdir(os.path.expanduser("~"))
# print('Starting System Scan...')
# os.system('mdfind ' + app_to_rem_stripped)
# raw_input('Remove the found leftovers? [Y/n]: ')sds


