'''
Once you’ve reviewed the precourse material, take a look at this island_counting problem which we will be going over in today’s guided project:
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
island_counter(islands) # returns 4

- connected: has edges, connected components
- array/2d: graph
- n, s, e, w: edges
- binary: values
- island/islands: connected components
'''
# y (up down) first then x (left right)
islands[0][4]

[0, 1, 0, 1, 0],
[1, 1, 0, 1, 1],
[0, 0, 1, 0, 0],
[1, 0, 1, 0, 0],
[1, 1, 0, 0, 0]

for island in islands:
    for i in island:
        if i == 1:
