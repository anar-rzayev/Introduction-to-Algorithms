from elice_utils import EliceUtils
import sys

elice_utils = EliceUtils()

# Implement here.


def solution(n, costs):
    max_possible_number = 999999
    sum_of_edges = 0  # desired output for MST
    temporary = []
    for i in range(len(costs)):
        temporary.append(costs[i][0])
        temporary.append(costs[i][1])
    number_of_vertices = max(temporary) + 1
    adjacency_matrix = [
        [0 for i in range(number_of_vertices)] for j in range(number_of_vertices)]
    for i in range(len(costs)):
        u = costs[i][0]
        v = costs[i][1]
        adjacency_matrix[u][v] = costs[i][2]
        adjacency_matrix[v][u] = costs[i][2]

    def obtain_key_for_minimum(stone, visited_list_0):
        minimum = max_possible_number    # initialize the min by infinite number
        minIndex = -1    # initialize the min index
        for i in range(number_of_vertices):
            # Find the edge with minimum stone if it is not visited
            if stone[i] < minimum and visited_list_0[i] == False:
                minimum = stone[i]
                minIndex = i
        # Return the index of the found edge with minimum weight
        return minIndex

    # This list will be implemented for saving the weights for all the vertices
    weight_for_vertices = [9999] * number_of_vertices
    # This will contain our minimum spanning tree for this problem
    minimum_spanning_tree = [None] * number_of_vertices
    # Assign the weight of the root node to be 0
    weight_for_vertices[0] = 0
    # Initialize all vertices to be not visited
    visited_nodes_of_list = [False] * number_of_vertices
    # We choose the first vertex as root node
    minimum_spanning_tree[0] = -1

    for _ in range(number_of_vertices):
        minimum_index_value = obtain_key_for_minimum(
            weight_for_vertices, visited_nodes_of_list)
        # mark the following index as visited
        visited_nodes_of_list[minimum_index_value] = True
        for node in range(number_of_vertices):
            if adjacency_matrix[minimum_index_value][node] > 0 and visited_nodes_of_list[node] == False and weight_for_vertices[node] > adjacency_matrix[minimum_index_value][node]:
                weight_for_vertices[node] = adjacency_matrix[minimum_index_value][node]
                minimum_spanning_tree[node] = minimum_index_value

    for i in range(1, number_of_vertices):
        sum_of_edges += adjacency_matrix[i][minimum_spanning_tree[i]]

    return sum_of_edges

# Do not change this part of the code.
# You may enter value of n and costs in the terminal to test your algorithm.
# Input format for n = 4, costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
# 4
# 5
# 0 1 1
# 0 2 2
# 1 2 5
# 1 3 1
# 2 3 8


def main():
    n = int(input())
    lenCosts = int(input())
    costs = [list(map(int, input().split())) for _ in range(lenCosts)]
    print(solution(n, costs))


if __name__ == "__main__":
    main()
