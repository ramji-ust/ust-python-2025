# Program to accept two numbers from the user
# and tell if the difference of the two numbers is positive, negative or zero after subtraction

# input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# process
res = a- b

# output
print("Differnce is : ", abs(res))
if( res > 0):
    print("The result is positive")
elif (res < 0):
    print("The reuslt is negative")
else:
    print("The result is zero")