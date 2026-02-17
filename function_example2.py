def add_numbers(a, b, c=0):
    """
    Adds 2 or 3 numbers
    :param a: first number
    :param b: second number
    :param c: third number
    :return: result of addition of two/three numbers
    """
    return a + b + c

print(add_numbers(1, 2, 3))
print(add_numbers(5, 7,))

# a function can call itself (recursive function)
def factorial(n):
    """
    Calculates the factorial of n
    :param n: the n
    :return: factorial of n
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def rec_factorial(n):
    if n == 0:
        return 1
    return n * rec_factorial(n - 1)

print(factorial(6))
print(rec_factorial(6))

# functions can call other functions

def bond_greeting(first, last, lang = "fr"):
    """
    Does the bond greeting
    :param first: forename
    :param last: surname
    :param lang: language
    :return: the greeting
    """
    if lang == "en":
        return english_greeting(first, last)
    elif lang == "fr":
        return french_greeting(first, last)
    elif lang == "esp":
        return spanish_greeting(first, last)

def english_greeting(first, last):
    return f"The name is {last}, {first} {last}"

def french_greeting(first, last):
    return f"J'mappelle le{last}, {first} le{last}"
def spanish_greeting(first, last):
    return f"Me Llamo {last}ito, {first}isto {last}ito"

print(bond_greeting("James", "Bond"))
print(bond_greeting("James", "Bond", lang = "en"))