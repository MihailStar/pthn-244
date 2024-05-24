needs_to_processed = int(input())
bigs: list[int] = []

for _ in range(needs_to_processed):
    big = max(int(digit) for digit in input().split())
    bigs.append(big)

print(";".join((str(num) for num in sorted(bigs, reverse=True))))
