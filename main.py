import sys
from PyQt5.QtWidgets import QApplication
from Calculadora import Calculadora

if __name__ == "__main__":
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
