import requests
import os
import dotenv

dotenv.load_dotenv()

# Environment Variables
URL = "https://api.currencyapi.com/v3/latest"
API_KEY = os.getenv("CURRENCY_API_KEY")

# Get Currency Exchange Rate
def get_currency_exchange_rate(from_currency, to_currency):
    response = requests.get(f"{URL}?apikey={API_KEY}&base_currency={from_currency}&currencies={to_currency}")
    response.raise_for_status()
    data = response.json()
    return data["data"][to_currency]["value"]

# Main Function
def main():
    from_currency = input("Enter the source currency (e.g., USD): ").upper()
    to_currency = input("Enter the target currency (e.g., EUR): ").upper()
    amount = float(input("Enter the amount to convert: "))
    
    try:
        exchange_rate = get_currency_exchange_rate(from_currency, to_currency)
        print(f"Current: 1 {from_currency} = {exchange_rate} {to_currency}")
        print(f"{amount} {from_currency} = {amount * exchange_rate} {to_currency}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching currency data: {e}")
    except KeyError:
        print("Invalid currency code. Please try again.")
        
main()