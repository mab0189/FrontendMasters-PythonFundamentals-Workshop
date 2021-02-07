# Dictonary Keys can only be immutable

# Creating dictionarys
dict1 = {}
dict2 = dict()
dict3 = {1: "Franziska", 2: "Julia", 3: "Karina"}

# Get: Throws no exception if the key does not exsist in the dictionary.
# You can also provide a default return value for get if the key does not
# exsists.
value_4 = dict3.get(4, "Default Value")

colors = {"r": "Red", "g": "Green", "b":"Blue"}
colors.update(dict3)


if __name__ == "__main__":

    print(dict3[2])
    print(value_4)
    print(colors)
    print(colors.keys())
    print(colors.values())
    print(colors.items())
