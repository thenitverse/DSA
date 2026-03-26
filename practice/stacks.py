

def make_stack():
    return []

def push(stack, value):
    stack.append(value)

def pop(stack):
    if stack != []:
        return stack.pop()
    return None

def peek(stack):
    if stack != []:
        return stack[-1]
    return None

def is_empty(stack):
    return stack == []




s = make_stack()

push(s, "a")
push(s, "b")
push(s, "c")

print(peek(s))   # "c"  (doesn't remove it)
print(pop(s))    # "c"  (removes it)
print(pop(s))    # "b"
print(is_empty(s))  # False
print(pop(s))    # "a"
print(is_empty(s))  # True
print(pop(s))    # None  (nothing left, safe)