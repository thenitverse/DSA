class HashMap:
    def __init__(self,size):
        self.hashmap = [None]*size

    def key_to_index(self,key):
        total = 0
        for ch in key:
            c = ord(ch)
            total+=c
        index = total % len(self.hashmap)
        return index
    def insert(self,key,value):
        index = self.key_to_index(key)
        self.hashmap[index] = value

    def get(self,key):
        index = self.key_to_index(key)
        return self.hashmap[index]
    

hm = HashMap(20)
hm.insert("ali","ali's data")
hm.insert("joy","joy's data")

print(hm.get("ali"))
print(hm.get("joy"))
print(hm.key_to_index("ali"))
print(hm.key_to_index("joy"))

        