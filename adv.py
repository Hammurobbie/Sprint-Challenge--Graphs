from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
cur_path = []


class Graph:

    def __init__(self):
        self.vertices = {}

    def dft(self, starting_vertex):

        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            cur_room = s.pop()
            print("cur room", cur_room)

            if cur_room not in visited:
                visited.add(cur_room)
                print("visited", visited)

                exits = player.current_room.get_exits()

                print("cur exits", exits)

                for exit_boi in exits:
                    if player.current_room.get_room_in_direction(exit_boi).id not in s.stack and player.current_room.get_room_in_direction(exit_boi).id not in visited:
                        s.push(
                            player.current_room.get_room_in_direction(exit_boi).id)
                print("stack", s.stack)
                if s.stack:
                    next_room = s.stack[-1]
                    print("next room", next_room)
                    next_rooms_arr = []
                    for exit_boi2 in exits:
                        next_rooms_arr.append(
                            player.current_room.get_room_in_direction(exit_boi2).id)
                    for exit_boi4 in exits:
                        if player.current_room.get_room_in_direction(exit_boi4).id == next_room:
                            next_room_dir = exit_boi4
                    if next_room_dir:
                        print(next_room_dir, "fgdsfghdshgdshdfghdsghdfsghfghfsh")
                        player.travel(next_room_dir)
                        traversal_path.append(next_room_dir)
                        cur_path.append(next_room_dir)
                        print("cur path", cur_path)
                    while set(next_rooms_arr).issubset(visited):
                        print("next rooms ar", next_rooms_arr, visited)
                        if cur_path:
                            last_move = cur_path.pop()
                            # print("cur path", cur_path)
                            if last_move == "n":
                                backtrack = "s"
                            elif last_move == "s":
                                backtrack = "n"
                            elif last_move == "e":
                                backtrack = "w"
                            elif last_move == "w":
                                backtrack = "e"
                            player.travel(backtrack)
                            traversal_path.append(backtrack)
                            next_rooms_arr.pop()
                            exits2 = player.current_room.get_exits()
                            next_room_dir_2 = None
                            for exit_boi3 in exits2:
                                next_rooms_arr.append(
                                    player.current_room.get_room_in_direction(exit_boi3).id)
                            for exit_boi3 in exits2:
                                if player.current_room.get_room_in_direction(exit_boi3).id == next_room:
                                    next_room_dir_2 = exit_boi3
                            if next_room_dir_2:
                                print("what the fuckjttttttttttttttt",
                                      player.current_room.id)
                                player.travel(next_room_dir_2)
                                traversal_path.append(next_room_dir_2)
                                print("what the fuckjttttttttttttttt",
                                      player.current_room.id)
                        else:
                            # if exit_boi3 == "n":
                            #     cur_path.append("s")
                            # elif exit_boi3 == "s":
                            #     cur_path.append("n")
                            # elif exit_boi3 == "e":
                            #     cur_path.append("w")
                            # elif exit_boi3 == "w":
                            #     cur_path.append("e")
                            break


Graph().dft(player.current_room.id)


print("player end room", player.current_room.id)
print("path end", traversal_path)


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
