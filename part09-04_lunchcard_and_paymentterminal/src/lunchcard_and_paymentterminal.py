# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000.0
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float) -> float:
        # A regular lunch costs 2.50 euros
        price = 2.50
        if payment >= price:
            self.funds += price
            self.lunches += 1
            return payment - price
        return payment

    def eat_special(self, payment: float) -> float:
        # A special lunch costs 4.30 euros
        price = 4.30
        if payment >= price:
            self.funds += price
            self.specials += 1
            return payment - price
        return payment

    def eat_lunch_lunchcard(self, card: LunchCard) -> bool:
        # A regular lunch costs 2.50 euros
        price = 2.50
        if card.subtract_from_balance(price):
            self.lunches += 1
            return True
        return False

    def eat_special_lunchcard(self, card: LunchCard) -> bool:
        # A special lunch costs 4.30 euros
        price = 4.30
        if card.subtract_from_balance(price):
            self.specials += 1
            return True
        return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.deposit_money(amount)
        self.funds += amount