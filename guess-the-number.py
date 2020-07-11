from random import randint
random_num = randint(0, 10)
attempts = 0
while True:
    num_player = int(input('What number did the computer choose? '))
    attempts += 1
    if num_player == random_num:
        print(f'you got it right on the {attempts} try !!! Congratulations')
        break   
    option = ' '
    while option not in 'YN':
        option = str(input('You were wrong, do you want to continue? [y / n] ')).upper()[0]
    if option == 'N':
        print('------ END ------')
        break