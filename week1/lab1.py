def linear_search(needle, haystack):
    for i, num in enumerate(haystack):
        if num == needle:
            return i
    return None

print(linear_search(8, [6, 2, 8, 4]))
print(linear_search(4, [6, 2, 8, 4]))
print(linear_search(5, [6, 2, 8, 4]))

def binary_search(needle, haystack):
    high = len(haystack) - 1
    low = 0

    while high >= low:

        mid = ((high - low) // 2) + low

        if haystack[mid] == needle:
            return mid

        elif haystack[mid] > needle:
            high = mid-1

        elif haystack[mid] < needle:
            low = mid+1
        
    return None


print(binary_search(8, [2, 4, 6, 8]))
print(binary_search(2, [2, 4, 6, 8]))
print(binary_search(1, [2, 4, 6, 8]))
print(binary_search(99, [2, 4, 6, 8]))
print(binary_search(4, [2, 4, 6, 8, 98, 99, 100, 101, 102, 103, 104]))
print(binary_search(103, [2, 4, 6, 8, 98, 99, 100, 101, 102, 103, 104]))

def linear_search_multi(needle, haystack):
    ls = []
    for i, num in enumerate(haystack):
        if num == needle:
            ls.append(i)
    return ls

print(linear_search_multi(8, [6, 2, 8, 4, 8, 7]))
print(linear_search_multi(4, [6, 2, 8, 4, 8, 7]))
print(linear_search_multi(5, [6, 2, 8, 4, 8, 7]))
