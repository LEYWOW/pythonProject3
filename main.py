import requests

def convert_to_usd(amount):
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for currency in data:
            if currency['ccy'] == 'USD':
                exchange_rate = float(currency['buy'])
                usd_amount = amount / exchange_rate
                return usd_amount
    return None

try:
    uah_amount = float(input("Введіть суму в гривнях: "))
    usd_amount = convert_to_usd(uah_amount)
    if usd_amount is not None:
        print(f"Еквівалентна сума в доларах США: {usd_amount:.2f}")
    else:
        print("Не вдалося отримати курс долара США")
except ValueError:
    print("Ви вели символ або некоректну сумму")
