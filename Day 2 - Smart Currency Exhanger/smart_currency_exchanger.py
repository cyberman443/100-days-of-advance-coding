import requests
import pyfiglet
from colorama import init, Fore, Style
import keyboard
import os
from datetime import datetime, timedelta
import sys
import time

# Initialize colorama
init(autoreset=True)


# Function for the app introduction
def intro_text():
    
    # Generate large ASCII art text using pyfiglet
    app_large_name = pyfiglet.figlet_format("Smart Currency Exchanger!", font="chunky")
    
    
# {Fore.RED}\tAs This Application is only for practicing purpose, 
# \tthus, we it only supports 10 currencies: USD, EUR, GBP, AUD, CHF, JPY, RUB, SGD, SAR, AFN{Fore.RESET}
    
    description = f"""

{Fore.YELLOW}{app_large_name}{Fore.RESET}

{Fore.RED}\tYour personal assistant for making smart and profitable currency exchange decisions!{Fore.RESET}
{Fore.GREEN}\tBased on the latest 1-week exchange rate trends, \n\twe'll help you decide which currency to exchange your base currency into, \n\tfor the best potential return on your investment.{Fore.RESET}
{Fore.BLUE}\t--------------------------------------------------
{Fore.RED}\tHow it works:{Fore.RESET}
{Fore.GREEN}\t1. You input your base currency (e.g., USD).{Fore.RESET}
{Fore.GREEN}\t2. We'll fetch the latest 1-week historical data for exchange rates.{Fore.RESET}
{Fore.GREEN}\t3. Based on trends and volatility, we provide you with our smart recommendation!{Fore.RESET}

{Fore.RED}\tDue to the fact that the API used in this applications only provides historical data for the base currency of Dollar, 
\tthus, our robot can only handle dollar base - Therefore, you should only enter [1] for Dollar, choosing your currency.
\tBut you can improve this code by subscribing to the openexchangerates.org's developer or enterprise accounts.{Fore.RESET}

{Fore.BLUE}\t--------------------------------------------------
{Fore.CYAN}\tLet's get started! 🚀{Fore.RESET}
{Fore.BLUE}\t--------------------------------------------------
"""
    print(description)



