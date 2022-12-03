import stack

num = int(input("Podaj liczbę: "))
print(f"Natural number: {num}")

while num!=0:
    stack.push(num%2)
    num//=2

print("Binary number: ",end="")
while(stack.empty()==False):
    print(stack.pop(),end="")