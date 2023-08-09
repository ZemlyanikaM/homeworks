from animal import Cat, Fish, Bird


class AnimalFactory:
    TYPES = {"bird": Bird, "cat": Cat, "fish": Fish}

    def get_animal(self, animal_type: str, *args, **kwargs):
        factory_animal = self._choose_type(animal_type)
        return factory_animal(*args, **kwargs)

    def _choose_type(self, animal_type: str):
        return self.TYPES[animal_type.lower()]


if __name__ == '__main__':
    fabric = AnimalFactory()
    fish = fabric.get_animal('fish', 'Flounder', 'orange', 10.2, 15.0)
    bird = fabric.get_animal('bird', 'Chichi', 'white', 82.3, 'forest')
    cat = fabric.get_animal('cat', 'Tom', 'black', 11, True)
    animals = (fish, bird, cat)
    for animal in animals:
        animal.show_info()
        animal.show_unique()
        print()

