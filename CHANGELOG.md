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
- (b3) Mode 3 is inefficient and dangerous, needs to be refined to avoid removing system files


