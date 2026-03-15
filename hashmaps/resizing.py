class Hashmap:
    def __init__(self,size):
        self.hashmap = [None for i in range(size)]
        
    def key_to_index(self, key):
        total = 0
        for c in key:
            total += ord(c)
        return total % len(self.hashmap)
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap.append(None)
            return
        if self.current_load() < 0.05:
            return
        current = self.hashmap
        self.hashmap = [None for i in range(len(current) * 10)]
        for kvp in current:
            if kvp is not None:
                index = self.key_to_index(kvp[0])
                self.hashmap[index] = (kvp[0], kvp[1])

    def current_load(self):
        length = len(self.hashmap)
        count = 0
        if length == 0:
            return 1
        for hash in self.hashmap:
            if hash != None:
                count += 1
        return count / length
    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final

hm = Hashmap(0)
hm.insert("apple",1)
hm.insert("banana",2)
hm.insert("cherry",3)
print(hm)

print(f"Load: {hm.current_load()}")
print(f"Size: {len(hm.hashmap)}")