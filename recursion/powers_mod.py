# #O(p) because this could run thro
# def power(a, p, m):
#     if p ==0:
#         return 1
#     out, i = recurse_fn(a, i=1, p=p, m=m, running_val=a)
#     if i < p:
#         for _ in range(i+1, p +1):
#             out = (a * out) % m
    
#     return out


# Thinking about this frame work here so that I am ablee to solvie it
# Now, this is on ovearge (O (log p))
def power(a, p, m):
    if p ==0:
        return 1
    if p %2 ==0:
        half = power(a, p//2, m)
        return half * half
    return (a * power(a, p-1, m)) % m 

      

def recurse_fn(a, i, p, m, running_val):
    if i + i > p:
       return running_val, i 
    return recurse_fn(a, i + i , p, m, (running_val * running_val) %m)

def run_tests():
  tests = [
    # Example 1 from book
    ((2, 5, 100), 32),
    # Example 2 from book
    ((2, 5, 30), 2),
    # Edge cases
    ((2, 0, 10), 1),
    ((3, 1, 5), 3),
    ((5, 3, 7), 6),
    # Large test case
    ((123456789, 987654321, 1000000007), 652541198),
  ]
  
  for (a, p, m), want in tests:
    got = power(a, p, m)
    assert got == want, f"\npower({a}, {p}, {m}): got: {got}, want: {want}\n"

if __name__ =='__main__':
    run_tests()