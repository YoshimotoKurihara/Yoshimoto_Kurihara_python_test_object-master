index=[]
character=[]
a=[]

f = open('input.txt', 'r')
lines = int(sum([1 for _ in open('input.txt')]))
i=0
for line in f:
    index.append(line.split(':')[0])
    character.append(line.split(':')[1])
    if i > lines-3:
        break
    i=i+1

for line in f:
    a.append(line)

f.close()

def bubble_sort(x):
    for k in range(len(index) - 1 ):
        for j in range(len(index) - k - 1 ):
            if index[j] > index[j + 1]:
                index[j], index[j + 1] = index[j + 1], index[j]
                character[j], character[j + 1] = character[j + 1], character[j]

    return index,character

index,character=bubble_sort(index)

#print(index)
#print(character)

output=""
#print(a[-1])
for k in range(lines - 1):
    if int(a[-1]) % int(index[k])  == 0:
        output += character[k]

if len(output) == 0:
    output = a[-1]

print(output.replace("\n",''))