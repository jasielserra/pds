apples = [20,4,5,10,15]

""" Programming Total Object Oriented! """

class Sorted:
    def __init__(self, items):
        self.data = items

    def head(self):
        return max(self.data)

def consumer1(cesta):
    """ Pega a maçã mais pesada."""

    s = Sorted(cesta)
    return s.head()

print(consumer1(apples))