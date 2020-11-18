import yfinance as yf
import pypfopt
from pypfopt import (
    risk_models,
    expected_returns,
    EfficientFrontier
)


# correlations = {
#     "UKX": {"UKX":1, "DAX":0.894, "SPX":0.665, "SHSZ30":0.332, "AS51":0.532, "XAU":0.036, "LUATTR":-0.358},
#     "DAX": {"UKX":0.894, "DAX":1, "SPX":0.680, "SHSZ30":0.343, "AS51":0.501, "XAU":0.078, "LUATTR":-0.332},
#     "SPX": {"UKX":0.665, "DAX":0.680, "SPX":1, "SHSZ30":0.282, "AS51":0.514, "XAU":0.058, "LUATTR":-0.431},
#     "SHSZ30": {"UKX":0.332, "DAX":0.343, "SPX":0.282, "SHSZ30":1, "AS51":0.341, "XAU":0.071, "LUATTR":-0.206},
#     "XAU": {"UKX":0.036, "DAX":0.078, "SPX":0.058, "XAU":1, "LUATTR":0.373},
#     "LUATTR": {"UKX":-0.358, "DAX":-0.332, "SPX":-0.431, "SHSZ30":-0.206, "AS51":-0.298, "XAU":0.036, "LUATTR":1},
# }
#
# standard_deviation = {
#     "UKX": 25.96,
#     "DAX": 29.32,
#     "SPX": 30.69,
#     "SHSZ30": 20.81,
#     "XAU": 20.865,
#     "LUATTR": 6.0
# }
#
# indices = ["DAX", "SPX", "UKX"]
#
# yahoo_financials_indices = YahooFinancials(indices)
#
# data = yahoo_financials_indices.get_historical_price_data('2018-11-15', '2020-11-15', 'daily')

# Those basically need then to be aligned, but this is fantastic

def get_historical_prices_close(tickers):
    ohlc = yf.download(tickers, period="max")
    return ohlc["Adj Close"]
