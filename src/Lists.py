# You can create a new empty list in two ways in python
list1 = []
list2 = list()

# You can check the length with the len() function.
# This function is not attached to the list object.
# false => names.len() correct => len(names) 
names = ["Heiko", "Valentin", "Ajinka"]

# Python has dynamic typing so we can store different
# datatypes in the same list
mixed = ["String", 1, 2.0, True]

# Sorting:
numbers = [2, 1, 3, 4, 6, 5, 8, 9, 7]

# Sorted will return a new list with the sorted numbers.
# Default it will sort ascending. sorted(numbers, reverse=true)
sorted_numbers = sorted(numbers)

# You can sort the list without creating a copy with .sort()
numbers.sort()

# Adding:
numbers.append(10)
numbers.insert(10, 77)

# You can combine two list with .extend()
numbers.extend(sorted_numbers)

# Searching:
mates = ["Marco", "Bodo", "Tobias", "Marco"]

# Will return true if there is such an item in the list
Bodo_in_List = "Bodo" in mates

# Returns the FIRST index for such an item in the list
Index_of_Tobias = mates.index("Tobias")

# Returns the amount of such entries in the list
Marco_count_in_List = mates.count("Marco")

# Removeing:

# It removes only the first index for such an item in the list
mates.remove("Marco")

# Removes the last item in the list
poped = mates.pop()

# Removes the item at a specific index
poped_index = mates.pop(1)

if __name__ == "__main__":

    print(list1)
    print(list2)
    print( len(names) )
    print(mixed)
    print(sorted_numbers)
    print(numbers)
    print(Bodo_in_List)
    print(Index_of_Tobias)
    print(Marco_count_in_List)
    print(poped)
    print(poped_index)