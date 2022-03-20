import random

print('-'*32)
print(' '*4,'PEDRA, PAPEL E TESOURA')
print('-'*32)

print('Vamos fazer uma melhor de três?')

scorePC = 0
scorePlay = 0

for i in range(1, 4):
    print(i)
    print('-'*32)
    play = input('{}{} RODADA!\nPEDRA, PAPEL OU TESOURA? ' .format(' '*10, i)).upper()
    pc = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])

    print('\nJogador: {}' .format(play))
    print('PC:{}{}' .format(' '*6,pc))

    if play != pc:
        '''Alguem ganhou'''
        if play == 'PEDRA':
            if pc == 'PAPEL':
                scorePC += 1
                print ('PC ganhou a {}º rodada' .format(i))
            else:
                scorePlay += 1
                print ('Player ganhou a {}º rodada' .format(i))
        elif play == 'PAPEL':
            if pc == 'TESOURA':
                scorePC += 1
                print ('PC ganhou a {}º rodada' .format(i))
            else:
                scorePlay +=  1
                print ('Player ganhou a {}º rodada' .format(i))
        elif play == 'TESOURA':
            if pc == 'PEDRA':
                scorePC += 1
                print ('PC ganhou a {}º rodada' .format(i))
            else:
                scorePlay += 1
                print ('Player ganhou a {}º rodada' .format(i))
        else:
            '''Informação Incorreta'''
            print('JOGA ANULADA | INFORMAÇÃO INCORRETA')
            i = i - 1
            print(i)
    else:
        '''Empate'''
        print('{}º Rodada deu Empate' .format(i))
    

print('-'*32)
if scorePlay > scorePC:
    print(' '*9,'PLAYER WIN')
elif scorePlay < scorePC:
    print(' '*9,'PC WIN')
else:
    print(' '*9,'EMPATE')
print('-'*32)
