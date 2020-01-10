"""
Program: MacUninstaller
Description: Lightweight uninstaller for MacOS and the files they leave behind
Author: Tyler Roca
Version: 0.0.8

Table of Contents
    1. Privilage Check
    2. Globals 
    3. Functions
    4. Setup Command Line Arguments
    5. Error Checking the Command Line Arguments
    6. Start Removal Process
        i.   Mode 1
        ii.  Mode 2
            a. "~/Library/Application Support/"
            b. "~/Library/LaunchAgents/"
            c. "~/Library/Application Scripts/"
            d. "/Library/Application Support/"
            e. "/Library/LaunchAgents/"
        iii. Mode 3 
            a. tbd
    7. Ending
"""

import os
import time
import argparse
import sys
import glob
import shutil
import platform
import getpass
from datetime import datetime
# from send2trash import send2trash # Due to Python not wanting to behave when working with the trash, using this library to help with it. Docs: https://pypi.org/project/Send2Trash/

##############################################################################
                            # 1. Privilage Check #
##############################################################################
# Requiring root privilage to run program
try:
    # Check whether user is root
    if os.geteuid() != 0:
        print('\nERROR: MacUninstaller must be run with root privileges. Try again with sudo:\n\t$ sudo python MacUninstaller.py\tor\n\t# python MacUninstaller.py')
        os._exit(1)

        if sys.platform.startswith('linux'):
            print('This program was intended for MacOS, your use on Linux may be sub-optimal.')
            print('Continuing...')
except:
    # User might be on Windows
    os._exit(1)


print('')
print('\t#################################################################')
print('\t#                                                               #')
print('\t#                       MacUninstaller                          #')
print('\t#                       --------------                          #')
print('\t#                     Author: Tyler Roca                        #')
print('\t#                       Version 0.0.8                           #')
print('\t#                                                               #')
print('\t#           *****************************************           #')
print('\t#     Run "sudo python MacUninstaller.py -h" for usage/help     #')
print('\t#           *****************************************           #')
print('\t#                                                               #')
print('\t#################################################################')
print('')

##############################################################################
                                # 2. Globals #
##############################################################################
error_occurred = False
cwd = ''
items_to_remove = ''
item_removed = False
current_mode = -1
other_user = ''
external_user_bool = False
user_is_root = False
raw_input = raw_input # Ignore, Python 2 things

### Checking if user is using sudo or escalated to root
if os.getenv("SUDO_USER") == None:
    user_is_root = True
else:
    user_is_root = False


##############################################################################
                                # 3. Functions #
##############################################################################
def scan_dir(cwd):
    items_to_remove = glob.glob('*' + APP_TO_REMOVE + '*')
    return items_to_remove

def delete(item): # Item is an absolute path
    try:
        # send2trash(item) # Delete it (should be moving to ~/.Trash but it isn't for some reason)
        if os.path.isdir(item):
            shutil.rmtree(item)
        else:
            os.remove(item)
    except Exception as e: # Error Logging
        error_occurred = True
        if os.path.exists('~/Desktop/MacUninstaller_ErrorLog'): # If error log exists, append to it
            f = open('~/Desktop/MacUninstaller_ErrorLog', 'a')
            f.write('\n\n' + str(datetime.now()) + '\n')
            f.write("{}: {}".format(str(item), str(e)))
            f.close()
        else:
            f = open(os.path.expanduser('~/Desktop/MacUninstaller_ErrorLog'), 'w') # If not, create it (i know probs better way to do this)
            f.write('\n\n' + str(datetime.now()))
            f.write("{}: {}".format(str(item), str(e)))
            f.close()
    finally:
        pass

def exit_program():
    if error_occurred:

        print('')
        print('===================================================================')
        print('There were errors in an operation, check the log file in ~/Desktop/')
        print('===================================================================')
        exit()
    else:
        print('')
        print('=========================================')
        print('Operation ran successfully with no errors')
        print('=========================================')
        exit()

def check_exit(): # Check if the program should keep running
    if MODE > current_mode: # Specified mode is greater than the current mode
        print('**Continuing to mode ' + str(current_mode+1) + ' to find leftovers**') # Continue
    else: # Specified mode is not greater than the current mode
        print('**Mode ' + MODE + 'removal complete**') # Exiting
        print('\n')
        exit_program()

