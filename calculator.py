import requests
from datetime import datetime

name = input('Название монеты: ').strip().lower()
date_input = input('Дата покупки (дд-мм-гггг): ')
purchase_date = datetime.strptime(date_input, '%d-%m-%Y')
count = float(input('Количество: '))
price_date = requests.get(f'https://api.coingecko.com/api/v3/coins/{name}/history?date={purchase_date.strftime("%d-%m-%Y")}')
price_then = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={name}&vs_currencies=usd')
data = price_date.json()
data1 = price_then.json()
price_late = float(data['market_data']['current_price']['usd'])
price_now = float(data1[name]['usd'])
final = round(price_now  * count - price_late* count , 2)
if final > 0 :
    print('Ваша прибыль:', final)
if final == 0:
    print('Вы ничего не заработали')
if final < 0:
    print('Вы в убытке на', final)
