# Recursive DFS template
def dfs_recursive(graph, start):
    visited = set()
    order = []
    
    def visit(node):
        visited.add(node)
        order.append(node)
        for child in graph[node]:
            if child in visited:
                continue
            visit(child)
                

    visit(start)

    return order


# # Iterative DFS template
# def dfs_iterative(graph, start):
#     visited = set()
#     order = []
#     stack = []

#     while stack:
#         node = stack.pop()
     
#         pass

#     return 


if __name__ == '__main__':
        # Test graphs
    graph1 = {
        1: [2, 3],
        2: [1, 4],
        3: [1],
        4: [2]
    }
    print(dfs_recursive(graph1, 1))
    # Connected chain with a branch
    # Expected DFS from 1 (one valid order): [1, 2, 4, 3]

    graph2 = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A'],
        'D': ['B']
    }
    print(dfs_recursive(graph2, "A"))
    # Expected DFS from 'A': one valid order is ['A', 'B', 'D', 'C']

    graph3 = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0],
        3: [1],
        4: [1]
    }
    print(dfs_recursive(graph3, 0))
    # Expected DFS from 0: [0, 1, 3, 4, 2] or [0, 1, 4, 3, 2]

    graph4 = {
        10: [],
    }
    # Single node, no neighbors
    # Expected DFS from 10: [10]

    graph5 = {
        1: [2],
        2: [3],
        3: [4],
        4: []
    }
    # Simple chain
    # Expected DFS from 1: [1, 2, 3, 4]