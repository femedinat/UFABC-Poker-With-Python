import random as r
from collections import Counter

tokens_p1 = 1000
tokens_p2 = 1000

def shuffle(deck:list):
    shuffled_cards = deck.copy()
    r.shuffle(shuffled_cards)
    return shuffled_cards

def take_hand(cards, hand_size):
    hand = r.sample(cards, hand_size)
    for card in hand:
        cards.remove(card)
    return hand

def addOrRemoveTokens(tokens, qnt, flag):
    if flag == True:
        tokens = tokens + qnt
    elif flag == False:
        tokens = tokens - qnt
    return tokens

def avaliate_hand(hand):
    def is_straight(cards):
        return all(cards[i] - cards[i - 1] == 1 for i in range(1, len(cards)))

    def is_flush(suits):
        return len(set(suits)) == 1

    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    hand_values = [card_values[card[:-1]] for card in hand]
    hand_suits = [card[-1] for card in hand]

    value_counts = Counter(hand_values)
    suit_counts = Counter(hand_suits)

    is_flush_hand = is_flush(hand_suits)
    is_straight_hand = is_straight(sorted(hand_values))

    if is_flush_hand and is_straight_hand and 10 in hand_values and 14 in hand_values:
        return ["Royal Flush", 10]

    if is_flush_hand and is_straight_hand:
        return ["Straight Flush", 9]

    if 4 in value_counts.values():
        return ["Four of a Kind", 8]

    if 3 in value_counts.values() and 2 in value_counts.values():
        return ["Full House", 7]

    if is_flush_hand:
        return ["Flush", 6]

    if is_straight_hand:
        return ["Straight", 5]

    if 3 in value_counts.values():
        return ["Three of a Kind", 4]

    if list(value_counts.values()).count(2) == 2:
        return ["Two Pairs", 3]

    if 2 in value_counts.values():
        return ["One Pair", 2]

    return ["High Card", 1]

def play(throw, hand_p1, hand_p2, communal, deck, moves):
    global tokens_p1, tokens_p2

    bet_max = min([tokens_p1, tokens_p2])
    print("\nRodada: " + str(throw))
    print("Suas cartas: " + ", ".join(hand_p1))
    print("Carta comunitária: " + communal[0])
    bet = int(input("\nValor da aposta (min: %s - max: %s): " % (1, bet_max)))

    if bet < 1 or bet > bet_max:
        return print("\nAposta inválida!")

    if bet == bet_max:
        moves.pop(1)

    move_p2 = r.choice(moves)

    if move_p2 == 'desistir':
        return print("\nP2 Desistiu...")

    elif move_p2 == 'aumentar':
        bet_p2 = r.randint(bet, bet_max)
        print("\nP2 decidiu aumentar a aposta... Valor da aposta no momento: " + str(bet_p2))
        decider   = str(input("\nVocê deseja cobrir com mais %s fichas ou desistir da aposta? " % (bet_p2 - bet)))

        while (decider != 'cobrir') and (decider != 'desistir'):
            print('\nDigite "cobrir" ou "desistir"')
            decider = str(input("\nVocê deseja cobrir com mais %s fichas ou desistir da aposta? " % (bet_p2 - bet)))

        if decider == 'desistir':
            tokens_p1 = addOrRemoveTokens(tokens_p1, bet, False)
            tokens_p2 = addOrRemoveTokens(tokens_p2, bet, True)
            print("\nVocê perdeu as fichas apostadas... Total: " + str(tokens_p1))
            return
        elif decider == 'cobrir':
            bet = bet + (bet_p2 - bet)
            print("\nVocê cobriu a aposta com mais %s fichas" % (bet_p2 - bet))

    elif move_p2 == 'apostar':
        bet_p2 = bet
        print("\nP2 continuou com a aposta...")

    print("\nRevelando Cartas...")
    print("\nMão P2: " + ", ".join(hand_p2))

    hand_p1.append(communal[0])
    hand_p2.append(communal[0])

    combination_p1, value_p1 = avaliate_hand(hand_p1)
    combination_p2, value_p2 = avaliate_hand(hand_p2)

    if value_p1 == value_p2:
        tokens_p1 = addOrRemoveTokens(tokens_p1, bet, True)
        tokens_p2 = addOrRemoveTokens(tokens_p2, bet, False)
        print("\nEmpate! Parabéns você venceu, Total de fichas: " + str(tokens_p1))
        print("\nFichas do P2: " + str(tokens_p2))
    elif value_p1 > value_p2:
        tokens_p1 = addOrRemoveTokens(tokens_p1, bet, True)
        tokens_p2 = addOrRemoveTokens(tokens_p2, bet, False)
        print("\nVocê venceu! (%s) Total de fichas: %s" % (combination_p1, tokens_p1))
        print("\nFichas do P2: " + str(tokens_p2))
    else:
        tokens_p1 = addOrRemoveTokens(tokens_p1, bet, False)
        tokens_p2 = addOrRemoveTokens(tokens_p2, bet, True)
        print("\nVocê perdeu... Total de fichas: " + str(tokens_p1))
        print("\nFichas do P2: " + str(tokens_p2))

def main():
    throw = 1

    while (tokens_p1 > 0) and (tokens_p2 > 0) and (throw <= 10):
        deck      = [
            '2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S', '4C', '4D', '4H', '4S',
            '5C', '5D', '5H', '5S', '6C', '6D', '6H', '6S', '7C', '7D', '7H', '7S',
            '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S', '10C', '10D', '10H', '10S',
            'JC', 'JD', 'JH', 'JS', 'QC', 'QD', 'QH', 'QS', 'KC', 'KD', 'KH', 'KS',
            'AC', 'AD', 'AH', 'AS'
        ]
        moves    = [
            'apostar','aumentar','desistir'
        ]

        shuffled_cards      = shuffle(deck)
        hand_p1             = take_hand(shuffled_cards, 4)
        hand_p2             = take_hand(shuffled_cards, 4)
        communal            = take_hand(shuffled_cards, 1)

        play(throw, hand_p1, hand_p2, communal, deck, moves)
        throw += 1
    print("Fim do jogo! :D")

main()