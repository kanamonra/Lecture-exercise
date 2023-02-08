# Chapter 10
# recursion selfEX
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

num = int(input('Please enter number for factorial result: '))
print('The factorial of', num, 'is', factorial(num))