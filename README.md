# Poker with Python

A game created for information processing class.

## General Specification of Implementation Work:

Create a simplified 2 player Poker game: Player (human - player 1) versus Computer (player 2).

#### Start of the Game and Deal of Cards:

Each player starts with 1000 chips to bet.

The game deals 4 cards to each player and 1 community card. Player 1's cards
(P1) and the community card are shown on the screen. Player 2 (P2) cards are not revealed
to P1. Remembering that the Poker hand is formed by 5 cards, in this simplified game, 4 of
player and 1 community.

The **first round of betting** is mandatory and starts with P1. The stake is on
minimum of 1 up to the chip limit of P1 or P2 (minimum(P1,P2)). The game should read the value
of the keyboard bet, then P2 can bet, raise, or fold. If P2 gives up,
the game reverts to dealing and stake returns to P1. If P2 bets or
increases, the game proceeds to the next round.

In the **second betting round**, P1 can bet or fold. If P1 folds, the chips
bets go to P2 and your cards are not revealed. For P1 to bet, he must first
check if P2 has raised the bet amount, if so, P1 must cover the amount, otherwise P1
must give up. If P1 called or P2 did not raise, P1 can bet and the game is over.
must evaluate the cards of the P1 vs P2 players, reveal the cards of P2 and declare who was the
winner as per Poker hand rules, for hands of equal scores, P1 wins. O
winner keeps the bet chips and the game returns to distribution of cards.