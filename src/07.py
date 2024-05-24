lengths = [len(word) for word in input().split()]
average = sum(lengths) / len(lengths)

print(round(average, 2))
