# implementing own hash tables

class hash_table():
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size

    def __str__(self):
        return str(self.__dict__)

    def _hash(self, key): #Our custom hash function
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % self.size #ord(key[i]) gives the unicode code point of the character key[i]
        return hash #The hash value obtained after applying the hash function to the key is returned
    
    def set(self, key, value):
        hash = self._hash(key)
        if not self.data[hash]:
            self.data[hash] = [[key, value]]
        else:
            self.data[hash].append([key, value])
    
    def get(self, key):
        hash = self._hash(key)
        if self.data[hash]:
            for i in self.data[hash]:
                if key in i:
                    return i[1]
            return "Key doesn't exist"
        else:
            return "Key doesn't exist"

new_hash = hash_table(2)
new_hash.set("one", 1)
new_hash.set("two", 2)
new_hash.set("five", 5)
new_hash.set('three',3)
new_hash.set('four',4)
print(new_hash)
