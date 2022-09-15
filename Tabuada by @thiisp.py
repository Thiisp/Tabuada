from time import sleep

print('''
Tabuada by @thiisp
''')

print('=' * 20)
print('')

i = 0

while i <= 0:
    num = int(input('Tabuada do numero: '))

    for n in range(11):
        print(f'{num} x {n} = {num*n}')

    pgt = int(input('''
(0) Sair
(1) Continuar

Resposta: '''))

    if pgt == 0:
        print('Saindo :)')
        sleep(1)
        exit()

    elif pgt >= 2:
        pgt = int(input('Digite apenas (0) Sair  ou  (1) Continuar: '))

        if pgt == 0:
            print('Saindo :)')
            sleep(1)
            exit()
