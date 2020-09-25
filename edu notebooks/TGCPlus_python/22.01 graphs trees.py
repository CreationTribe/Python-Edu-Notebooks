# this is basically a graph. Use indices for easy ordering
# a tree is just a tree with indexed nodes

# make sure to keep child & parent indices

class Node:
    def __init__(self, name, population=0):
        self._name = name
        self._pop = population

    def getName(self):
        return self._name

    def getPopulation(self):
        return self._pop


class Edge:
    def __init__(self, index1, index2, weight=0):
        self._city1 = index1
        self._city2 = index2
        self._distance = weight

    def getIndex1(self):
        return self._city1

    def getIndex2(self):
        return self._city2

    def getIndices(self):
        return self._city1, self._city2

    def getWeight(self):
        return self._distance
    
    
cities = []
roads = []

city = Node("SLC", 100)
cities.append(city)

city = Node("Sandy", 20)
cities.append(city)

city = Node("Bakersville", 350)
cities.append(city)

city = Node("Provo", 180)
cities.append(city)

city = Node("Logan", 33)
cities.append(city)


road = Edge(0, 1, 44)
roads.append(road)

road = Edge(0, 2, 98)
roads.append(road)

road = Edge(2, 1, 47)
roads.append(road)

road = Edge(2, 3, 83)
roads.append(road)

road = Edge(3, 4, 34)
roads.append(road)

road = Edge(4, 2, 48)
roads.append(road)


road = roads[0]

pop1 = cities[road.getIndex1()].getPopulation()
pop2 = cities[road.getIndex2()].getPopulation()

total_population = pop1 + pop2


# weird note: "indirection" - using an index instead of a name *le sigh*

# imbalance exchange exploits