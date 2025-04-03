from pybit.unified_trading import HTTP
import services.listik as le

session_pos = HTTP(
    demo = le.acsses["demo"],
    api_key=le.acsses["key"],
    api_secret=le.acsses["sicret_key"],
)
def get_qty(leverage_current: str, my_leverage: list, qtyCoin: str, balance_current: float) -> float:
    leverage_current = float(leverage_current)
    my_leverage[0] = float(my_leverage[0])
    my_leverage[1] = float(my_leverage[1])
    qtyCoin = float(qtyCoin)
    print(balance_current, leverage_current, qtyCoin)
    if leverage_current <= my_leverage[1]:
        return [((balance_current * 0.1) * leverage_current)/qtyCoin, leverage_current]
    else:
        return [((leverage_current * (balance_current * 0.1)))/qtyCoin, my_leverage[1]]
