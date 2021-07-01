'''Write a Python program to convert temperatures to and from celsius, fahrenheit.C = (5/9) * (F -32)'''

fahrenheit=float(input("enter a number in fahrenheit : "))
c=(5/9)*(fahrenheit-32)#formula
print(f" {fahrenheit} fahrenheit is {c} degree celcius")

# now conversion from celcius to fahrenheit

celsius=int(input("enter a number in celcius : "))
f=(9/5)*c+32 #inverse of formula
print(f"{celsius} celsius is {f} degree fahrenheit")


