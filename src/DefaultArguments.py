def function_with_default_arguments(first, second = "Marco", third = "Barbara"):
    print(first)
    print(second)
    print(third)

# Warning: You should never use mutable default arguments in functions such as
# a list because the default argument will not be instantiated for each call!
def function_with_mutable_default_argument(a, b = []):
    b.append(a)
    return print("B is:", b)

# This is the correct way to define a function with mutable default arguments 
# such as list. It will work as intended.
def function_with_mutable_default_argument_better(a, b = None):

    if b is None:
        b = []
    
    b.append(a)
    return print("B is:", b)


if __name__ == "__main__":

    # You can change the order of the arguments if you label them
    function_with_default_arguments(third = "Simon", second="Stefan", first="Peter")
    print()

    # You would expect "B is: [2]" for as the result for the second function call but
    # it is "B is: [1, 2]" because the default list argument b is not instaniated for
    # each functin call.
    function_with_mutable_default_argument(1)
    function_with_mutable_default_argument(2)
    print()

    function_with_mutable_default_argument_better(1)
    function_with_mutable_default_argument_better(2)
    print()