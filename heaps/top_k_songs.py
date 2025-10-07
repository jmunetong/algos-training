import heapq
def k_most_played(ls, k):
    if len(ls) < k :
        return [song for (song, _) in ls]

    elements = [(-priority, song) for (song, priority) in ls]
    heapq.heapify(elements)
    final_list = []
    for _ in range(k):
        final_list.append(heapq.heappop(elements)[-1])
    return final_list

heapq.nlargest()

def run_tests():
  test_cases = [
      # Example from the book
      ([["All the Single Brackets", 132],
        ["Oops! I Broke Prod Again", 274],
        ["Coding In The Deep", 146],
        ["Boolean Rhapsody", 193],
        ["Here Comes The Bug", 291],
        ["All About That Base Case", 291]], 3,
       ["All About That Base Case", "Here Comes The Bug", "Oops! I Broke Prod Again"]),

      # Test with fewer songs than k
      ([["Song A", 100], ["Song B", 200]], 5,
       ["Song A", "Song B"]),

      # Test with exact k songs
      ([["Song A", 100], ["Song B", 200], ["Song C", 300]], 3,
       ["Song A", "Song B", "Song C"]),

      # Test with k = 1
      ([["Song A", 100], ["Song B", 200], ["Song C", 300]], 1,
       ["Song C"]),

      # Test with ties in play counts
      ([["Song A", 100], ["Song B", 100], ["Song C", 200], ["Song D", 200]], 2,
       ["Song C", "Song D"]),

      # Test empty input
      ([], 3, []),
  ]

  # Test all implementations
  implementations = [
      ("min_heap", k_most_played),
  ]

  for solution_name, solution_func in implementations:
    for songs, k, want in test_cases:
      got = solution_func(songs, k)
      got.sort()
      want.sort()
      assert got == want, f"\n{solution_name}({songs}, {k}): got: {got}, want: {want}\n"

    # Also test tie breaking, any possible result is accepted
    got = solution_func([["Song A", 100], ["Song B", 100]], 1)
    assert got == ["Song A"] or got == [
        "Song B"], f"\n{solution_name}: got: {got}, want: ['Song A'] or ['Song B']\n"
    
run_tests()