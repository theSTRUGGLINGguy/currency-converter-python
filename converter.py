from currencies import exchange_rates


def convert_currency(amount, from_currency, to_currency):

    if from_currency not in exchange_rates:
        return None

    if to_currency not in exchange_rates:
        return None

    amount_in_usd = amount / exchange_rates[from_currency]

    converted_amount = amount_in_usd * exchange_rates[to_currency]

    return converted_amount