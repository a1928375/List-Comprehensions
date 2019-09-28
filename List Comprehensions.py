#print ([i for i in [x**3 for x in range(100) if x%2 == 0] if i < 20])    or
print ([x**3 for x in range(100) if x%2 == 0 and x**3 < 20])
