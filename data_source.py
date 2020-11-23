import yfinance as yf
import pypfopt
from pypfopt import (
    risk_models,
    expected_returns,
    EfficientFrontier
)

security_information = {
    # US - Equity
    "IVV" : { "name": "iShares Core S&P 500 ETF)", "type": "EQUITY" },

    # EM - Equity
    "EEM" : { "name": "iShares MSCI Emerging Markets ETF)", "type": "EQUITY" },
    "IEMG" : { "name": "iShares Core MSCI Emerging Markets ETF)", "type": "EQUITY" },

    # Europe - Equity
    "EWG" : { "name": "iShares MSCI Germany ETF", "type": "EQUITY" },
    "EWU" : { "name": "iShares MSCI United Kingdom ETF", "type": "EQUITY" },
    "EWQ" : { "name": "iShares MSCI France ETF", "type": "EQUITY" },
    "ERUS" : { "name": "iShares MSCI Russia ETF", "type": "EQUITY" },
    "EIS" : { "name": "iShares MSCI Israel ETF", "type": "EQUITY" },

    # Asia - Equity
    "EWJ" : { "name": "iShares MSCI Japan ETF", "type": "EQUITY" },
    "MCHI" : { "name": "iShares MSCI China ETF", "type": "EQUITY" },
    "EWY" : { "name": "iShares MSCI South Korea ETF", "type": "EQUITY" },
    "INDA" : { "name": "iShares MSCI India ETF", "type": "EQUITY" },

    # Commodities
    "COMT" : { "name": "iShares Commodities Select Strategy ETF", "type": "CMDTY" },

    # Treasuries
    "IEF" : { "name": "iShares 7-10 Year Treasury Bond ETF", "type": "CMDTY" },
    "IEI" : { "name": "iShares 3-7 Year Treasury Bond ETF", "type": "CMDTY" },

    # Investment grade - US
    "USIG" : { "name": "iShares Broad USD Investment Grade Corporate Bond ETF", "type": "CMDTY" },

    # HY - US
    "USHY" : { "name": "iShares Broad USD High Yield Corporate Bond ETF", "type": "CMDTY" },

    # EM Bonds
    "EMB" : { "name": "iShares J.P. Morgan USD Emerging Markets Bond ETF", "type": "EM BONDS" },
}


def get_security_universe():
    return security_information


def get_historical_prices_close(tickers):
    ohlc = yf.download(tickers, period="max")
    return ohlc["Adj Close"]
