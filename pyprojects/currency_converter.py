import requests

def convert_currency():
    CURRENCIES = {
        "1": "USD","2": "JPY", "3": "BGN", "4": "CZK", "5": "DKK","6": "GBP","7": "HUF","8": "PLN","9": "RON","10": "SEK","11": "CHF","12": "ISK","13": "NOK","14": "TRY","15": "AUD","16": "BRL","17": "CAD","18": "CNY","19": "HKD","20": "IDR","21": "ILS","22": "INR","23": "KRW","24": "MXN","25": "MYR","26": "NZD","27": "PHP","28": "SGD","29": "THB","30": "ZAR",
    }
    for keys in CURRENCIES:
        print(f"{keys}. {CURRENCIES[keys]}")
    while True:
        try:
            base_currency = str(input("Select your base currency from the list:  "))
            target_currency = str(input("Select your target currency from the list:  "))
            amount = float(input("Enter the amount you want to convert: "))
            
            print(CURRENCIES[base_currency] + " to " + CURRENCIES[target_currency])
            response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={CURRENCIES[base_currency]}&to={CURRENCIES[target_currency]}")
            print(f"{amount} {CURRENCIES[base_currency]} is {response.json()['rates'][CURRENCIES[target_currency]]} {CURRENCIES[target_currency]}")
            break

        except KeyError and ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
    


convert_currency()