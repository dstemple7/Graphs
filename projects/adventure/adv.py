import random

from room import Room
from player import Player
from world import World
from ast import literal_eval

world = World() # Load world
map_file = "projects/adventure/maps/main_maze.txt" # load map
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph) # Loads the map into a dictionary
world.print_rooms() # Print an ASCII map
player = Player(world.starting_room)

# Fill this out with directions to walk
path = []
backtrack = [] # need somewhere to go if get to a dead end, s back track
visited = {}
visited[0] = player.current_room.get_exits() # starting room

# if need to backup, these are inverse of what was just done, key is direction went & value is inverse of it
inverse_directions = {"n": "s", "s": "n", "e": "w", "w": "e"}

# while the number of rooms that are visited smaller than number in the graph
while len(room_graph) > len(visited):

    # base case, last room, final move to end while loop
    while len(room_graph) - len(visited) == 1:
        visited[player.current_room.id] = player.current_room.get_exits()

    # if the room i'm in currently i haven't been in before
    # get all the potential exits from the current room and add to the index of current room & add to visited
    # remove from the index of current room the room at the last index of the backtrack array, so keep moving "forward"
    while player.current_room.id not in visited and len(room_graph) - len(visited) > 1:
        visited[player.current_room.id] = player.current_room.get_exits()
        visited[player.current_room.id].remove(backtrack[-1])

    # if there aren't any exits from the current room, its a dead end or explored so backup
    # pop the last room off the end of the backtrack array and that's the backup room
    # append that backup room to the end of the path
    # travel to the backup room
    while len(visited[player.current_room.id]) == 0:
        backup = backtrack.pop()
        path.append(backup)
        player.travel(backup)

    # pop the last room off the options to go explore from current room
    # append to the backtrack array the inverse direction to the direction gonna take to the next room to go explore
    # append the next room to go explore to the end of the path
    # travel to the next room set to go explore
    explore_next = visited[player.current_room.id].pop()
    backtrack.append(inverse_directions[explore_next])
    path.append(explore_next)
    player.travel(explore_next)

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
