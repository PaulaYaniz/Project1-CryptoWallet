def login(user: str, password: str) -> bool:
    """
    :param user: string
    :param password: string
    :return: true or false
    """
    # result = login(user=input("Please enter the user: "), password=input("Please enter the password: "))

    with open("login.csv") as file:
        database = file.readlines()
    output = False
    for line in database:
        clear_line = line.strip()
        separated_line = clear_line.split(",")
        if user == separated_line[0] and password == separated_line[1]:
            output = True

    return output

# result = login(user=input("Please enter the user: "), password=input("Please enter the password: "))
