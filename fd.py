# Multiple 15 and 5
for i in range(1, 20+1):
    if i % 15 == 0:
        print('fizzbuzz')
    elif i % 5 ==0:
        print('buzz')
    else:
        print(f'{i}')

