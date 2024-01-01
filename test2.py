art = """

░█▀▀░█▀▀░░░█▀▀░█░█░█▀▀░█▀▀░█░█░█▀▀░█▀▄░░
░█░░░█░░░░░█░░░█▀█░█▀▀░█░░░█▀▄░█▀▀░█▀▄░░
░▀▀▀░▀▀▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░░
            by https://t.me/DarkSathanHell 
            Contact me if you want more script

"""


import requests
import urllib3    
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
from urllib3.exceptions import InsecureRequestWarning    
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
from fake_useragent import UserAgent

ua01 = UserAgent()
random_user_agent01 = ua01.random

urllib3.disable_warnings(InsecureRequestWarning)



url = "https://m.stripe.com/6"

headers = {
    "authority": "m.stripe.com",
    "method": "POST",
    "path": "/6",
    "scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.6",
    "content-length": "1440",
    "content-type": "text/plain;charset=UTF-8",
    "cookie": "m=4a223862-84e6-4db8-9ed9-958457d58378915d4c",
    "origin": "https://m.stripe.network",
    "referer": "https://m.stripe.network/",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="110", "Brave";v="110"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "sec-gpc": "1",
    "user-agent": random_user_agent01,
}

payload = {
    "JTdCJTIydjIlMjIlM0ExJTJDJTIyaWQlMjIlM0ElMjI4YWY2OGZjNzRiY2E1NDNiNTRjMzZlZDc2ZmJhODA1MCUyMiUyQyUyMnQlMjIlM0E0MiUyQyUyMnRhZyUyMiUzQSUyMjQuNS40MyUyMiUyQyUyMnNyYyUyMiUzQSUyMmpzJTIyJTJDJTIyYSUyMiUzQW51bGwlMkMlMjJiJTIyJTNBJTdCJTIyYSUyMiUzQSUyMiUyMiUyQyUyMmIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRlhXLS1DalE2QVJJcnR3S2tVZERPVDZfRWxLRUFIdENDNU9ubXRWemxmbE0uQy0yTlVHVk8wdF9SZHNRbVB3TXBPX3pBNkZtWDlXcUdsSlJMSmlOTU5ITS5MVHpKSzBrejMtVFIyLVpVUkN0eFgxem8zcFRsMExQWE55ZWNqQk51MzZVLmlEb1BkOEJVdWFfMXJkcEtwQUVOekEtQnVuWGg1NVhETkM4aThBcG5pa28lMkZmbFc2VFlPSkNoRjU0SEdPWjYzOG5iVllxRXYzRXpIanptbnRQRW9XZGRnJTNGcy04bFlSZFVGT0VzN1hTcUlSWHNiNDNtMlFZSnVKY1FsQmM0UzlubldROCUzRHNXZkxHTHQtV090aUptdnJ2S2twOG92N0hMQ3JMUW5vY0JEclN0SXF0Y1ElMjZXaXREU3o5VUZucUhlbXdZZHMxTHp2dFpSeEVNTWtaUUl1VzBGVHpnZTJFJTNEUzRUT3hwLWZaM0RqN01RdU1wTWJzY08zZ2Jmcmo3NlBSRERyS0ZMN2Q1QSUyMiUyQyUyMmMlMjIlM0ElMjI0ZlNEM3QxdGY5X3A3QXhFcDNtdVJpOGtUbUNaN3J0RVhxZzhyZ2tnX3MwJTIyJTJDJTIyZCUyMiUzQSUyMjNhZGQ5ODNmLTZlODAtNGUxNi1iMjM1LTlhYzkyZGYzYmVmMjc5ZjdjMiUyMiUyQyUyMmUlMjIlM0ElMjJOQSUyMiUyQyUyMmYlMjIlM0FmYWxzZSUyQyUyMmclMjIlM0F0cnVlJTJDJTIyaCUyMiUzQXRydWUlMkMlMjJpJTIyJTNBJTVCJTIybG9jYXRpb24lMjIlNUQlMkMlMjJqJTIyJTNBJTVCJTVEJTJDJTIybiUyMiUzQTEwMzklMkMlMjJ1JTIyJTNBJTIyc2VjdXJlLm5oc2NoYXJpdGllc3RvZ2V0aGVyLmNvLnVrJTIyJTJDJTIydyUyMiUzQSUyMjE3MDQwMTE2ODU5ODMlM0EzMjllYmNlNDNlZWEzMWU1YzZkMDYxZTE5MjFkNzcyYjllNDA5MzI0ZjVkMTM3MTZiYzA2NWM5MWZiMDgyMWQzJTIyJTdEJTJDJTIyaCUyMiUzQSUyMmI2OTMxNjBkZGU5NzQzZjI2NDgyJTIyJTdE"
}

response = requests.post(url, headers=headers, data=payload, verify=False)

extract = response.json()
   
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
muid = extract.get('muid')    
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
guid =  extract.get('guid')
sid = extract.get('sid')   
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script   

# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script


