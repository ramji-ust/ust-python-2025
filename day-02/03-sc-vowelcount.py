 # Create a program to accept text from the user and count the number of vowels
 # in the text

# input
text = input("Enter some text: ")

# process

text = text.lower()
vcount = 0
# vcount = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')
for v in 'aeiou':
    vcount += text.count(v)

# output

print(f"The number of vowels in the text is {vcount}")