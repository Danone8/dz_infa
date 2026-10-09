import string

with open('data.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower()
for symbol in string.punctuation:
    text = text.replace(symbol, ' ')
counts = {}
text = text.replace('—', ' ')

for word in text.split():
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

for i in range(10):
    most_common = max(counts, key=counts.get)
    print(most_common, counts[most_common])
    del counts[most_common]