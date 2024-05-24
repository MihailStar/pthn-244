words = input().lower().split()
word_to_number_of: dict[str, int] = {}

for word in words:
    word_to_number_of[word] = word_to_number_of.get(word, 0) + 1

print(*max(word_to_number_of.items(), key=lambda item: item[1]))
