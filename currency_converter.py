import requests
import json
import os
from datetime import datetime

API_URL = "https://api.exchangerate-api.com/v4/latest"
CACHE_FILE = "currency_cache.json"

# load cache if exists
def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

# save cache to file
def save_cache(data):
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f)

# fetch exchange rates
def fetch_exchange_rates(amount, from_currency, to_currency):
    try:
        url = f"{API_URL}/{from_currency}"
        res = requests.get(url)
        data = res.json()

        if "rates" in data and to_currency in data["rates"]:
            rate = data["rates"][to_currency]
            result = amount * rate

            # save to cache
            cache = load_cache()
            if from_currency not in cache:
                cache[from_currency] = {}
            cache[from_currency][to_currency] = rate
            save_cache(cache)

            return result, rate, "live"
    except:
        return None, None, None

    return None, None, None

# offline fallback
def offline_fallback(amount, from_currency, to_currency):
    cache = load_cache()
    rate = cache.get(from_currency, {}).get(to_currency)
    if rate:
        return amount * rate, rate, "offline"
    return None, None, None

# swap currencies
def swap_currencies(from_currency, to_currency):
    return to_currency, from_currency

# main program
def main():
    print("---- Python Currency Converter -----")
    from_currency = input("From currency (e.g., USD): ").upper()
    to_currency = input("To currency (e.g., EUR): ").upper()
    amount = input("Amount to convert: ")

    try:
        amount = float(amount)
        if amount <= 0:
            print("Amount must be a positive number")
            return
    except:
        print("Invalid amount")
        return

    # try live API
    result, rate, source = fetch_exchange_rates(amount, from_currency, to_currency)

    if result is None:
        print("Unable to fetch live data. Trying offline cache...")
        result, rate, source = offline_fallback(amount, from_currency, to_currency)

    if result is not None:
        print(f"Conversion rate ({source}): 1 {from_currency} = {rate} {to_currency}")
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
        print(f"Last updated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("Conversion rate not found in cache.")

    # optional swap demo
    swap_demo = input("\nDo you want to swap currencies and convert again? (y/n): ").lower()
    if swap_demo == "y":
        from_currency, to_currency = swap_currencies(from_currency, to_currency)
        print(f"Swapped: From {from_currency} to {to_currency}")
        result, rate, source = fetch_exchange_rates(amount, from_currency, to_currency)
        if result:
            print(f"Conversion rate ({source}): 1 {from_currency} = {rate} {to_currency}")
            print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

if __name__ == "__main__":
    main()

