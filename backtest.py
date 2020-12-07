import datetime
import pandas as pd
import math
import numpy as np

TRADING_DAYS = 250
RISK_FREE_RATE = 0.02

def calculate_backtest_prices(prices, weights, prices_benchmark):
    prices["benchmark"] = prices_benchmark
    prices = prices.dropna()

    # 1. Calculate returns of benchmark
    benchmark_returns = (prices[["benchmark"]] / prices[["benchmark"]].iloc[0]) * 100
    prices = prices.drop('benchmark', 1)

    # 2. Calculate the returns for the portfolio
    for ticker, weight in weights.items():
        divider = (prices[[ticker]].iloc[0] / weight) / 100
        prices[[ticker]] = prices[[ticker]] / divider

    portfolio_returns = prices.sum(axis=1)

    combined = pd.concat([benchmark_returns, portfolio_returns], axis=1)
    combined.columns = ["benchmark", "portfolio"]
    return combined

def back_test_prices_to_json(backtest_prices):
    return [{"date":row.Index.strftime('%Y-%m-%d'), "benchmark": round(row.benchmark, 1), "portfolio": round(row.portfolio,1)} for row in backtest_prices.itertuples()]

def calculate_backtest_performance(backtest_prices, benchmark_name):
    days_passed = backtest_prices.index[-1] - backtest_prices.index[0]
    years_passed = days_passed.days / TRADING_DAYS

    # 1. Calculate returns timeseries
    backtest_prices = backtest_prices.to_numpy()
    returns_benchmark = []
    returns_portfolio = []

    for i in range(1, len(backtest_prices)):
        temp1 =  backtest_prices[i][0] / backtest_prices[i-1][0] - 1
        temp2 =  backtest_prices[i][1] / backtest_prices[i-1][1] - 1
        returns_benchmark.append(temp1)
        returns_portfolio.append(temp2)

    returns_benchmark = np.array(returns_benchmark)
    returns_portfolio = np.array(returns_portfolio)

    # 2. Calculate average returns and average
    abs_return_benchmark = backtest_prices[-1][0] / backtest_prices[0][0]
    ann_return_benchmark = pow(abs_return_benchmark, (1 / years_passed)) -1
    ann_vol_benchmark    = returns_benchmark.std() * math.sqrt(TRADING_DAYS)
    sharpe_benchmark     = sharpe_ratio(ann_return_benchmark, ann_vol_benchmark)

    abs_return_portfolio = backtest_prices[-1][1] / backtest_prices[0][1]
    ann_return_portfolio = pow(abs_return_portfolio, (1 / years_passed)) -1
    ann_vol_portfolio    = returns_portfolio.std() * math.sqrt(TRADING_DAYS)
    sharpe_portfolio     = sharpe_ratio(ann_return_portfolio, ann_vol_portfolio)

    metrics = {
        "benchmark" : {
            "return":  to_percent(ann_return_benchmark),
            "vol": to_percent(ann_vol_benchmark),
            "sharpe": round(sharpe_benchmark, 2),
            "name": benchmark_name
        },
        "portfolio": {
            "return":  to_percent(ann_return_portfolio),
            "vol": to_percent(ann_vol_portfolio),
            "sharpe": round(sharpe_portfolio, 2)
        }
    }

    return metrics

def sharpe_ratio(ann_return, ann_vol):
    return (ann_return - RISK_FREE_RATE) / ann_vol

def to_percent(val):
    return round(val * 100, 2)
