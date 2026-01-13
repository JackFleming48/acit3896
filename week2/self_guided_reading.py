'''
A quantile cuts the sorted dataset into equal-sized parts
- Must be sorted
Quantiles are based on position, not the values themselves

Quartiles split the data into 4 equal parts
- Q1, First Quartile, 25th percentile
- Q2, Second Quartile (Median), 50th percentile
- Q3, Third Quartile, 75th percentile

'''

# Computing a percentile

n = 10 # dataset size
p = 25 # desired percentile

position = (p / 100) * (n + 1)
# print(position)

'''
About time.time

Return the time in seconds since the Unix epoch (January 1, 1970) as a floating point number.
- Affected by system clock changes
- NTP sync
- Manual time adjustments
- Not monotonic
- Can have lower precision on some systems
'''

'''
About time.perf_counter()

Return the value (in fractional seconds) of a performance counter:
- Examples
    - clock with the highest available resolution to measure a short duration.

- Highest available resolution
- Not tied to real-world time
- Immune to clock changes

'''

def f(n):
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3*n) + 1

# print("f(3):")
# f(3)
# print("")
# print("f(21):")
# f(21)

#f(3):
#
#f(21):