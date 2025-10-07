class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        connected_components = 0
        start_root_nodes = set()
        adj_list = []
        for i in range(n):
            start_root_nodes.add(i)
            adj_list.append([])


        # adj_list = [[] for i in range(n)]
        for start_edge, end_edge in edges:
            adj_list[start_edge].append(end_edge)
            adj_list[end_edge].append(start_edge)

        # s
        parent_nodes = []
        visited = set()
        while len(start_root_nodes) > 0:
            parent = start_root_nodes.pop()
            parent_nodes.append(parent)
            visited.add(parent)
            substack = adj_list[parent]
            while len(substack) > 0:
                child = substack.pop()
                if child in visited:
                    continue
                visited.add(child)
                start_root_nodes.remove(child)
                substack.extend(adj_list[child])
        
        return len(parent_nodes)
                

                





        

        