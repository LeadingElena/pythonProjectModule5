class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) == len(other) or len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) == len(other) or len(self) > len(other)

    def __ne__(self, other):
        return len(self) != len(other)

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        self.number_of_floors = self.number_of_floors - value
        return self

    def __mul__(self, value):
        self.number_of_floors = self.number_of_floors * value
        return self

    def __truediv__(self, value):
        self.number_of_floors = self.number_of_floors / value
        return self

    def __divmod__(self, value):
        self.number_of_floors = self.number_of_floors //value
        return self

    def __pow__(self, power, modulo=None):
        self.number_of_floors = self.number_of_floors ** power
        return self


    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print ('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h1.go_to(5)
# h2.go_to(10)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
# print(len(h1))
# print(len(h2))

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)

print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__