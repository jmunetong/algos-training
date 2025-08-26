"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        connections = {}
        stack = []
        if node:
            connections[node.val] = Node(node.val)
            stack.append(node)
            while stack:
                current = stack.pop()
                for child in current.neighbors:
                    if child.val not in connections:
                        connections[child.val] = Node(child.val)
                        stack.append(child)
                    connections[current.val].neighbors.append(connections[child.val])
            return connections[node.val]
    


        


            




            


        