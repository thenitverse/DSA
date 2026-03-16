class Tries:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self,word):
        current_level = self.root
        for w in word:
            if w not in current_level:
                current_level[w] = {}
                current_level = current_level[w]
        current_level[self.end_symbol] = True

trie = Tries()
trie.add("nitika")
trie.add("help")
trie.add("hello")

print(trie.root)