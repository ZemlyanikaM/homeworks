from datetime import date

account = 0
count = 0
cashout_fee = 0.015
third_operation_fee = 0.03
wealth_tax = 0.1


def cash_in(cash: float) -> None:
    global account
    global count
    account += cash
    count += 1
    if count % 3 == 0:
        add_third_op_bonus()


def add_third_op_bonus():
    global account
    account = account + third_operation_fee * account
    print("Third operation bonus added: ", third_operation_fee * account)


def cash_out(cash: float) -> None:
    global account
    global count
    account -= cash
    count += 1
    message = "The cashout fee is took: "

    if cash * cashout_fee < 30:
        account -= 30
        print(message, 30)
    elif cash * cashout_fee > 600:
        account -= 600
        print(message, 600)
    else:
        account -= cash * cashout_fee
        print(message, cash * cashout_fee)
    if count % 3 == 0:
        add_third_op_bonus()


def quit_acc():
    print("Have a nice day! See you later! \n")
    exit()

def check_value() -> int:
    while True:
        cash = int(input("Enter the transaction amount in multiples of 50\n"))
        if cash % 50 == 0:
            return cash


def get_wealth_tax():
    global account
    fee = account * wealth_tax
    account = account - fee
    print("The wealth tax is took", fee)


def show_balance():
    print("The account balance is: ", account)


list_op_history = []

while True:
    action = input("1 - cash-out\n2 - cash-in\n3 - the account balance\n4 - the list of operations\n5 - quit\n")

    if action == '1':
        if account > 5_000_000:
            get_wealth_tax()
        cash = check_value()
        if cash < account:
            cash_out(cash)
            list_op_history.append([str(date.today()), -1 * cash])
        else:
            print("Insufficient funds!\n")
        if account > 5_000_000:
            get_wealth_tax()
        show_balance()
    elif action == '2':
        if account > 5_000_000:
            get_wealth_tax()
        cash = check_value()
        cash_in(cash)
        show_balance()
        list_op_history.append([str(date.today()), cash])

    elif action == '3':
        show_balance()
    elif action == '4':
        print(list_op_history)
    else:
        quit_acc()