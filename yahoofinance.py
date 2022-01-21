import requests

url = "https://yfapi.net/v6/finance/quote"

querystring = {"symbols":"AAPL,BTC-USD,EURUSD=X"}

headers = {
    'x-api-key': "BZiD57EbwJ1dYlFDmRlZf3J1pM4GWiwT6KjXy1YQ"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
