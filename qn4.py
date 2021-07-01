'''Write a Python program to construct the following pattern, using a nested for loop'''

row=5
for i in range(0,row):
    for j in range(0,i+1):
        print(" *",end='')
    print("\r")
for i in range(5,0,-1):
    for j in range(i-1):
        print(" *",end='')
    print("\r")