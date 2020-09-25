# GAH! Dude, this guys example is hella botched, I'm not even going
# to waste my time fixing it ...



# two basic methods for seaching graphs
#   > follow the edges as far as you can
#   > spread out from the starting pont (breadth-first search)

# noinspection DuplicatedCode


class Node:
    def __init__(self, word):
        self._word = word
        self._friends = []
        self._status = 0
        self._discovered_by = 0

    def get_name(self):
        return self._word

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


def add_word_link(word_list, word1, word2):
    for i in range(len(word_list)):
        if word_list[i].get_word() == word1:
            n1 = i
        if word_list[i].get_word() == word2:
            n2 = i

    word_list[n1].add_neighbor(n2)
    word_list[n2].add_neighbor(n1)


def add_link(word_list, index1, index2):
    word_list[index1].add_neighbor(index2)
    word_list[index2].add_neighbor(index1)


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










































