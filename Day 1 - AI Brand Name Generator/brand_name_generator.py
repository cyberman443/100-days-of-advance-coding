import openai
import keyboard
import os
from colorama import init

init()

# We're currently using api.pawan.krd server to get a free access to gpt api for free
openai.api_key = 'pk-qrGlEEYmNYnSBbNkdNBZaUFeqEGjCEyyqVilsrOAdHrYEZKo'
openai.base_url = "https://api.pawan.krd/v1/"


# These variables are for coloring the output to make the application more stylish
green = "\033[92m"
red = "\033[91m"
orange = "\033[93m"
blue = "\033[94m"
purple = "\033[95m"
reset = "\033[0m"


# This section is for requesting the openai to give a respond for the prompt which is given to
def openai_request(prompt):
    
    try:
        completion = openai.chat.completions.create(
            model="pai-001",
            messages=[
                {"role": "user", "content": prompt},
            ],
        )

        return completion.choices[0].message.content
    except Exception as e:
        print(f"\t{red}Something went wrong, please click the{reset} {blue}Space{reset} {red}button to restart the app{reset}")
        while True:
            if keyboard.is_pressed('space'):
                restart_application()
                


# This section is only for displaying the introduction part of the application
def app_init_description_print_function():
    description = f"""
    
    {orange}🌟 Brand Name Generator 🌟{reset}

    {red}Unlock your brand's potential with our AI-powered generator!{reset}
    
    ✨ Features:
    - {blue}**Keywords**:{reset} Infuse your brand with meaningful words.
    - {blue}**City Name**:{reset} Add a local flair to connect with your community.
    - {blue}**Business Type**:{reset} Tailor names to your industry for better resonance.
    - {blue}**Themes**:{reset} Convey emotions like innovation, elegance, or sustainability.
    - {blue}**Target Audience**:{reset} Align names with your ideal customers.

    {purple}Combine options or use them separately to create a unique brand identity. Let your imagination soar!{reset}
    
    """
    
    print(description)
    


    
# This section is for getting the required inputs from the user, making a prompt and then requesting 
# openai_request function to get the result of the prompt
def brandNameGenerator():
    
    try:
        # Gather user inputs, and set default values for global brands.
        keywords = input(f"\t{green}Add Comma-separated Keywords associated with your brand:{reset} ").strip() or None
        country_name = input(f"\t{green}Add your country name or hit enter if it's a global brand:{reset} ").strip() or "Global"
        city_name = input(f"\t{green}Add your city name or hit enter if it's a global brand:{reset} ").strip() or "Global"
        business_type = input(f"\t{green}Add your Comma-separated business type:{reset} ").strip() or None
        themes = input(f"\t{green}Add your Comma-separated business themes:{reset} ").strip() or None
        target_audience = input(f"\t{green}Add comma-separated target Audience for your brand:{reset} ").strip() or None

        if not keywords or not business_type or not themes or not target_audience:
            print(f"\t{red}All field except Country Name and City Name are required, please click the{reset} {blue}Space{reset} {red}button to restart the app{reset}")
            while True:
                if keyboard.is_pressed('space'):
                    restart_application()

        # Construct the prompt with clean input.
        my_prompt = f"""
        You are an expert brand strategist and creative marketer with experience in generating unique, catchy, and memorable brand names. Please generate a list of 10 highly attractive, innovative, and relevant brand name suggestions for the following business:

        - **Keywords**: {keywords}
        - **Country**: {country_name}
        - **City**: {city_name}
        - **Business Type**: {business_type}
        - **Themes**: {themes}
        - **Target Audience**: {target_audience}

        The brand names should meet the following criteria:
        - **Relevance**: The name should reflect the business type, target audience, and themes provided.
        - **Memorability**: The name should be short, easy to pronounce, and have a lasting impression.
        - **Appeal**: The name should be attractive and evoke positive emotions related to the business.
        - **Uniqueness**: Avoid generic names; the name should be distinctive and stand out from competitors in the industry.
        - **Availability**: Ideally, the name should have a domain name (e.g., .com, .co) available and be free of obvious trademark conflicts.
        - **Creativity**: Feel free to use wordplay, abstract combinations, and innovative approaches to come up with something fresh and modern.
        - **Emotion**: The name should evoke a sense of trust, innovation, luxury, or whatever best fits the brand’s essence.

        Please provide the list of brand names in a comma-separated format, along with short descriptions of why each name is a great fit for the brand, based on the inputs above.
        """
        
        print("\n")
        print(f"\t{green}==========================================={reset}")
        print(f"\t{green}You're less than a minute behind finding your beloved brand name...{reset}")
        print(f"\t{green}==========================================={reset}")
        print("\n")
        

        # Get the response from OpenAI.
        my_response = openai_request(my_prompt)
        # Split the response into individual lines
        response_lines = my_response.splitlines()
        # Loop through each line and print with a tab
        for line in response_lines:
            print("\t" + line)
        
    except Exception as e:
        print(f"\t{red}Something went wrong, please click the{reset} {blue}Space{reset} {red}button to restart the app{reset}")
        while True:
            if keyboard.is_pressed('space'):
                restart_application()



# This function gives the user the ability to click the space button and restart the application
def request_to_restart_application():
    print(f"\n\t{red}You can click the{reset} {blue}Space{reset} {red}button to restart the app:){reset}\n")
    while True:
        if keyboard.is_pressed('space'):
            restart_application()



# This function clears the shell screen
def clear_screen():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

# This function restarts the application
def restart_application():
    print(f"\t{green}Restarting your application...{reset}")
    clear_screen()
    main()





# Main section of the robot
def main():
    app_init_description_print_function()
    brandNameGenerator()
    request_to_restart_application()

# Run the main application
if __name__ == "__main__":
    main()