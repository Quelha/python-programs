import random
import time

print('-'*32)
print(' '*4,'PEDRA, PAPEL E TESOURA')
print('-'*32)

print('Vamos fazer uma melhor de três?')

scorePC = 0
scorePlay = 0
i = 0

while scorePC != 2 or scorePlay != 2:
    print(f'PC: {scorePC}')
    print(f'Play: {scorePlay}')
    i += 1
    print('-'*32)
    play = input(f'{i:>11} RODADA!\nPEDRA, PAPEL OU TESOURA?').upper()
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO')
    time.sleep(1)

    pc = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])

    print('\nJogador: {}' .format(play))
    time.sleep(1)
    print('PC:{}{}' .format(' '*6,pc))
    time.sleep(0.5)

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
