import random

ROWS = 3
COLS = 3
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}
symbol_values = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slop_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
    

def deposit():
    while True:
        amount = input('what would you like to deposit? $$ ')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break;
            else:
                print('amount should we greater than 0.')
        else: 
            print('Enter a number.')
    return amount

def get_number_of_line():
    while True:
        lines = input('Enter a number of lines you wanna bet in (1-'+str(MAX_LINES)+') ')
        if lines.isdigit():
            lines = int(lines)
            if MAX_LINES >= lines >= 1:
                break;
            else:
                print('Enter a valid number of lines.')
        else: 
            print('Enter a number.')
    return lines

def get_bet():
    while True:
        amount = input('what would you like to bet on each line? $$ ')
        if amount.isdigit():
            amount = int(amount)
            if MAX_BET >= amount >= MIN_BET:
                break;
            else:
                print(f'amount should be between ${MIN_BET} - ${MAX_BET}.')
        else: 
            print('Enter a number.')
    return amount


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else: 
            winnings += bet * values[symbol]
            winnings_lines.append(line + 1)
    return winnings, winnings_lines


def spin(balance):
    lines = get_number_of_line()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f'You do not have enough to bet that amount. Your current blance is ${balance}')
        else: break

    print(f'You are betting ${bet} on ${lines} lines. Total bet is ${total_bet}');

    solts = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slop_machine(solts)
    winnings, winning_lines= check_winnings(solts, lines, bet, symbol_values)
    print(f'you Won ${winnings}')
    print(f'You Won on lines:' , * winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f'Your balance is ${balance}')
        answer = input('Press Enter to spin Again(q to quite)')
        if answer == 'q':
            break
        balance += spin(balance)

    print(f'You left with total of ${balance}')

main()