# Lecture 14 - OOP inheritance exercise
# Kod: Engelska
# Kommentarer: Svenska

class OldCoinsStash:
    def __init__(self, owner):
        self.owner = owner
        #   _namn  <-- är som vanligt privad "by convention"
        self._riksdaler = 0
        self._skilling = 0

    def deposit(self, riksdaler, skilling):
        if riksdaler <= 0 or skilling <= 0:
            raise ValueError(
                f"You try to deposit {riksdaler} riksdaler and {skilling} skilling they have to be positive")

        self._riksdaler += riksdaler
        self._skilling += skilling

    def withdraw(self, riksdaler, skilling):
        if riksdaler > self._riksdaler or skilling > self._skilling:
            raise ValueError(
                f"You cannot withdraw more than you have in your stash")

        self._riksdaler -= riksdaler
        self._skilling -= skilling

    def check_balance(self):
        return f"Coins in stash: {self._riksdaler} riksdaler, {self._skilling} skilling"

    def __repr__(self):
        return f"OldCoinStash(owner='{self.owner}')"
