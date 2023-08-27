# IMPORTANT LEGAL DISCLAIMER

Yahoo!, Y!Finance, and Yahoo! finance are registered trademarks of Yahoo, Inc.

this is not affiliated, endorsed, or vetted by Yahoo, Inc. It's an open-source tool that uses Yahoo's publicly available APIs, and is intended for research and educational purposes.

You should refer to Yahoo!'s terms of use (here, here, and here) for details on your rights to use the actual data downloaded. Remember - the Yahoo! finance API is intended for personal use only.

# Yahoo Finance API Documentation

The Yahoo Finance API provides a simple way to fetch company information using their ticker symbols. This API utilizes the `yfinance` Python module to fetch data from Yahoo Finance. You can use the following endpoints to retrieve information about a specific company.

**Base URL**: `https://yahoo-finance-o4q4dihi1-kushalsrinivas.vercel.app/`

## Endpoints

## Get Company Information

Retrieve detailed information about a company using its ticker symbol.

- **Endpoint**: `/{ticker}`
- **Method**: GET
- **Parameters**:
  - `{ticker}`: The ticker symbol of the company you want to fetch information about.
- **Example**: `/TSLA`

#### Response Format

```json
{
  "52WeekChange": -0.16231304,
  "SandP52WeekChange": 0.09306288,
  "address1": "1 Tesla Road",
  "ask": 239.19,
  "askSize": 900,
  "auditRisk": 8,
  // ... (other fields)
  "trailingPE": 65.36712,
  "trailingPegRatio": 2.6832,
  "twoHundredDayAverage": 197.05995,
  "underlyingSymbol": "TSLA",
  "uuid": "ec367bc4-f92c-397c-ac81-bf7b43cffaf7",
  "volume": 105274610,
  "website": "https://www.tesla.com",
  "zip": "78725"
}
```

### Response Fields

- `52WeekChange`: Change in stock price over the last 52 weeks.
- `SandP52WeekChange`: Change in S&P 500 index over the last 52 weeks.
- `address1`: Company's address.
- `ask`: Current ask price.
- `askSize`: Size of the ask.
- ... (other fields, similar to the provided example)

## Get Historical Data

Retrieve historical data for a company using its ticker symbol for the past one month.

- **Endpoint**: `/history/{ticker}`
- **Method**: GET
- **Parameters**:
  - `{ticker}`: The ticker symbol of the company for which you want to fetch historical data.
- **Example**: `/history/MSFT`

#### Response Format

```json
{
  "2023-07-26": {
    "Close": 337.0563659667969,
    "Dividends": 0,
    "High": 343.94181236443984,
    "Low": 332.4062077205621,
    "Open": 340.71862557906644,
    "Stock Splits": 0,
    "Volume": 58383700
  },
  "2023-07-27": {
    "Close": 330.0212707519531,
    "Dividends": 0,
    "High": 340.6088397996611,
    "Low": 328.35478565410773,
    "Open": 339.7606600042334,
    "Stock Splits": 0,
    "Volume": 39635300
  },
  // ...

  "2023-08-24": {
    "Close": 319.9700012207031,
    "Dividends": 0,
    "High": 332.9800109863281,
    "Low": 319.9599914550781,
    "Open": 332.8500061035156,
    "Stock Splits": 0,
    "Volume": 23281400
  },
  "2023-08-25": {
    "Close": 322.9800109863281,
    "Dividends": 0,
    "High": 325.3599853515625,
    "Low": 318.79998779296875,
    "Open": 321.4700012207031,
    "Stock Splits": 0,
    "Volume": 21671400
  }
}
```

### Response Fields

The response for the historical data endpoint includes fields such as:

- `Close`: Closing price for the specified date.
- `Dividends`: Dividend amount on the specified date.
- `High`: Highest price during the specified date.
- `Low`: Lowest price during the specified date.
- `Open`: Opening price for the specified date.
- `Stock Splits`: Stock splits on the specified date.
- `Volume`: Volume of trades on the specified date.

## Examples

### Python Code Example

```python
import requests

base_url = "https://yahoo-finance-o4q4dihi1-kushalsrinivas.vercel.app/"
ticker = "TSLA"
endpoint = f"/{ticker}"
url = f"{base_url}{endpoint}"

response = requests.get(url)
data = response.json()

print(data)
```

## Note

This API uses the `yfinance` module to fetch data from Yahoo Finance. Make sure to handle errors and exceptions appropriately in your code when making requests to the API.
