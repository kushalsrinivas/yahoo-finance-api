

# Yahoo Finance API Documentation

The Yahoo Finance API provides a simple way to fetch company information using their ticker symbols. This API utilizes the `yfinance` Python module to fetch data from Yahoo Finance. You can use the following endpoints to retrieve information about a specific company.

**Base URL**: `https://yahoo-finance-o4q4dihi1-kushalsrinivas.vercel.app/`

## Endpoints

### Get Company Information

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


