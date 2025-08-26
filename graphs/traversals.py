from collections import deque

#STACK: LIFO 
#QUEUE: FIFO
graph = {"a":["b", "c"],
         "b": ["d"],
         "c": ["e"],
         "d": ["f"],
         "e": [],
         "f": []
}


def depth_first(graph, start):
    is_visited = set()
    stack = []
    stack.append(start)
    is_visited.add(start)
    while stack:
        current = stack.pop()
        print(current)
        ls = graph[current]
        
        for element in ls:
            if element not in is_visited:
                is_visited.add(element)
                stack.append(element)

def breadth_first_search(graph, start):
    is_visited = set()
    queue = deque()
    queue.append(start)
    is_visited.add(start)
    while queue:
        current = queue.popleft()
        print(current)
        ls = graph[current]
        
        for element in ls:
            if element not in is_visited:
                is_visited.add(element)
                queue.append(element)
    


if __name__ == '__main__':
    print("Computing depth first Search")
    depth_first(graph, "a")
    print("Computing breadth first search")
    breadth_first_search(graph, "a")


