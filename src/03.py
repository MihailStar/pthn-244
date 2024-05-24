left_border = int(input())
right_border = int(input())
in_range = True

while True:
    try:
        inputed = input()

        if inputed == "":
            break

        number = int(inputed)

        if number < left_border or number > right_border:
            in_range = False
            break
    except EOFError:
        break

print(in_range)
