# collection=set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.remove(1)
# # collection.remove(5) #give error 
# collection.add((1, 2, 3))
# collection.add("loom")
# collection.clear()
# # collection.add([1, "logic",4])
# print(len(collection))

collection={"hello", "loom", "logic", "world", "python"}

print(collection.pop())
print(collection.pop())

# set.union( set2 ) #combines both set values & returns new

set1={1, 2, 3}
set2={2, 3, 4}
print(set1.union(set2)) #{1, 2,  3, 4}
print(set1.intersection(set2)) #{2, 3}






