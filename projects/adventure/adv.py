# class Queue():
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, value):
#         self.queue.append(value)
#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None
#     def size(self):
#         return len(self.queue)

from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# directions = {0: 'n', 1: 's', 2: 'e', 3: 'w'}

# print(directions[random.randrange(3)])

# print(nextDirection())

path = []
backtrack = [] # need somewhere to go if get to a dead end, s back track

visited = {}
visited[0] = player.current_room.get_exits() # starting room

# if need to backup, these are inverse of what was just done, key is direction went & value is inverse of it
inverse_directions = {
    "n": "s",
    "s": "n",
    "e": "w",
    "w": "e"
    }

# while the number of rooms that are visited smaller than number in the graph
while len(room_graph) > len(visited):

    # base case, last room, final move to end while loop
    while len(room_graph) - len(visited) == 1:
        visited[player.current_room.id] = player.current_room.get_exits()

    # if the room i'm in currently i haven't been in before
    while player.current_room.id not in visited and len(room_graph) - len(visited) > 1:
        # get all the potential exits from the current room and add to the index of current room & add to visited
        visited[player.current_room.id] = player.current_room.get_exits()
        # remove from the index of current room the room at the last index of the backtrack array, so keep moving "forward"
        visited[player.current_room.id].remove(backtrack[-1])

    # if there aren't any exits from the current room, its a dead end or explored so backup
    while len(visited[player.current_room.id]) == 0:
        # pop the last room off the end of the backtrack array and that's the backup room
        backup = backtrack.pop()
        # append that backup room to the end of the path
        path.append(backup)
        # travel to the backup room
        player.travel(backup)

    # pop the last room off the options to go explore from current room
    explore_next = visited[player.current_room.id].pop()

    # append to the backtrack array the inverse direction to the direction gonna take to the next room to go explore
    backtrack.append(inverse_directions[explore_next])

    # append the next room to go explore to the end of the path
    path.append(explore_next)

    # travel to the next room set to go explore
    player.travel(explore_next)

# def bfs(self, starting_room, target_exit):
#     q = Queue()
#     q.enqueue(path)

#     while q.size() > 0:

#         cur = q.dequeue()

#         if cur[-1] == target_exit:
#             return cur

#         for i in self.get_neighbors(cur[-1]):
#             explore_next = [*cur, i]
#             q.enqueue(explore_next)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
