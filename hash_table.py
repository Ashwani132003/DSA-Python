class HashTable:

    #simple hash table without collision solution

    def __init__(self):
        self.Max=10
        self.arr = [None for i in range(self.Max)]

    def get_hash(self,key):
        h=0
        for i in key:
            h+=ord(i)
        return h%self.Max

    # def add(self,key,val):      #replaced by __setitem__ which allow assigning value like this ha['342'] = 291, but for add : ha.add('342',291)
    #     h=self.get_hash(key)
    #     self.arr[h]=val

    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h]
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        self.arr[h] = val
    def __delitem__(self,key):
        h=self.get_hash(key)
        self.arr[h]=None
          



ha = HashTable()
print(ha.get_hash('mar 4'))
print(ha.get_hash('mor 4'))
ha['mar 4'] = 10
ha['mor 4']= 100
# ha.add('ma 4', 1000)

print(ha.arr)
print(ha['mar 4'])
ha['feb 3'] = 20
print(ha['feb 3'])
del ha['mor 4']
print(ha.arr)
ha['mar 4']=75
print(ha.arr)




class HashTableChaining:



    def __init__(self):
        self.Max=10
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self,key):
        h=0
        for i in key:
            h+=ord(i)
        return h%self.Max

    def __getitem__(self,key):
        h=self.get_hash(key)
        for k in range(len(self.arr[h])):
            if self.arr[h][k][0]==key:
                return self.arr[h][k][1]
    
    def __delitem__(self,key):
        h=self.get_hash(key)
        for k in range(len(self.arr[h])):
            if self.arr[h][k][0]==key:
                del self.arr[h][k]
                return
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        present = False
        for k in range(len(self.arr[h])):
            if self.arr[h][k][0]==key:
                self.arr[h][k] = key,val
                present=True
        if not present:
            self.arr[h].append((key,val))      


hac = HashTableChaining()
print(hac.get_hash('mar 4'))
print(hac.get_hash('mor 4'))
hac['mar 4'] = 10
hac['mor 4']= 100

print(hac.arr)
print(hac['mar 4'])
hac['feb 3'] = 20
print(hac['feb 3'])
print(hac.arr)
hac['mar 4']=75
print(hac.arr)
print(hac['feb 3'])

del hac['mar 4']
print(hac.arr)
