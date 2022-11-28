try:
    with open("8.txt") as file:
        text = file.read()
except:
    print("er")
print(text)