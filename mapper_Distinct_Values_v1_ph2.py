import sys

categories = []

for line in sys.stdin:
    categories.append(line.strip().split(',')[1])

for category in categories:
    print(f"{category}\t{1}")