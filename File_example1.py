try:
    fd = open('text.txt')
    print("File opened successfully")
    content = fd.read()
    print(content)
    fd.close()
    print("File closed successfully")
except FileNotFoundError:
    print("File not found")

try:
    with open('text.txt') as fd:
        print("File opened successfully")
        content = fd.read()
        print(content)
        fd.close()
        print("File closed successfully")
except FileNotFoundError:
        print("File not found")

# a safer way is to read the file line by line
with open('text.txt') as fd:
    for line in fd:
        line = line.upper()
        print(line, end="") # or line.strip(), strips new line characters from end