def get_user():
    # getpass.getuser() returns 'root' when running with sudo so working around it to find who ran the sudo
    username = os.getenv("SUDO_USER")
    return str(username)

def check_user(USER):
    if USER in os.listdir('/Users/') and USER != get_user(): # Specified user exists and is not the logged in user
        check_user_input = raw_input('The specified user account belongs to someone else, are you sure you would like to proceed? [Y/n]: ')
        if check_user_input.strip() == 'Y' or 'y' or '':
            other_user = USER
            external_user_bool = True
        elif check_user_input.strip() == 'n' or 'N':
            print('Exiting...')
            exit()
        else:
            print('Could not verify input')
            exit(1)
    elif USER == get_user():
        print('Continuing as current user: ' + get_user())
        external_user_bool = False
    elif USER not in os.listdir('/Users/'):
        print('User not found')
        print('Exiting...')
        exit()
    else:
        print('User not found')
        print('Exiting...')
        exit(1)

def clear_variables():
    error_occurred = False
    cwd = ''
    items_to_remove = ''
    item_removed = False

def print_scan_status():
    print('::CWD: "' + cwd + '"')
    print('Searching and removing...')

def print_removal_status():
    if item_removed:
        print('Removed item(s)')
    else:
        print('Item does not exist')

def can_remove():
    can_remove_input = raw_input('Remove? [Y/n]: ') # Verify with operator that they would like to delete found items
    print('"' + can_remove_input + '"')#check
    if can_remove_input.strip() == '' or 'Y' or 'y': # Operator agrees
        print('Removing...')
        return True
    elif can_remove_input.strip() == 'n' or 'N': # Operator declines
        print('Exiting...')
        return False
    else:
        print('Unexpected Error [Could not verify user choice]')
        exit_program()

def print_intro():
    if user_is_root: print('RUNNING AS ROOT')
    else: print('RUNNING WITH SUDO')
    
    if sys.platform == "darwin": print('OPERATING SYSTEM: Mac OS')
    elif sys.platform.startswith('linux'): print('OPERATING SYSTEM: Linux')

    print('APP TO REMOVE: "{}"'.format(APP_TO_REMOVE))

    print('\n')


##############################################################################
                       # 4. Set up command line arguments #
##############################################################################
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--application', help='Application Name [How it appears in "/Applications/" without the ".app"]', required='TRUE', metavar='')
parser.add_argument('-m', '--mode', help='Intensity of Scan [1: Light, (2): Standard, 3: Intense]', metavar='')
# parser.add_argument('-u', '--user', help='Name of the user account to scan [How it appears on the Home directory] (default=current user)', metavar='')
args = parser.parse_args()

# Setting command line argument variables and making sure right data type is used
APP_TO_REMOVE = str(args.application)

# Setting default mode to 2 if nothing is specified
if args.mode is not None:
    MODE = int(args.mode)
else:
    MODE = 2

# if args.user is not None: # If a user is specified, save as string in USER
#     USER = str(args.user)
# else: # No user is specified, getting username of user who ran the sudo
#     USER = get_user()

# Error checking command line args
if '/' in APP_TO_REMOVE: # Yeeting the '/' if there is one in the file name specified
    print('Not valid application name')
    print('Exiting...')
    exit(1)

if MODE == None:
    mode = 2

if MODE < 1 or MODE > 3:
    print('Not valid mode')
    print('Exiting...')
    exit(1)

##############################################################################
                           # 6. Start Removal Process
##############################################################################
print_intro()
clear_variables()

#################################### i. Mode 1 ##################################
print('Mode 1 Removal Starting') # Starting cause mode has to be at least 1 to get this far
print('=======================')
current_mode = 1

### Remove from main applications directory
cwd = '/Applications/'
print_scan_status()

os.chdir(cwd) # Change working directory to "/Applications/"
items_to_remove = os.listdir('.')
for item in items_to_remove: # Index all items in the cwd
    if APP_TO_REMOVE.lower() in item.lower(): # If item specified exists, case insensitive
        print(os.path.abspath(item))
        delete(os.path.abspath(item))
        item_removed = True

print_removal_status() # Let operator know if things were removed or if nothing found
check_exit() # Check if program continues to next mode
clear_variables()

