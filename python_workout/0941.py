
print('Chapter 08 - Exercise 41')
print('Enforce a limit to scoops with a BigBowl instance variable with the ICPO rule.')


class Scoop:
    flavour: str

    def __init__(self, flavour):
        self.flavour = flavour
    
    def __repr__(self):
        return f"I'll have me a scoop-a' {self.flavour} yessir."


class Bowl:
    scoops: list
    def __init__(self, max_scoops = 3) -> None:
        self.scoops = []
        self.max_scoops = max_scoops

    def add_scoops(self, *scoops):
        for i, s in enumerate(scoops):
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(s)
            else:
               print(f"You're only allowed {self.max_scoops} scoops. Not adding {s.flavour}") 
    
    def __repr__(self):
        return "\n".join(s.flavour for s in self.scoops)

class BigBowl(Bowl):
    def __init__(self, max_scoops = 5) -> None:
        super().__init__()
        self.max_scoops = max_scoops

if __name__ == '__main__':
    scoop1 = Scoop('Raspberry')
    scoop2 = Scoop('Blueberry')
    scoop3 = Scoop('Vanilla')
    scoop4 = Scoop('Chocolate')
    scoop5 = Scoop('Melon')
    scoop6 = Scoop('Bubblegum')
    b = BigBowl()
    b.add_scoops(scoop1, scoop2)
    b.add_scoops(scoop3, scoop4)
    b.add_scoops(scoop5, scoop6)

    print(b)
