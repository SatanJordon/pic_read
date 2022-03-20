from datetime import datetime

from dataService import insert_users_tax, read_users_account_by_carNumber, \
    read_users_tax_by_carNumber, update_users_tax_by_carNumber


def time_now():
    curDT = datetime.now()
    date_time = curDT.strftime("%m/%d/%Y, %H:%M:%S")
    return date_time


def calculate_amount(amount):
    return int(amount) + 100


def ifRegistered(number):
    users_account = read_users_account_by_carNumber(number)
    users_amount = read_users_tax_by_carNumber(number)

    if users_amount == [] and users_account == []:
        print("Not registered")
        insert_users_tax(number, time_now(), "N", "0")

    elif users_amount == [] and users_account[0][1] == number:
        insert_users_tax(number, time_now(), "Y", "100")

    else:
        if users_amount[0][1] == number:
            print("Not Registered" if users_account == [] else "Registered")
            a = "0" if users_account == [] else str(calculate_amount(users_amount[0][4]))
            update_users_tax_by_carNumber(number, time_now(), a)
