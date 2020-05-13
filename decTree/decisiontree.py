

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
        self._group = group

    def check_level(self, lvl):
        if len(self.layers[lvl]) == 2 ** lvl:
            return False
        return True

    def push_layer(self, lvl, layer):
        if self.check_level(lvl):
            self.layers[lvl].append(layer)

    """ Test le niveau de l'arbre"""
    def try_lvl(self, lvl, group):
        global_pool = []
        group_turn = True
        group_itr = -1

        def lvl_execution(layer, sets):
            r = {True: [], False: []}
            for j in sets:
                r[layer.rule(j)].append(j)
            return r

        for i in range(len(self.layers[lvl])):
            if lvl == 0:
                global_pool.append(lvl_execution(self.layers[lvl][i], group))
            else:
                if group_turn:
                    group_itr += 1

                global_pool.append(lvl_execution(self.layers[lvl][i], group[group_itr][group_turn]))
                group_turn = not group_turn

        return global_pool

    def execute(self):
        for i in range(self.deep):
            if i == 0:
                self.results[i] = self.try_lvl(i, self.group)
            else:
                self.results[i] = self.try_lvl(i, self.results[i-1])

        return self.results
