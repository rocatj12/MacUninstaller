# MacUninstaller
___
##### Completely remove applications and the files they leave behind

<br>

## Starting the Terminal
________________________
1. Open **Launchpad** from the Dock, click on **Utilities**, then **Terminal**
1. Press COMMAND + SPACE to launch Spotlight, search for **Terminal**

You will be faced with something that looks a little like this:

``` 
$
```

<br>

## Usage
________
```
$ python MacUninstaller.py -a <APPLICATION NAME> -m <MODE>
```
Flags:
|short|long|desctiption
|---|---|---|
| `-h` | `--help` | Show this help message|
| `-a` | `--application` | Name of application (as it appears in "/Applications/")
| `-m` | `--mode` | Intensity of removal (1-3)

<br>

## Privilage Escalation
_______________________ 
Because some of the directories that will be modified/removed are protected, user password may be required at various stages in program execution

**Most Macintoshes will have root user disabled and it is advised to leave it alone**

However, if root user is enabled, and password is available, enter in the terminal prior to running MacUninstaller:
```
$ sudo su
```
It may or may not prompt for a password, so respond accordingly

Additionally, instructions to enable the root user can be found at https://support.apple.com/en-us/HT204012

Check the user on the terminal prompt. it may have, for example, changed from 

this
```
username@MacBookPro $
```
to this
```
root@MacBookPro #
```
Once you are in the root shell, run the program to avoid various password prompts

> Notes:
> - Everything that is removed is only put into Trash Can, not completely removed, in case something goes wrong and needs to be put back

- Known issues
  - If another file/directory with the same name as something being deleted is already in the trash can, it will not be deleted
  - If the applications stores its data under different/abbreviated name, it will not be found
  - Mode 3 needs to be refined to exclude system directories and files