def CurrencyEchanger():
    try:
        currency = int(input(f"""
        {Fore.BLUE}[1]{Fore.RESET} for USD  \t {Fore.BLUE}[2]{Fore.RESET} for EUR  \t {Fore.BLUE}[3]{Fore.RESET} for GBP  \t {Fore.BLUE}[4]{Fore.RESET} for AUD
        {Fore.BLUE}[5]{Fore.RESET} for CHF  \t {Fore.BLUE}[6]{Fore.RESET} for JPY  \t {Fore.BLUE}[7]{Fore.RESET} for RUB  \t {Fore.BLUE}[7]{Fore.RESET} for SGD
        {Fore.BLUE}[7]{Fore.RESET} for SAR  \t {Fore.BLUE}[7]{Fore.RESET} for AFN

        {Fore.GREEN}+ Enter your currency based on the above options: {Fore.RESET}"""))
        
        if currency not in range(1, 10):
            print(f"\t{Fore.RED}You should only type numbers associated with your options [1-10], Now Please press the {Fore.RESET} {Fore.BLUE}Space{Fore.RESET} {Fore.RED}button to restart the app{Fore.RESET}")
            while True:
                if keyboard.is_pressed('space'):
                    restart_application()
    except:
        print(f"\t{Fore.RED}You should only type numbers associated with your options [1-10], Now Please press the {Fore.RESET} {Fore.BLUE}Space{Fore.RESET} {Fore.RED}button to restart the app{Fore.RESET}")
        while True:
            if keyboard.is_pressed('space'):
                restart_application()
                
    try:
        amount = float(input(f"""
        {Fore.GREEN}How much you want to put into the stick?: {Fore.RESET}"""))
    except:
        print(f"\t{Fore.RED}You should only type numbers for the amount, Now Please press the {Fore.RESET} {Fore.BLUE}Space{Fore.RESET} {Fore.RED}button to restart the app{Fore.RESET}")
        while True:
            if keyboard.is_pressed('space'):
                restart_application()
                
    
    print("\n")
    def loading_animation(text):
        for _ in range(10):  # Only run for 10 cycles
            for i in range(4):  # This will loop through 0, 1, 2, 3 dots
                sys.stdout.write(f"\r{Fore.MAGENTA}{text + '.' * i}{Fore.RESET}")  # Write text and dots
                sys.stdout.flush()  # Ensure the output is written immediately
                time.sleep(0.5)  # Delay to show the animation

    # Run the loading animation
    loading_animation(f"\tThe Result has gone to a walk, He will be here soon ")
    print("\n")
    


    app_id = "b6c3e25e7f4f4282b1fda8f7cf70b316"
    today = datetime.now()
    dates = []
    
    for i in range (1, 7):
        date = today - timedelta(days=i)
        date = date.strftime("%Y-%m-%d")
        dates.append(date)
        
        


    # Currently We can't change our base Currency due to the limitation of the free subscription,
    # However, those who love to explore more, can subscribe to a Developer, Enterprise or Unlimited Account,
    # to put their version of this app to a next level.
    
    # So, for now, Our base Currency can only be Dollar
    
    response_data = []
    
    for date in dates:
        try:
            response =  requests.get('https://openexchangerates.org/api/historical/' + date + '.json' + '?app_id=' + app_id )
            data = response.json()
            response_data.append(data['rates'])
        except:
            print(f"\t{Fore.RED}Oops! Connection could not establish with the API, Please press the {Fore.RESET} {Fore.BLUE}Space{Fore.RESET} {Fore.RED}button to restart the app{Fore.RESET}")
            while True:
                if keyboard.is_pressed('space'):
                    restart_application()
        
        
    all_currencies_and_their_rates = {}
    
    interesting_currencies = []
    
    
    for rates in response_data:
        for key, value in rates.items():
            if key not in all_currencies_and_their_rates:
                all_currencies_and_their_rates[key]=[value] 
            else:
                all_currencies_and_their_rates[key].append(value)
        
        
    top_5_growing_interest_rate = []

    for key, value in all_currencies_and_their_rates.items():
        currency = key
        peak_rate = max(value)
        bottom_rate = min(value)
        average_rate = sum(value)/len(value)
        todays_rate = value[0]
        average_growth_rate = 0
        
        
        
        if todays_rate<average_rate and peak_rate-todays_rate>todays_rate-bottom_rate:
            # Calculate the percentage change from the first day's rate to today's rate
            growth_rates = []
            
            for i in range(1, len(value)):
                previous_rate = value[i]
                current_rate = value[i-1]
                
                if current_rate>previous_rate:
                    growth_rate = (current_rate-previous_rate)/previous_rate
                    growth_rates.append(growth_rate)
                    
            if growth_rates:
                average_growth_rate = sum(growth_rates)/len(growth_rates)
        
        if average_growth_rate:
            if not average_growth_rate in top_5_growing_interest_rate:
                
                if len(top_5_growing_interest_rate)<=5:
                    top_5_growing_interest_rate.append(average_growth_rate)
                elif average_growth_rate>min(top_5_growing_interest_rate):
                    top_5_growing_interest_rate.pop(top_5_growing_interest_rate.index(min(top_5_growing_interest_rate)))
                    top_5_growing_interest_rate.append(average_growth_rate)

            possibility_of_growth = ((todays_rate - bottom_rate) / ((peak_rate - todays_rate) + (todays_rate - bottom_rate))) * average_growth_rate
            
            interesting_currencies.append(
                    {
                    "currency": currency,
                    "growing_interest_rate": average_growth_rate,
                    "current_exchange_rate": todays_rate,
                    "bottom_exchange_rate": bottom_rate,
                    "peak_exchange_rate": peak_rate,
                    "average_exchange_rate": average_rate,
                    "possiblity_of_growth": possibility_of_growth
                    },
                )
         
    top_interesting_currencies = []  
    
    
    for item in interesting_currencies:
         if item['growing_interest_rate'] in top_5_growing_interest_rate and item not in top_interesting_currencies:
             top_interesting_currencies.append(item)
    
    
    print(f"""{Fore.GREEN}
\t===========================================
\tBased on the last weeks' global exchange rates calculation, 
\tThere is a list of highly Highly Profitable Currency Exchanges with their
\tHighest Exchanges Rate, Lowest Exchange Rate, Average Exchange Rate,
\tCurrent Exchange Rate and its Highly Likely Interest Rate
\t==========================================={Fore.RESET}
""")
    
    print(f"""\t----------
{Fore.BLUE}\tYour Amount: {amount} USD Dollars{Fore.RESET}
\t----------""")
    
    print(f"""{Fore.GREEN}
\t===========================================
\tTop Highly Profitable and Highly Likely to Grow Currencies, your Amount should be Exchanged to:
\t==========================================={Fore.RESET}
""")
    
    for item in top_interesting_currencies:
        print(f"""\t{Fore.BLUE}Currency: {Fore.RESET} {item['currency']}
\t{Fore.BLUE}Money Exchanged Now: {Fore.RESET} {(item['current_exchange_rate']*amount):.7f}
\t{Fore.BLUE}Money Could Be Exchanged the Lowest this week: {Fore.RESET} {(item['bottom_exchange_rate']*amount):.7f}
\t{Fore.BLUE}Money Can Be Exchanged to the Highest: {Fore.RESET} {(item['peak_exchange_rate']*amount):.7f}
\t{Fore.BLUE}Money Can be Exchanged to the Average of: {Fore.RESET} {(item['average_exchange_rate']*amount):.7f}
\t{Fore.BLUE}Your Money's Average Growth Everyday: {Fore.RESET} {(item['growing_interest_rate']*amount):.3f}
\t{Fore.BLUE}Possibility of Growth from today till tomorrow: {Fore.RESET} {item['possiblity_of_growth']:.2f}%
""")


# This function gives the user the ability to click the space button and restart the application
def request_to_restart_application():
    print(f"\n\t{Fore.RED}You can click the{Fore.RESET} {Fore.BLUE}Space{Fore.RESET} {Fore.RED}button to restart the app:){Fore.RESET}\n")
    while True:
        if keyboard.is_pressed('space'):
            restart_application()
    

def restart_application():
    if os.name=="nt":
        os.system('cls')
    else:
        os.system('clear')
    main()

def main():
    intro_text()
    CurrencyEchanger()
    request_to_restart_application()


if __name__ == "__main__":
    main()