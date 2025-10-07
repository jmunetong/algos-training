class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.current = self.root

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._assign(self.root, val)

    def _assign(self, tree_node, val):
        if val < tree_node.val:
            if tree_node.left is None:
                tree_node.left = TreeNode(val)
            else:
                self._assign(tree_node.left, val)
        else:
            if tree_node.right is None:
                tree_node.right = TreeNode(val)
            else:
                self._assign(tree_node.right, val)


    def search(self, val):
        return self._searcher(self.root, val)
        
    
    def _searcher(self, tree_node, val):
        if tree_node.val == val:
            return True
        else:
            if tree_node.val < val:
                if tree_node.right == None:
                    return False
                return self._searcher(tree_node.right, val)
            else:
                if tree_node.left ==None:
                    return False
                return self._searcher(tree_node.left, val)

    def delete(self, val):
        self.root = self._delete_node(self.root, val)

    
    def _delete_node(self, node, val):
        pass
    
        
        # parent_node = self._get_node(self.root, val)
        # child_node, is_left = self._get_from_parent(parent_node, val)
        # if self._is_leaf(child_node):
        #     new_child_node = None
        # else:
        #     if child_node.left is not None and child_node.right is not None:
        #         new_child_node = self._maxpl_v(child_node.left)
        #         new_child_parent = self._get_node(self.root, new_child_node.val)
        #         if new_child_parent.left.val == new_child_node.val:
        #             new_child_parent.left = None
        #         else:
        #             new_child_parent.right = None
                
        #         if new_child_node == child_node:
        #             new_child_node = None
        #         else:
        #             new_child_node.right = child_node.right
        #             new_child_node.left = child_node.left
        #     else:
        #         new_child_node= child_node.left if child_node.left is not None else child_node.right
            
        # if is_left:
        #     parent_node.left = new_child_node
        # else:
        #     parent_node.right = new_child_node
        
                    


    def inorder(self):
        ls = []
        self._get_in_order_vals(ls, self.root)
        return ls

    def _get_in_order_vals(self, ls, tree_node):
        if tree_node is not None:
            self._get_in_order_vals(ls, tree_node.left)
            ls.append(tree_node.val)
            self._get_in_order_vals(ls, tree_node.right)

    

    def min_value(self):
        return self._min_v(self.root).val


    def _min_v(self, tree_node):
        if tree_node.left is None:
            return tree_node
        else:
            return self._min_v(tree_node.left)
        
    def max_value(self):
        return self._max_v(self.root).val
    
    def _max_v(self, tree_node):
        if tree_node.right is None:
            return tree_node
        else:
            return self._max_v(tree_node.right)
        
    
    def _get_node(self, tree_node, val):
        if tree_node.left.val == val or tree_node.right.val == val:
            return tree_node
        else:
            return self._get_node(tree_node.right if tree_node.val < val else tree_node.left, val)
    
    def _get_from_parent(self, tree_node, val):
        return (tree_node.left, True) if tree_node.left.val == val else (tree_node.right, False)

    def _is_leaf(self, tree_node):
        return tree_node.left ==None and tree_node.right==None
        

            


bst = BST()

# Insertion
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)

# Search
assert bst.search(10) == True
assert bst.search(5) == True
assert bst.search(100) == False

# # Inorder traversal should be sorted
assert bst.inorder() == [3, 5, 7, 10, 12, 15, 18]
print("test passed")

# # # Minimum and maximum
assert bst.min_value() == 3
assert bst.max_value() == 18
print("min max passed")

# # # # Deletion cases
bst.delete(3)   # leaf node
assert bst.search(3) == False
bst.delete(15)  # node with two children
assert bst.search(15) == False
# print('Did not found these values after deleted passed')
bst.delete(5)   # node with one child
assert bst.search(5) == False

# # # # Check after deletions
assert bst.inorder() == [7, 10, 12, 18], f'{bst.inorder()} final'
# # # or [7, 10, 12, 18] or some correct variant
assert bst.search(3) == False
# # assert bst.search(15) == Falseb