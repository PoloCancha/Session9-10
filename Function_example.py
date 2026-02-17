# def allows us to create our own functions
# """ allows us to make a "fancy" comment instead of using #
def greeting():
    """
    Prints out a bunch of greetings in different languages
    :return: None
    """
    print("Hello World")
    print("Hola")
    print("Bonjour")
    print("Ciao")
    print("Hallo")
    print("Privet")
    print("Ni Hao")

for i in range (10):
    greeting()
print("I can take a break")
for i in range (5):
    greeting()

print(help(greeting))

def greeting2(name):
    """
    Prints out a bunch of greetings in different languages
    :param name: the name of the person to greet
    :return:
    """
    print("Hello World", name)
    print("Hola", name)
    print("Bonjour", name)
    print("Ciao", name)
    print("Hallo", name)
    print("Privet", name)
    print("Ni Hao", name)
for i in range (10):
    greeting()
print("I can take a break")
for i in range (5):
    greeting2("John")

def greeting3(name):
    """
    Prints out a bunch of greetings in different languages
    :param name: the name of the person to greet
    :return:
    """
    message = ""
    message += f"Hello {name}\n"
    message += f"Bonjour {name}\n"
    message += f"Hola {name}\n"
    message += f"Hallo {name}\n"
    message += f"Privet {name}\n"
    message += f"Ni Hao {name}\n"
    return message

for i in range (10):
    greeting()
print("I can take a break")
for i in range (5):
    greeting2("John")
print(greeting3("Bob").replace("Bob", "Billy Bob").upper())
