def linear_search(needle, haystack):
    for i, x in enumerate(haystack):
        if x == needle:
            return i
    return None

# print(linear_search(8, [6, 2, 8, 4]))
# print(linear_search(4, [6, 2, 8, 4]))
# print(linear_search(5, [6, 2, 8, 4]))

def binary_search(needle, haystack):
    maxi = len(haystack) - 1
    low = 0

    while maxi >= low:

        mid = ((maxi - low) // 2) + low

        if haystack[mid] == needle:
            return mid
        
        elif needle > haystack[mid]:
            low = mid + 1

        elif needle < haystack[mid]:
            maxi = mid - 1
    
    return None

print(binary_search(8, [2, 4, 6, 8]))
print(binary_search(2, [2, 4, 6, 8]))
print(binary_search(1, [2, 4, 6, 8]))
print(binary_search(99, [2, 4, 6, 8]))
print(binary_search(4, [2, 4, 6, 8, 98, 99, 100, 101, 102, 103, 104]))
print(binary_search(103, [2, 4, 6, 8, 98, 99, 100, 101, 102, 103, 104]))