# Q04
# age
print('****WELCOME****')
age = input('Dear user, please enter your age: ')
if age == '18' or age > '18':
    print('you can vote ^^')
elif age == '17':
    print('You can learn to drive!')
elif age == '16':
    print('You can buy a lottery ticket!')
elif age < '16':
    print('You can go Trick or-Treating!')
else:
    print('Wrong entered , try again!')
