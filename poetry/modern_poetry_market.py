# Modern Poetry Market

class ModernPoetryMarket:
    def __init__(self, poems):
        self.poems = poems
        self.state = ['stale', 'stinky', 'rotting', 'dead']

    @classmethod
    def meta(cls, poem):
        return poem.write(poem)

    @classmethod
    def anti(cls, poem):
        return poem.diss(poem)

    @classmethod
    def non(cls, poem):
        return poem.remove(poem)

    @classmethod
    def eat(cls, poem):
        return cls.meta(cls.meta(cls.anti(cls.anti(cls.non(cls.non(poem))))))


market = ModernPoetryMarket(kusa_poems)
if man.tooth == market.eat(poem):
    man.tooth = me.tooth
    man.status = 'bad dealer'
else:
    man.status = 'good dealer'
