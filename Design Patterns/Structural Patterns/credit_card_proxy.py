from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CashBundle(Payment):
    def pay(self, amount):
        print(f"Paying {amount} in cash.")

class BankAccount(Payment):
    def __init__(self, account_number):
        self.account_number = account_number

    def pay(self, amount):
        print(f"Paying {amount} from account number {self.account_number}.")

class CreditCard(Payment):
    def __init__(self, bank_account):
        self.bank_account = bank_account

    def pay(self, amount):
        print("Using credit card to pay...")
        self.bank_account.pay(amount)

# Example usage
bundle_of_cash = CashBundle()
bank_account = BankAccount("35054583159")
credit_card = CreditCard(bank_account)

bundle_of_cash.pay(50) # Pays in cash
bank_account.pay(100) # Pays from bank account
credit_card.pay(200) # Uses credit card to pay from bank account
