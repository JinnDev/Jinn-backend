from pypfopt import (
    risk_models,
    expected_returns,
    EfficientFrontier
)

from data_source import (
    get_historical_prices_close
)

map_risk_level_to_vol = {
    "0" : 0.12,
    "1": 0.17,
    "2": 0.23,
    "3": 0.28,
    "4": 0.33
}

def calculate_covariance_matrix(prices):
    sample_cov = risk_models.sample_cov(prices, frequency=252)
    return risk_models.CovarianceShrinkage(prices).ledoit_wolf()

def calculate_expected_capm_returns(prices):
    return expected_returns.capm_return(prices)

def calculate_portfolio(prices, risk_level):
    target_volatility = map_risk_level_to_vol[risk_level]
    print(risk_level)
    print(target_volatility)
    cov_matrix = calculate_covariance_matrix(prices)
    expected_returns = calculate_expected_capm_returns(prices)
    ef = EfficientFrontier(expected_returns, cov_matrix, weight_bounds=(0, None))
    ef.efficient_risk(target_volatility)
    weights = ef.clean_weights()
    return weights

# prices = get_historical_prices_close(tickers)
# print(calculate_portfolio(prices, 0.15))
