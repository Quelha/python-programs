from time import sleep


print('-='*18)
print(' '*8, 'FELIPE S2 JULIANA')
print('-='*18)

print('Olá, minha linda!')
status = input('Você está bem? [Y] SIM [N] NÃO ').upper()
if status == 'Y':
    print('Que ótimo!')
    sleep(2)
    print('Queria de contar uma coisa muito importante')
    sleep(4)
    print('É que...')
    sleep(5)
    print('Então...')
    sleep(6)
    print('...')
    sleep(4)
    nada = input('Você sabe que eu te amo, né? [Y] SIM [Y] SIM ')
    print('Ah que bom, muito importante você saber disso antes de te contar')
    sleep(5)
    x = input('Está sentada? [Y] SIM [N] NÃO ').upper()
    if x == 'Y':
        sleep(5)
        print('Ótimo, então acho que agora posso te contar')
    else:
        sleep(5)
        print('Melhor sentar então... :)')
else:
    print('Poxa, o que houve??\nClica aqui nesse link e me conta o que está acontecendo')