class Trie:
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            current_key = list(current.keys())
            if self.end_symbol in current_key:
                break
            if len(current_key) == 1:
                prefix += current_key[0]
                current = current[current_key[0]]
            else:
                break
        return prefix

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True



trie = Trie()
words = input("Enter words separated by spaces: ").split()
for word in words:
    trie.add(word)
print("Longest common prefix:", trie.longest_common_prefix())

