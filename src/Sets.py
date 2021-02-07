# A set cannot contain duplicates

# Creating a Set:
# Warning: You cannot create a empty set with {} because that
# will create a dictionary and not a set!
set1 = set()
set2 = {"Matthias", "Marco", "Ismail", "Heiko", "Matthias"}

# You can only put inmutable items in a set. => You cannnot put
# a list in a set because it is mutable.

# You can create a set from a list => Removing duplicates
list1 = ["Petet", "Stefan", "Valentin", "Peter"]
set3 = set(list1)

# Removing:
colors = {"Red", "Green", "Blue"}

# Discard will remove items in the list but will not throw
# an exception if the item was not in the set
colors.discard("Pink")

# Remove will remove items in a set but will thorw an exception
# if the item was not in the set
colors.remove("Red")

# Updating:
# This will combine the two sets to one set
colors2 = {"Pink", "Orange"}
colors.update(colors2)

# Update expects a sequence of data. If you put a String in update
# it will interpret the String as a sequence of charchakters 
colors.update("Matthias")

# Contains:
is_Blue_in_set = "Blue" in colors

# Set Operations: Union 
rainbow_colors = {"Red", "Orange", "Yellow", "Blue", "Purple"}
favorite_colors = {"Red", "Orange", "Black"}

color_union  = rainbow_colors.union(favorite_colors)
color_union2 = rainbow_colors | favorite_colors

# Set Operation: Intersection
color_instersection = rainbow_colors.intersection(favorite_colors)
color_instersection2 = rainbow_colors & favorite_colors

# Set Operation: Difference
color_difference = rainbow_colors.difference(favorite_colors)
color_difference2 = rainbow_colors ^ favorite_colors

if __name__ == "__main__":

    print(set2)
    print(set3)

    print(colors)
    print(is_Blue_in_set)

    print(color_union)
    print(color_union2)

    print(color_instersection)
    print(color_instersection2)

    print(color_difference)
    print(color_difference2)
