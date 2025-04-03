from pybit.unified_trading import HTTP
from services import listik as le
leverage = 0
def get_Leverage(symbol, leverage):
    session = HTTP(
        demo = le.acsses["demo"],
        api_key=le.acsses["key"],
        api_secret=le.acsses["sicret_key"],
    )
    respons = session.get_instruments_info(category = 'linear',symbol = symbol+"USDT")
    if respons.get('retCode') == 0:
        max_leverage = respons['result']['list'][0]['leverageFilter']['maxLeverage']
        if leverage<max_leverage:
            return [leverage, max_leverage]
        else:
            return [leverage,max_leverage]
    else:
        return respons['retMsg']