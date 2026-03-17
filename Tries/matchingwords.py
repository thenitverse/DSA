class Trie:
    def find_matches(self, document):
        s = set()
        for i in range(len(document)):
            current_level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in current_level:
                    break
                current_level = current_level[ch]
                if self.end_symbol in current_level:
                    s.add(document[i:j+1])
        return s

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
words_input = input("Enter words separated by space: ").split()

for word in words_input:
    trie.add(word)

document = input("Enter a document: ")

matches = trie.find_matches(document)

print("Matches found:", matches)
