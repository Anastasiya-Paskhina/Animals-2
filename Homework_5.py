class Animals:
    name = 'Unname'
    weight = 0
    voice = 'none'
    feed = True
    product_animal = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def collect_product(self, volume_product):
        self.product_animal -= volume_product

    def food(self, hungry):
        self.feed = False
        self.weight += hungry


class Goose(Animals):
    voice = 'Ga-ga-ga'
    product_animal = 3  # яйца


class Cow(Animals):
    voice = 'Muuuu'
    product_animal = 15  # литров


class Sheep(Animals):
    voice = 'Me-e-e'
    product_animal = 2  # кг шерсти


class Chicken(Animals):
    voice = 'Cocococo'
    product_animal = 5  # яиц


class Goat(Animals):
    voice = 'Be-e-e-e'
    product_animal = 2  # литра


class Duck(Animals):
    voice = 'Crya-Crya'
    product_animal = 2  # яицa


goose_1 = Goose('Серый', 2)
goose_2 = Goose('Белый', 3)
cow = Cow('Манька', 600)
sheep_1 = Sheep('Барашек', 20)
sheep_2 = Sheep('Кудрявый', 15)
chicken_1 = Chicken('Ко-ко', 3)
chicken_2 = Chicken('Кукареку', 4)
goat_1 = Goat('Рога', 30)
goat_2 = Goat('Копыта', 25)
duck = Duck('Кряква', 5)

goose_1.food(0.2)
goose_2.food(0.2)
cow.food(3)
sheep_1.food(1.5)
sheep_2.food(1.5)
chicken_1.food(0.1)
chicken_2.food(0.1)
goat_1.food(0.2)
goat_2.food(0.2)
duck.food(0.1)


goose_1.collect_product(3)
goose_2.collect_product(3)
cow.collect_product(15)
sheep_1.collect_product(2)
sheep_2.collect_product(2)
chicken_1.collect_product(5)
chicken_2.collect_product(5)
goat_1.collect_product(2)
goat_2.collect_product(2)
duck.collect_product(2)

zoo = [goose_1, goose_2, cow, sheep_1, sheep_2, chicken_1, chicken_2, goat_1, goat_2, duck]

total_weight = 0
max_weight = 0
heaviest_animal = str()
for animal in zoo:
    total_weight += animal.weight
    if animal.weight > max_weight:
        max_weight = animal.weight
        heaviest_animal = animal.name

print('Вес всех животных {} кг'.format(total_weight))
print('Самое тяжелое животное {}'.format(heaviest_animal))
