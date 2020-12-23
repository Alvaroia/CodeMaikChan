import random

options = ('piedra', 'papel', 'tijera')

draw = 0
win = 0
lose = 0
while True:
    while win < 3 and lose < 3:
        guess = input('Introduce piedra papel o tijera')

        if guess not in options:
            print('guess mal')
            continue

        machine_guess = random.choice(options)

        if guess == machine_guess:
            draw += 1
        elif guess == 'piedra' and machine_guess == 'tijera':
            win += 1
        elif guess == 'tijera' and machine_guess == 'piedra':
            lose += 1
        elif guess == 'piedra' and machine_guess == 'papel':
            lose += 1
        elif guess == 'papel' and machine_guess == 'piedra':
            win += 1
        elif guess == 'papel' and machine_guess == 'tijera':
            lose += 1
        elif guess == 'tijera' and machine_guess == 'papel':
            win += 1
        else:
            print('falta una combinación '+guess+' '+machine_guess)

        print('Eliges ' + guess)
        print('Maquina elige ' + machine_guess)
        print(win)
        print(lose)
        print(draw)

    print('SE ACABO')
    if win == 5:
        print('GANASTE')
    elif lose == 5:
        print('PERDISTE')
    else:
        print('BUUUUUUUUUUUUUUUUUUUGGG')

    input()