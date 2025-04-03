import services.listik as le
from pybit.unified_trading import HTTP
import time
pnlNO = 0
position_size = 0
def get_Balance():
    session = HTTP(
        demo = le.acsses["demo"],
        api_key=le.acsses["key"],
        api_secret=le.acsses["sicret_key"],
    )
    response = session.get_wallet_balance(
        accountType="UNIFIED",
        coin="USDT",
    )
    if response.get("retCode") == 0:
        coins = response["result"]["list"][0]["coin"]
        usdt_info = next(coin for coin in coins if coin["coin"] == "USDT")
        wallet_balance = usdt_info["walletBalance"]  # Полный баланс
        available_balance = response["result"]["list"][0]["totalAvailableBalance"]  # Доступный баланс
        print(response,wallet_balance, available_balance)
        return [wallet_balance,available_balance]
    else:
        return response.get('retMsg')
def get_active_orders(variable, list = []):
    session = HTTP(
        demo = le.acsses["demo"],
        api_key=le.acsses["key"],
        api_secret=le.acsses["sicret_key"],
    )
    resp = session.get_positions(category="linear", symbol=variable+"USDT")
    time.sleep(0.1)
    if resp['retCode'] == 0:
        positions = resp['result']['list']
        if positions:
            if float(positions[0]['size']) > 0:
                return False
            else:
                print(f"Нет открытых позиций для {variable}")
                return True
    else:
        return f"Ошибка: {resp['retMsg']}"
def get_balance_with_orders(pln, pssize, active_orders = []):
    session = HTTP(
        demo = le.acsses["demo"],
        api_key=le.acsses["key"],
        api_secret=le.acsses["sicret_key"],
    )
    for i in range(len(active_orders)):
        response = session.get_tickers(
            category="inverse",
            symbol=active_orders[i][0]+'USDT',
        )
        if response.get("retCode") == 0:
            market_cost = response["result"]["list"][0]["lastPrice"]
            # return market_cost
        else:
            print(response.get('retMsg'))
        resp = session.get_positions(category="linear", symbol=active_orders[i][0]+"USDT")
        time.sleep(0.1)
        if resp['retCode'] == 0:
            positions = resp['result']['list']
            if positions:
                if float(positions[0]['size']) > 0:
                    pln = pln + float(resp['result']['list'][0]['unrealisedPnl'])
                    pssize = float(resp['result']['list'][0]['size']) * float(market_cost)
                else:
                    print(f"Нет открытых позиций для {active_orders[i][0]}")
        else:
            print(f"Ошибка: {resp['retMsg']}")
    print(get_Balance())
    wallet_all = 0
    wallet = get_Balance()
    if pln >= 0:
        wallet_all = float(wallet[1])-pssize-pln
        print(str(wallet_all)+" Балик1")
    elif pln <= 0:
        wallet_all = float(wallet[1])-pssize+(pln*(-1))
        print(str(wallet_all)+" Балик2")
    return wallet_all
        
        # wallet[1]+
# get_balance_with_orders(pnlNO, position_size, active_orders)
# get_Balance - возвращает просто баланс достпуный и полный
# get_active_orders - возвращает список активных позиций а также может его изменять
# get_balance_with_orders - возвращает полный баланс учитывая сам баланс, размер открытых позиций, игнорирует P&L