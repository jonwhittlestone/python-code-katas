print('Chapter 09 - Exercise 43')
print('Create a set of Animal classes for a zoo using methods, attributes, composition and inheritance.')

# The book says that readability can be improved
# with the init statement on the base class
# being used to instantiate all attributes
# eg:
# class Animal():
#     def __init__(self, color, number_of_legs):     ❶
#         self.species = self.__class__.__name__     ❷
#         self.color = color
#         self.number_of_legs = number_of_legs

# class Wolf(Animal):
#     def __init__(self, color):
#         super().__init__(color, 4)


class Animal:
    def __init__(self, species):
        self.species = species

    def __repr__(self):
        return f"{self.colour} {self.species} {self.number_of_legs} legs"


class Sheep(Animal):
    species = 'Sheep'
    number_of_legs = 4

    def __init__(self, colour):
        super().__init__(self.species)
        self.colour = colour


class Wolf(Animal):
    species = 'Wolf'
    number_of_legs = 4

    def __init__(self, colour):
        super().__init__(self.species)
        self.colour = colour


class Snake(Animal):
    species = 'Snake'
    number_of_legs = 0

    def __init__(self, colour):
        super().__init__(self.species)
        self.colour = colour


class Parrot(Animal):
    species = 'Parrot'
    number_of_legs = 0

    def __init__(self, colour):
        super().__init__(self.species)
        self.colour = colour


if __name__ == '__main__':
    the_sheep = Sheep('White')
    the_wolf = Wolf('Grey')
    the_snake = Snake('Green')
    the_parrot = Parrot('Multi-colour')
    print(the_sheep)
    print(the_wolf)
    print(the_snake)
    print(the_parrot)
