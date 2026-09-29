import csv
import os


file_name = "data/conversion_history.csv"


def save_conversion(amount, from_currency, result, to_currency):

    os.makedirs("data", exist_ok=True)

    file_exists = os.path.exists(file_name)

    with open(file_name, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(
                ["Amount", "From", "Result", "To"]
            )

        writer.writerow(
            [amount, from_currency, result, to_currency]
        )


def show_history():

    if not os.path.exists(file_name):

        print("\nNo conversion history found.")
        return

    print("\n==============================")
    print("       CONVERSION HISTORY")
    print("==============================")

    with open(file_name, "r") as file:

        reader = csv.reader(file)

        next(reader, None)

        count = 0

        for row in reader:

            print(
                f"{row[0]} {row[1]} = "
                f"{float(row[2]):.2f} {row[3]}"
            )

            count += 1

        if count == 0:
            print("No conversion history found.")