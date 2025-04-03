from pybit.unified_trading import HTTP
from services import listik as le

def get_Symbol(symbol):
    session = HTTP(
           demo = le.acsses["demo"],
        api_key=le.acsses["key"],
        api_secret=le.acsses["sicret_key"],
        )
    response = session.get_tickers(
        category="inverse",
        symbol=symbol+'USDT',
    )
    print(symbol)
    if response.get("retCode") == 0:
        market_cost = response["result"]["list"][0]["lastPrice"]
        return market_cost
    else:
        return response.get('retMsg')