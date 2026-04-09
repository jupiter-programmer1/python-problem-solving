num = int(input('Enter last number for the series: '))
skip = int(input('Which number do you want to skip?: '))

for i in range (1, num + 1, 1):
    if i == skip:
        continue
    else:
        print(i, end=' ')

print(f'\nSkipped number: {skip}')
