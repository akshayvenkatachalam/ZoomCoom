import pyautogui as pepe
import subprocess
import time
import sys
import argparse
import os

#PLEASE FILL IN DEFAULTS IF REQUIRED 
os.system("TASKKILL /F /IM Zoom.exe")
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--email", help = "email", type = str, default = 'PLEASE FILL')
parser.add_argument("-m", "--meet", help = "meeting id", type = str, default = 'PLEASE FILL')
parser.add_argument("-p", "--pwd", help = "meeting password", type = str, default = 'PLEASE FILL')
parser.add_argument("-ep", "--epwd", help = "email password", type = str, default = 'PLEASE FILL')
parser.add_argument("-exe", "--exeloc", help = "zoom exe location", type = str, default = 'PLEASE FILL')
args = parser.parse_args()
subprocess.Popen(args.exeloc)

def cooming(meet, pwd, email, epwd):
	time.sleep(5)
	#find join button if available
	if pepe.locateCenterOnScreen('images/join.png') is not None:
		centre = list(pepe.locateCenterOnScreen('images/join.png'))
		pepe.click(x = centre[0], y = centre[1])
		time.sleep(2)
		pepe.typewrite(meet)
		centre = pepe.locateCenterOnScreen('images/join_flat.png')
		pepe.click(x = centre[0], y = centre[1])
		time.sleep(2)
		pepe.typewrite(pwd)
		centre = pepe.locateCenterOnScreen('images/join_meet.png')
		pepe.click(x = centre[0], y = centre[1])
	else:# pepe.locateCenterOnScreen('images/sign_in.png') is not None:
		centre = list(pepe.locateCenterOnScreen('images/sign_in.png'))
		pepe.click(x = centre[0], y = centre[1])
		time.sleep(2)
		pepe.typewrite(email)
		pepe.typewrite(['tab'])
		pepe.typewrite(epwd)
		centre = list(pepe.locateCenterOnScreen('images/sign_in_blue.png'))
		pepe.click(x = centre[0], y = centre[1])
		cooming()
	
if __name__ == '__main__':
	while True:
		try:
			cooming(args.meet, args.pwd, args.email, args.epwd)
			break
		except TypeError:
			print("Program is not work")
			os.system("TASKKILL /F /IM Zoom.exe")
			sys.exit()

