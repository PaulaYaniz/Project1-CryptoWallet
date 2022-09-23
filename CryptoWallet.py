from proj_lib import validate_int_input, end_code, colors, bold_green
import datetime
import csv

# INTRO
# while True:
welcome_msg = "Welcome to your digital DOGECOIN ledger".center(50, "·")
description_msg = "Dogecoin is a cryptocurrency created as an initial joke, making fun of the wild speculation in cryptocurrencies at the time.\nIt is considered both the first meme coin, and, more specifically, the first dog coin. \n"
doge_art = '''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣀⣤⠀⣤⡄⡤⣤⢤⣀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡐⠯⠹⣛⣋⢠⣭⣥⣭⣬⣬⣋⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣘⠧⣓⢥⣶⣿⣿⣿⣷⣝⣿⣏⠰⣹⣿⠁    
⠀⠀⠀⠀⠀⠀⡀⣶⣿⣿⢟⣥⣾⣏⡏⠫⠯⠊⢱⣿⣿⣮⢿⣿⣿⠃      DOGECOIN
⠀⠀⠀⠀⠀⠀⠘⢮⡻⣫⣾⣿⡳⠡⠀⢀⡀⠀⠹⣻⣿⣿⣎⣿⠃         TO THE
⠀⠀⠀⠀⠀⠀⠀⢠⠸⡞⣿⣿⡇⢘⡂⡀⠀⠀⠀⣿⣿⣿⡟⠀⠀⠀⠀         MOON
⠀⠀⢀⣠⣶⡶⠶⠶⠤⠙⣞⣿⣞⢄⡀⠀⠀⣀⢜⢞⡿⠋⠀⠀⠀⠀⠀        !!!
⠀⢠⠿⢿⣿⣿⡿⠒⠀⠀⠈⢮⣻⣿⣾⣿⣿⣾⠵⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⣿⣿⠋⢀⣀⣠⡄⠀⣀⠑⢝⠿⢝⣫⣵⡞⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⣿⣯⣶⣿⣿⣿⡇⣠⡟⡘⠀⢦⢿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣾⣿⣿⣿⣿⠟⠁⣿⣿⡿⡡⠁⠀⠈⠋⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠼⠿⠿⠟⠋⠁⠀⠾⠛⠉⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
'''
prompt_msg = "Please enter an option [1-5]: "

print(f"{colors[2]}{welcome_msg}{end_code}")
print(description_msg, f"{colors[3]}{doge_art}{end_code}")
print(f"{colors[1]}Options{end_code}".center(20))

menu = """1. Show all data
2. Enter transaction
3. Withdraw transaction
4. Record transaction
5. Edit past transactions
6. View real-time value of Dogecoin
7. Edit password
"""
print(menu)
option = validate_int_input(prompt_msg)
while option > 5 or option < 1:
    option = validate_int_input(f"{colors[1]}Invalid option. {prompt_msg}{end_code}")


# Option 1: Show all data
with open("data_transactions.csv", "r") as file:
    all_transactions = file.readlines()

if option == 1:
    print(f"{bold_green}Showing all data: {end_code}")
    index = 0
    for transaction in all_transactions:
        if index > 0:
            # print(transaction.strip())  # strip removes the \n at the end of the line
            print(f"No.{index}: {transaction}", end="")
        index += 1
    # print(all_transactions)

# Option 2: Enter data (rewrite?)
# should I create this new csv file or should I use the original one? even if then the data is rewritten and lost
# Why is it not working?
if option == "2":
    with open("new_data_transactions.csv", "w+") as file:
        myFile = csv.writer(file)
        myFile.writerow(["transaction", "crypto_amount", "value"])
        num_transactions = int(input("Please enter how many transactions you want to do: "))
        for i in range(num_transactions):
            transaction = input("Transaction " + str(i+1) + ": Please enter the transaction type: ")
            crypto_amount = input("Transaction " + str(i+1) + f": Please enter the crypto amount you {transaction}: ")
            value = input("Transaction " + str(i+1) + ": Please enter in JPY yen the value of your transaction: ")
            myFile.writerow([transaction, crypto_amount, value])


# Option 4: Record transaction (probando)
if option == "4":
    with open("data_transactions.csv", "r") as file:
        all_transactions = file.readlines()

    transaction = []
    crypto_amount = []
    value = []

    for row in all_transactions:
        transaction.append(row[0])
        crypto_amount.append(row[1])
        value.append(row[2])

    print(transaction)
    print(crypto_amount)
    print(value)


# Option 5: Edit data
if option == "5":
    myList = []

    with open('data_transactions.csv', 'r') as file:
        myFile = csv.reader(file)
        for row in myFile:
            myList.append(row)

    # Show the content of the file and print row number to make selection easy
    print("Please see details of the csv file below:")
    for i in range(len(myList)):
        print("Row " + str(i) + ": " + str(myList[i]))

    # User selects which row to edit
    editRow = int(input("\nWhich row would you like to change? Enter 1 - " + str(len(myList) - 1) + ": "))
    print("Please enter the new details for each of the following :")

    # User adds the changes and appends changes to the list
    for i in range(len(myList[0])):
        newDetails = input("Enter new data for " + str(myList[0][i]) + ": ")
        myList[editRow][i] = newDetails

    # Show the new list
    print("\nPlease see the details of the new file below:")
    for i in range(len(myList)):
        print("Row " + str(i) + " :" + str(myList[i]))

    # PROBLEM: DOES NOT SAVE CHANGES
    # Confirm changes
    changes = input("\nWould you like to confirm the changes to the digital ledger? [Y/N]: ").lower()

    if changes == "y":
        with open('data_transactions.csv', 'w+') as file:
            # myFile = csv.writer(file)
            for i in range(len(myList)):
                myFile.writerow(myList[i])
                print("Row " + str(i) + " :" + str(myList[i]))


