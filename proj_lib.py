import csv
from website_data import WebsiteDataXLM
import matplotlib.pyplot as plt

# I will put all the code that I want to reuse in this file

end_code = "\033[00m"

black = "\33[0;30m"
red = "\33[0;31m"
green = "\33[0;32m"
yellow = "\33[0;33m"
blue = "\33[0;34m"
purple = "\33[0;35m"
cyan = "\33[0;36m"
white = "\33[0;37m"

bold_black = "\33[1;30m"
bold_red = "\33[1;31m"
bold_green = "\33[1;32m"
bold_yellow = "\33[1;33m"
bold_blue = "\33[1;34m"
bold_purple = "\33[1;35m"
bold_cyan = "\33[1;36m"
bold_white = "\33[1;37m"

intense_black = "\33[0;90m"
intense_red = "\33[0;91m"
intense_green = "\33[0;92m"
intense_yellow = "\33[0;93m"
intense_blue = "\33[0;94m"
intense_purple = "\33[0;95m"
intense_cyan = "\33[0;96m"
intense_white = "\33[0;97m"


def validate_int_input(msg: str) -> int:
    """This function validates that the user enters an integer"""
    number = input(msg)
    while not number.isdigit():
        # number = input(f"{red}Error. {msg}{end_code}") # Lo he comentado para poder poner mi propio mensaje en EV_calculator
        number = input(f"{red}{msg}{end_code}")

    return int(number)


def graph():
    from datetime import date
    '''
    while True:
        with open("xlm_historical_price.csv", "a", newline="") as xlm_historical_price:
            new_price = csv.writer(xlm_historical_price)
            date = date.today()
            xlm_eur = WebsiteDataXLM()
            new_price.writerow([date, xlm_eur])
        print("New prices correctly recorded.")
        time.sleep(86400)
    '''
    with open("xlm_historical_price.csv", "a", newline="") as xlm_historical_price:
        new_price = csv.writer(xlm_historical_price)
        date = date.today()
        xlm_eur = WebsiteDataXLM()
        new_price.writerow([date, xlm_eur])

    with open("xlm_historical_price.csv", "r") as xlm_historical_price:
        all_prices = xlm_historical_price.readlines()

    list_data = []
    list_price = []
    index = 0
    for data in all_prices:
        values = data.split(",")
        list_data.append(data[5:10])
        list_price.append(float(data[11:18]))

    print(list_data)
    print(list_price)
    plt.plot(list_data, list_price)
    plt.ylabel('XLM to EUR value')
    plt.xlabel('Dates')
    plt.show()


