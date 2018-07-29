strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''

for i in strings:
    sentence += i + ' '
    
print(sentence[:-1])
print(' '.join(strings))
