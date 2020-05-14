
import random
from datasets.objects import Plant
from decTree.decisiontree import DecisionTree
from decTree.layers.PlantsLayers import *

""" nbpetals : 5 < x < 10
    lgtpetals : 2 < x < 4 - float 
     lgtroot : 10 < x < 25 """


def generate_group():
    return [Plant(i, random.randint(5, 10), random.uniform(2.0, 4.0), random.randint(5, 25)) for i in range(100)]


def main():
    ml = DecisionTree(2)

    l0 = RootLgtLayer()
    l1 = PetalslgtLayer()
    l1p = PetalsNbLayer()

    l0.push_next(True, l1.name)
    l0.push_next(False, l1p.name)

    l1.push_next(True, 'ClassA')
    l1.push_next(False, 'ClassB')

    l1p.push_next(True, 'ClassC')
    l1p.push_next(False, 'ClassD')

    ml.push_layer(0, l0)
    ml.push_layer(1, l1)
    ml.push_layer(1, l1p)

    group = generate_group()
    ml.group = group

    ml.execute()
    print(ml.results)


if __name__ == '__main__':
    main()
