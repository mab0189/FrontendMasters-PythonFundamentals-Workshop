status = "Unchanged"

# The function scope is preventing the change of the global variable
def function_that_will_not_change_global():
    status = "Changed"
    return

# If we want to use global variables we need to 'define' them first 
# with the global keyword and the variable name inside the function.
def function_that_will_change_global():
    global status
    status= "Changed"
    return


if __name__ == "__main__":

    print(status)

    function_that_will_not_change_global()
    print(status)

    function_that_will_change_global()
    print(status)