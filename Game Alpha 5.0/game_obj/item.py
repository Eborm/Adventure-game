import math

class Item():
    def __init__(self, name: str, initial_cost: int, description : str):
        self.name = name
        self.initial_cost = initial_cost
        self.description = description
        self.cost : int = 0
        self.quantity : int = -1
        self.initial_quantity : int = -1
        
    def tick(self, economic_factor: float):
        self.cost = int(self.initial_cost * economic_factor)
        if (self.initial_quantity != -1):
            self.quantity = self.initial_quantity
        
    def sell(self, amount: int, player_money: int) -> bool:
        if (amount*self.cost <= player_money):
            if (self.initial_quantity == -1):
                return True
            elif (self.quantity >= amount):
                return True
        else:
            return False