from pypfopt import (
    risk_models,
    expected_returns,
    EfficientFrontier,
    objective_functions
)

def calculate_covariance_matrix(prices):
    sample_cov = risk_models.sample_cov(prices, frequency=252)
    return risk_models.CovarianceShrinkage(prices).ledoit_wolf()

def calculate_expected_capm_returns(prices, prices_benchmark):
    # prices_benchmark = prices_benchmark.rename("mkt")
    # return expected_returns.capm_return(prices, prices_benchmark)
    return expected_returns.ema_historical_return(prices)

def calculate_historical_volatilities(prices):
    return {sec:prices[sec].std(skipna=True) for sec in prices.columns.values}

def calculate_portfolio(prices, prices_benchmark, risk_level, restrictions, securities_risk):
    cov_matrix = calculate_covariance_matrix(prices)
    ef = EfficientFrontier(None, cov_matrix, weight_bounds=(0, None))

    # Add restrictions
    for r in restrictions:
        r_index =  ef.tickers.index(r["ticker"])
        ef.add_constraint(lambda w: w[r_index] == r["weight"])

    # Add risk restriction
    high_risk_min = (risk_level / 10) / 1.25
    low_risk_min = (1 - risk_level / 10) / 1.25

    risk_lower = {
        "High": high_risk_min,
        "Low": low_risk_min,
    }

    risk_upper = {
        "High": high_risk_min + 0.1,
        "Low": low_risk_min + 0.1,
    }

    print(risk_lower)
    print(risk_upper)
    ef.add_sector_constraints(securities_risk, risk_lower, risk_upper)

    # Get min vol
    ef.min_volatility()
    weights = ef.clean_weights()

    return weights

def calculate_max_sharpe_portfolio(prices):
    mu = expected_returns.capm_return(prices)
    S = risk_models.CovarianceShrinkage(prices).ledoit_wolf()

    ef = EfficientFrontier(mu, S)  # weight_bounds automatically set to (0, 1)

    ef.max_sharpe()
    weights = ef.clean_weights()
    return weights
