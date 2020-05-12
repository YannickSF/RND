

class Plant:
    def __init__(self, pid, nbpetals, lgtpetals, lgtroot):
        self.pid = pid
        self.nb_petals = nbpetals
        self.petals_lentgh = lgtpetals
        self.root_length = lgtroot

    def __repr__(self):
        return {'pid': self.pid,
                'nb_petals': self.nb_petals,
                'petals_lentgh': self.petals_lentgh,
                'root_length': self.root_length}.__str__()

    def __str__(self):
        return self.__repr__().__str__()
