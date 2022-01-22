import requests
import streamlit as st
import yfinance as yf
#z = dir(yf)

#url = "https://yfapi.net/v6/finance/quote"
#url = "https://yfapi.net/v6/finance/quote/marketSummary?lang=en&region=US"

#querystring = {"symbols":"AAPL,BTC-USD,EURUSD=X"}

#headers = {
#    'x-api-key': "BZiD57EbwJ1dYlFDmRlZf3J1pM4GWiwT6KjXy1YQ" \
#     'accept: application/json' 
#    }

#response = requests.request("GET", url, headers=headers)

#print(response.text)
#st.write(z)
msft = yf.Ticker("MSFT")
st.write(msft.info)
