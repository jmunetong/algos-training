

class Solution:
    def search_leaf_nodes(self, matrix, idx_list):
        return [k for k in idx_list if len(matrix[k])==1 ]

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 1) Build Adjacencxy Matrix
    
        adj_list = [set() for i in range(n)]
        idx_list = set([i for i in range(n)])
        for edge in edges:
            a_edge, b_edge = edge
            adj_list[a_edge].add(b_edge)
            adj_list[b_edge].add(a_edge)
        
        leaf_nodes = self.search_leaf_nodes(adj_list, idx_list)
        available_nodes= n
       
        while available_nodes > 2:
            q = leaf_nodes
            next_layer = []
            while q:
                current_node = q.pop()
                idx_list.remove(current_node)
                parent_node = adj_list[current_node].pop()
                adj_list[parent_node].remove(current_node)
                if len(adj_list[parent_node]) <=1:
                    next_layer.append(parent_node)
                available_nodes -=1
                
            leaf_nodes = next_layer
        return list(idx_list)



            


            
           