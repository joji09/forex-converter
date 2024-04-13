from flask import Flask, request, render_template
from forex_python.converter import CurrencyRates

app = Flask(__name__)
currency_converter = CurrencyRates()


# access key and URL for other tool
# access_key = "6ebeba7680fbe2507fc3c03963d54ac9"
# exchange_api_url = "https://api.exchangerate.host/live"
# 'https://api.exchangerate.host/' + '?access_key=' + access_key

SUPPORTED_CURRENCIES = {
    "EUR", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON",
    "MYR", "SEK", "SGD", "HKD", "AUD", "CHF", "KRW", "CNY", "TRY", "HRK",
    "NZD", "THB", "USD", "NOK", "RUB", "INR", "MXN", "CZK", "BRL", "PLN",
    "PHP", "ZAR"
}

def check_currency(currency_code):
    #VALIDATES CURRENCY ENTERED
    return currency_code.strip().upper() in SUPPORTED_CURRENCIES

@app.route('/', methods=['GET', 'POST'])
def convert_function():
    error_message = None
    converted_amount = None
    if request.method == 'POST':
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency'].upper()
        to_currency = request.form['to_currency'].upper()

        if check_currency(from_currency) and check_currency(to_currency):
            converted_amount = currency_converter.convert(from_currency, to_currency, amount)
        else:
            error_message = "Invalid Currency code."

    return render_template('index.html', converted_amount=converted_amount, error_message=error_message)
