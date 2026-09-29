from currencies import exchange_rates, currency_names


def show_title():

    print("\n=======================")
    print(" [CURRENCY CONVERTER] ")
    print("=======================\n")


def show_menu():

    print("\n1. Convert Currency")
    print("2. View Available Currencies")
    print("3. View Conversion History")
    print("4. Exit")


def show_currencies():

    print("\n==============================")
    print("   AVAILABLE CURRENCIES")
    print("==============================")

    for currency in exchange_rates:

        print(
            f"{currency}: "
            f"{currency_names[currency]}" )