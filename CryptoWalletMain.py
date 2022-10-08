from proj_lib import validate_int_input, end_code, colors, bold_green
from website_data import WebsiteDataXLM, WebsiteDataJPYEUR
from login import login
from datetime import date
from tabulate import tabulate
import os, csv, requests

# INTRO
welcome_msg = "Welcome to your digital STELLAR LUMENS ledger".center(51, "·")
description_msg = "Lumens (XLM) is the native token of Stellar, an open source, decentralized protocol for digital transactions. Borderless. Limitless. Powerful."
text_art = '''                                                                                                                                  
                                                                                  ⡀⡤⠂
                ▓▓██                                                          ⢀⣴⡿⠁
                ██▒▒████                                                   ⢀⣴⣿⡿⠁⠀
                ██▒▒▒▒▒▒▓▓                                               ⢀⣾⣿⣿⡇
      ▓▓▓▓▓▓    ██▒▒▒▒▒▒██                                              ⣼⣿⣿⣿⠀ 
    ██▒▒▒▒▓▓████████████████████████████████████████████              ⢰⣿⣿⣿⣿  
  ▓▓░░░░▒▒▓▓▓▓██░░    ░░                ░░  ▓▓▒▒▓▓▒▒▒▒▒▒▒▒           ⢸⣿⣿⣿⣿⡇
▓▓░░░░▒▒▒▒▒▒▓▓██░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓         ⢸⣿⣿⣿⣿⣿⡀
  ▓▓▒▒▒▒▒▒▓▓▓▓██░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒██            ⢸⣿⣿⣿⣿⣿⣷⡀⠀
    ██▒▒▓▓▓▓▓▓██████████████████████████████████████████               ⢿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      ⠀⢀⣴⠃
      ▓▓▓▓▓▓    ██▓▓▓▓▓▓██                                              ⠘⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⣀⣴⣿⠏⠀
        ░░      ██▒▒▒▒▒▒██                                                ⠘⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⣀⣀⣀⣀⣠⣤⣶⣿⣿⣿⠋⠀
                ██▒▒▓▓▓▓                                                    ⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀
                ████       ⠀                                                      ⠉⠛⠻⠿⠿⠿⠿⠿⠿⠟⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                               
'''
prompt_msg = "Please enter an option [1-8]: "

print(f"{colors[8]}{welcome_msg}{end_code}")
print(description_msg, f"{colors[6]}{text_art}{end_code}")

output = False
while not output:
    # output = login(user=input("Please enter your username: "), password=input("Please enter your password: "))
    output = login(user="sato", password="123")

    if not output:
        print(f"{colors[1]}Incorrect username or password. Please try again.{end_code}")

if output:
    print(f"\n{colors[8]}Correct username and password! You can now view the program:{end_code}")

while output:
    print(f"{colors[1]}Options{end_code}".center(20))
    menu = """1. Show all data
2. Deposit crypto
3. Withdraw crypto
4. View statistics
5. Edit past transactions
6. View real-time value of XLM
7. Edit password
8. Exit program
    """
    print(menu)
    option = validate_int_input(prompt_msg)
    while option > 8 or option < 1:
        option = validate_int_input(f"{colors[1]}Invalid option. {prompt_msg}{end_code}")

# Option 1: Show all data
    with open("data_transactions.csv", "r") as data_transactions:
        all_data = data_transactions.readlines()

    if option == 1:
        print("Now you will be able to see all data about past transactions you have made.")
        print(f"{bold_green}Showing all data: {end_code}")
        '''
        index = 0
        for data in all_data:
            if index > 0:
                # print(transaction.strip())  # strip removes the \n at the end of the line
                print(f"No.{index}: {data}", end="")
            index += 1
        '''
        list_values = []
        for data in all_data:
            values = data.split(",")
            list_values.append(values)
        print(tabulate(list_values, tablefmt='fancy_grid'))

# Option 2: Record transaction
    if option == 2:
        print("Now you will be able to deposit the new crypto you have bought")
        with open("data_transactions.csv", "a", newline="") as data_transactions:
            new_data = csv.writer(data_transactions)
            transaction_type = "buy"
            date = date.today()
            description = input("Please enter a description for your transaction: ")
            crypto_amount = input("Please enter the crypto amount you buy: ")
            jpy_value = input("Please enter in yen (JPY) the value of your transaction: ")
            new_data.writerow([transaction_type, date, description, crypto_amount, jpy_value])
        print("New data correctly recorded.")

