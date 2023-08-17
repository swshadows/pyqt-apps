from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculadora")
        self.setWindowIcon(QIcon("assets/calculator.svg"))
        self.setFixedSize(400, 400)
        self._cw = QWidget()
        self._grid = QGridLayout(self._cw)

        self._display = QLineEdit()
        self._grid.addWidget(self._display, 0, 0, 1, 5)
        self._display.setDisabled(True)
        self._display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_button(QPushButton("7"), 1, 0, 1, 1)
        self.add_button(QPushButton("8"), 1, 1, 1, 1)
        self.add_button(QPushButton("9"), 1, 2, 1, 1)
        self.add_button(QPushButton("+"), 1, 3, 1, 1)
        self.add_button(
            QPushButton("💜"), 1, 4, 1, 1, lambda: self._display.setText("Feito por @swshadows, obrigado por testar 💜")
        )

        self.add_button(QPushButton("4"), 2, 0, 1, 1)
        self.add_button(QPushButton("5"), 2, 1, 1, 1)
        self.add_button(QPushButton("6"), 2, 2, 1, 1)
        self.add_button(QPushButton("-"), 2, 3, 1, 1)
        self.add_button(QPushButton("C"), 2, 4, 1, 1, lambda: self._display.setText(""), "clear")

        self.add_button(QPushButton("1"), 3, 0, 1, 1)
        self.add_button(QPushButton("2"), 3, 1, 1, 1)
        self.add_button(QPushButton("3"), 3, 2, 1, 1)
        self.add_button(QPushButton("/"), 3, 3, 1, 1)
        self.add_button(
            QPushButton("<-"),
            3,
            4,
            1,
            1,
            lambda: self._display.setText(self._display.text()[:-1]),
            "del",
        )

        self.add_button(QPushButton("."), 4, 0, 1, 1)
        self.add_button(QPushButton("0"), 4, 1, 1, 1)
        self.add_button(QPushButton("%"), 4, 2, 1, 1)
        self.add_button(QPushButton("*"), 4, 3, 1, 1)
        self.add_button(QPushButton("="), 4, 4, 1, 1, self.eval_equal, "equals")

        self.setCentralWidget(self._cw)

        with open("assets/styles.css", "r") as f:
            stylesheet = f.read()
            self.setStyleSheet(stylesheet)

    def add_button(
        self,
        btn: QPushButton,
        row,
        col,
        rowspan,
        colspan,
        fn=None,
        class_name=None,
    ):
        self._grid.addWidget(btn, row, col, rowspan, colspan)
        if not fn:
            btn.clicked.connect(lambda: self._display.setText(self._display.text() + btn.text()))
        else:
            btn.clicked.connect(fn)

        if class_name:
            btn.setProperty("class", class_name)
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_equal(self):
        try:
            self._display.setText(str(eval(self._display.text())))
        except Exception:
            self._display.setText("Conta inválida")
