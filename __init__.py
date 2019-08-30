from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import sqlite3
import connectDB_createTB
import connectDB_fetchTB
import connectDB_operateTB
from colorama import init
init()
from colorama import Fore
print(Fore.MAGENTA)

def Registeration():
    name = input("Please enter name: ")
    for n in name:
        if n in sc:
            print("Name can not contain special character")
            name = ''
            Registeration()
        else:
            continue
    age = int(input("Please enter age: "))
    sex = input("Please enter sex[M or F]: ")
    for s in sex:
        if s in sc:
            print("Sex can not contain special character")
            sex = ''
            Registeration()
        else:
            continue
    initial_deposit = float(input("Please enter initial deposit: "))
    print(name, age, sex, initial_deposit)
    return name, age, sex, initial_deposit


if __name__ == '__main__':

    input1 = input("""\t\t\t\t You are using ABN AMRO Bank application
    Press 'A' to register, 'B' to check your details, 'C' to do a transaction """)

    sc = "~!@#$%^&*()_+=-}{\|:';""/>,<.1234567890"

    if input1 == 'B':
        name2 = input("Enter your name: ")
        recordB = connectDB_fetchTB.search(name2)
        print(recordB)
    elif input1 == exit:
        print("You are exiting")
    elif input1 == 'A':
        name, age, sex, initial_deposit = Registeration()
        connectDB_createTB.register(name, age, sex, initial_deposit)
    elif input1 == 'C':
        name3 = input("Enter your name: ")
        oper = input("Type 'W' to withdraw or 'D' for deposit: ")
        record = connectDB_fetchTB.search(name3)
        try:
            name, age, sex, initial_amount = record[0]
            if oper == 'D':
                deposit_amount = float(input("Enter value to deposit: "))
                initial_amount = initial_amount + deposit_amount
                connectDB_operateTB.credit(name3, initial_amount)
                print(f"Available balance: {initial_amount}")
            elif oper == 'W':
                withdraw_amount = float(input("Enter value to withdraw: "))
                if withdraw_amount > initial_amount:
                    print("Insufficiant funds!!")
                else:
                    initial_amount = initial_amount - withdraw_amount
                    connectDB_operateTB.debit(name3, initial_amount)
                    print(f"Available balance: {initial_amount}")
        except:
            print("Unregistered customer")
    else:
        print("Enter A or B or exit")


