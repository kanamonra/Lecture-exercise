# Chapter 10 Recursion
# Palindrome

def palindrome(pStr):
    if len(pStr) <= 1:
        return True

    if pStr[0] != pStr[-1]:
        return False

    return palindrome(pStr[1:len(pStr) - 1])


strAry = ["reaver", "kayak", "Borrow or rob", "Lie or iel", "fight and dna th gif"]


for testStr in strAry:
    print(testStr, end='--> ')
    testStr = testStr.lower().replace(' ', '')
    if palindrome(testStr):
        print('O')
    else:
        print('X')
