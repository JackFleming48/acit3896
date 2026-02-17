def reverse_list(first):
    """
    Reverse a singly linked list in-place.
    Returns the new first node.
    """
    prev = None
    curr = first

    while curr is not None:
        next_node = curr.next
        curr.next = prev   
        prev = curr        
        curr = next_node

    return prev  

class LLN:
    def __init__(self, contents):
        self.contents = contents
        self.next = None


    def __repr__(self):
        # This isn't the greatest implementation ever, but I don't want to give too much away
        # You could try to improve this, that's up to you
        return f"LLN({str(self.contents)})"

    def insertAfter(self, contents):
        new_node = LLN(contents)
        new_node.next = self.next
        self.next = new_node
        return new_node
        # This function should made a new LLN, and it should attach that LLN after the current one
        #   ... and it should return the new LLN.
        # If there was already a node after the current one, don't destroy it, just bump it over to make space!

    def toList(self):
        # This function is not supposed to print!
        # It should return a list, with all the contents from the Linked List
        ls = []
        curr = self
        while curr.next != None:
            ls.append(curr.contents)
            curr = curr.next
        ls.append(curr.contents)   
        return ls
                

    def findLast(self):
        # This should return the LLN that is last in the LL
        curr = self
        while curr.next != None:
            curr = curr.next
        return curr
        pass

    def findAfter(self, needle):
        # This should return the LLN that has the needle as its contents
        #   But only if it's later-than the current self node
        #   And if there are more than one, return the first one, just like how `List.index` does.
        curr = self.next
        while curr != None:
            if curr.contents == needle:
                return curr
            curr = curr.next
        raise KeyError(needle)

def main():
    first = LLN("alice")
    second = first.insertAfter("bob")
    third = second.insertAfter("carol")

    print("original:", first.toList())

    new_first = reverse_list(first)

    print("reversed:", new_first.toList())

if __name__ == "__main__":
    main()