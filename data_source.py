import yfinance as yf
import pypfopt
from pypfopt import (
    risk_models,
    expected_returns,
    EfficientFrontier
)

security_information = {
    # US - Equity
    "IVV" : { "name": "iShares Core S&P 500 ETF", "type": "EQUITY" },
    "IJH" : { "name": "iShares Core S&P Mid-Cap ETF", "type": "EQUITY" },
    "IJR" : { "name": "iShares Core S&P Small-Cap ETF", "type": "EQUITY" },
    "IVE" : { "name": "iShares S&P 500 Value ETF", "type": "EQUITY" },
    "DGRO" : { "name": "iShares Core Dividend Growth ETF", "type": "EQUITY" },
    "IYY" : { "name": "iShares Dow Jones U.S. ETF", "type": "EQUITY" },

    # EM - Equity
    "EEM" : { "name": "iShares MSCI Emerging Markets ETF", "type": "EQUITY" },
    "IEMG" : { "name": "iShares Core MSCI Emerging Markets ETF", "type": "EQUITY" },

    # Europe - Equity
    "EWG" : { "name": "iShares MSCI Germany ETF", "type": "EQUITY" },
    "EWU" : { "name": "iShares MSCI United Kingdom ETF", "type": "EQUITY" },
    "EWQ" : { "name": "iShares MSCI France ETF", "type": "EQUITY" },
    "EIS" : { "name": "iShares MSCI Israel ETF", "type": "EQUITY" },
    "EWL" : { "name": "iShares MSCI Switzerland ETF", "type": "EQUITY" },

    # Asia - Equity
    "EWJ" : { "name": "iShares MSCI Japan ETF", "type": "EQUITY" },
    "MCHI" : { "name": "iShares MSCI China ETF", "type": "EQUITY" },
    "EWY" : { "name": "iShares MSCI South Korea ETF", "type": "EQUITY" },
    "INDA" : { "name": "iShares MSCI India ETF", "type": "EQUITY" },
    "EWT" : { "name": "iShares MSCI Taiwan ETF", "type": "EQUITY" },

    # Commodities
    "IAU" : { "name": "iShares Gold Trust", "type": "CMDTY" },
    "SLV" : { "name": "iShares Silver Trust", "type": "CMDTY" },

    # Treasuries
    "IEF" : { "name": "iShares 7-10 Year Treasury Bond ETF", "type": "FI" },
    "IEI" : { "name": "iShares 3-7 Year Treasury Bond ETF", "type": "FI" },

    # Other
    "MBB" : { "name": "iShares MBS ETF", "type": "FI" },
    "MUB" : { "name": "iShares National Muni Bond ETF", "type": "FI" },
    "TLT" : { "name": "iShares 20+ Year Treasury Bond ETF", "type": "FI" },
    "MBB" : { "name": "iShares MBS ETF", "type": "FI" },

    # Investment grade - US
    "USIG" : { "name": "iShares Broad USD Investment Grade Corporate Bond ETF", "type": "FI" },

    # HY - US
    "USHY" : { "name": "iShares Broad USD High Yield Corporate Bond ETF", "type": "FI" },

    # EM Bonds
    "EMB" : { "name": "iShares J.P. Morgan USD Emerging Markets Bond ETF", "type": "EM BONDS" }
}

security_risk_mapping = {
        # US - Equity
        "IVV" : "High",
        "IJH" : "High",
        "IJR" : "High",
        "IVE" : "High",
        "DGRO" : "High",
        "IYY" : "High",

        # EM - Equity
        "EEM" : "High",
        "IEMG" : "High",

        # Europe - Equity
        "EWG" : "High",
        "EWU" : "High",
        "EWQ" : "High",
        "EIS" : "High",
        "EWL" : "High",

        # Asia - Equity
        "EWJ" : "High",
        "MCHI" : "High",
        "EWY" : "High",
        "INDA" : "High",
        "EWT" : "High",

        # Commodities
        "IAU" : "High",
        "SLV" : "High",

        # Treasuries
        "IEF" : "Low",
        "IEI" : "Low",

        # Other
        "MBB" : "Low",
        "MUB" : "Low",
        "TLT" : "Low",
        "MBB" : "Low",

        # Investment grade - US
        "USIG" : "Low",

        # HY - US
        "USHY" : "Low",

        # EM Bonds
        "EMB" : "High",
}

benchmark_information = {
    "ticker": "^GSPC",
    "name": "EURO STOXX 50 Index",
    "type": "EQUITY"
}

# benchmark_information = {
#     "ticker": "^RUA",
#     "name": "Russel 3000 Index",
#     "type": "EQUITY"
# }

def get_security_universe():
    return security_information

def get_security_risk():
    return security_risk_mapping

def get_historical_prices_close(tickers):
    ohlc = yf.download(tickers, period="max")
    return ohlc["Adj Close"]

def get_benchmark():
    return benchmark_information
