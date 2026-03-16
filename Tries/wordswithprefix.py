class Tries:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self,word):
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
        current_level[self.end_symbol] = True

    def search_level(self,current_level , current_prefix,words):
        if self.end_symbol in current_level:
            words.append(current_prefix)
        for ch in sorted(current_level):
            if ch != self.end_symbol:
                self.search_level(current_level[ch],current_prefix + ch,words)
        return words
    
    def words_with_prefix(self,prefix):
        matching_list = []
        current_level = self.root
        for ch in prefix:
            if ch not in current_level:
                return matching_list
            if ch in current_level:
                current_level = current_level[ch]
            self.search_level(current_level,prefix,matching_list)
            return matching_list
        
trie = Tries()

print("Enter words one by one.Type 'done' when finished: ")
while True:
    word = input("words: ")
    if word == "done":
        break
    trie.add(word)

prefix = input("Enter prefix to search: ")
results = trie.words_with_prefix(prefix)
if results:
    print(f"wordswith prefix '{prefix}': {results}")
else:
    print(f"NO words found with prefix '{prefix}'")
    

            

        