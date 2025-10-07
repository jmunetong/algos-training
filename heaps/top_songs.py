import heapq
import math
from collections import defaultdict

class TopSongs:
    def __init__(self, k:int):
        self.k = k
        assert self.k > 0, "value error must be greater than k"
        self.heap = []
        self.dict_counter = defaultdict(int)
        self.is_heapified = False
        
    def register_plays(self, title, plays):
        self.dict_counter[title] += plays

    def top_k(self):
        if not self.is_heapified:
           self.heap = [(-count, song) for (song, count) in self.dict_counter.items()]
           heapq.heapify(self.heap) #O(N)
        
        #O(K LOG N)
        return [heapq.heappop(self.heap)[-1] for _ in range(min(self.k, len(self.heap)))]
    

        

def run_tests():
  """Test TopSongs class"""
  # Example from the book
  s = TopSongs(3)
  s.register_plays("Boolean Rhapsody", 193)
  s.register_plays("Coding In The Deep", 146)
  result = s.top_k()
  assert set(result) == set([
      "Boolean Rhapsody",
      "Coding In The Deep"
  ]), f"Test failed for TopSongs with initial songs"

  s.register_plays("All About That Base Case", 291)
  s.register_plays("Here Comes The Bug", 223)
  s.register_plays("Oops! I Broke Prod Again", 274)
  s.register_plays("All the Single Brackets", 132)
  result = s.top_k()
  assert set(result) == set([
      "All About That Base Case",
      "Here Comes The Bug",
      "Oops! I Broke Prod Again"
  ]), f"Test failed for TopSongs after more songs"

  # Additional test cases
  # Test with fewer songs than k
  s = TopSongs(5)
  s.register_plays("Song A", 100)
  s.register_plays("Song B", 200)
  result = s.top_k()
  assert set(result) == set([
      "Song A",
      "Song B"
  ]), f"Test failed for TopSongs with fewer songs than k"

  # Test with exact k songs
  s = TopSongs(3)
  s.register_plays("Song A", 100)
  s.register_plays("Song B", 200)
  s.register_plays("Song C", 300)
  result = s.top_k()
  assert set(result) == set([
      "Song A",
      "Song B",
      "Song C"
  ]), f"Test failed for TopSongs with exact k songs"

  # Test with ties in play counts
  s = TopSongs(2)
  s.register_plays("Song A", 100)
  s.register_plays("Song B", 100)
  s.register_plays("Song C", 100)
  s.register_plays("Song D", 100)
  result = s.top_k()
  assert len(result) == 2, f"Test failed for TopSongs with ties in play counts"

run_tests()


def run_tests():
  """Test TopSongs class with updates"""
  # Example from the book
  s = TopSongs(3)
  s.register_plays("Boolean Rhapsody", 100)
  s.register_plays("Boolean Rhapsody", 193)  # Total 293
  s.register_plays("Coding In The Deep", 75)
  s.register_plays("Coding In The Deep", 75)  # Total 150
  s.register_plays("All About That Base Case", 200)
  s.register_plays("All About That Base Case", 90)  # Total 290
  s.register_plays("All About That Base Case", 1)   # Total 291
  s.register_plays("Here Comes The Bug", 223)
  s.register_plays("Oops! I Broke Prod Again", 274)
  s.register_plays("All the Single Brackets", 132)
  got = s.top_k()
  want = ["All About That Base Case",
          "Boolean Rhapsody", "Oops! I Broke Prod Again"]
  assert set(got) == set(want), f"\ntop_k(): got: {got}, want: {want}\n"

  # Additional test cases
  # Test with fewer songs than k
  s = TopSongs(5)
  s.register_plays("Song A", 100)
  s.register_plays("Song B", 200)
  got = s.top_k()
  want = ["Song A", "Song B"]
  assert set(got) == set(want), f"\ntop_k() with fewer songs than k: got: {got}, want: {want}\n"

  # Test with exact k songs
  s = TopSongs(3)
  s.register_plays("Song A", 100)
  s.register_plays("Song B", 200)
  s.register_plays("Song C", 300)
  got = s.top_k()
  want = ["Song A", "Song B", "Song C"]
  assert set(got) == set(want), f"\ntop_k() with exactly k songs: got: {got}, want: {want}\n"

  # Test with ties in play counts
  s = TopSongs(2)
  s.register_plays("Song A", 100)
  s.register_plays("Song B", 100)
  s.register_plays("Song C", 100)
  s.register_plays("Song D", 100)
  got = s.top_k()
  assert len(got) == 2, f"\ntop_k() with tied play counts: got length {len(got)}, want length 2\n"


run_tests()