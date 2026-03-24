import time

before = time.perf_counter()

b = 0
for x in range(100000000):
    b += x

after = time.perf_counter()

total = after-before

print(total)
print(b)