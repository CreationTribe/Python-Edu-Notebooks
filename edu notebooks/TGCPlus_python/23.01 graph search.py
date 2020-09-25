# breadth-first search

# two basic methods for seaching graphs
#   > follow the edges as far as you can
#   > spread out from the starting pont (breadth-first search)

class Node:
    def __init__(self, name):
        self._name = name
        self._friends = []
        self._status = 0
        self._discovered_by = 0

    def get_name(self):
        return self._name

    def get_friends(self):
        return self._friends

    def add_friend(self, friend_index):
        self._friends.append(friend_index)

    def is_unseen(self):
        if self._status == 0:
            return True
        else:
            return False

    def is_seen(self):
        if self._status == 1:
            return True
        else:
            return False

    def set_unseen(self):
        self._status = 0

    def set_seen(self):
        self._status = 1

    def discover(self, n):
        self._discovered_by = n

    def discovered(self):
        return self._discovered_by


class Queue:
    def __init__(self):
        self._queue = []

    def enqueue(self, x):
        self._queue.append(x)

    def dequeue(self):
        return self._queue.pop()

    def is_empty(self):
        return len(self._queue) == 0


people = []


def make_friends(name1, name2):
    for i in range(len(people)):
        if people[i].get_name() == name1:
            n1 = i
        if people[i].get_name() == name2:
            n2 = i

    people[n1].add_friend(n2)
    people[n2].add_friend(n1)


def retrieve_path(node_list, start, goal):
    # return the path from start to goal
    if start == goal:
        path = [start]
        return path
    else:
        previous = node_list[goal].discovered()
        previous_path = retrieve_path(node_list, start, previous)
        previous_path.append(goal)
        return previous_path


def BFS(node_list, start, goal):
    to_visit = Queue()
    node_list[start].set_seen()
    to_visit.enqueue(start)

    found = False
    while not found and not to_visit.is_empty():
        current = to_visit.dequeue()
        neighbors = node_list[current].get_friends()
        for neighbor in neighbors:
            if node_list[neighbor].is_unseen():
                node_list[neighbor].set_seen()
                node_list[neighbor].discover(current)
                if neighbor == goal:
                    found = True
                else:
                    to_visit.enqueue(neighbor)
    return retrieve_path(node_list, start, goal)


people.append(Node('John'))
people.append(Node('Joe'))
people.append(Node('Sue'))
people.append(Node('Fred'))
people.append(Node('Kathy'))

make_friends('John', 'Joe')
make_friends('John', 'Sue')
make_friends('Joe', 'Sue')
make_friends('Sue', 'Fred')
make_friends('Fred', 'Kathy')

path_list = BFS(people, 0, 4)

for index in path_list:
    print(people[index].get_name())










































