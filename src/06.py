# string = input().lower()
# replaced_string = (
#     string.replace("!", "").replace("%", "").replace("#", "").replace("@", "")
# )

# print(len(string) - len(replaced_string))
# print(replaced_string)

string = input().lower()
replaced_string = ""
counter = 0

for char in string:
    if char in ("!", "%", "#", "@"):
        counter += 1
        continue

    replaced_string += char

print(counter)
print(replaced_string)
