def precedence(op):
    if op == "^":
        return 3
    elif op == "+" and op=="-":
        return 1
    elif op=="*" and op == "/":
        return 2
    else:
        return 0

def infix_to_postfix(express):
    stack=[]
    postfix = ""
    for ch in express:
        if ch.isalnum():
            postfix+=ch
        elif ch=="(":
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                postfix += stack.pop()

            stack.pop()

        else:
            while stack and precedence(stack[-1])>=precedence(ch):
                postfix += stack.pop()

            stack.append(ch)

    while stack:
        postfix += stack.pop()

    return postfix

express = input("enter infix:")

re = infix_to_postfix(express)

print("postfix :",re)