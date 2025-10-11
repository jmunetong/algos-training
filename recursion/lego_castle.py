
a = [1]


def lego_castle(n):
    if n ==1:
        return 1
    return 2*lego_castle(n-1) + compute_ceiling(n)



def compute_ceiling(n):
    if len(a)> n-1:
        return a[n-1]
    result = 2 * compute_ceiling(n-1) + 1
    a.append(result)
    return result
    
    

def run_tests():
  tests = [
      # Test cases derived from problem description
      (1, 1),
      (2, 5),
      (3, 17),
      (4, 49),
      (5, 129),
      (6, 321),
      (7, 769),
      (8, 1793),
      (9, 4097),
      (10, 9217),
  ]
  for n, want in tests:
    got = lego_castle(n)
    assert got == want, f"\nblocks({n}): got: {got}, want: {want}\n"
    
    

if __name__ =='__main__':
   run_tests()
    

# let us think about the number of values 
    