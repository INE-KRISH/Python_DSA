normal_set = set(["a", "b", "c"])
print('Normal Set')

normal_set.add("d")  #this works and does not raises an error.
print(normal_set)
#frozen set

frozen_set = frozenset(["e", "f", "g"])

print("\nFrozen Set")
#frozen_set.add("h")   this will not work and raise a error in the code
print(frozen_set)


'''
Frozen sets in python are immutable objects that only support methods and operations that produce a result
without affecting the frozen set or sets to which they are applied. While elements of set can be modified at 
any time, elements of the frozen set remain the same after creation.

like the example of the .add() function on the sets.
'''