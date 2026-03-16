class Tries:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self,word):
        current_level = self.root
        for w in word:
            if w not in current_level:
                current_level[w]= {}
            current_level = current_level[w]
        current_level[self.end_symbol] = True

    def Exists(self,word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        if self.end_symbol in current:
            return True
        else:
            return False
        
trie = Tries()
trie.add("avi")
trie.add("jelly")
print(trie.root)
print(trie.Exists("v"))
print(trie.Exists("avi"))
print(trie.Exists("jelly"))