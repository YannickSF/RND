
from decTree.tools import Layer

""" Class qui hérite du Layer mais spécifique à notre cas des plantes. """


class PetalsNbLayer(Layer):
    def __init__(self):
        Layer.__init__(self, 'PetalsNbLayer')

    @staticmethod
    def rule(value):
        if value.nb_petals > 4:
            return True
        return False

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__().__str__()


class PetalslgtLayer(Layer):
    def __init__(self):
        Layer.__init__(self, 'PetalsLgtLayer')

    @staticmethod
    def rule(value):
        if value.petals_lentgh > 2.5:
            return True
        return False

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__().__str__()


class RootLgtLayer(Layer):
    def __init__(self):
        Layer.__init__(self, 'RootLgtLayer')

    @staticmethod
    def rule(value):
        if value.root_length > 15:
            return True
        return False

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__().__str__()
