# string = input()

# if ("a" in string or "o" in string) and ("e" not in string and "i" not in string):
#     print(True)
# else:
#     print(False)

string = input()
has_a_or_o = False

for char in string:
    if char == "e" or char == "i":
        print(False)
        break

    if char == "a" or char == "o":
        has_a_or_o = True
else:
    print(has_a_or_o)
