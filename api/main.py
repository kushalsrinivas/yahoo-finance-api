from flask import Flask
import yfinance as yf

app = Flask(__name__)


@app.route('/<ticker>')
def hello_world(ticker):
    res = yf.Ticker(ticker)
    return res.info
