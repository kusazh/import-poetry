# Modern Poetry Market

class ModernPoetryMarket:
    states = ['stale', 'stinky', 'rotting', 'dead']

    def __init__(self, poems):
        self.poems = poems

    def meta(self, poem):
        return poem.write(poem)

    def anti(self, poem):
        return poem.diss(poem)

    def non(self, poem):
        return poem.remove(poem)

    def eat(self, man, poem):
        man.tooth = me.tooth
        return self.meta(self.meta(self.anti(self.anti(self.non(self.non(poem))))))


market = ModernPoetryMarket(kusa_poems)
if market.eat(man, poem):
    man.status = 'bad dealer'
else:
    man.status = 'good dealer'
