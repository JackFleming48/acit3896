class DLLN:
    def __init__(self, contents):
        self.contents = contents
        self.next = None
        self.prev = None  

    def __repr__(self):
        return f"LLN({str(self.contents)})"

    def insertAfter(self, contents):
        """
        Insert a new node immediately after self.
        Return the newly created node.
        """
        new_node = DLLN(contents)

        # new_node goes between self and old_next
        old_next = self.next

        new_node.prev = self
        new_node.next = old_next

        self.next = new_node

        if old_next is not None:
            old_next.prev = new_node

        return new_node

    def insertBefore(self, contents):
        """
        Insert a new node immediately before self.
        Return the newly created node.
        """
        new_node = DLLN(contents)
        old_prev = self.prev

        new_node.next = self
        new_node.prev = old_prev

        self.prev = new_node

        if old_prev is not None:
            old_prev.next = new_node

        return new_node

    def toList(self):
        """
        Return a Python list of contents from self onward.
        """
        ls = []
        curr = self
        while curr is not None:
            ls.append(curr.contents)
            curr = curr.next
        return ls

    def findLast(self):
        """
        Return the last node reachable from self going forward.
        """
        curr = self
        while curr.next is not None:
            curr = curr.next
        return curr

    def findFirst(self):
        """
        Return the first node reachable from self going backward.
        """
        curr = self
        while curr.prev is not None:
            curr = curr.prev
        return curr

    def findAfter(self, needle):
        """
        Return the first node AFTER self (strictly later) whose contents == needle.
        Raise KeyError if not found.
        """
        curr = self.next
        while curr is not None:
            if curr.contents == needle:
                return curr
            curr = curr.next
        raise KeyError(needle)

    def findBefore(self, needle):
        """
        Return the first node BEFORE self (strictly earlier) whose contents == needle.
        Search backward; raise KeyError if not found.
        """
        curr = self.prev
        while curr is not None:
            if curr.contents == needle:
                return curr
            curr = curr.prev
        raise KeyError(needle)
    


def main():
    one = DLLN("one")
    two = one.insertAfter('two')
    print("should be one two:", one.toList())

    five = one.findLast().insertAfter('five')
    print("should be one two five:", one.toList())

    three = two.insertAfter('three')
    print("should be one two three five:", one.toList())

    zero = one.insertBefore('zero')
    print("should be zero one two three five:", one.findFirst().toList())

    four = one.findAfter('five').insertBefore('four')
    print("should be zero one two three four five:", one.findFirst().toList())

    the_two = one.findFirst().findAfter('two')
    print("should successfully find two:", the_two)

    the_two = one.findLast().findBefore('two')
    print("should successfully find two:", the_two)


    print("should fail to find two:")
    try:
        print(two.findBefore('two'), "this should not print")
    except KeyError as ke:
        print("KEY ERROR", ke)
    
if __name__ == "__main__":
    main()