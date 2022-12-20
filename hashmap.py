# Hash maps are indexed data structures. A hash map makes use of a hash function to compute an index with a key into an array of buckets or slots
def print_hash(hash):
    for key in hash:
        print(key, "->", hash[key])


hm = {0: 'first', 1: 'second', 2: 'third', 3: 'fourth', 4: 'fifth', 5: 'sixth'}
print_hash(hm)
print()
