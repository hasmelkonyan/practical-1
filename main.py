import math
import time


def my_name_surname():

    """This function asks for the user's name, surname and address information and prints it on the screen
    """

    name = input("Input your name: ")
    surname = input("Input your surname: ")
    address = input("Input your address: ")
    return f"My name is {name} {surname} from {address}"


def hello():

    """This function asks for the user's name and welcomes on the screen using the name
    """

    name = input(f"Input your name: ")
    print(f"Hello {name}")


def room_area():

    """This function gets room's length and width from the user and calculates area of the room
    """

    length = float(input("Input length of the room: "))
    height = float(input("Input height of the room: "))
    area = length * height
    return f"The area of your room is {area} square metre"


def area_field():

    """This function gets length and width from the user in feet and counts the area in acres
    """

    length = int(input("Input length of the field by pound: "))
    width = int(input("Input width of the field by pound: "))
    area = length * width / 43560
    return f"Area of your field is {area} acre"


def bottle_price():

    """This function asks the user quantity of bottles of less or more than 1 liter and shows the total amount
    """

    little_bottles = int(input("Bottles up to 1 liter: "))
    big_bottles = int(input("Bottles more than 1 liter: "))
    total_price = little_bottles * 0.10 + big_bottles * 0.25
    total_price = format(total_price, '.2f')
    return f"the total amount  for your bottles is ${total_price}"


def total_pay():

    """This function asks the user the amount of the restaurant order, then calculates the taxes, the tip and the
     total amount to be paid
     """

    order_amount = float(input("Input order amount: "))
    tip = order_amount * 0.18
    tax = (order_amount + tip) * 0.2
    total = order_amount + tip + tax
    tip = format(tip, '.2f')
    tax = format(tax, '.2f')
    total = format(total, '.2f')
    return f"tip: {tip} fee: {tax} total amount: {total}"


def sum():

    """This function asks the user any number, then calculates sum from 0 to the number
    """

    sum_to_n = 0
    n = int(input("input number: "))
    for each in range(n):
        sum_to_n += each
    print(f"The sum from 0 to the {n} is {sum_to_n}")


def total_weight():

    """This function asks the user for the quantity of souvenirs and small items he has bought, calculates the
    total purchase weight and writes it on the screen
    """

    weight_of_souvenir = 75
    weight_of_small_items = 112
    quantity_of_souvenir = int(input("How many souvenirs did you buy?։ "))
    quantity_of_small_item = int(input("How many trifles did you buy?։ "))
    total = weight_of_souvenir * quantity_of_souvenir + weight_of_small_items * quantity_of_small_item
    print(f"The total weight of your purchases is: {total} gram")


def deposit_balance():

    """This function asks the user the amount of the initial investment, after which he calculates and brings out the
    balance of the first, second and third years on the screen.
    """

    deposit_amount = float(input("How much is your deposit?  "))
    percent_for_year = 4
    for each in range(1, 4):
        annual_income = deposit_amount * 0.04
        deposit_amount += annual_income
        print(f"will be your deposit balance in {each} year: {deposit_amount}")


def calc():

    """This function asks the user the values of the numbers a and b, then prints on the screen their sum, the
    difference, a divided by b, the whole part of a divided by b, the remainder of a divided by b and the decimal
    logarithm of a
    """

    a = int(input("Input first number: "))
    b = int(input("Input second number: "))
    if b == 0:
        raise ZeroDivisionError("The second number have to be not zero!")
    else:
        print(f"the sum of the entered numbers։ {a + b}")
        print(f"subtraction of entered numbers: {a - b}")
        print(f"The first number divided by the second number։ {a / b}")
        print(f"the whole part of the first number divided by the second number: {a // b}")
        print(f"the remainder of the first number divided by the second number: {a % b}")
        print(f"the decimal logarithm of first number: {math.log10(a)}")


def fuel_calc():

    """This function asks the user for MPG fuel consumption and out to L / 100km.
    """

    fuel_mpg = float(input("Input fuel in Miles per gallon: "))
    fuel_liter_per_100_km = fuel_mpg / 235.215
    print(f"{fuel_mpg} MPG fuel is equal to {fuel_liter_per_100_km} Liter per 100 kilometers")


