import random

# Function to spin a row of the slot machine
def spin_row():
    symbols = ['🍒', '🍉','🍋','🔔','⭐']  # List of possible symbols

    results = []
    for symbol in range(3):  # Spin three times to get three symbols
        results.append(random.choice(symbols))  # Randomly choose a symbol
    return results  # Return the list of symbols

# Function to print the row of symbols
def print_row(row):
    print("*************")
    print(" | ".join(row))  # Join the symbols with ' | ' and print
    print("*************")

# Function to calculate the payout based on the row and bet amount
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:  # Check if all three symbols are the same
        if row[0] == '🍒':
            return bet * 3  # Payout for three cherries
        elif row[0] == '🍉':
            return bet * 4  # Payout for three watermelons
        elif row[0] == '🍋':
            return bet * 5  # Payout for three lemons
        elif row[0] == '🔔':
            return bet * 10  # Payout for three bells
        elif row[0] == '⭐':
            return bet * 20  # Payout for three stars

    return 0  # No payout if symbols don't match

# Main function to run the slot machine game
def main():
    balance = 100  # Starting balance
    print("*************************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*************************")

    while balance > 0:  # Continue playing while there is balance
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():  # Check if the bet is a valid number
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:  # Check if the bet is more than the balance
            print("Insufficient funds")
            continue

        if bet <= 0:  # Check if the bet is greater than 0
            print("Bet must be greater than 0")
            continue

        balance -= bet  # Deduct the bet from the balance

        row = spin_row()  # Spin the slot machine
        print("Spinning....\n")
        print_row(row)  # Print the result

        payout = get_payout(row, bet)  # Calculate the payout

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout  # Add the payout to the balance

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != 'Y':  # Exit the game if the player doesn't want to continue
            break

    print("********************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("********************************************")

if __name__ == '__main__':
    main()  # Run the main function
