# import itertools
beerTable = []

class BeerEntry(object):
    class_counter= 1
    def __init__(self,man,model,volume,quantity,price):
        self.man = man
        self.model = model
        self.volume = volume
        self.quantity = quantity
        self.price = price
        self.id= BeerEntry.class_counter
        BeerEntry.class_counter += 1

beerTable.append(BeerEntry(man='Miller',
                    model='High Life',
                    volume=12,
                    quantity=12,
                    price=8.99    )
                )

beerTable.append(BeerEntry(man='Miller',
                    model='Lite',
                    volume=12,
                    quantity=12,
                    price=9.99    )
                )

for beer in beerTable:
    print(beer.model)
    print(beer.id)

print(len(beerTable))
