# Brand Name Generator

![alt text](https://github.com/cyberman443/100-days-of-advance-coding/blob/main/screenshots/ai_brand_name_generator.PNG?raw=true)

## Overview

The **Brand Name Generator** is a Python-based application powered by OpenAI's GPT-3 model to help users generate creative, catchy, and unique brand names based on their input. The application takes key information from the user, such as **keywords**, **business type**, **themes**, **target audience**, and **location**, and then generates a list of highly relevant brand names along with explanations of why each name is a good fit.

The app is designed to be interactive, colorful, and easy to use, with output displayed in a visually appealing format using **ANSI escape sequences** for color.

---

## Features

- **AI-powered brand name generation** based on user input.
- **Customizable inputs** for:
  - **Keywords** associated with your brand.
  - **Location** (country and city name).
  - **Business type** (e.g., e-commerce, lifestyle, etc.).
  - **Themes** (e.g., minimalism, luxury, etc.).
  - **Target audience** (e.g., millennials, eco-conscious consumers).
- **Colorful output** using ANSI escape sequences (Green, Red, Orange, Blue, etc.).
- **Interactive design** with spacebar restart functionality.
- **Error handling** that prompts the user to restart the application if needed.

---

## Requirements

- Python 3.6 or higher.
- The following Python libraries:
  - **openai**: To interact with OpenAI's GPT-3 API.
  - **keyboard**: To handle user input from the keyboard (spacebar to restart).
  - **colorama**: To provide colored output in the terminal.

---

## Installation

1. **Clone all the 100 Days of Advanced Coding repository and go to "Day 1 - AI Brand Name Generator"** or download the script:

    ```bash
    git clone https://github.com/cyberman443/100-days-of-advance-coding.git
    ```

2. **Install the required libraries**:

    ```bash
    pip install openai keyboard colorama
    ```

3. **API Key Setup**:
    - Sign up for access to OpenAI’s API at [OpenAI](https://openai.com/).
    - Replace the placeholder in the script with your own OpenAI API key:
      ```python
      openai.api_key = 'your-api-key-here'
      ```

---

## Usage

### Running the Application

1. **Execute the script** by running:

    ```bash
    python brand_name_generator.py
    ```

2. The program will prompt you for input in the terminal:
    - **Keywords**: Comma-separated list of words associated with your brand.
    - **Country Name**: The country of your brand, or "Global" if it's a global brand.
    - **City Name**: Your city or "Global" if no specific city is associated.
    - **Business Type**: The type of business (e.g., e-commerce, technology, etc.).
    - **Themes**: The themes associated with your brand (e.g., luxury, minimalism, eco-friendly).
    - **Target Audience**: A comma-separated list of the target audience (e.g., millennials, tech enthusiasts, etc.).

3. The application will then generate 10 brand name suggestions based on your input. Each name will be followed by an explanation of why it’s a good fit for your brand.

4. **Spacebar Restart**:
    - If you want to restart the application, press the **spacebar** on your keyboard. This will clear the screen and run the process again.

---

## Features in Detail

### Colorful Output

The application uses **ANSI escape sequences** to display the following colors:

- **Green**: For headings, prompts, and key information.
- **Red**: For error messages and alerts.
- **Orange**: For highlighting important features.
- **Blue**: For general information and instructions.
- **Purple**: For additional motivational or creative prompts.

### Error Handling

- If an error occurs (such as an issue with the OpenAI API), a friendly error message is displayed in **Red**. The user is then prompted to press the **spacebar** to restart the application.

### Restart Functionality

- If the user wants to restart the app (for example, after receiving results), they can simply press the **spacebar** on the keyboard. The application will clear the terminal screen and begin the process again.

---

## Troubleshooting

1. **Error: "Something went wrong, please click the Space button to restart the app"**
   - This could happen if the OpenAI API request fails. Ensure you have an active internet connection and a valid API key. If the issue persists, try restarting the app using the **spacebar**.

2. **Color not displaying in CMD or PowerShell on Windows**
   - Ensure you are using a terminal that supports ANSI escape sequences. For **Windows**, you may need to use **Windows Terminal** or install the **`colorama`** library for compatibility with **CMD** and **PowerShell**.
   - Install `colorama` using: 
     ```bash
     pip install colorama
     ```

3. **Keyboard input not working**
   - Make sure you are running the script with appropriate permissions. The `keyboard` library requires administrator permissions on Windows to detect key presses.

---

## Code Structure

### Main Components:

1. **`openai_request()`**:
   - Sends a request to the OpenAI API with a generated prompt and returns the response.
   
2. **`app_init_description_print_function()`**:
   - Prints an introductory description of the application, including features and instructions.

3. **`brandNameGenerator()`**:
   - Collects user input for the brand name generation.
   - Constructs a detailed prompt and sends it to the OpenAI API.
   
4. **`request_to_restart_application()`**:
   - Handles the restart mechanism, prompting the user to restart by pressing the **spacebar**.

5. **`clear_screen()`**:
   - Clears the terminal screen (works across different operating systems).

6. **`restart_application()`**:
   - Restarts the application by calling the main function after clearing the screen.

### Dependencies:
- **`openai`**: Interacts with the OpenAI API for brand name generation.
- **`keyboard`**: Detects keyboard input (spacebar for restart).
- **`colorama`**: Provides support for colored terminal output.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or issues, feel free to open an issue on the repository.
