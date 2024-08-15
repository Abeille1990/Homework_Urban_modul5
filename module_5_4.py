class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        instanse = super(House, cls).__new__(cls)
        return instanse

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

        House.houses_history.append((self.name, self.number_of_floors))

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')


h1 = House(" ЖК Эльбрус", 10)
for e in House.houses_history:
    print(e[0], e[1], end='', sep=' ')
print()
h2 = House(" ЖК Акация", 20)
for e in House.houses_history:
    print(e[0], e[1], end='', sep=' ')
print()
h3 = House(" ЖК Матрешки", 20)
for e in House.houses_history:
    print(e[0], e[1], end='', sep=' ')
print()
del h2
del h3
for e in House.houses_history:
    print(e[0], e[1], end='', sep=' ')
print()
del h1
