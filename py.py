from pybit.unified_trading import HTTP
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import services
import services.leverage
import services.market_cost as market_cost
import services.pattern
import services.qty
import services.wallet
import services.listik as le
from services import place_or

driver = webdriver.Chrome()
url = 'https://web.telegram.org/a/'
driver.get(url)
activer = []
input('')
Market_options = []
page_sourse = driver.page_source
nextvalue = 0
soup = BeautifulSoup(page_sourse, 'html.parser')
while True:
    message_container = soup.find(class_="messages-container")
    elements = message_container.find_all(id=lambda x: x and x.startswith('message-'))
    last_element = max(elements, key=lambda el: int(el['id'].split('-')[1]))
    last_value = int(last_element['id'].split('-')[1])
    nextvalue = last_value + 1
    while True:
        page_sourse = driver.page_source
        soup = BeautifulSoup(page_sourse, 'html.parser')
        message_container = soup.find(class_="messages-container")
        elements = message_container.find_all(id=lambda x: x and x.startswith('message-'))
        last_element_clone =max(elements, key=lambda el: int(el['id'].split('-')[1]))
        last_value_clone = int(last_element['id'].split('-')[1])
        if(last_value_clone == nextvalue):
            time.sleep(1)
            parent_element = message_container.find('div', id=f'message-{nextvalue}')
            nextvalue == last_value_clone + 1
            if(parent_element == None):
                continue
            else:
                break
        elif last_value_clone>nextvalue:
            time.sleep(1)
            nextvalue = last_value_clone
            parent_element = message_container.find('div', id=f'message-{nextvalue}')
            nextvalue = last_value_clone+1
            if(parent_element == None):
                continue
            else:
                break
        elif last_value_clone<nextvalue:
            time.sleep(1)
            parent_element = message_container.find('div', id=f'message-{nextvalue}')
            if(parent_element == None):
                continue
            else:
                break
    if(len(activer) == 1):
        parent_element = message_container.find('div', id=f'message-{nextvalue}')
        if parent_element:
            activer = []
        else:
            continue
    if parent_element:
        full_text = parent_element.get_text(separator="\n", strip=True)
        activer.append(last_value)
    else:
        print("Следующий ожидаемый пост: ",last_value+1)
        continue
    try:
        if parent_element != "":
            Market_options = []
            response = services.pattern.pattern(full_text)
            if(response != None):
                print("Номер поста",nextvalue)
                Market_options = [response[0],response[1],response[2],response[3],response[4]]
                Balik = services.wallet.get_balance_with_orders(services.wallet.pnlNO, services.wallet.position_size)# получаю полный баланс исходя также из открытых ордеров
                Lever = services.leverage.get_Leverage(Market_options[1],Market_options[2])# получаю кредитное плечо (может быть изменено позже)
                Market_C = market_cost.get_Symbol(Market_options[1])#Получаю цену валюты
                Qty = services.qty.get_qty(response[2], Lever, Market_C, Balik) # получаю цену на которую можно зайти для того чтобы открыть сделку с учётом баланса, кредитного плеча
                Active_Order = services.wallet.get_active_orders(Market_options[1],activer)# получаю список активных позиций
                if Active_Order:
                    try:
                        # 1 - название валюты 2- направление 3 - Стоимость 4 - плечо 5 - тп 6 - сл
                        print(Market_options[1], Market_options[0], Qty, response[2], Market_options[3], Market_options[4])
                        if (Market_options[1] == "BTC"):
                            place_or.place(Market_options[1], Market_options[0], round(Qty[0],3), Qty[1], Market_options[3], Market_options[4])
                        else:
                            place_or.place(Market_options[1], Market_options[0], round(Qty[0],1), Qty[1], Market_options[3], Market_options[4])
                        print("Ордер создан")  
                    except Exception as e:
                        print(e)
                    finally:
                        continue
                else:
                    continue
        else:
            continue
    except Exception as e:
        print(f"Ошибка: {e}")
