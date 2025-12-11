# Bitcoin Price Index: Implement a program that:
#       - Expects the user to specify as a command-line argument the number of
#         Bitcoins, n, that they would like to buy. If that argument cannot be
#         converted to a float, the program should exit via `sys.exit` with an
#         error message.
#       - Queries the API for the CoinCap Bitcoin Price Index at
#         https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey.
#         You should replace `YourApiKey` with the acutal API key you obtained
#         from you CoinCap account dashboard, which returns a JSON object, among
#         whose nested keys is the current price of Bitcoin as a `float`. Be
#         sure to catch any exceptions.
#       - Outputs the current cost of n Bitcoins in USD to four decimal places,
#         using `,` as a thousands separator.

import requests
import sys

from os import getenv

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    purchase_amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
else:
    api_key = getenv("COINCAP_API_KEY")
    try:
        # response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}")
    except requests.RequestException:
        sys.exit()
    else:
        # bitcoin_price = response.json()["bpi"]["USD"]["rate_float"]
        bitcoin_price = response.json()["data"]["priceUsd"]
        amount_price = float(bitcoin_price) * purchase_amount

print(f"${amount_price:,.4f}")
