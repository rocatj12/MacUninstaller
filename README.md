# MacUninstaller
___
#### Completely remove applications and the files they leave behind
##### Built on Python 2.7 to take advantage of the built in Python language in MacOS

<br>

## Starting the Terminal
________________________
1. Open **Launchpad** from the Dock, click on **Utilities**, then **Terminal**
1. Press COMMAND + SPACE to launch Spotlight, search for **Terminal**

You will be faced with something that looks a little like this:

``` 
user@Mac~ $
```

<br>

## Usage
________
```
# python MacUninstaller.py -a <APPLICATION NAME> -m <MODE>
```
Similarly...
```
$ sudo python MacUninstaller.py -a APPLICATION NAME> -m <MODE>
```
**Flags:**
|short|long|desctiption
|---|---|---|
| `-h` | `--help` | Show this help message|
| `-a` | `--application` | Name of application (as it appears in "/Applications/", without the ".app:")|
| `-m` | `--mode` | Intensity of Scan [ 1:Light, (2):Standard, 3:Intense]|

<br>

## Privilage Escalation
_______________________ 
### **Using `sudo`**
Some of the files that will potentially be removed are in protected directories, user password will be required at various stages throughout the process

To circumvent this, privilage escalation is recommended

**Most Macintoshes will have root user disabled and it is advised to leave it alone**

It is recommended to simply stay in the user account and proceed command with `sudo` and enter the users password

If prompted with the following message, proceed with accepting the risk and/or running the program again
```
We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:
 
     #1) Respect the privacy of others.
     #2) Think before you type.
     #3) With great power comes great responsibility.
```

<br><br>
### **Enabling Root User**
If using the root account is required, follow these steps to enable and use it.

- Go to `System Preferences` > `Users & Groups`
- Click the lock button in the lower left and enter the user's password
- Click on `Login Options`
- Click on `Join...` next to "Network Account Server"
- Click on `Open Directory Utility...`
- Click on the lock in the lower left of the "Directory Utility" window and enter user's password
- From the "Directory Utility" menu at the top of the screen
  - Go to `Edit` > `Enable Root User` and enter the new root password - **Remember This!!** (Toggle On) --The socially accepted default password for root accounts is "toor" ("root" backwards)
  - Or Choose `Edit` > `Disable Root User` (Toggle Off)

Again, it is advised to disable the root user when done

Source: [Apple](https://support.apple.com/en-us/HT204012)

<br>

To escalate to the root user, type
```
$ su
```
Then enter the password you created for the root account

You should then be prompted with something like 
```
root@Mac~ #
```
Run the program as specified above

<br>


> Notes:
> - Everything that is removed is only put into Trash Can, not completely removed, in case something goes wrong and needs to be put back
> - View [CHANGELOG.md](CHANGELOG.md) to see known issues and additional information

<br>

> - **Please report all bugs and issues to roca.dvlpr@gmail.com or on the GitHub project**
>   - Please keep in mind this was a side project created by myself so issues may or may not be resolved quickly