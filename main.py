
import random
from datasets.objects import Plant
from decTree.decisiontree import DecisionTree
from decTree.layers.PlantsLayers import *

""" nbpetals : 5 < x < 10
    lgtpetals : 2 < x < 4 - float 
     lgtroot : 10 < x < 25 """


def generate_group():
    return [Plant(i, random.randint(5, 10), random.uniform(2.0, 4.0), random.randint(5, 25)) for i in range(10)]


def main():
    ml = DecisionTree(2)

    ml.push_layer(0, RootLgtLayer)
    #ml.push_layer(1, PetalslgtLayer)
    ml.push_layer(1, PetalsNbLayer)

    group = generate_group()
    ml.group = group

    ml.execute()
    print(ml.results)


if __name__ == '__main__':
    main()
