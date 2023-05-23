# implementing own hash tables

class hash_table():
    def __init__(self, size): # constructor initialization
        self.size = size # create an array size "size" and value None
        self.data = [None] * self.size

    def __str__(self): # print the attributes of the object in the form of dictionary
        return str(self.__dict__)

    def _hash(self, key): #Our custom hash function
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % self.size #ord(key[i]) gives the unicode code point of the character key[i]
        return hash #The hash value obtained after applying the hash function to the key is returned
    
    def set(self, key, value):  # sets the value in a dictionary
        hash = self._hash(key) # get the hash for the location
        if not self.data[hash]: # if location is not occupied
            self.data[hash] = [[key, value]]
        else: # if location is occupied
            self.data[hash].append([key, value])
    
    def get(self, key): # gets the value
        hash = self._hash(key) # locates the hashed key
        if self.data[hash]: # if the location is occupied
            for i in self.data[hash]: # looping over each array to check the key
                if key in i:
                    return i[1]
            return "Key doesn't exist" # if key doesnt exist
        else: # if hash doesnt exist
            return "Key doesn't exist"
    
    def key(self):
        keys = []
        for i in self.data: # loop over the whole length of data
            if i is not None: # will go inside if index is not none
                for j in i: # will loop over nested object or collision
                    if j is not None: # will go inside if it is not none
                        keys.append(j[0])
        return keys
    
new_hash = hash_table(2)
# new_hash.set("one", 1)
# new_hash.set("two", 2)
# new_hash.set("five", 5)
# new_hash.set('three',3)
# new_hash.set('four',4)
print(new_hash)
print(new_hash.key())
