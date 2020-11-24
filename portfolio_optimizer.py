from pypfopt import (
    risk_models,
    expected_returns,
    EfficientFrontier
)

def calculate_covariance_matrix(prices):
    sample_cov = risk_models.sample_cov(prices, frequency=252)
    return risk_models.CovarianceShrinkage(prices).ledoit_wolf()

def calculate_expected_capm_returns(prices):
    return expected_returns.capm_return(prices)

def calculate_historical_volatilities(prices):
    return {sec:prices[sec].std(skipna=True) for sec in prices.columns.values}
    
def calculate_portfolio(prices, risk_level):
    cov_matrix = calculate_covariance_matrix(prices)
    expected_returns = calculate_expected_capm_returns(prices)
    ef = EfficientFrontier(expected_returns, cov_matrix, weight_bounds=(0, None))

    # Get min vol
    ef.min_volatility()
    expected_return_min_vol, min_vol, sharpe_ratio_min_vol = ef.portfolio_performance()

    # Get max vol
    ef.efficient_risk(1)
    expected_return_max_vol, max_vol, sharpe_ratio_max_vol = ef.portfolio_performance()

    target_volatility = min_vol + (risk_level / 5) * (max_vol * 0.75 - min_vol)
    ef.efficient_risk(target_volatility)
    weights = ef.clean_weights()

    return weights

# prices = get_historical_prices_close(tickers)
# print(calculate_portfolio(prices, 0.15))
