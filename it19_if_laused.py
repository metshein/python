tehtemark = input('''
Palun vali õige tehtemärk:
+ liitmiseks
- lahutamiseks
* korrutamiseks
/ jagamiseks
''')

number_1 = int(input('Esimene number: '))
number_2 = int(input('Teine number: '))

if tehtemark == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif tehtemark  == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif tehtemark  == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif tehtemark  == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('Sa ei valinud tehtemärki')

