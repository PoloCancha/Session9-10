try:
    fd = open('/Users/stokesshaun126/PycharmProjects/P2Session9and10/text.txt')
# if the file is in the current directory you don't need the whole path, if it is you can just add the file name
    print("File opened successfully")
    content = fd.read()
    print(content)
    fd.close()
    print("File closed successfully")
except FileNotFoundError:
    print("File not found.")



try:
    with open("text.txt") as fd:
        print("File opened successfully")
        content = fd.read()
        print(content)
    print("File closed successfully")
except FileNotFoundError:
    print("File not found.")

# a safer way is to read the file line by line
with open("text.txt") as fd:
    for line in fd:
        line = line.upper()
        print(line.strip()) # line strip prevents line breaks and copies it direct from the file