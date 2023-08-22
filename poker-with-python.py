import random as r

fichas_p1 = 1000
fichas_p2 = 1000
cartas    = [
  'Ás de Copas', '2 de Copas', '3 de Copas', '4 de Copas', '5 de Copas', '6 de Copas', '7 de Copas', '8 de Copas', '9 de Copas', '10 de Copas', 'Valete de Copas', 'Rainha de Copas', 'Rei de Copas',
  'Ás de Ouros', '2 de Ouros', '3 de Ouros', '4 de Ouros', '5 de Ouros', '6 de Ouros', '7 de Ouros', '8 de Ouros', '9 de Ouros', '10 de Ouros', 'Valete de Ouros', 'Rainha de Ouros', 'Rei de Ouros',
  'Ás de Espadas', '2 de Espadas', '3 de Espadas', '4 de Espadas', '5 de Espadas', '6 de Espadas', '7 de Espadas', '8 de Espadas', '9 de Espadas', '10 de Espadas', 'Valete de Espadas', 'Rainha de Espadas', 'Rei de Espadas',
  'Ás de Paus', '2 de Paus', '3 de Paus', '4 de Paus', '5 de Paus', '6 de Paus', '7 de Paus', '8 de Paus', '9 de Paus', '10 de Paus', 'Valete de Paus', 'Rainha de Paus', 'Rei de Paus'
]

def embaralhar(cartas:list):
    cartas_embaralhadas = cartas.copy()
    r.shuffle(cartas_embaralhadas)
    return cartas_embaralhadas

def pegar_mao(cartas, tamanho_mao):
    mao = r.sample(cartas, tamanho_mao)
    for carta in mao:
        cartas.remove(carta)
    return mao


def play():
    cartas_embaralhadas = embaralhar(cartas)
    mao_p1              = pegar_mao(cartas_embaralhadas, 4)
    mao_p2              = pegar_mao(cartas_embaralhadas, 4)
    comunitario         = pegar_mao(cartas_embaralhadas, 1)

    print("Quantidade de fichas: " + str(fichas_p1))
    print(mao_p1)
    print(comunitario)
    aposta = int(input("Valor da aposta: "))
    

def main():
    while fichas_p1 >= 0 or fichas_p2 >= 0:
        play()
    print("Fim do jogo! :D")

main()