import re
def pattern(full_text):
    response = _pattern_one(full_text)
    if(response):
        return _pattern_one(full_text)
    response = _pattern_two(full_text)
    if(response):
        return _pattern_two(full_text)
    return None

def _safe_search(pattern, text, flags = 0):
        match = re.search(pattern, text, flags)
        if match:
            return match.group(1)
        return None
def _pattern_one(full_text):
    direction = str(_safe_search(r'(LONG|short|long|Short|Long|SHORT)', full_text, re.IGNORECASE)).upper()
    currency = str(_safe_search(r'(\w+)\s*/USDT', full_text, re.IGNORECASE)).upper()
    leverage = _safe_search(r'Leverage:.*?(\d+)X', full_text)
    take_profit = _safe_search(r'Take-Profit Targets:\s*1\)\s*([\d\.]+)', full_text)
    stop_target = _safe_search(r'Stop Target:\s*1\)\s*([\d\.]+)', full_text)
    print(direction, currency, leverage, take_profit, stop_target)
    if direction != "NONE" and currency != "NONE" and leverage != None and take_profit != None and stop_target != None:
        return [direction, currency, leverage, take_profit, stop_target]
    else:
         return None
def _pattern_two(full_text):
    direction = str(_safe_search(r"Direction\s*:\s*(LONG|short|long|Short|Long|SHORT)", full_text, re.IGNORECASE)).upper()
    currency = str(_safe_search(r"([A-Z]+)\/USDT", full_text, re.IGNORECASE)).upper()
    leverage = _safe_search(r"Leverage:\s*Cross\s*(\d+x)", full_text)
    take_profit = _safe_search(r"Targets:-\s*([\d.]+)", full_text)
    stop_target = _safe_search(r"Stop-Loss:\s*([\d.]+)", full_text)
    print(direction, currency, leverage, take_profit, stop_target)
    if direction != "NONE" and currency != "NONE" and leverage != None and take_profit != None and stop_target != None: 
        return [direction, currency, leverage, take_profit, stop_target]
    else:
         return None