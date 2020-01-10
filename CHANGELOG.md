# **CHANGELOG**

<br>

# Version 0.0.5
### **Functionality**

- Mode 1, 2 with various levels of intensity for removal
  - **Mode 1**
    - Searches through `/Applications/` for any items matching the item specified
  - **Mode 2**
    - Additionally searches through `~/Library/Application Support/` and `/Library/Application Support` for any items related to that specified

### **Known Issues**
- (b1) If a file or directory in `~/.Trash/` matches the name of an item being deleted, it will not delete
- (b2) If an application stores its information under a different name, it will not be found
- (b3) Mode 2 will sometimes delete all contents of the cwd instead of the specified child directory
- (b4) Mode 3 is inefficient and dangerous, needs to be refined to avoid removing system files


# Version 0.0.6
### **Functionality**

- Mode 1, 2, 3 with various levels of intensity for removal
  - **Mode 1**
    - Searches through `/Applications/` for any items matching the item specified
  - **Mode 2**
    - Additionally searches through `~/Library/Application Support/` and `/Library/Application Support` for any items related to that specified
    - Searches through `~/Library/LaunchAgents` and `/Library/LaunchAgents`
  - **Mode 3**
    - *tbd*

### **Other Changes**
- Changed README.md for better practices to run and operate the program
- Rewriting the delete() function to work better with items that are already in `~/.Trash`
- Replacing some instances of `for item in glob.glob():` with `for item in os.listdir()`

### **Resolved Issues**
- (b1) If a file or directory in `~/.Trash` matches the name of an item being deleted, it will not delete
  - **Resolution** Check if the current file being deleted already exists in `~/.Trash`, remove that first, then continue deleting the one specified


# Version 0.0.7
### **Functionality**

- Mode 1, 2, 3 with various levels of intensity for removal
  - **Mode 1**
    - Searches through `/Applications/` for any items matching the item specified
  - **Mode 2**
    - Additionally searches through `~/Library/Application Support/` and `/Library/Application Support` for any items related to that specified
    - Searches through `~/Library/LaunchAgents` and `/Library/LaunchAgents`
  - **Mode 3**
    - *tbd*

### **Other Changes**
- Modified version numbers to accurately represent progress
- Added new option '--user' to specify a user account to search and scan through
- Changes to README.md
- Modifying the delete() function to work better
- Error logging
- Altering how program reads input and compares to items found in OS for removal to work better

### **Resolved Issues**
- Program does not run successfully in wide variety of uses
  - **Resolution** Corrected the improper comparison between application specified and items in OS
  - **Resolution** Altered the way that the program deletes files and directories due to Python not working with the `~/.Trash` directory
  - **Resolution** Other minor changes
- Mode flag and value not being read and compared properly by program causing in an exit() call


# Version 0.0.8
### **Functionality**

- Mode 1, 2, 3 with various levels of intensity for removal
  - **Mode 1**
    - Searches through `/Applications/` for any items matching the item specified
  - **Mode 2**
    - Additionally searches through `~/Library/Application Support/` and `/Library/Application Support` for any items related to that specified
    - Searches through `~/Library/LaunchAgents` and `/Library/LaunchAgents`
    - Searches through `~/Library/Application Scripts/`
  - **Mode 3**
    - *tbd*

### **Other Changes**


### **Resolved Issues**
- Program fails on execution due to missing build dependency
  - **Resolution** Leaving out the Send2Trash dependency and using calls from the `os` module instead