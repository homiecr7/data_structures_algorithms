# creating an array

class myArray():
    def __init__(self) -> None:
        self.length = 0 # length of array
        self.data ={} # data stored in dict
    
    def __str__(self): # this function will return the dict when called print
        return str(self.__dict__)

    def get(self, index): # this function will return the array at a particular index
        return self.data[index]
    
    def push(self, item): # pushing the item into an array
        self.length += 1  # adds to index length 
        self.data[self.length - 1] = item
    
    def pop(self): # poping last element
        lastitem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1 # shifting length
        return lastitem
    
    def insert(self, item, index): # inserting an item
        self.length += 1 # adding one to length
        for i in range(self.length - 1, index, -1): # reverse loop to insertion index
            self.data[i] = self.data[i - 1] # shifting items to right
        self.data[index] = item
    
    def delete(self, index): # delete an item
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1] # loop from index to the end of the dict and shifting to left
        del self.data[self.length - 1] # deleting last duplicate
        self.length -= 1

arr = myArray()
arr.push(5)
arr.push(6)
arr.push(7)
arr.insert(8, 1)
arr.insert(9, 2)
arr.delete(3)
print(arr)
    
