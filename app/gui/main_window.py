from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QHBoxLayout,
)

from game.game import Game


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

        self.player_label = QLabel("Your hand")
        main_layout.addWidget(self.player_label)

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

        self.update_display()

        result = self.game.check_winner()

        if result == "player_win":
            self.status_label.setText("You win!")
        elif result == "dealer_win":
            self.status_label.setText("Dealer wins!")
        else:
            self.status_label.setText("It's a tie!")

        self.hit_button.setEnabled(False)
        self.stand_button.setEnabled(False)

    def update_display(self):
        player_value = self.game.player_hand.get_value()
        dealer_value = self.game.dealer_hand.get_value()

        self.player_label.setText(
            f"Your hand: {player_value} | "
            f"{', '.join(str(card) for card in self.game.player_hand.cards)}"
        )

        self.dealer_label.setText(
            f"Dealer's hand: {dealer_value} | "
            f"{', '.join(str(card) for card in self.game.dealer_hand.cards)}"
        )