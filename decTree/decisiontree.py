

class DecisionTree:
    """ Algorithme de Decision => Class"""
    def __init__(self, deep=0):
        self.deep = deep
        self._group = None

        self.results = dict()
        self.layers = dict()

        for i in range(self.deep):
            self.layers[i] = []

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, group):
        # self.results[0] = group
        self._group = group

    def check_level(self, lvl):
        if len(self.layers[lvl]) == 2 ** lvl:
            return False
        return True

    def push_layer(self, lvl, layer):
        if self.check_level(lvl):
            self.layers[lvl].append(layer)

    def execute(self):
        for lvl in range(self.deep):
            self.results[lvl + 1] = {}
            if lvl == 0:
                # self.results[i] = self.try_lvl(i, self.group)
                self.layers[lvl][0].execute(self.group)
                self.results[lvl + 1].update({key: value for key, value in self.layers[lvl][0].next_leaf()})
            else:
                # self.results[i] = self.try_lvl(i, self.results[i-1])
                for l in range(len(self.layers[lvl])):
                    lays = self.layers[lvl][l]
                    lays.execute(self.results[lvl][lays.name])
                    self.results[lvl + 1].update({key: value for key, value in lays.next_leaf()})

        return self.results
