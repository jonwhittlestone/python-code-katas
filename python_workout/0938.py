print('Chapter 08 - Exercise 38')
print('Create Ice Cream scoop objects')
print('')


class Scoop:
    flavour: str

    def __init__(self, flavour):
        self.flavour = flavour


def create_scoops():
    flavours = ['chocolate', 'vanilla', 'raspberry']
    return [Scoop(f) for f in flavours]


if __name__ == '__main__':
    for s in create_scoops():
        print(f"Ice Cream scoop with flavour: {s.flavour}")