def height_calc():

    """This function asks the user for his height in feet or inches and calculates it and prints it on the screen in cm
    """

    unit = input("If you want to input your height in\nfeet: press 1\ninches: press 2\nfor exit: "
                 "press another key: ")
    if unit == "1":
        height = float(input("Input your height in feet: "))
        height_in_cm = height * 30.48
        print(f"Your height is {height_in_cm}cm")
        return height_calc()
    elif unit == "2":
        height = float(input("Input your height in inches: "))
        height_in_cm = height * 2.54
        print(f"Your height is {height_in_cm}cm")
        return height_calc()
    else:
        print("Bye!")


def length_calc():

    """This function asks the user for the distance in feet, then it calculates in inches, yards and miles and prints
    them on the screen
    """

    length_in_feet = float(input("Input length in feet: "))
    length_in_inches = length_in_feet * 12
    length_in_yards = length_in_feet / 3
    length_in_miles = length_in_feet / 5280
    print(f"{length_in_feet} feet is {length_in_inches} inches or {length_in_yards} yards or {length_in_miles} miles")


def area_volume():

    """This function asks the user for the radius, then prints the area of the circle with that radius and the volume
    of the sphere with that radius
    """

    r = float(input("Input radius: "))
    area = math.pi * (r ** 2)
    volume = 4 * (math.pi * r ** 3) / 3
    print(f"area is: {area}\nvolume is: {volume}")


def volume_of_cylinder():

    """This function asks the user for the height of the cylinder and the radius of the base, then calculates and prints
    the volume of the cylinder on the screen
    """

    radius = float(input("Input radius: "))
    height = float(input("input height: "))
    volume = height * (math.pi * radius ** 2)
    volume = format(volume, ".1f")
    print(f"The volume of cylinder with height {height} and with base radius {radius} is {volume}")


def final_speed():

    """This function asks the user for the height d, then calculates the speed of the object thrown from the height
    d without the initial speed when it reaches the ground
    """

    height = float(input("Input height: "))
    g = 9.8
    speed = math.sqrt(2 * g * height)
    print(f"final speed is {speed}")


def area_of_triangle():

    """This function asks the user for the height and base of the triangle, then prints the area of the triangle on the
    screen
    """

    height = float(input("The height of triangle is: "))
    base = float(input("The base of triangle is: "))
    area = (height * base) / 2
    print(f"Area of triangle is {area}")


def area_triangle_2():

    """This function asks the user triangle's sides, then prints the area of the triangles on the screen
    """

    sight1 = float(input("input first sight of triangle: "))
    sight2 = float(input("input second sight of triangle: "))
    sight3 = float(input("input third sight of triangle: "))
    s = (sight1 + sight2 + sight3) / 2
    area = math.sqrt(s * (s - sight1) * (s - sight2) * (s - sight3))
    print(f"Area of triangle is {area}")


def calc_seconds():

    """This function asks the user for the number of days, hours, minutes and seconds, then prints that period in
    seconds on the screen
    """

    days = int(input("Input days: "))
    hours = int(input("Input hours: "))
    minutes = int(input("Input minutes: "))
    seconds = int(input("Input seconds: "))
    total_seconds = seconds + minutes * 60 + hours * 3600 + days * 86400
    print(f"Total seconds in {days} days, {hours} hours {minutes} minutes and {seconds} seconds is {total_seconds}"
          f" seconds")


def current_time():

    """this function returns the current time
    """

    return time.asctime()


def month_days():

    """This function asks the user the month name and print on the screen how many days the month has
    """

    month_name = (input("Input month name: ")).capitalize()
    if month_name in ("January", "March", "May", "July", "August", "October", "December"):
        print(f"{month_name} has 31 days")
    elif month_name in ("April", "June", "September", "November"):
        print(f"{month_name} has 30 days")
    elif month_name == "February":
        print(f"{month_name} has 28 days, if year is leap or 29 days, if year is not leap")
    else:
        print("Wrong data!!!")


