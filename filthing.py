class Trader:
    def __init__(self, name, years_trading):
        self.name = name
        self.years_trading = years_trading
    
    def get_name(self):
        return self.name
    
    def get_years_trading(self):
        return self.years_trading
    
    def set_nickname(self, name):
        self.name = name

class Trading_Today:
    def __init__(self, name, max_traders):
        self.name = name
        self.max_traders = max_traders
        self.traders = []
    
    def add_trader(self, trader):
        if len(self.traders) < self.max_traders:
            self.traders.append(trader)
            return True
        else:
            return False
    
    def get_average_years_trading(self):
        value = 0
        for trade in self.traders:
            value += trade.get_years_trading()

        return value /len(self.traders)

    
    
a = Trader("Alex", 2)
b = Trader("Bradon", 10)
f = Trader("Fil", 3)

f.set_nickname("faggyfil")

trading_today = Trading_Today("YellowJacket", 2)
trading_today.add_trader(a)
trading_today.add_trader(b)

print(trading_today.get_average_years_trading())
