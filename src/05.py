number_1 = int(input())
number_2 = float(input())
number_3 = int(input())

# :fill align sign # 0 width sep .prec type
# @tutorial https://cheatography.com/brianallan/cheat-sheets/python-f-strings-number-formatting

print(f"{number_1:+010}")
print(f"{number_2:#>10.2f}")
print(f"{number_3:019_b}")
