from collections import defaultdict

with open('data.txt', 'r') as file:
    text = file.read()

words = text.lower().split()
mapped = [(word, 1) for word in words]

reduced = defaultdict(int)
for word, count in mapped:
    reduced[word] += count

for word, count in reduced.items():
    print(word, count)
