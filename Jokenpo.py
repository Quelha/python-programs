
import random

''' Colocar emoji
Papel :hand_with_fingers_splayed_light_skin_tone:
Pedra :oncoming_fist_light_skin_tone:
Tesoura :victory_hand_light_skin_tone:
'''
print('-'*22)
print('PEDRA, PAPEL E TESOURA')
print('-'*22)

print('Vamos fazer uma melhor de três?\n')
print('''Primeira jogada!

Pedra
Papel
Tesoura
''')

scorePC = int(0)
scorePlay = int(0)

for i in range(1, 4):
    print('-'*22)
    play = input('{} JOGADA! PEDRA, PAPEL OU TESOURA? ' .format(i))
    pc = random.choice(['Pedra', 'Papel', 'Tesoura'])

    print('\nJogador jogou: {}' .format(play))
    print('PC jogou: {}' .format(pc))

    if play != pc:
        '''Alguem ganhou'''
        if play == 'Pedra':
            if pc == 'Papel':
                scorePC += 1
                print ('PC ganhou a {}º rodada' .format(i))
            else:
                scorePlay += 1
                print ('Player ganhou a {}º rodada' .format(i))
        elif play == 'Papel':
            if pc == 'Tesoura':
                scorePC += 1
                print ('PC ganhou a {}º rodada' .format(i))
            else:
                scorePlay +=  1
                print ('Player ganhou a {}º rodada' .format(i))
        elif play == 'Tesoura':
            if pc == 'Pedra':
                scorePC += 1
                print ('PC ganhou a {}º rodada' .format(i))
            else:
                scorePlay += 1
                print ('Player ganhou a {}º rodada' .format(i))
        else:
            '''Informação Incorreta'''
            print('{}º JOGA ANULADA POR INFORMAÇÃO INCORRETA')
    else:
        '''Empate'''
        print('{}º Rodada deu Empate' .format(i))
    

print('-'*22)
if scorePlay > scorePC:
    print('PLAYER WIN')
elif scorePlay < scorePC:
    print('PC WIN')
else:
    print('EMPATE')
print('-'*22)
