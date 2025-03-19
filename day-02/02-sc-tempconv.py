# Program to convert temperature from celcius to farenheit and vice versa

'''
What do you want to do?
1. convert c to f 
2. convert f to c 
Your choice -> 1

Enter the celius value? 100
------------------------------------------
212
'''
# input

print("Tempreature conversion app\n")
print("What do you want to do? ")
print("1. convert c to f")
print("2. convert f to c")
choice = int(input('Your choice -> '))

# process

if(choice == 1):
    temp = float(input("Enter celcius value: "))
    res = temp * 1.8 + 32
elif(choice == 2):
    temp = float(input("Enter farenheit value: "))
    res = (temp - 32) / 1.8
else:
    temp = 'Invalid'
    res = 'Invalid'

# output

print("------------------------------------------")
print(res)

'''
    if(a == b):
        if(c == d):
            <statements>
        else:
            <statments>
    elif(a > b):
         if(c == d):
            <statements>
        else:
            <statments>
    else:
         if(c == d):
            <statements>
        else:
            <statments>

'''