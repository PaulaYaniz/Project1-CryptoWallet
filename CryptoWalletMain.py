import website_data
from proj_lib import validate_int_input, end_code
from website_data import WebsiteDataXLM, WebsiteDataJPYEUR
from login import login
from datetime import date
from tabulate import tabulate
import os, csv, requests
import proj_lib

# INTRO
try:
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
    prompt_msg = "Please enter an option [1-9]: "

    print(f"{proj_lib.intense_green}{welcome_msg}{end_code}")
    print(description_msg, f"{proj_lib.cyan}{text_art}{end_code}")

    output = False
    while not output:
        output = login(user=input("Please enter your username: "), password=input("Please enter your password: "))

        if not output:
            print(f"{proj_lib.intense_red}Incorrect username or password. Please try again.{end_code}")

    if output:
        print(f"\n{proj_lib.intense_green}Correct username and password! You can now view the program:{end_code}")

    while output:
        print(f"{proj_lib.intense_purple}Options:{end_code}".center(20))
        menu = """1. Show all data
2. Deposit crypto
3. Withdraw crypto
4. Edit past transactions
5. View statistics
6. View real-time value of XLM
7. View graphic of the historical price of XLM
8. Edit password
9. Exit program
        """
        print(proj_lib.intense_yellow, menu, end_code)
        option = validate_int_input(prompt_msg)
        while option > 9 or option < 1:
            option = validate_int_input(f"{proj_lib.red}Invalid option. {prompt_msg}{end_code}")

        # Option 1: Show all data
        if option == 1:
            with open("data_transactions.csv", "r") as data_transactions:
                all_data = data_transactions.readlines()

            print(f"{proj_lib.intense_green}Now you will be able to see all data about past transactions you have made.{end_code}")
            print(f"{proj_lib.intense_purple}Showing all data: {end_code}{proj_lib.intense_blue}")

            list_values = []
            for data in all_data:
                values = data.split(",")
                list_values.append(values)
            print(tabulate(list_values, tablefmt='fancy_grid'))
            print(end_code)

        # Option 2: Deposit crypto
        if option == 2:
            print(f"{proj_lib.intense_green}Now you will be able to deposit the new crypto you have bought{end_code}")
            with open("data_transactions.csv", "a", newline="") as data_transactions:
                new_data = csv.writer(data_transactions)
                transaction_type = "deposit"
                date = date.today()
                crypto_amount = input(f"{proj_lib.intense_blue}Please enter the crypto amount you want to deposit: ")
                jpy_value = input("Please enter in yen (JPY) the value of your transaction: ")
                comment = input(f"Please enter a comment for your transaction: {end_code}")
                new_data.writerow([transaction_type, date, comment, crypto_amount, jpy_value])
            print(f"{proj_lib.intense_purple}New data correctly recorded. {end_code}")

        # Option 3: Withdraw crypto
        if option == 3:
            print(f"{proj_lib.intense_green}Now you will be able to withdraw the crypto you have.{end_code}")
            with open("data_transactions.csv", "a", newline="") as data_transactions:
                new_data = csv.writer(data_transactions)
                transaction_type = "withdraw"
                date = date.today()
                crypto_amount = input(f"{proj_lib.intense_blue}Please enter the crypto amount you want to withdraw: ")
                jpy_value = input("Please enter in yen (JPY) the value of your transaction: ")
                comment = input(f"Please enter a comment for your transaction: {end_code}")
                new_data.writerow([transaction_type, date, comment, crypto_amount, jpy_value])
            print(f"{proj_lib.intense_purple}New data correctly recorded.{end_code}")

        # Option 4: Edit past transactions
        if option == 4:
            print(f"{proj_lib.intense_green}Now you can edit your past transactions: {end_code}")
            edited_list = []
            with open('data_transactions.csv', 'r') as data_transactions:
                edited_data = csv.reader(data_transactions)
                for row in edited_data:
                    edited_list.append(row)

            # Show the content of the file and print row number to make selection easy
            print(f"{proj_lib.intense_purple}Please see details of your past transactions below:{end_code}{proj_lib.intense_blue}")
            for i in range(len(edited_list)):
                print("Row " + str(i) + ": " + str(edited_list[i]))

            # User selects which row to edit
            editRow = int(input(f"\n{end_code}{proj_lib.intense_purple}Which row would you like to change? Enter 1 - " + str(len(edited_list) - 1) + ": "))
            print("Please enter the new details for each of the following :")

            # User adds the changes and appends changes to the list
            for i in range(len(edited_list[0])):
                new_data = input("Enter new data for " + str(edited_list[0][i]) + ": ")
                edited_list[editRow][i] = new_data

            # Show the new list
            print("\nPlease see the details of the new file below:")
            for i in range(len(edited_list)):
                print(f"{proj_lib.intense_blue}Row {str(i)}: {str(edited_list[i])}{end_code}")

            # Confirm changes
            confirm_changes = input(f"\n{proj_lib.intense_purple}Would you like to confirm the changes to the digital ledger? [Y/N]: ").lower()

            # Save changes
            if confirm_changes == "y":
                with open('data_transactions.csv', 'w+', newline="") as data_transactions:
                    edited_data = csv.writer(data_transactions)
                    for i in range(len(edited_list)):
                        edited_data.writerow(edited_list[i])

                # Show changes
                with open("data_transactions.csv", "r") as data_transactions:
                    all_data = data_transactions.readlines()

                print(f"{proj_lib.intense_purple}This is the new save data: {end_code}{proj_lib.intense_blue}")

                list_values = []
                for data in all_data:
                    values = data.split(",")
                    list_values.append(values)
                print(tabulate(list_values, tablefmt='fancy_grid'))
                print(end_code)

            elif confirm_changes == "n":
                print(f"{proj_lib.red}Changes not saved. Going back to the main menu.{end_code}")
            else:
                print(
                    f"{proj_lib.intense_red}Incorrect answer entered. You have to enter Y for yes or N for no. Going back to the main menu. {end_code}")

        # Option 5: View statistics
        if option == 5:
            print(f"{proj_lib.intense_green}Now you are seeing some statistics about your wallet and the crypto:{end_code}")
            with open("data_transactions.csv", "r") as data_transactions:
                all_data = data_transactions.readlines()
                index = 0
                total_crypto = 0
                total_jpy_deposit = 0
                total_jpy_withdraw = 0
                for row in all_data:
                    if index > 0:
                        values = row.split(",")
                        crypto_amount = values[3]
                        jpy_amount = values[4]
                        if values[0] == "deposit":
                            total_crypto += float(crypto_amount)
                            total_jpy_deposit += float(jpy_amount)
                        if values[0] == "withdraw":
                            total_crypto -= float(crypto_amount)
                            total_jpy_withdraw += float(jpy_amount)
                    index += 1
                stats_message = f"""Right now you have {total_crypto} XLM Stellar Lumens.
    Since you started buying cryptos, you have spent {total_jpy_deposit} JPY yen in total.
    But you have solt cryptos valued in {total_jpy_withdraw} JPY yen. 
    You have a net balance of {total_jpy_withdraw - total_jpy_deposit} JPY yen.
    """
                print(proj_lib.intense_blue, stats_message, end_code)

        # Option 6: View real time value
        if option == 6:
            xlm_eur = WebsiteDataXLM()
            jpy_eur = WebsiteDataJPYEUR()
            print(f"{proj_lib.intense_blue}1 XML is equal to {float(xlm_eur)} euros (EUR).")
            print(f"1 XLM is equal to {float(xlm_eur) * float(jpy_eur)} yen (JPY).{end_code}")

        # Option 7: Graphic of the historical price
        if option == 7:
            print(f"{proj_lib.intense_green}Viewing graphic of the historical price of XLM...{end_code}")
            proj_lib.graph()

        # Option 8: Change password and username
        if option == 8:
            print(f"{proj_lib.intense_green}Now, you are able to change your current username and password for a new one: {end_code}")
            with open("login.csv", "w+") as login:
                new_login = csv.writer(login)
                user = input("Please enter your new username: ")
                password = input("Please enter your new password: ")
                new_login.writerow([user, password])
                print(f"{proj_lib.intense_green}Your new username is '{user}' and your new password is '{password}'.\n{end_code}")
            input("Press intro to exit the program")
            exit()

        # Option 9: Exit program
        if option == 9:
            print(f"{proj_lib.intense_green}Bye!{end_code}")
            exit()

        input("Press intro to continue: ")
        print("""
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """)

except:
    print("Oops, you did something wrong. Exiting the program.")
    exit()

