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
# map_file = "maps/test_loop.txt"
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


class Graph:

    def __init__(self):
        self.vertices = {}

    def dft(self, starting_vertex):

        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            cur_room = s.pop()

            if cur_room not in visited:
                visited.add(cur_room)
                print("visited", visited)

                exits = player.current_room.get_exits()

                print("cur exits", exits)

                for exit_boi in exits:
                    if player.current_room.get_room_in_direction(exit_boi).id not in s.stack and player.current_room.get_room_in_direction(exit_boi).id not in visited:
                        s.push(
                            player.current_room.get_room_in_direction(exit_boi).id)
                        # new_room = player.current_room.id
                        # s.push(new_room)
                print("stack", s.stack)
                if s.stack:
                    next_room = s.stack[-1]
                    print("next room", next_room)
                    for exit_boi2 in exits:
                        if player.current_room.get_room_in_direction(exit_boi2).id == next_room:
                            player.travel(exit_boi2)
                            traversal_path.append(exit_boi2)

    # def dft_recursive(self, starting_vertex, visited=None):

    #     exits = player.current_room.get_exits()

    #     if visited is None:
    #         visited = set()

    #     visited.add(starting_vertex)
    #     print("start point", starting_vertex)

    #     for exit_boi in exits:
    #         if exit_boi not in visited:
    #             player.travel(exit_boi)
    #             new_room = player.current_room.id
    #             self.dft_recursive(new_room, visited)


Graph().dft(player.current_room.id, )


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
