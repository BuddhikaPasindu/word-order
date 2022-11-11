n = int(input("\n"))
words = dict()
for i in range(n):
    word = input("\n")
    if word in words:
        words[word] = words.get(word,0) + 1
    else:
        words[word] = 1

length = len(words)    
print(length)
counts = list(words.values())
for count in counts:
    print(count, end=' ')


    

