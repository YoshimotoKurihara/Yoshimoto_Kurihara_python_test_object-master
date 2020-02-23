index=[]
character=[]
a=[]

f = open('input.txt', 'r')
lines = int(sum([1 for _ in open('input.txt')]))

for line in f:
    index.append(line[:1])
    character.append(line[2:])
    a.append(line)

f.close()

def bubble_sort(x):
    for k in range(len(index) - 1 - 1):
        for j in range(len(index) - k - 1 - 1):
            if index[j] > index[j + 1]:
                index[j], index[j + 1] = index[j + 1], index[j]
                character[j], character[j + 1] = character[j + 1], character[j]

    return index,character

index,character=bubble_sort(index)

#print(index)
#print(character)
output=""

for k in range(lines - 1):
    if int(a[-1]) % int(index[k])  == 0:
        output += character[k]

if len(output) == 0:
    output = a[-1]

print(output.replace("\n",''))