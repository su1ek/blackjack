from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QHBoxLayout,
)

from game.game import Game
from gui.card_widget import CardWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.game = Game()

        self.setWindowTitle("Blackjack")
        self.resize(800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        self.status_label = QLabel("Welcome to Blackjack!")
        main_layout.addWidget(self.status_label)

        self.dealer_label = QLabel("Dealer's hand")
        main_layout.addWidget(self.dealer_label)

        self.dealer_cards_layout = QHBoxLayout()
        main_layout.addLayout(self.dealer_cards_layout)

        self.player_label = QLabel("Your hand")
        main_layout.addWidget(self.player_label)

        self.player_cards_layout = QHBoxLayout()
        main_layout.addLayout(self.player_cards_layout)

        buttons_layout = QHBoxLayout()

        self.new_game_button = QPushButton("New Game")
        self.hit_button = QPushButton("Hit")
        self.stand_button = QPushButton("Stand")

        buttons_layout.addWidget(self.new_game_button)
        buttons_layout.addWidget(self.hit_button)
        buttons_layout.addWidget(self.stand_button)

        main_layout.addLayout(buttons_layout)

        self.new_game_button.clicked.connect(self.new_game)
        self.hit_button.clicked.connect(self.hit)
        self.stand_button.clicked.connect(self.stand)

        self.hit_button.setEnabled(False)
        self.stand_button.setEnabled(False)

    def new_game(self):
        self.game.new_game()

        self.update_display()

        self.status_label.setText("Your turn.")

        self.hit_button.setEnabled(True)
        self.stand_button.setEnabled(True)

    def hit(self):
        self.game.hit()

        self.update_display()

        state = self.game.check_game_state()

        if state == "bust":
            self.status_label.setText("You busted! Dealer wins.")
            self.hit_button.setEnabled(False)
            self.stand_button.setEnabled(False)

        elif state == "21":
            self.status_label.setText("You have 21!")
            self.hit_button.setEnabled(False)

    def stand(self):
        self.game.stand()

        self.update_display(show_dealer_cards=True)

        result = self.game.check_winner()

        if result == "player_win":
            self.status_label.setText("You win!")
        elif result == "dealer_win":
            self.status_label.setText("Dealer wins!")
        else:
            self.status_label.setText("It's a tie!")

        self.hit_button.setEnabled(False)
        self.stand_button.setEnabled(False)

    def update_display(self, show_dealer_cards=False):
        self.clear_card_layout(self.player_cards_layout)
        self.clear_card_layout(self.dealer_cards_layout)

        player_value = self.game.player_hand.get_value()

        self.player_label.setText(f"Your hand: {player_value}")

        for card in self.game.player_hand.cards:
            self.player_cards_layout.addWidget(CardWidget(card))

        if show_dealer_cards:
            dealer_value = self.game.dealer_hand.get_value()
            self.dealer_label.setText(f"Dealer's hand: {dealer_value}")

            for card in self.game.dealer_hand.cards:
                self.dealer_cards_layout.addWidget(CardWidget(card))
        else:
            dealer_visible_card = self.game.dealer_hand.cards[1]

            self.dealer_label.setText("Dealer's hand")

            hidden_card = QLabel("Hidden")
            hidden_card.setAlignment(Qt.AlignmentFlag.AlignCenter)
            hidden_card.setFixedSize(100, 140)
            hidden_card.setStyleSheet("""
                QLabel {
                    background-color: #444;
                    color: white;
                    border: 2px solid black;
                    border-radius: 8px;
                    font-size: 18px;
                    font-weight: bold;
                }
            """)

            self.dealer_cards_layout.addWidget(hidden_card)
            self.dealer_cards_layout.addWidget(CardWidget(dealer_visible_card))

    def clear_card_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()

            if widget is not None:
                widget.deleteLater()