import stack
import re

wyr = input("Podaj wyrażenie w RPN: ")
wyr = list(wyr)

decimal = "\d"
for i in wyr:
    if re.match(decimal,i)!=None:
        stack.push(int(i))
    else:
        match i:
            case "+":
                stack.push(stack.pop()+stack.pop())
            case "-":
                a=stack.pop()
                b=stack.pop()
                stack.push(b-a)
            case "*":
                stack.push(stack.pop()*stack.pop())
            case "/":
                a=stack.pop()
                b=stack.pop()
                stack.push(b/a)
            case _:
                print(stack.pop())
