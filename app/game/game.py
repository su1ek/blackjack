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
        player_value = self.player_hand.get_value()

        if player_value > 21:
            return "bust"

        if player_value == 21:
            return "21"

        return "playing"

    def check_initial_result(self):
        player_blackjack = self.player_hand.is_blackjack()
        dealer_blackjack = self.dealer_hand.is_blackjack()

        if player_blackjack and dealer_blackjack:
            return "tie"

        if player_blackjack:
            return "player_blackjack"

        if dealer_blackjack:
            return "dealer_blackjack"

        return None

    def check_winner(self):
        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()

        if player_value > 21:
            return "dealer_win"

        if dealer_value > 21:
            return "player_win"

        if player_value > dealer_value:
            return "player_win"

        if player_value < dealer_value:
            return "dealer_win"

        return "tie"