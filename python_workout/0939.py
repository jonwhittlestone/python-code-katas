
print('Chapter 09 - Exercise 39')
print('Create Ice Cream scoop objects, and have a Bowl object add them')
print('')


class Scoop:
    flavour: str

    def __init__(self, flavour):
        self.flavour = flavour
    
    def __repr__(self):
        return f"I'll have me a scoop-a' {self.flavour} yessir."


class Bowl:
    scoops: list
    def __init__(self) -> None:
        self.scoops = []

    def add_scoops(self, *scoops):
        for s in scoops:
            self.scoops.append(s)


if __name__ == '__main__':
    scoop1 = Scoop('Raspberry')
    scoop2 = Scoop('Blueberry')
    b = Bowl()
    b.add_scoops(scoop1, scoop2)

    for s in b.scoops:
        print(s)
