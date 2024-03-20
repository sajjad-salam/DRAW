from time import sleep
import time
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'

import os
try:
 from cfonts import render, say
except:
 os.system('pip install python-cfonts')
def SAJ(text, delay, add_new_line=True):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    if add_new_line:
        print("\n", end="", flush=True)

output = render('SAJJAD', colors=['red', 'green'], align='center')
print(output)
SAJ(F+f"\033[1;32m\n                  『ᴍᴀᴅᴇ ʙʏ : ENG.DEV SAJJAD ™ \n                         ᴛᴇʟᴇɢʀᴀᴍ: https://t.me/S_J_O_D \n                            ᴄʜᴀɴɴᴇʟ : https://t.me/KING_OF_ENG  』", 0.07, True)
SAJ(C+f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", 0.07, True)

SAJ(X+f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", 0.07, True)