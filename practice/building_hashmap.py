class Hashmap:
    def __init__(self,capacity):
        self.capacity = capacity
        self.slots = [None]*capacity
        self.count = 0
 

    def _Hash(self,key):
        total = 0
        for chr in key:
            total += ord(chr)

        return total % self.capacity
    def _resize(self):
        old_slots = self.slots
        self.capacity = self.capacity*2
        self.slots = [None]*self.capacity
        self.count = 0

        for item in old_slots:
            if item is not None:
                key,value = item
                self.set_item(key,value)

    def set_item(self,key,value):
        if (self.count+1)*2 > self.capacity:
            self._resize()

        index = self._Hash(key)
        while True:
            if self.slots[index] is  None:
                self.slots[index] = (key,value)
                self.count+=1
                return
            current_key,current_value = self.slots[index]
            if current_key == key:
                self.slots[index] = (key,value)
                return
            index +=1
            if index == self.capacity:
                index = 0

    def get_item(self,key):
        index = self._Hash(key)
        checked = 0

        while checked < self.capacity:
            item = self.slots[index]
            if item is None:
                return None
            current_key,current_value = item
            if current_key == key:
                return current_value
            
            index += 1
            if index == self.capacity:
                index = 0

            checked+=1
        return None


hm = Hashmap(2)
hm.set_item("joy",20)
hm.set_item("Roy",35)
hm.set_item("jay",34) # here resizing will work
print(f"current capacity: {hm.capacity}")
print(f"Age of joy: {hm.get_item("joy")}")
print(f"Age of Roy: {hm.get_item("Roy")}")
print(f"Age of jay after resizing the slots: {hm.get_item("jay")}")
hm.set_item("joy", 29)
print(f"updated age of joy: {hm.get_item("joy")}")



            