# Option 3: Withdraw transaction
    if option == 3:
        print("Now you will be able to withdraw the crypto you have.")
        with open("data_transactions.csv", "a", newline="") as data_transactions:
            new_data = csv.writer(data_transactions)
            transaction_type = "sell"
            date = date.today()
            description = input("Please enter a description for your transaction: ")
            crypto_amount = input("Please enter the crypto amount you sell: ")
            jpy_value = input("Please enter in yen (JPY) the value of your transaction: ")
            new_data.writerow([transaction_type, date, description, crypto_amount, jpy_value])
        print("New data correctly recorded.")

# Option 4: View statistics
    if option == 4:
        print("Now you are seeing some statistics about your wallet and the crypto:")
        with open("data_transactions.csv", "r") as data_transactions:
            all_data = data_transactions.readlines()
            index = 0
            total_crypto = 0
            total_euros_buy = 0
            total_euros_sell = 0
            for row in all_data:
                if index > 0:
                    values = row.split(",")
                    crypto_amount = values[4]
                    euros_amount = values[5]
                    if values[0] == "buy":
                        total_crypto += float(crypto_amount)
                        total_euros_buy += float(euros_amount)
                    if values[0] == "sell":
                        total_crypto -= float(crypto_amount)
                        total_euros_sell += float(euros_amount)
                index += 1
            stats_message = f"""Right now you have {total_crypto} XLM Stellar Lumens.
Since you started buying cryptos, you have spent {total_euros_buy} EUROS in total.
But you have solt cryptos valued in {total_euros_sell} EUROS. 
You have a net balance of {total_euros_sell - total_euros_buy} EUROS.
"""
            print(stats_message)

# Option 5: Edit past transactions
    if option == 5:
        print("Now you can edit tra")
        edited_list = []
        with open('data_transactions.csv', 'r') as data_transactions:
            edited_data = csv.reader(data_transactions)
            for row in edited_data:
                edited_list.append(row)

        # Show the content of the file and print row number to make selection easy
        print("Please see details of your past transactions below:")
        for i in range(len(edited_list)):
            print("Row " + str(i) + ": " + str(edited_list[i]))

        # User selects which row to edit
        editRow = int(input("\nWhich row would you like to change? Enter 1 - " + str(len(edited_list) - 1) + ": "))
        print("Please enter the new details for each of the following :")

        # User adds the changes and appends changes to the list
        for i in range(len(edited_list[0])):
            new_data = input("Enter new data for " + str(edited_list[0][i]) + ": ")
            edited_list[editRow][i] = new_data

        # Show the new list
        print("\nPlease see the details of the new file below:")
        for i in range(len(edited_list)):
            print("Row " + str(i) + " :" + str(edited_list[i]))

        # Confirm changes
        confirm_changes = input("\nWould you like to confirm the changes to the digital ledger? [Y/N]: ").lower()

        # Save changes
        if confirm_changes == "y":
            with open('data_transactions.csv', 'w+', newline="") as data_transactions:
                edited_data = csv.writer(data_transactions)
                for i in range(len(edited_list)):
                    edited_data.writerow(edited_list[i])

            # Show changes
            with open("data_transactions.csv", "r") as data_transactions:
                all_transactions = data_transactions.readlines()
            index = 0
            print(f"{colors[8]}This is the new saved data:{end_code}")
            for transaction in all_transactions:
                if index > 0:
                    print(f"No.{index}: {transaction}", end="")
                index += 1

        elif confirm_changes == "n":
            print(f"{colors[1]}Changes not saved. Going back to the main menu.{end_code}")
        else:
            print(
                f"{colors[1]}Incorrect answer entered. You have to enter Y for yes or N for no. Going back to the main menu. {end_code}")


    # Option 6: View real time value
    if option == 6:
        try:
            xlm_eur = WebsiteDataXLM()
            jpy_eur = WebsiteDataJPYEUR()
            print(f"100 XML are equal to {float(xlm_eur)*100} euros (EUR).")
            print(f"100 XLM are equal to {float(xlm_eur)*float(jpy_eur)*100} yen (JPY).")
        except:
            print("There is no internet conexion. Please try again later.")

    # Option 7: Change password and username
    if option == 7:
        with open("login.csv", "w+") as login:
            new_login = csv.writer(login)
            user = input("Please enter your new username: ")
            password = input("Please enter your new password: ")
            new_login.writerow([user, password])
        input("Username and password changed. Press intro to exit the program")
        exit()

    # Option 8: Exit program
    if option == 8:
        print("Bye!")
        exit()

    input("Press intro to continue: ")
    print("""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """)
