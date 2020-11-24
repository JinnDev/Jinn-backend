def parse_weights(weights, tickers, vols):
    portfolio = []
    for key, value in weights.items():
        if value == 0.0:
            continue
        temp = {}
        temp["ticker"] = key
        temp["weight"] = round(value * 100, 1)
        temp["historical_vol"] = round(vols[key],1)
        portfolio.append({**temp, **tickers[key]})
    return portfolio
