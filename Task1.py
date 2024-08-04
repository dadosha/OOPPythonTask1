class Animal:
    def __init__(self, name, type_animal, sound, weight):
        self.name = name
        self.type_animal = type_animal
        self.sound = sound
        self.weight = weight

    def eat(self, weight_eat):
        self.weight += weight_eat
        print(f'Покормили {self.type_animal} по имени {self.name}')

    def music(self):
        print(f'{self.type_animal} издает звук {self.sound}')


class Bird(Animal):
    def get_eggs(self):
        print(f'Собрали яйца у {self.type_animal} с именем {self.name}')


class Sheep(Animal):
    def shear(self):
        print(f'Постригли {self.type_animal} с именем {self.name}')


class CowGoat(Animal):
    def milk(self):
        print(f'Подоили {self.type_animal} с именем {self.name}')


list_animal = []

gray = Bird('Серый', "Гусь", "Га-га", 20)
list_animal.append(gray)

white = Bird('Белый', "Гусь", "Га-га", 15)
list_animal.append(white)

lamb = Sheep('Барашек', "Овца", "Беее", 70)
list_animal.append(lamb)

curly = Sheep('Кудрявый', "Овца", "Беее", 62)
list_animal.append(curly)

koko = Sheep('Ко-Ко', "Курица", "Кукареку", 8)
list_animal.append(koko)

chicken = Sheep('Кукареку', "Курица", "Кукареку", 9)
list_animal.append(chicken)

manka = CowGoat('Манька', "Корова", "Мууу", 150)
list_animal.append(manka)

hooves = Sheep('Копыта', "Коза", "Меее", 57)
list_animal.append(hooves)

horns = Sheep('Рога', "Коза", "Меее", 50)
list_animal.append(horns)

duck = Sheep('Кряква', "Утка", "Кря-кря", 15)
list_animal.append(duck)


max_weight = 0
all_weight = 0
max_weight_animal = {}

for animal in list_animal:
    if animal.weight > max_weight:
        max_weight = animal.weight
        max_weight_animal = animal
    all_weight += animal.weight

print(all_weight)
print(max_weight_animal.weight)
