#init method

class example:
    def __init__(self,food,amount):
        self.food=food
        self.amount=amount
    def foods(self):
        print(self.food, "amount is ", self.amount)
a=example("salad",200)
a.foods()
