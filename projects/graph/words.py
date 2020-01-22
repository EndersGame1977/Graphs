# from graph import Graph
# with open('words.txt', 'r') as file:
#     word_list = [line.lower().rstrip() for line in file]


f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())


def get_neighbors(word):
    neighbors = []
    string_word = list(word)
    for i in range(len(string_word)):
        for letter in list('abcdefghijklmnopqrstuvwxyz'):
            temp_word = list(string_word)
            temp_word[i] = letter
            w = "".join(temp_word)
            if w != word and w in word_set:
                neighbors.append(w)
    return neighbors


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


def find_word_ladder(begin_word, end_word):
    visited = set()
    queue = Queue()
    queue.enqueue([begin_word])
    while queue.size() > 0:
        path = queue.dequeue()
        v = path[-1]
        if v not in visited:
            visited.add(v)
            if v == end_word:
                return path
            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                queue.enqueue(path_copy)


print(find_word_ladder("sail", "boat"))

# def isEditDistanceOne(s1, s2):
#     # Find lengths of given strings
#     m = len(s1)
#     n = len(s2)
#     # If difference between lengths is more than 1,
#     # then strings can't be at one distance
#     if abs(m - n) > 1:
#         return False
#     count = 0    # Count of isEditDistanceOne
#     i = 0
#     j = 0
#     while i < m and j < n:
#         # If current characters dont match
#         if s1[i] != s2[j]:
#             if count == 1:
#                 return False
#             # If length of one string is
#             # more, then only possible edit
#             # is to remove a character
#             if m > n:
#                 i += 1
#             elif m < n:
#                 j += 1
#             else:    # If lengths of both strings is same
#                 i += 1
#                 j += 1
#             # Increment count of edits
#             count += 1
#         else:    # if current characters match
#             i += 1
#             j += 1
#     # if last character is extra in any string
#     if i < m or j < n:
#         count += 1
#     return count == 1


# def shortest_sequence(word_1, word_2):
#     graph = Graph()
#     short_list = []
#     for i in word_list:
#         # Filter out words that dont have the same first letter
#         # as starting words
#         if i[0] == word_1[0] or i[0] == word_2[0]:
#             if abs(len(word_1) - len(i)) <= 1:
#                 short_list.append(i)
#     # Create vertices
#     for i in short_list:
#         graph.add_vertex(i)
#     # For each word in short list
#     for i in short_list:
#         # for each vertex
#         for j in list(graph.vertices.keys()):
#             # if edit distance is one
#             if isEditDistanceOne(i, j):
#                 # connect the two vertices
#                 graph.add_edge(i, j)
#     return graph.bfs(word_1, word_2)


# print(shortest_sequence('sail', 'boat'))
