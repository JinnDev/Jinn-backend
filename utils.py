def parse_weights(weights, tickers):
    portfolio = []
    for key, value in weights.items():
        if value == 0.0:
            continue
        temp = {}
        temp["ticker"] = key
        temp["weight"] = value
        portfolio.append({**temp, **tickers[key]})
    return portfolio
