import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100, 0)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        result = account.withdraw(amount)
        if result == "Insufficient funds.":
            print(result)
        else:
            print(f"Withdrew: ${result}")
    elif command == "display":
        balance = account.display_balance()
        print(f"Current balance: ${balance}")
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()