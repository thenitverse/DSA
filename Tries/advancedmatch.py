class Trie:
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

    def advanced_find_matches(self, document, variations):
        matches = set()
        for i in range(len(document)):
            current_level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch in variations:
                    ch = variations[ch]
                if ch not in current_level:
                    break
                current_level = current_level[ch]
                if self.end_symbol in current_level:
                    matches.add(document[i : j + 1])
        return matches




trie = Trie()

words = input("Enter words to filter (space separated): ").split()
for word in words:
    trie.add(word)

variations = {"@": "a", "1": "i", "3": "e", "0": "o", "!": "i", "4": "a"}

document = input("Enter a document to scan: ")

matches = trie.advanced_find_matches(document, variations)

if matches:
    print(f"Matches found: {matches}")
else:
    print("No matches found.")