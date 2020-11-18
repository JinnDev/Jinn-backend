from utils import parse_weights
from collections import OrderedDict

def test_parse_weights():
    # GIVEN
    weights = OrderedDict(ACN=0.0, AMZN=0.1, DIS=0.2).items()
    tickers = {
        "ACN" : { "name": "ACN firm", "type": "EQUITY" },
        "AMZN" : {"name": "AMZN firm", "type": "EQUITY" },
        "DIS" : { "name": "DIS firm", "type": "EQUITY" },
    }
    expected_result = [
        {"ticker": "ACN", "name": "ACN firm", "type": "EQUITY",  "weight": 0.0},
        {"ticker": "AMZN", "name": "AMZN firm", "type": "EQUITY", "weight": 0.1},
        {"ticker": "DIS", "name": "DIS firm", "type": "EQUITY",  "weight": 0.2}
    ]
    # WHEN
    result = parse_weights(weights, tickers)
    print(result)
    # THEN
    assert result == expected_result
    # assert result["AMZN"] == expected_result["AMZN"]
    # assert result["ACN"] == expected_result["ACN"]
    # assert result["DIS"] == expected_result["DIS"]
