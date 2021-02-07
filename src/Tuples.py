# Tuples are immutable!

# Creating Tuples:
# Warning if you create a tuple with 1 item you need to place the , at the 
# end otherwise it may change to an int for example if you do tuple2 = (1).
# The , is important to declare a tuple. You do not nedd the ().
tuple1 = ()
tuple2 = (2,)
tuple3 = 1, 2, 3,

# You can unpack the information from tuples in variables in this way.
# If you want to skip a value use "_".
student_marco = ("Marco", 20, "Maths", 2.1)
name, age, _ , gpa = student_marco

if __name__ == "__main__":

    # Access tuple elements with []
    print(student_marco[0])

    print("Name:", name)
    print("Age:", age)
    print("GPA:", gpa)
