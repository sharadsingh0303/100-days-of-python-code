'''for i in 'sharad':
    if i == 'a':
        continue
    else:

        print(i)


for i in range(1, 10):
    for j in range(1, i+1):
        print('i', end='')
    print()


i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(i, '*', j, '=', i*j)
        j += 1

        print()'''

list1 = [1, 2, 3, 4, 5]
list2 = [12345]
total = 0
for i in list1:
    total = total + i
print(total)

i = 0
sum = 0
while i < len(list1):
    sum = sum + list1[i]
    i += 1
    print(i)
