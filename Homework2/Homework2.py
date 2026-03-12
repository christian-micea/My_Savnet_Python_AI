# Exercise 2.1
# print("Astăzi mă duc la \"facultate\".")
# print("/*\\/*\\*/*\\/*\\")
# print("Python")
# print("\\./\\./\\./\\./")
# print("P\ty\tt\th\to\tn")

# Exercise 2.2
# nume = input("Cum te numesti? ")
# varsta = input("Ce varsta ai? ")
# print("Ceau " + nume + "! Te-ai nascut in anul " + str(2026 - int(varsta)))

# Exercise 2.3
# string = input("Introduceti un sir: ")
# print("Lungimea sirului este {length}".format(length=len(string)))
# print(f"Lungimea sirului este {len(string)}")
# print("Lungimea sirului este " + str(len(string)))
# print("Lungimea sirului este", len(string))

# Exercise 2.4
def pyramid(height, size, character):
    for i in range(height):
        print((character * (2 * i + 1)).center(size))

def rhombus(height):
    # the format is a number of pairs of /\ per level with either a - or _ in the middle, alternating between levels
    # the center is of '-' times the no. of characters on the last level + 2 
    # and lastly, the first half mirrored
    for i in range(height):
        print(((i + 1) * "/" + ("-" if i % 2 == 0 else "_") + (i + 1) * "\\").center(2 * (height + 1) + 1))
    print(((2 * (height + 1) + 1) * "-"))
    for i in range(height - 1, -1, -1):
        print(((i + 1) * "\\" + ("-" if i % 2 == 0 else "_") + (i + 1) * "/").center(2 * (height + 1) + 1))

def trapesus(height, base=4):
    # argumentul base luat ca default 4 pentru a se conforma cu desenul din enunt
    # center este de base + height * 2 pentru ca la fiecare nivel de inaltime trebuie adaugat /\ si umplut cu spatii astfel incat
    # sa fie simetric sub nivelul anterior, adica cu inca 2 spatii in plus, per nivel de inaltime => la ultimul nivel, 2 * height spatii
    print((base * "-").center(base + height * 2))
    for i in range(height):
        print(("/" + (base + 2 * i) * " " + "\\").center(base + height * 2))
    print(((base + 2 * height) * "-"))

# Exercise 2.5
# def isPalindrome(string):
#     return string == string[::-1]

# print(isPalindrome("ana"))
# print(isPalindrome("abc"))

# Exercise 2.6
# strArr = ["Hello Python", "Ana are mere", "Pizza Party"]
# def splitStrings(inputArr, sep):
#     outputArr = []
#     for current in inputArr: 
#         words = current.split(" ")
#         output = ""
#         for i in range(len(words)):
#             output += words[i]
#             if i < len(words) - 1:
#                 output += sep
#         outputArr.append(output)
#     return outputArr

# print(splitStrings(strArr, "_"))

# # prints the strings with a terminating '.'
# for current in strArr:
#     print(current + ".")

# # prints the strings with each first word repeated 4 times
# for current in strArr:
#     words = current.split(" ")
#     for i in range(len(words)):
#         if i == 0:
#             print(3 * (words[i] + " "), end="")
#         print(words[i] + " ", end="")
#     print()

# Exercise 2.7
# a = 5
# b = 5
# c = "ana"
# arr = [a, b, c]
# for i in range(len(arr)):
#     print(f"for {i}, type is {type(arr[i])}, memory location is {id(arr[i])}")