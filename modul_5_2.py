class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    # def go_to(self, new_floor):
    #     if new_floor < 1 or new_floor > self.number_of_floors:
    #         print("Такого этажа не существует")
    #     else:
    #         for new_floor in range (new_floor):
    #             new_floor += 1
    #             print(f'\n{new_floor}', end = ' ')
    #         print()
    #
    def __len__(self):
        return  self.number_of_floors


    def __str__(self):
        return f'Название:{self.name}, кол-во этажей {self.number_of_floors}'


h1 = House(" ЖК Гродский", 18)
h2 = House(" ЖК Домик в деревне", 2)


#__str__
print(h1)
print(h2)

#__len__
print(len(h1))
print(len(h2))

