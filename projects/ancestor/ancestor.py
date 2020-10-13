# import string

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# def get_neighbors(word):
#     neighbors = []

#     letters = list(string.ascii_lowercase)  # 'a' .. 'z'

#     word_letters = list(word)

#     for i in range(len(word_letters)):   # O(n) over the length of the word
#         for l in letters:  # O(26)
#             word_letters_copy = list(word_letters)
#             word_letters_copy[i] = l
#             candidate_word = "".join(word_letters_copy)

#             if candidate_word != word and candidate_word in words:
#                 neighbors.append(candidate_word)

#     return neighbors

def earliest_ancestor(ancestors, starting_node):
    # Init empty dict to hold graph of family tree
    # Init patriarch as the oldest, i.e. one w/no parents, value = -1
    family_tree = {}
    patriarch = -1

    # create the graph iterating over the ancestors passed in
    # for graph, node is a set with parent at zeroth index and child at first index and edge their connection
    for a in ancestors:
        parent = a[0]
        child = a[1]
        # if the child is not in the family tree dict yet, add to the family tree at key of child an empty set/value of parent(s)
        if child not in family_tree:
            family_tree[child] = set()
        # add to the set at the child's key the value(s) of the parent(s)
        family_tree[child].add(parent)

    # do a BFS and return last ancestor or as base case, the patriarch default value meaning the child is the patriarch
    q = Queue()
    q.enqueue(starting_node)

    while q.size() > 0:
        
        # take the first one off the queue
        cur = q.dequeue()

        # if it's in the family tree
        if cur in family_tree:
            # initialize the matriarch as none
            matriarch = None
            # for the parent(s) in the family tree of the current node
            for parent in family_tree[cur]:
                # if the matriarch still is none or greater then the parent, the parent is the matriarch
                if matriarch is None or matriarch > parent:
                    matriarch = parent
                # put the parent back on the queue
                q.enqueue(parent)
            # if the matriarch is not None, then the matriarch is the patriarch (i.e. first ances)
            if matriarch is not None:
                patriarch = matriarch
    return patriarch
