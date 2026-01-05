# def isPalindrome(str):
#     backwards = str[::-1]
#     if str == backwards:
#         return True
#     return False

# print(isPalindrome("abba"))
# print(isPalindrome("abomination"))
# print(isPalindrome('racecar'))
# print(isPalindrome('r aceca r'))
# print(isPalindrome('race car'))
# print(isPalindrome('🙃🙂🙃'))

# def counter(i):
#     count = {}
    
#     for x in i:
#         if x in count:
#             count[x] += 1
#         else:
#             count[x] = 1
#     return count

# print(counter('abcabc'))
# print(counter(['ab', 'ab', 'ba', 'ba', 'aba', 'ab']))


def ourSharedValues(iter1, iter2):
    count = {}
    count2 = {}
    res = {}
    for x in iter1:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    
    for x in iter2:
        if x in count2:
            count2[x] += 1
        else:
            count2[x] = 1

    for x in count:
        if x in count2:
            if count[x] > count2[x]:
                res[x] = count2[x]
            elif count[x] < count2[x]:
                res[x] = count[x]
            elif count[x] == count2[x]:
                res[x] = count[x]
        
    return res



print(ourSharedValues('abcdef', 'abba'))
print(ourSharedValues('babar', 'librarian'))