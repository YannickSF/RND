

class Layer:
    def __init__(self, name):
        self._name = name
        self.result = {True: [], False: []}
        self.children = {True: None, False: None}

    @property
    def name(self):
        return self._name

    @staticmethod
    def rule(value):
        # describe rule here
        pass

    def push_next(self, vector, layer_name):
        self.children[vector] = layer_name

    def next_leaf(self):
        return (self.children[True], self.result[True]), (self.children[False], self.result[False])

    def execute(self, pset):
        for i in pset:
            self.result[self.rule(i)].append(i)
