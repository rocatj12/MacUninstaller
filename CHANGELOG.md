# **CHANGELOG**

<br>

# Version 1.0.0
### **Functionality**

- Mode 1, 2, and 3 with various levels of intensity for removal
  - **Mode 1**
    - Searches through `/Applications/` for any items matching the item specified
  - **Mode 2**
    - Additionally searches through `~/Library/Application Support/` and `/Library/Application Support` for any items related to that specified
  - **Mode 3**
    - Very throughough scan of entire system searching recursively starting at the root directory `/`

### **Known Issues**
- (b1) If a file or directory in `~/.Trash/` matches the name of an item being deleted, it will not delete
- (b2) If an application stores its information under a different name, it will not be found
- (b3) Mode 2 will sometimes delete all contents of the cwd instead of the specified child directory
- (b4) Mode 3 is inefficient and dangerous, needs to be refined to avoid removing system files


# Version 1.0.1
### **Functionality**

- Mode 1, 2, and 3 with various levels of intensity for removal
  - **Mode 1**
    - Searches through `/Applications/` for any items matching the item specified.
  - **Mode 2**
    - Additionally searches through `~/Library/Application Support/` and `/Library/Application Support` for any items related to that specified.
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
  - 