#################################### ii. Mode 2 ##################################
print('\nMode 2 Removal Starting')
print('=======================')
current_mode = 2

### Remove files and directories from known support locations

################################### a. "~/Library/Application Support/"
# Have to check the file path due to root escalation causing issues
if user_is_root: # Operator escalated to root, specify the home dir using env variable
    cwd = '/Users/' + str(os.getenv("USER")) + '/Library/Application Support/'
elif not user_is_root: # Operator using sudo
    cwd = os.path.expanduser('~/Library/Application Support/') #  Setting the cwd variable
print_scan_status() # Formatting

os.chdir(cwd) # Change directories to the cwd variable path
items_to_remove = scan_dir(cwd) # Build list of items that match the item specified

if len(items_to_remove) == 0: # If nothing was found as a match
    print('No Application Suppoort found in "' + cwd + '"')
else:
    print('Found Application Support data') # Found something
    print('Listing matching items...')
    for item in items_to_remove: # Print all the items out
        print(item)
    if can_remove(): # confirm with the operator that they would like to delete it
        for item in items_to_remove:
            delete(item)
            item_removed = True

print_removal_status() # Inform operator if items have been deleted by the operation that just finished
clear_variables()

################################### b. "~/Library/LaunchAgents/"
if user_is_root:
    cwd = '/Users/' + str(os.getenv("USER") + '/Library/LaunchAgents/')
elif not user_is_root:
    cwd = os.path.expanduser('~/Library/LaunchAgents/')
print_scan_status()

os.chdir(cwd)
items_to_remove = scan_dir(cwd)

if len(items_to_remove) == 0:
    print('No Launch Agents data found in "' + cwd + '"')
else:
    print('Found Launch Agents data')
    print('Listing matching items...')
    for item in items_to_remove:
        print(item)
    if can_remove():
        for item in items_to_remove:
            delete(item)
            item_removed = True

print_removal_status()
clear_variables()

################################### c. "~/Library/Application Scripts/"
if user_is_root:
    cwd = '/Users/' + str(os.getenv("USER") + '/Library/Application Scripts/')
elif not user_is_root:
    cwd = os.path.expanduser('~/Library/Application Scripts/')
print_scan_status()

os.chdir(cwd)
items_to_remove = scan_dir(cwd)

if len(items_to_remove) == 0:
    print('No Application Scripts data found in "' + '"')
else:
    print('Found Application Script data')
    print('Listing matching items...')
    for item in items_to_remove:
        print(item)
    if can_remove():
        for item in items_to_remove:
            delete(item)
            item_removed = True
    
print_removal_status()
clear_variables()

################################### d. "/Library/Application Support/"
cwd = '/Library/Application Support/'
print_scan_status()

os.chdir(cwd)
items_to_remove = scan_dir(cwd)

if len(items_to_remove) == 0:
    print('No Application Support data found in "' + cwd + '"')
else:
    print('Found Application Support data')
    print('Listing matching items...')
    for item in items_to_remove:
        print(item)
    if can_remove():
        for item in items_to_remove:
            delete(item)
            item_removed = True

print_removal_status()
clear_variables()

################################### e. "/Library/LaunchAgents/"
cwd  = '/Library/LaunchAgents'
print_scan_status()

os.chdir(cwd)
items_to_remove = scan_dir(cwd)

if len(items_to_remove) == 0:
    print('No Launch Agents data found in "' + cwd + '"')
else:
    print('Found Launch Agents data')
    print('Listing matching items...')
    for item in items_to_remove:
        print(item)
    if can_remove():
        for item in items_to_remove:
            delete(item)
            item_removed = True

print_removal_status()
clear_variables()

check_exit() # See if we continue to Mode 3 

#################################### iii. Mode 3 ##################################
print('\nMode 3 Removal Starting') # Starting cause mode has to be at least 1 to get this far
print('=======================')
current_mode = 3

# tbd
# Want to do a system scan here but need to perfect how it will exclude certain directories as to not delete important system files.
# As more common support locations are discovered, they will probably be added to mode 2, mode 3 will be reserved for the system scan.
# Thanks for your patiencej


##############################################################################
                                # 7. Ending
##############################################################################

# maybe more cleanup here
exit_program()


