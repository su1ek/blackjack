from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel


class CardWidget(QLabel):
    def __init__(self, card):
        super().__init__()

        self.card = card

        rank = card.rank["rank"]
        suit = card.suit

        suit_names = {
            "♠": "♠",
            "♣": "♣",
            "♥": "♥",
            "♦": "♦"
        }

        self.setText(
            f"{rank}\n\n{suit_names.get(suit, suit)}"
        )

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setFixedSize(100, 140)

        if suit in ["♥", "♦"]:
            text_color = "red"
        else:
            text_color = "black"

        self.setStyleSheet(f"""
                QLabel {{
                    background-color: white;
                    color: {text_color};
                    border: 2px solid black;
                    border-radius: 8px;
                    font-size: 18px;
                    font-weight: bold;
                }}
            """)