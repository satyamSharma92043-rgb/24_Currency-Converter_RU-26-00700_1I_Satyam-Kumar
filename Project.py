
#Project No. 24:  Currency Converter Project
# Language: Python 3

exchange_rates = {
    "INR": 1,
    "USD": 83,
    "EUR": 90,
    "GBP": 105
}


def convert_to_inr(amount, currency):
    return amount * exchange_rates[currency]


def convert_currency(amount, from_currency, to_currency):

    amount_in_inr = convert_to_inr(amount, from_currency)

    result = amount_in_inr / exchange_rates[to_currency]

    return round(result, 2)


print("===== CURRENCY CONVERTER =====")
print("Available currencies: INR, USD, EUR, GBP")

try:
    amount = float(input("Enter amount: "))

    from_currency = input("From currency: ").upper()
    to_currency = input("To currency: ").upper()

    if amount < 0:
        print("Amount cannot be negative.")

    elif from_currency not in exchange_rates:
        print("Unsupported currency '" + from_currency + "'. Available: INR, USD, EUR, GBP")

    elif to_currency not in exchange_rates:
        print("Unsupported currency '" + to_currency + "'. Available: INR, USD, EUR, GBP")

    else:
        converted_amount = convert_currency(
            amount, from_currency, to_currency
        )

        print(
            f"{amount:g} {from_currency} = "
            f"{converted_amount:.2f} {to_currency}"
        )

except ValueError:
    print("Invalid amount. Enter a number.")
