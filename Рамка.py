width = int(input())
length = int(input())
for i in range(length):
    print('|', end='')
    if i in (0, length - 1):
        print('-' * (width - 2), end='')
    else:
        print(' ' * (width - 2), end='')
    print('|')

