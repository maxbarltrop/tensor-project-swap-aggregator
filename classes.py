class Node:
    def __init__(self, amount, previous, exchangeName):
        self.amount = amount
        self.previous = previous
        self.exchangeName = exchangeName

    def __repr__(self):
        return (str(self.amount) + ", " + str(self.exchangeName) + ", " + str(self.previous))

    def update(self, amount, previous, exchangeName):
        self.amount = amount
        self.previous = previous
        self.exchangeName = exchangeName


class Pair:
    def __init__(self, rate, exchangeName):
        self.rate = rate
        self.exchangeName = exchangeName

    def __repr__(self):
        return (str(self.rate) + ", " + str(self.exchangeName))


class Exchange:
    def __init__(self, name, market):
        self.name = name
        self.market = market
