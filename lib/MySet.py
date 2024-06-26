class MySet:

    def __init__(self, list = []):
        self.dictionary = {} # we need to keep track of all the values  that passed in. O(1) for insertion,deletion, and accessing ,search O(n)

        for value in list:
            self.dictionary[value] = True


    def has(self, value):
        return value in self.dictionary
    

    def add(self, value):
        self.dictionary[value] = True # value is the key, if it does not exist => returns KeyError. 
        return self # return the updated set
    

    def delete(self, value):
        # removes the value from the set.
        #returns the updated set
        self.dictionary.pop(value, None)  # O(1) runtime
        return self

    def size(self):
        return len(self.dictionary)