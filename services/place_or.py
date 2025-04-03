from pybit.unified_trading import HTTP
from services import listik as le
# 1 - название валюты 2- направление 3 - Стоимость 4 - плечо 5 - тп 6 - сл
def place(symbol, side, qty, leverage, tp, sl):
    try:
        session = HTTP(
            demo = le.acsses["demo"],
            api_key=le.acsses["key"],
            api_secret=le.acsses["sicret_key"],
        )
        session.set_leverage(
        category="linear",
        symbol=symbol+"USDT",
        buyLeverage=str(leverage), 
        sellLeverage=str(leverage)
        )
        leverage = int(leverage)-1
        session.set_leverage(
        category="linear",
        symbol=symbol+"USDT",
        buyLeverage=str(leverage), 
        sellLeverage=str(leverage)
        )
        print(leverage)
        leverage = int(leverage)+1
        session.set_leverage(
        category="linear",
        symbol=symbol+"USDT",
        buyLeverage=str(leverage), 
        sellLeverage=str(leverage)
        )
        if side == "LONG":
            side = "Buy"
        elif side=="SHORT":
            side = "Sell"
        print(leverage)
        # Отправка запроса на размещение ордера
        response = session.place_order(
            category="linear",
            symbol=symbol + "USDT",
            side=side,
            orderType="Market",
            qty=str(qty),
            takeProfit=tp,
            stopLoss=sl,
        )
    except Exception as e:
        leverage = int(leverage)-1
        session.set_leverage(
        category="linear",
        symbol=symbol+"USDT",
        buyLeverage=str(leverage), 
        sellLeverage=str(leverage)
        )
        print(leverage)
        leverage = int(leverage)+1
        session.set_leverage(
        category="linear",
        symbol=symbol+"USDT",
        buyLeverage=str(leverage), 
        sellLeverage=str(leverage)
        )
        if side == "LONG":
            side = "Buy"
        elif side=="SHORT":
            side = "Sell"
        print(leverage)
        response = session.place_order(
            category="linear",
            symbol=symbol + "USDT",
            side=side,
            orderType="Market",
            qty=str(qty),
            takeProfit=tp,
            stopLoss=sl,
        )

    # Проверка ответа
    if response is None:
        return "Ошибка: метод place_order вернул None"
    
    # Обработка успешного ответа
    if response.get("retCode") == 0:
        return f"Ордер успешно размещён: {response}"
    else:
        return f"Ошибка: {response.get('retMsg', 'Неизвестная ошибка')} Hello"
