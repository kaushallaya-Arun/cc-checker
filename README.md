# Stripe Payment Script

This script automates the process of testing credit card payments using the Stripe API. It attempts to confirm payment intents using the provided credit card information.

## Features

- Utilizes a combo list from a file named `cc.txt`.
- Supports proxy usage for testing (optional).
- Saves working and declined credit card information to separate files.
- Uses fake user agents for requests.

## Prerequisites

- Python 3.x
- Install required packages using `pip install -r requirements.txt`.

## Usage

1. Ensure you have a file called `cc.txt` in the same folder containing your combo list.
2. Run the script by executing `python stripe_payment_script.py`.
3. Follow the prompts, and optionally input proxy details if needed.

## Note

- This script is for educational purposes only. Use it responsibly and in compliance with Stripe's terms of service.

## Author

- [@kaushallaya OR @DarkSathanHell]


