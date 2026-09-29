from converter import convert_currency
from validator import get_amount, get_currency
from history import save_conversion, show_history
from display import show_title, show_menu, show_currencies


show_title()


while True:

    show_menu()

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":

        amount = get_amount()

        from_currency = get_currency(
            "Enter currency to convert FROM: "
        )

        to_currency = get_currency(
            "Enter currency to convert TO: "
        )

        result = convert_currency(
            amount,
            from_currency,
            to_currency
        )

        print("\n--------------------------------")
        print(
            f"     {amount} {from_currency} = "
            f"{result:.2f} {to_currency}"
        )
        print("--------------------------------")

        save_conversion(
            amount,
            from_currency,
            result,
            to_currency
        )

    elif choice == "2":

        show_currencies()

    elif choice == "3":

        show_history()

    elif choice == "4":

        print("\nThank you for using the Currency Converter!")
        print("Goodbye!")
        break

    else:

        print("\nInvalid choice.")
        print("Please select 1, 2, 3, or 4.")