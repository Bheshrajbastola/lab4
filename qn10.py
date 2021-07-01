'''Write a Python program that accepts a string and calculate the number of digits and letters'''
word=str(input("enter word with letter : "))
d=0
l=0
for i in word:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        l=l+1
print("digit is  :",d)
print("letter is :",l)
