# import libraries
import requests
import json
import os
from datetime import datetime


# set API key and cache file name
API_URL = "https://api.exchangerate-api.com/v4/latest"
CACHE_FILE = "currency_cache.json"


# load cache if exists
def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

# save cache 
def save_cache(data):
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f)


# get exchange rate from API or cache

def get_exchange_rate(amount, from_currency, to_currency):
    try:
        # fetch cache
        url = f"{API_URL}/{from_currency}"
        response = requests.get(url=url)
        data = response.json()

        if "rates" in data and to_currency in data["rates"]:
            rate = data["rates"][to_currency]
            converted_amount = amount * rate

            # save to cache
            cache = load_cache()
            if from_currency not in cache:
                cache[from_currency] = {}
                cache[from_currency][to_currency] = rate
                save_cache(cache)

                return converted_amount , rate , "Live"
    
    except:
        return None , None, None
    return None, None, None


# offline fallback to cache
def offline_fallback(amount, from_currency, to_currency):
    cache = load_cache()
    rate = cache.get(from_currency, {}).get(to_currency)

    if rate:
        return amount * rate, rate, "offline"
    return None, None, None

# swap currencies
def swap_currencies(from_currency, to_currency):
    return to_currency, from_currency


# main function
def main():

    print("----Python Currency Converter----")
    from_currency = input("Enter the base currency (e.g., USD)").upper()
    to_currency = input("Enter the target currency (e.g., EUR)").upper()
    amount = float(input("Amount to convert: "))

    try:
        if amount <= 0:
            print("Amount must be a positive number")
            return
    except: 
        print("Invalid amount")
        return
    
    # try to get Live rate
    converted_amount, rate, source = get_exchange_rate(amount, from_currency, to_currency)

    if converted_amount is None:
        # fallbck to offline cache
        converted_amount, rate, source = offline_fallback(amount, from_currency, to_currency)
        print("Unable to fetch live rates. Trying offline cache...")

    if converted_amount is not None:
        print(f'Conversion Rate: 1 {from_currency} = {rate} {to_currency} ({source})')
        print(f"{amount} {from_currency} = {converted_amount : .2f} {to_currency}")
        print(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
    else:
        print("Conversion rate not found in cache. Please check your currency codes or try again later")

    # option to swap currencies
    swap_demo = input("\n Do you want to swap currencies and convert again? (yes/no): ").lower()

    if swap_demo == "yes":
        from_currency, to_currency = swap_currencies(from_currency, to_currency)

        print(f"\n Swapped currencies: {from_currency} to {to_currency}")
        converted_amount, rate, source = get_exchange_rate(amount, from_currency, to_currency)

        if converted_amount:
            print(f'Conversion Rate : 1 {from_currency} = {rate} {to_currency} ({source})')
            print(f"{amount} {from_currency} = {converted_amount : .2f} {to_currency}")


if __name__ == "__main__":
    main()