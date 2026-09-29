from currencies import exchange_rates


def get_amount():

    while True:

        try:
            amount = float(input("Enter the amount to convert: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            return amount

        except ValueError:
            print("Invalid amount. Please enter a number.")


def get_currency(message):

    while True:

        currency = input(message).upper()

        if currency in exchange_rates:
            return currency

        print("Invalid currency code.")
        print("Please enter a valid currency code.")