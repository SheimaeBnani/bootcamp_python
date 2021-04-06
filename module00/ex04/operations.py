import sys

def fun(a, b):
        addition = a + b
        subtraction = a - b
        multiplication = a * b
        division = a / b
        modulus = a % b
        return addition, subtraction, multiplication, division, modulus

a=int(sys.argv[1])
b=int(sys.argv[2])
print("Sum :")
print(fun(a, b)[0])
print("Difference :")
print(fun(a,b)[1])
print("Product :")
print(fun(a,b)[2])
print("Division :")
print(fun(a,b)[3])
print("Modulus :")
print(fun(a,b)[4])

