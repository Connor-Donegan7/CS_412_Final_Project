import copy
"""
    Brute force for TSP, this is O(n!).
"""


# Ensures all verticies have been visited.
def all_visited(dict, arr):
    to_check = []
    for key in dict.keys():
        to_check.append(key)

    for elem in arr:
        if elem[0] in to_check:
            to_check.remove(elem[0])
    
    if len(to_check) > 0:
        return False

    return True

# A traversal can "travel back", but it cannot travel accross an edge the same way twice.
def oscillating(path, curr_node, next_node):
    for i in range(len(path) - 1):
        if path[i][0] == curr_node and path[i + 1][0] == next_node:
            return True
    
    return False

# Just sums up the path.
def path_sum(path):
    sum = 0
    for i in range(1, len(path)):
        sum += float(path[i][1])
    
    return sum

# Finds shortest traversal.
def find_shortest_path(dict):
    best_solution = []
    best_sum = -1
    
    search_stack = []
    verts = []
    for key in dict.keys():
        verts.append(key)

    start_vert = verts[0]

    for tuple in dict[start_vert]:
        search_stack.append((tuple, [start_vert])) # Init the stack.
        
    while len(search_stack) > 0:    # When the stack is empty, all has been explored.
        current_state = search_stack.pop()  # Inspect next node.
        curr_node = current_state[0]    # Node itself.
        curr_path = current_state[1]    # Path to get to above node.
        new_path = copy.deepcopy(curr_path)  # To be safe.
        new_path.append(curr_node)  # for better or for worse...
        
        sum_so_far = path_sum(new_path)  # For memoization.

        for tuple in dict[curr_node[0]]:
            if tuple[0] == start_vert:  # Back where we started.

                if all_visited(dict, new_path):
                    possible_solution = copy.deepcopy(new_path)  # Again.
                    possible_solution.append(tuple)  # To properly denote the tour.

                    sum = path_sum(possible_solution)

                    if sum < best_sum or best_sum < 0:  # If best or first, make official.
                        best_sum = sum
                        best_solution = possible_solution


            # Essentially, only consider further nodes which have not been trampled
            # or have a chance to lead to a better solution
            if (not oscillating(curr_path, curr_node[0], tuple[0]) and 
                (sum_so_far <= best_sum or best_sum < 0)):
                search_stack.append((tuple, new_path))

    return best_solution


# Sets stuff up, doesn't matter.
def main():
    num_of_verts = int(input())
    graph_dict = {}

    for verts in range(num_of_verts):
        line = input().split()
        vert = line[0]

        neighbor_arr = []
        for i in range(1, len(line) - 1, 2):
            neighbor_arr.append((line[i], line[i + 1]))

        graph_dict[vert] = neighbor_arr
    
    
    best_solution = find_shortest_path(graph_dict)

    clean_path = ""
    clean_path += best_solution[0]

    for i in range(1, len(best_solution)):
        clean_path += " -> " + best_solution[i][0]

    sum = path_sum(best_solution)


    print("Path:")
    print(clean_path)
    print(f"\nCost: {sum}")

if __name__ == '__main__':
    main()