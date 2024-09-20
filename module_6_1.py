class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f'{self.name} съел {food.name}')
                self.fed = True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.alive = False
        else:
            raise TypeError("Пища должна быть растением.")

class Plant:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name, edible=True)

# Создаем объекты классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Проверка значений атрибутов
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

# Питание
a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)