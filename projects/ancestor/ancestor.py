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
    visited = set()
    q = Queue()
    q.enqueue([starting_node])

    while q.size() > 0:
        path = q.dequeue()

        v = path[-1]

        if v not in visited:
            visited.add(v)
            # print(visited)
            neighbors = []

            for f in ancestors:
                if f[1] == v:
                    neighbors.append(f[0])

            for neighbor in neighbors:
                # path_copy = path + [neighbor]
                q.enqueue(path + [neighbor])