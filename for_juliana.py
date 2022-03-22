from time import sleep
import webbrowser



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
    sleep(4)
    print('Então...')
    sleep(4)
    print('...')
    sleep(4)
    nada = input('Você sabe que eu te amo, né? [Y] SIM [Y] SIM ')
    sleep(1)
    print('Ah que bom, muito importante você saber disso antes de te contar')
    sleep(5)
    x = input('Está sentada? [Y] SIM [N] NÃO ').upper()
    if x == 'Y':
        sleep(3)
        print('Ótimo, então acho que agora posso te contar')
    else:
        sleep(3)
        print('Melhor sentar então... :)')
    sleep (4)
    print('Não sou muito bom com textos mas vou deixar aqui algumas coisas que ja falei mas vou continar falando sempre')
    sleep(9)
    print('Todos os dias me sinto a pessoa mais sortuda por ter você comigo, e para estar do lado de alguem tão incrivel como você, a pessoa precisa ser MUITO sortuda')
    sleep(13)
    print('Você alem de LINDA, possui um caração gigante')
    sleep(5)
    print('Com uma beleza ABSURDA, interna e externa')
    sleep(5)
    print('Me apaixono por você cada dia mais')
    sleep(4)
    for i in range(1,5):
        print('E mais')
        sleep(1)
    print('Espero poder fazer de você a mulher mais feliz de todas!')
    sleep(5)
    print('Beijo amor, espero que seu dia seja incrivel!')
    sleep(4)
    print('TE AMO S2')
    fim = input(' ')
else:
    print('Poxa, o que houve??\nAperta ENTER e me conta o que está acontecendo')
    enter = input('')
    webbrowser.open('https://wa.me/5521965550516?text=Amor%20quero%20conversar')
