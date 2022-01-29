from random import randint
from time import sleep
from emoji import emojize

jogar = 'S'
jogador_vence =  comp_vence = empate = 0

while jogar == 'S':
    pedra = emojize('Pedra :fist:', use_aliases=True)
    papel = emojize('Papel :hand:', use_aliases=True)
    tesoura = emojize('tesoura :v:', use_aliases=True)
    opcoes = (pedra , papel , tesoura)
    computador = randint (0, 2)
    print (emojize (''' \033[31m -----------------JOKENPO------------- \033[m 
Escolha sua jogada:
[ 0 ] PEDRA :fist:
[ 1 ] PAPEL :hand:
[ 2 ] TESOURA :v:''', use_aliases=True))
    jogador = ''
    lista = [0, 1, 2 ]
    jogador = int(input('Sua jogada: '))
    while jogador not in lista:
        jogador = int(input('Digite um valor valido [0, 1, ou 2]. Qual e a sua jogada: '))
   
    print(f'Computador jogou {opcoes[computador]}.')
    print(f'Jogador jogou {opcoes[jogador]}.\n')
    
    if computador == 0:
        if jogador == 0:
            empate += 1
        elif jogador == 1:
            jogador_vence += 1
        elif jogador == 2:
            comp_vence += 1
            
    elif computador == 1:
        if jogador == 0:
            comp_vence += 1
        elif jogador == 1:
            empate += 1
        elif jogador == 2:
            jogador_vence += 1
            
    elif computador == 2:
        if jogador == 0:
            jogador_vence += 1
        elif jogador == 1:
            comp_vence += 1
        elif jogador == 2:
            empate += 1
            
    print(emojize(f'''\033[31mPONTUAÇAO\033[m
Voce :smiley: :{jogador_vence}
Computador :computer: : {comp_vence}''', use_aliases=True))
    jogar = str(input('\nDeseja continuar a jogar ? :'
                            '[S/N] :' )).upper().strip()[0]
    while jogar not in 'SN':
        jogar = str(input('Digite um dado valido. Deseja continuar a jogar? [S/N]')).upper().strip()[0]
        
else:
    if jogador_vence > comp_vence:
        print('O jogador venceu a partida ')
    elif jogador_vence < comp_vence:
        print('O computador venceu a Partida  ')
    elif jogador_vence == comp_vence:
        print(f'Empate.')
            
    