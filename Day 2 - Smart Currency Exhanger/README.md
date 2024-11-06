# Smart Currency Exchanger

![Smart Currency Exchanger](https://github.com/cyberman443/100-days-of-advance-coding/blob/main/screenshots/smart_currency_exchanger.PNG?raw=true)

## Overview

The **Smart Currency Exchanger** is a Python-based application that helps users make smart decisions when it comes to currency exchange. By utilizing the latest historical exchange rate data, the app evaluates the trends and volatility of different currencies and makes recommendations for optimal exchange based on predicted growth potential.

This application fetches the last week's exchange rate trends and evaluates the possible future growth of various currencies to provide the best exchange recommendation.

---

## Features

- **Currency Exchange Predictions**: Based on 1-week historical data.
- **Smart Recommendations**: Analyzes the potential growth of currencies.
- **User-friendly Interface**: Allows easy currency selection and amount entry.
- **Colorful Output**: Uses **ANSI escape sequences** to colorize the output in the terminal (Green, Red, Blue, etc.).
- **Interactive Design**: Restart the process by pressing the **spacebar**.
- **Exchange Data for 10 Currencies**: USD, EUR, GBP, AUD, CHF, JPY, RUB, SGD, SAR, AFN.

---

## Requirements

This app requires Python 3.6 or higher and the following Python libraries:

- **requests**: For fetching historical exchange rate data from OpenExchangeRates API.
- **pyfiglet**: For generating ASCII art for the application’s title.
- **colorama**: To apply colors in terminal output.
- **keyboard**: To handle keyboard inputs for restarting the app.
- **datetime**: For manipulating date ranges.
  
## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/cyberman443/100-days-of-advance-coding.git
    ```

2. **Install the required libraries**:

    ```bash
    pip install -r requirements.txt
    ```

3. **API Key Setup**:
    - You need an Open Exchange Rates API key to fetch historical exchange rate data.
    - Sign up for access at [Open Exchange Rates](https://openexchangerates.org/).
    - Replace the placeholder `app_id` in the script with your API key.

---

## Usage

### Running the Application

1. **Execute the script** by running:

    ```bash
    python smart_currency_exchanger.py
    ```

2. The application will prompt you for the following inputs in the terminal:
    - **Base Currency**: Choose from the list of available currencies (USD, EUR, GBP, etc.).
    - **Amount**: Enter the amount you wish to exchange.

3. The application will then:
    - Fetch historical data for the last 7 days of exchange rates.
    - Evaluate which currencies have the highest potential for growth.
    - Display a list of recommended currencies to exchange your base currency into.

4. **Restarting the Application**:
    - After receiving results, you can restart the app by pressing the **spacebar** on your keyboard. The screen will be cleared, and the process will start again.

---

## How it Works

1. **Currency Selection**: The app prompts the user to select a base currency (USD, EUR, GBP, etc.).
2. **Amount Input**: The user enters the amount of money to exchange.
3. **API Request**: The app fetches the last week's exchange rate data for the selected base currency.
4. **Growth Analysis**: It calculates potential growth for each currency based on historical trends.
5. **Recommendation**: The app recommends the best currencies to exchange the base currency into for the best return.

---

## Troubleshooting

1. **Error: "You should only type numbers for the amount"**
   - Ensure that the input is a valid number. If the issue persists, press the **spacebar** to restart the app.

2. **Error: "Connection could not establish with the API"**
   - Check your internet connection and verify that your API key is correct. If the issue persists, restart the app by pressing the **spacebar**.

3. **Windows Terminal Color Issues**
   - Ensure that you're using a terminal that supports ANSI escape sequences, such as **Windows Terminal** or **PowerShell**. If using **CMD**, you may need to install **colorama**:
     ```bash
     pip install colorama
     ```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or issues, feel free to open an issue on the repository.
