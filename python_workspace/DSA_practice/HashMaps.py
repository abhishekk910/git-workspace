class HashMap:

    def __init__(self):
        self.size = 10
        self.bucket = [None] * self.size 
        print(self.bucket) 

    def hashFunction(self, key):
        Hash = 0
        for char in key:
            Hash += ord(char) 
        return Hash % self.size 

    def Add(self, key, value):
        keyIndexHash = self.hashFunction(key)
        arr = [key, value]

        if self.bucket[keyIndexHash] is None:
            self.bucket[keyIndexHash] = list([arr])
            return True 
        else:
            """
            [
                ["apple", "Apple"]
            ]
            """
            for pair in self.bucket[keyIndexHash]:
                if pair[0] == key:
                    pair[1] = value  #replace value. 
                else:
                    pass 
            self.bucket[keyIndexHash].append(arr)
            return True 

    def __setitem__(self, key, value):
        return self.Add(key, value) 

    def print(self):
        print(self.bucket) 

    def __str__(self):
        return f"{self.bucket}" 

    def get(self, key):
        keyHashIndex = self.hashFunction(key)
        if self.bucket[keyHashIndex] is None:
            return None
        else:
            for pair in self.bucket[keyHashIndex]:
                if pair[0] == key:
                    return pair[1] 
            return None 

    def __getitem__(self, item):
        return self.get(item) 

    def delete(self, key):
        keyHashIndex = self.hashFunction(key) 
        if self.bucket[keyHashIndex] is None:
            return None 
        else:
            for i in range(0, len(self.bucket[keyHashIndex])):
                self.bucket[keyHashIndex].pop()
                return True 
            return None 

if __name__ == "__main__":
    d = HashMap()
    d["name"] = "Abhishek"
    # d["eman"] = "Test"
    # d.Add("name", "Abhishek")
    print(d)
    # print(d["name"])
    d.delete("name")
    print(d)


