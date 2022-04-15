apples = [20,4,5,10,15]

""" Procedural Programming with Class"""

class Sorted:
    def __init__(self, items):
        self.data = items

    def head(self):
        self.data.sort()
        return self.data[-1]

def consumer1(cesta):
    """ Pega a maçã mais pesada."""

    s = Sorted(cesta)
    return s.head()


print(consumer1(apples))