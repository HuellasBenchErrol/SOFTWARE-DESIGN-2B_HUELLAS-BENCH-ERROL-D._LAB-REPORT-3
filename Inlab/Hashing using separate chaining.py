def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")

        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()


HashTable = [[] for _ in range(10)]


def Hashing(keyvalue):
    return keyvalue % len(HashTable)


def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)


insert(HashTable, 10, 'Manila')
insert(HashTable, 25, 'Cebu')
insert(HashTable, 20, 'Pangasinan')
insert(HashTable, 9, 'Dagupan')
insert(HashTable, 21, 'Urdaneta')
insert(HashTable, 21, 'Dasol')

display_hash(HashTable)
