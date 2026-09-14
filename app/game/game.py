from game.deck import Deck
from game.hand import Hand


class Game:
    def __init__(self):
        self.deck = None
        self.player_hand = None
        self.dealer_hand = None

    def new_game(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand = Hand()
        self.dealer_hand = Hand(dealer=True)

        for _ in range(2):
            self.player_hand.add_card(self.deck.deal(1))
            self.dealer_hand.add_card(self.deck.deal(1))

    def hit(self):
        self.player_hand.add_card(self.deck.deal(1))

    def stand(self):
        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.add_card(self.deck.deal(1))

    def check_game_state(self):
        player_hand_value = self.player_hand.get_value()

        if player_hand_value < 21:
            return 'playing'
        elif player_hand_value > 21:
            return 'bust'
        else:
            return '21'

    def check_winner(self):
        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()

        if dealer_value > 21:
            return 'player_win'
        elif player_value > dealer_value:
            return 'player_win'
        elif player_value < dealer_value:
            return 'dealer_win'
        else:
            return 'tie'