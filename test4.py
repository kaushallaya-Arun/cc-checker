art = """

░█▀▀░█▀▀░░░█▀▀░█░█░█▀▀░█▀▀░█░█░█▀▀░█▀▄░░
░█░░░█░░░░░█░░░█▀█░█▀▀░█░░░█▀▄░█▀▀░█▀▄░░
░▀▀▀░▀▀▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░░
            by https://t.me/DarkSathanHell 
            Contact me if you want more script

"""
  
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script

import requests    
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
import urllib3
from urllib3.exceptions import InsecureRequestWarning    
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
from fake_useragent import UserAgent


# Disable SSL warnings
urllib3.disable_warnings(InsecureRequestWarning)

ua03 = UserAgent()
random_user_agent03 = ua03.random    
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script

head1={    
 'user-agent': random_user_agent03,
 'Pragma':'no-cache',
 'Accept':'*/*',
 }
response1 = requests.get('https://randomuser.me/api?results=1&gender=&password=upper,lower,12&exc=register,picture,id&nat=US',headers=head1).json()

for x in response1['results']:
    name=x['name']['first']       
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
    second=x['name']['last']     
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
    email=(name+second+'@outlook.com').lower()
    


    
