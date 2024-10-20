class Node:
    def __init__(self):
        self.next = [None] * 26
        self.end = False


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, string):
        """Insert a string into the Trie."""
        p = self.head
        for char in string:
            id = ord(char.lower()) - 97
            if not p.next[id]:
                p.next[id] = Node()
            p = p.next[id]
        p.end = True

    def find(self, string, k):
        """Find the longest prefix of string starting from index k that exists in the Trie."""
        p = self.head
        for i in range(k, len(string)):
            if p.end:
                return i
            id = ord(string[i].lower()) - 97
            if not p.next[id]:
                return 0
            p = p.next[id]
        return len(string) - 1


def longest_substring(review, prohibited):
    """Find the longest substring of review that does not contain any prohibited strings."""
    trie = Trie()
    for word in prohibited:
        trie.insert(word)

    mp = {}
    for i in range(len(review)):
        s = trie.find(review, i) - 1
        if s > 0:
            mp[s] = i

    last_index = 0
    max_len = 0

    # Greedy implementation
    for i in range(len(review)):
        if i in mp and last_index <= mp[i]:
            max_len = max(max_len, i - last_index)
            last_index = mp[i] + 1

    max_len = max(max_len, len(review) - last_index)
    return max_len


# Example usage
review = "FastDeliveryOkayProduct"
prohibited = ["yo", "eli", "eryokay"]
print(longest_substring(review, prohibited))  # Output: 11
