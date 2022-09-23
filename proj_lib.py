# I will put all the code that I want to reuse in this file
colors = ["\033[0;30m", "\033[0;31m", "\033[0;32m", "\033[0;34m"]
end_code = "\033[00m"
bold_green = "\33[1;32m"


def author():
    return "Paula"


def maximum(a: int, b: int) -> int:
    if a > b:
        out = a
    else:
        out = b
    return out


def validate_int_input(msg:str)->int:
    """This function validates that the user enters an integer"""
    end_code = "\033[00m"
    red = "\033[0;31m"
    number = input(msg)
    while not number.isdigit():
        # number = input(f"{red}Error. {msg}{end_code}") # Lo he comentado para poder poner mi propio mensaje en EV_calculator
        number = input(f"{red}{msg}{end_code}")

    return int(number)


'''
r - read
w - write (rewrites)
a - append (adds to the file)
'''