def consonant_or_vocal():

    """This function asks the user the letter's name and prints on the screen that letter is consonant or vocal
    """

    letter = input("Input a letter: ").lower()
    if letter in ("a", "i", "o", "u", "e"):
        print(f"{letter} is vocal letter")
    elif letter == "y":
        print(f"{letter} can be both vowel and consonant letter")
    elif letter in ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"):
        print(f"{letter} is  consonant letter")
    else:
        print("wrong data!")


def seasons():

    """This function asks the user month name and day of month and prints on the screen what season is it
    """

    month = input("Input name of the month: ").capitalize()
    day = int(input("Input day of the month: "))
    if month in ("December", "January", "February"):
        if month == "January" or month == "December" and 21 < day < 32 or month == "February":
            print(f"{month} {day} is winter")
        elif month == "December" and 0 < day < 21:
            print(f"{month} {day} is autumn")
        else:
            print("Wrong data!")
    elif month in ("March", "April", "May"):
        if month in ("April", "May") or month == "March" and 21 < day < 32:
            print(f"{month} {day} is spring")
        elif month == "March" and 0 < day < 21:
            print(f"{month} {day} is winter")
        else:
            print("Wrong data!")
    elif month in ("June", "July", "August"):
        if month in ("July", "August") or month == "June" and 21 < day < 31:
            print(f"{month} {day} is summer")
        elif month == "June" and 0 < day < 21:
            print(f"{month} {day} is spring")
        else:
            print("Wrong data!")
    elif month in ("September", "October", "November"):
        if month in ("October", "November") or month == "September" and 21 < day < 31:
            print(f"{month} {day} is autumn")
        elif month == "September" and 0 < day < 21:
            print(f"{month} {day} is summer")
        else:
            print("Wrong data!")
    else:
        print("Wrong data!")


def write_number():
    return int(input("Input digit: "))


def the_arithmetic_average():

    """This function calculates the arithmetic average of all the numbers entered by the user and prints it on the
    screen
    """

    print("Input the different numbers from 0 whose arithmetic mean you want to count, and 0, for exit")
    sum, quantity = 0, 0
    digit = write_number()
    while digit != 0:
        sum += digit
        quantity += 1
        digit = write_number()
    if quantity == 0:
        print("Bye!")
    else:
        arithmetic_average = sum / quantity
        print(f"The arithmetic mean of the numbers you input is {arithmetic_average}")


def celsius_to_fahrenheit():
    for i in range(11):
        celsius = i * 10
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius}C | {fahrenheit}F")


def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz-Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def unrepeatable_words():

    """This function asks the user for words and prints them, but repeated words prints only once
    """

    words = input("Write some words: ")
    words_lst = list(words.split(" "))
    words_set = set(words_lst)
    for word in words_set:
        print(word)


def number_divisors(num):

    """This function gets one parameter

    :param num:
    prints divisors for num
    """

    print(f"divisors for {num} are: ")
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            print(i)


def user_number_divisors():

    """This function asks the user a number and prints divisors of that number
    """

    num = int(input("Input number: "))
    number_divisors(num)


def is_perfect_number(num):

    """This function gets one parameter

    :param num:
    :return: is it perfect number or not
    """

    divisors_sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisors_sum += i
    if num == divisors_sum:
        return True
    return False


def is_palindrome():

    """this function asks the user the sentence and returns that sentence is palindrome or not
    """

    sentence = input("Input sentence: ").lower()
    lst_sentence = sentence.split(" ")
    print(lst_sentence)
    for i in range(len(lst_sentence) // 2):
        if lst_sentence[i] != lst_sentence[-(i + 1)]:
            return False
    return True


def compression_of_numbers():
    sum, quan = 0, 0
    lst = []
    num = write_number()
    lst.append(num)
    while num != 0:
        sum += num
        quan += 1
        num = write_number()
        lst.append(num)
    average = sum / quan
    lst = list(set(lst))
    print(f"entered numbers that are larger than the {average} arithmetic mean")
    for el in lst:
        if el > average:
            print(el)
    print(f"entered numbers that are smaller than the {average} arithmetic mean")
    for el in lst:
        if el < average:
            print(el)
    for el in lst:
        if el == average:
            print(f"There is a number equal to the {average} average number in the entered numbers")




print(compression_of_numbers())