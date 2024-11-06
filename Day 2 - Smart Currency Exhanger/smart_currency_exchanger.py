import requests
import pyfiglet
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)


# Function for the app introduction
def intro_text():
    
    # Generate large ASCII art text using pyfiglet
    app_large_name = pyfiglet.figlet_format("Smart Currency Exchanger!", font="chunky")
    
    
    description = f"""

{Fore.YELLOW}{app_large_name}{Fore.RESET}

{Fore.RED}\tYour personal assistant for making smart and profitable currency exchange decisions!{Fore.RESET}
{Fore.GREEN}\tBased on the latest 1-week exchange rate trends, \n\twe'll help you decide which currency to exchange your base currency into, \n\tfor the best potential return on your investment.{Fore.RESET}
{Fore.BLUE}\t--------------------------------------------------
{Fore.RED}\tHow it works:{Fore.RESET}
{Fore.GREEN}\t1. You input your base currency (e.g., USD).{Fore.RESET}
{Fore.GREEN}\t2. We'll fetch the latest 1-week historical data for exchange rates.{Fore.RESET}
{Fore.GREEN}\t3. Based on trends and volatility, we provide you with our smart recommendation!{Fore.RESET}
{Fore.BLUE}\t--------------------------------------------------
{Fore.CYAN}\tLet's get started! 🚀{Fore.RESET}
{Fore.BLUE}\t******************************************
"""
    print(description)

# Call the function to display the introductory message
intro_text()



# app_id = "b6c3e25e7f4f4282b1fda8f7cf70b316"
# date = "2010-10-10"

# response =  requests.get('https://openexchangerates.org/api/historical/' + date + '.json' + '?app_id=' + app_id )

# data = response.json()

# print(data)
