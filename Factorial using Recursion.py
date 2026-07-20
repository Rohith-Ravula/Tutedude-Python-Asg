# Factorial using Normal function
# def factorial(n):
#     fact=1
#     if n==0:
#         return n
#     else:
#         while n>=1:
#             fact*=n
#             n-=1
#         return fact
# a=int(input("Enter a number: "))
# print(f"Factorial of {a} is {factorial(a)}")

# Factorial using Recursion:
def fact_rec(n):
# Base/ Terminal condition:
    if n==1:
        return n
    else:
# Recursive function
         while n>1:
             fact=n*fact_rec(n-1)
             return fact
b=int(input("Enter a number: "))
print(f"Factorial of {b} is {fact_rec(b)}")






