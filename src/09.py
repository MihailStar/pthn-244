string = input().lower()
unique_chars = set(char for char in string if char != " ")

print(*sorted(unique_chars))
