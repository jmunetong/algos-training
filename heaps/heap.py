import math

class MinHeap:
    def __init__(self, arr=None):
        self.arr = arr if arr is not None else []
        if arr is not None:
            self.heapify()

    def size(self):
        return len(self.arr)

    def top(self):
        return self.arr[0] if len(self.arr) > 0 else None
    
    def get_parent_idx(self, idx):
        return (idx - 1) //2
    
    def get_child_idx(self, idx):
        return 2 *idx +1, 2*idx +2

    def swap(self, idx1, idx2):
        self.arr[idx1], self.arr[idx2] = self.arr[idx2], self.arr[idx1]

    def bubble_up(self, idx):
        # These will be my two cases for the bubble up algorithm
        if idx ==0:
            return
        parent_idx = self.get_parent_idx(idx)
        if self.arr[parent_idx] < self.arr[idx]:
            return
        self.arr[parent_idx], self.arr[idx] = self.arr[idx], self.arr[parent_idx]

        self.bubble_up(parent_idx)
            
    def push(self, elem):
        self.arr.append(elem)
        child_idx = len(self.arr) - 1
        self.bubble_up(child_idx)

    def bubble_down(self, idx):
        left_child_idx, right_child_idx = self.get_child_idx(idx)
        if left_child_idx > len(self.arr) -1:
            return
        chosen_child_idx = idx
        if self.arr[left_child_idx] < self.arr[idx]:
            chosen_child_idx = left_child_idx

        if right_child_idx < len(self.arr) and self.arr[right_child_idx] < self.arr[chosen_child_idx]:
           chosen_child_idx = right_child_idx

        if chosen_child_idx == idx:
            return
        self.swap(chosen_child_idx, idx)
        self.bubble_down(chosen_child_idx)

    def pop(self):
        if len(self.arr) > 0:
            first_element = self.arr[0]
            last_element = self.arr.pop()
            if len(self.arr )> 0:
                self.arr[0] = last_element
                parent_idx = 0
                self.bubble_down(parent_idx)
            return first_element
        
    def heapify(self):
        for idx in range((len(self.arr))//2 - 1, -1, -1):
            self.bubble_down(idx)
        



import unittest
import random

class TestMinHeap(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.heap = MinHeap()
    
    # Basic Constructor Tests
    def test_empty_constructor(self):
        """Test creating an empty heap."""
        heap = MinHeap()
        self.assertEqual(heap.size(), 0)
        self.assertIsNone(heap.top())
    
    def test_constructor_with_empty_array(self):
        """Test creating heap with empty array."""
        heap = MinHeap([])
        self.assertEqual(heap.size(), 0)
        self.assertIsNone(heap.top())
    
    def test_constructor_with_single_element(self):
        """Test creating heap with single element."""
        heap = MinHeap([5])
        self.assertEqual(heap.size(), 1)
        self.assertEqual(heap.top(), 5)
    
    def test_constructor_with_multiple_elements(self):
        """Test creating heap with multiple elements."""
        heap = MinHeap([3, 1, 6, 5, 2, 4])
        self.assertEqual(heap.size(), 6)
        self.assertEqual(heap.top(), 1)  # Should be min element
    
    def test_constructor_with_duplicates(self):
        """Test creating heap with duplicate elements."""
        heap = MinHeap([5, 3, 5, 1, 5, 2])
        self.assertEqual(heap.size(), 6)
        self.assertEqual(heap.top(), 1)
    
    def test_constructor_with_negative_numbers(self):
        """Test creating heap with negative numbers."""
        heap = MinHeap([-3, -1, -6, -5, -2, -4])
        self.assertEqual(heap.size(), 6)
        self.assertEqual(heap.top(), -6)
    
    def test_constructor_with_mixed_numbers(self):
        """Test creating heap with positive and negative numbers."""
        heap = MinHeap([3, -1, 6, -5, 2, -4])
        self.assertEqual(heap.size(), 6)
        self.assertEqual(heap.top(), -5)
    
    # Size Tests
    def test_size_empty_heap(self):
        """Test size of empty heap."""
        self.assertEqual(self.heap.size(), 0)
    
    def test_size_after_push(self):
        """Test size increases after push operations."""
        self.heap.push(5)
        self.assertEqual(self.heap.size(), 1)
        self.heap.push(3)
        self.assertEqual(self.heap.size(), 2)
        self.heap.push(7)
        self.assertEqual(self.heap.size(), 3)
    
    def test_size_after_pop(self):
        """Test size decreases after pop operations."""
        self.heap.push(5)
        self.heap.push(3)
        self.heap.push(7)
        self.assertEqual(self.heap.size(), 3)
        self.heap.pop()
        self.assertEqual(self.heap.size(), 2)
        self.heap.pop()
        self.assertEqual(self.heap.size(), 1)
        self.heap.pop()
        self.assertEqual(self.heap.size(), 0)
    
    # Top Tests
    def test_top_empty_heap(self):
        """Test top() returns None for empty heap."""
        self.assertIsNone(self.heap.top())
    
    def test_top_single_element(self):
        """Test top() with single element."""
        self.heap.push(42)
        self.assertEqual(self.heap.top(), 42)
    
    def test_top_multiple_elements(self):
        """Test top() always returns minimum element."""
        elements = [5, 2, 8, 1, 9, 3]
        for elem in elements:
            self.heap.push(elem)
        self.assertEqual(self.heap.top(), 1)
    
    def test_top_after_pop(self):
        """Test top() after pop operations."""
        elements = [5, 2, 8, 1, 9, 3]
        for elem in elements:
            self.heap.push(elem)
        
        self.assertEqual(self.heap.top(), 1)
        self.heap.pop()
        self.assertEqual(self.heap.top(), 2)
        self.heap.pop()
        self.assertEqual(self.heap.top(), 3)
    
    def test_top_doesnt_modify_heap(self):
        """Test that top() doesn't modify the heap."""
        elements = [5, 2, 8, 1, 9, 3]
        for elem in elements:
            self.heap.push(elem)
        
        initial_size = self.heap.size()
        initial_top = self.heap.top()
        
        # Call top multiple times
        for _ in range(5):
            self.assertEqual(self.heap.top(), initial_top)
        
        self.assertEqual(self.heap.size(), initial_size)
    
    # Push Tests
    def test_push_to_empty_heap(self):
        """Test pushing to empty heap."""
        self.heap.push(10)
        self.assertEqual(self.heap.size(), 1)
        self.assertEqual(self.heap.top(), 10)
    
    def test_push_maintains_heap_property(self):
        """Test that push maintains min heap property."""
        elements = [10, 5, 15, 2, 8, 12, 20, 1]
        for elem in elements:
            self.heap.push(elem)
            # After each push, verify heap property
            self.assertTrue(self._is_valid_min_heap())
    
    def test_push_duplicate_elements(self):
        """Test pushing duplicate elements."""
        self.heap.push(5)
        self.heap.push(5)
        self.heap.push(5)
        self.assertEqual(self.heap.size(), 3)
        self.assertEqual(self.heap.top(), 5)
        self.assertTrue(self._is_valid_min_heap())
    
    def test_push_in_ascending_order(self):
        """Test pushing elements in ascending order."""
        for i in range(1, 11):
            self.heap.push(i)
            self.assertEqual(self.heap.top(), 1)
        self.assertTrue(self._is_valid_min_heap())
    
    def test_push_in_descending_order(self):
        """Test pushing elements in descending order."""
        for i in range(10, 0, -1):
            self.heap.push(i)
            self.assertEqual(self.heap.top(), i)
        self.assertTrue(self._is_valid_min_heap())
    
    def test_push_negative_numbers(self):
        """Test pushing negative numbers."""
        elements = [-5, -2, -8, -1, -9, -3]
        for elem in elements:
            self.heap.push(elem)
        self.assertEqual(self.heap.top(), -9)
        self.assertTrue(self._is_valid_min_heap())
    
    def test_push_zero(self):
        """Test pushing zero along with other numbers."""
        elements = [5, 0, -3, 2, 0, -1]
        for elem in elements:
            self.heap.push(elem)
        self.assertEqual(self.heap.top(), -3)
        self.assertTrue(self._is_valid_min_heap())
    
    # Pop Tests
    def test_pop_empty_heap(self):
        """Test popping from empty heap."""
        result = self.heap.pop()
        self.assertIsNone(result)
        self.assertEqual(self.heap.size(), 0)
    
    def test_pop_single_element(self):
        """Test popping from heap with single element."""
        self.heap.push(42)
        result = self.heap.pop()
        self.assertEqual(result, 42)
        self.assertEqual(self.heap.size(), 0)
        self.assertIsNone(self.heap.top())
    
    def test_pop_maintains_heap_property(self):
        """Test that pop maintains min heap property."""
        elements = [10, 5, 15, 2, 8, 12, 20, 1, 6, 9]
        for elem in elements:
            self.heap.push(elem)
        
        prev_min = float('-inf')
        while self.heap.size() > 0:
            current_min = self.heap.pop()
            self.assertGreaterEqual(current_min, prev_min)
            prev_min = current_min
            if self.heap.size() > 0:
                self.assertTrue(self._is_valid_min_heap())
    
    def test_pop_all_elements(self):
        """Test popping all elements returns them in sorted order."""
        elements = [15, 3, 9, 1, 7, 12, 4, 8, 2, 11]
        for elem in elements:
            self.heap.push(elem)
        
        sorted_elements = sorted(elements)
        popped_elements = []
        
        while self.heap.size() > 0:
            popped_elements.append(self.heap.pop())
        
        self.assertEqual(popped_elements, sorted_elements)
    
    def test_pop_with_duplicates(self):
        """Test popping with duplicate elements."""
        elements = [5, 3, 5, 1, 5, 2, 3, 1]
        for elem in elements:
            self.heap.push(elem)
        
        sorted_elements = sorted(elements)
        popped_elements = []
        
        while self.heap.size() > 0:
            popped_elements.append(self.heap.pop())
        
        self.assertEqual(popped_elements, sorted_elements)
    
    # Mixed Operations Tests
    def test_alternating_push_pop(self):
        """Test alternating push and pop operations."""
        # Start with some elements
        initial_elements = [5, 2, 8, 1]
        for elem in initial_elements:
            self.heap.push(elem)
        
        # Alternate between push and pop
        self.assertEqual(self.heap.pop(), 1)  # Pop min
        self.heap.push(3)
        self.assertEqual(self.heap.pop(), 2)  # Pop current min
        self.heap.push(0)
        self.assertEqual(self.heap.top(), 0)  # New minimum
        
        self.assertTrue(self._is_valid_min_heap())
    
    def test_push_after_empty_by_popping(self):
        """Test pushing after emptying heap by popping."""
        # Add and remove all elements
        self.heap.push(5)
        self.heap.push(2)
        self.heap.pop()
        self.heap.pop()
        
        # Heap should be empty
        self.assertEqual(self.heap.size(), 0)
        self.assertIsNone(self.heap.top())
        
        # Add new elements
        self.heap.push(10)
        self.heap.push(3)
        self.assertEqual(self.heap.size(), 2)
        self.assertEqual(self.heap.top(), 3)
    
    # Edge Cases and Stress Tests
    def test_large_number_of_elements(self):
        """Test with a large number of elements."""
        elements = list(range(1000, 0, -1))  # 1000 down to 1
        for elem in elements:
            self.heap.push(elem)
        
        self.assertEqual(self.heap.size(), 1000)
        self.assertEqual(self.heap.top(), 1)
        self.assertTrue(self._is_valid_min_heap())
        
        # Pop all elements and verify they come out sorted
        popped = []
        while self.heap.size() > 0:
            popped.append(self.heap.pop())
        
        self.assertEqual(popped, list(range(1, 1001)))
    
    def test_random_operations(self):
        """Test random sequence of push and pop operations."""
        random.seed(42)  # For reproducible tests
        reference_list = []
        
        for _ in range(100):
            if random.random() < 0.7 or self.heap.size() == 0:  # 70% chance to push
                value = random.randint(1, 100)
                self.heap.push(value)
                reference_list.append(value)
                reference_list.sort()
            else:  # Pop
                if reference_list:
                    expected = reference_list.pop(0)
                    actual = self.heap.pop()
                    self.assertEqual(actual, expected)
            
            # Verify heap property and size
            if self.heap.size() > 0:
                self.assertTrue(self._is_valid_min_heap())
                self.assertEqual(self.heap.top(), reference_list[0] if reference_list else None)
            self.assertEqual(self.heap.size(), len(reference_list))
    
    def test_very_large_numbers(self):
        """Test with very large numbers."""
        large_numbers = [10**10, 10**15, 10**12, 10**8]
        for num in large_numbers:
            self.heap.push(num)
        
        self.assertEqual(self.heap.top(), 10**8)
        self.assertTrue(self._is_valid_min_heap())
    
    def test_floating_point_numbers(self):
        """Test with floating point numbers."""
        floats = [3.14, 2.71, 1.41, 0.57, 2.23]
        heap = MinHeap()
        for f in floats:
            heap.push(f)
        
        self.assertEqual(heap.top(), 0.57)
        
        # Pop all and verify order
        popped = []
        while heap.size() > 0:
            popped.append(heap.pop())
        
        self.assertEqual(popped, sorted(floats))
    
    def test_heapify_functionality(self):
        """Test that heapify works correctly in constructor."""
        # Test with various unsorted arrays
        test_arrays = [
            [5, 2, 8, 1, 9, 3],
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            [1],
            [3, 3, 3, 3],
            [-5, -2, -8, -1, -9, -3],
            []
        ]
        
        for arr in test_arrays:
            heap = MinHeap(arr.copy())
            if arr:
                self.assertEqual(heap.top(), min(arr))
                self.assertTrue(self._is_valid_min_heap(heap))
                
                # Verify all elements are present by popping
                popped = []
                while heap.size() > 0:
                    popped.append(heap.pop())
                self.assertEqual(sorted(popped), sorted(arr))
            else:
                self.assertEqual(heap.size(), 0)
                self.assertIsNone(heap.top())
    
    def test_heap_property_after_every_operation(self):
        """Comprehensive test ensuring heap property is maintained after every operation."""
        operations = [
            ('push', 10), ('push', 5), ('push', 15), ('pop', None),
            ('push', 2), ('push', 8), ('push', 12), ('pop', None),
            ('push', 20), ('push', 1), ('pop', None), ('pop', None),
            ('push', 6), ('push', 9), ('push', 3), ('pop', None)
        ]
        
        for op, value in operations:
            if op == 'push':
                self.heap.push(value)
            elif op == 'pop':
                self.heap.pop()
            
            # After every operation, verify heap property
            if self.heap.size() > 0:
                self.assertTrue(self._is_valid_min_heap(), 
                              f"Heap property violated after {op} {value}")
    
    # Helper Methods
    def _is_valid_min_heap(self, heap=None):
        """Helper method to check if the heap maintains the min heap property."""
        if heap is None:
            heap = self.heap
        
        if heap.size() <= 1:
            return True
        
        arr = heap.arr
        for i in range(len(arr)):
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            
            if left_child < len(arr) and arr[i] > arr[left_child]:
                return False
            if right_child < len(arr) and arr[i] > arr[right_child]:
                return False
        
        return True

# Additional specialized test cases
class TestMinHeapSpecialCases(unittest.TestCase):
    
    def test_parent_child_index_calculations(self):
        """Test the parent and child index calculation methods."""
        heap = MinHeap([1, 2, 3, 4, 5, 6, 7])
        
        # Test parent indices
        self.assertEqual(heap.get_parent_idx(1), 0)
        self.assertEqual(heap.get_parent_idx(2), 0)
        self.assertEqual(heap.get_parent_idx(3), 1)
        self.assertEqual(heap.get_parent_idx(4), 1)
        self.assertEqual(heap.get_parent_idx(5), 2)
        self.assertEqual(heap.get_parent_idx(6), 2)
        
        # Test child indices
        self.assertEqual(heap.get_child_idx(0), (1, 2))
        self.assertEqual(heap.get_child_idx(1), (3, 4))
        self.assertEqual(heap.get_child_idx(2), (5, 6))
        self.assertEqual(heap.get_child_idx(3), (7, 8))
    
    def test_bubble_up_scenarios(self):
        """Test various bubble up scenarios."""
        # Test bubble up from leaf to root
        heap = MinHeap([10, 5, 8])
        heap.push(1)  # Should bubble up to root
        self.assertEqual(heap.top(), 1)
        
        # Test bubble up stops at correct position
        heap = MinHeap([2, 5, 8, 10])
        heap.push(3)  # Should bubble up but stop before root
        self.assertEqual(heap.top(), 2)
        self.assertTrue(heap.arr[2] == 3 or heap.arr[1] == 3)  # Should be at level 1
    
    def test_bubble_down_scenarios(self):
        """Test various bubble down scenarios."""
        # Create heap and remove root to test bubble down
        heap = MinHeap([1, 2, 3, 4, 5, 6, 7])
        heap.pop()  # Remove 1, should bubble down properly
        self.assertEqual(heap.top(), 2)
        
        # Test bubble down with only left child
        heap = MinHeap([1, 2])
        heap.pop()
        self.assertEqual(heap.top(), 2)
    
    def test_swap_method(self):
        """Test the swap method."""
        heap = MinHeap([1, 2, 3])
        original = heap.arr.copy()
        heap.swap(0, 2)
        self.assertEqual(heap.arr[0], original[2])
        self.assertEqual(heap.arr[2], original[0])
        self.assertEqual(heap.arr[1], original[1])


if __name__ == '__main__':
    # Run all tests
    unittest.main(verbosity=2)