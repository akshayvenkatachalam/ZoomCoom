# ZoomCoom (not racist)
Auto login to Zoom meetings  
Joins meetings using "computer audio"  

### Dependencies
1. pyautogui
2. subprocess
3. time
4. sys
5. argparse
6. os

### Usage
1. Make sure to fill up the deafults for arguments if the program will be used repeatedly for/with the same meeting/email  
2. #### **FILL UP DEFAULT FOR ZOOM.EXE IN THE WINDOWS FORMAT**
3. Required arguments (if defaults not filled):  
  -h, --help            show this help message and exit  
  -e EMAIL, --email EMAIL      email id  
  -m MEET, --meet MEET         meeting id  
  -p PWD, --pwd PWD            meeting password  
  -ep EPWD, --epwd EPWD        zoom user password  
  -exe EXELOC, --exeloc EXELOC zoom exe location

### Example
> python zoomcoom_not_racist.py -m 12345678900 -p password -e e@mail.com -ep hackmepls -exe "C:\\\GarbageUser\\\Zoom.exe"

Feel free to change the name of the program file, but I suggest you let it remain, for tradition's sake
