from flask import Flask
import yfinance as yf

app = Flask(__name__)


@app.route('/<ticker>')
def hello_world(ticker):
    res = yf.Ticker(ticker)
    return res.info


@app.route("/history/<ticker>")
def get_history(ticker):
    stock = yf.Ticker(ticker)
    df = stock.history(period="1mo")
    jsonData = {}
    for index, date in enumerate(df.index):
        jsonData[str(date).split(' ')[0]] = {}
        for col in df.columns:
            jsonData[str(date).split(' ')[0]][col] = df.loc[date][col]
    return jsonData