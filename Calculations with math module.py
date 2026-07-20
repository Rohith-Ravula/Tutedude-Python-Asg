import math
def operations(n):
    expression1=math.sqrt(n)
    expression2=math.log(n)
    expression3=math.sin(n)
    return expression1,expression2,expression3
a=int(input("Enter the number: "))
result1,result2,result3=operations(a)
print(f"Square root of {a} is: {result1}")
print(f"Natural logarithm of {a} is: {result2}")
print(f"Sine of {a} is: {result3}")

# from math import sqrt,log,sin
# def arithmatic(n):
#     exp1=sqrt(n)
#     exp2=log(n)
#     exp3=sin(n)
#     return exp1,exp2,exp3
# a=int(input("Enter the number: "))
# res1,res2,res3=arithmatic(a)
# print(f"Square root of {a} is {res1}")
# print(f"Logarithm of {a} is {res2}")
# print(f"Sine of {a} is {res3}")


