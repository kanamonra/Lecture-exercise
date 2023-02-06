stack = [None for _ in range(5)]

top = -1
top += 1
stack[top] = "Coffee"
top += 1
stack[top] = 'Latte'
top += 1
stack[top] = 'Cappuccino'
top += 1
stack[top] = 'Ice tea'
top += 1
stack[top] = 'Mint tea'

for i in range(len(stack)-1, -1, -1):
    print(stack[1])

data = stack[top]
stack[top] = None
top -= 1
print("pop data -->", data)
