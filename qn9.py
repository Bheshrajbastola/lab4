'''Write a program to find the factorial of a number.'''
def fact(num):
    if num<=1:
        return 1
    else:
        return num*fact(num-1)
ans=fact(5)
print("fact of given num is : ",ans)

