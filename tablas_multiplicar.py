for i in range(1,11):
    for j in range(1,11):
        print(f'{i} * {j} = {i*j}')
    print('-----------------------')

for i in range(1,11):
    for j in range(1,11):
        print(i*j, end='\t'*2)
    print(' ')
