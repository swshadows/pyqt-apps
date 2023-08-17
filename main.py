import sys
from PyQt5.QtWidgets import QApplication
from classes.Calculadora import Calculadora
from classes.ImageResizer import ImageResizer

if __name__ == "__main__":
    valid_args = {"calc": Calculadora, "img": ImageResizer}

    args = sys.argv[1:]
    for arg in args:
        if arg in valid_args:
            qt = QApplication(sys.argv)
            app = valid_args[arg]()
            app.show()
            qt.exec_()
            break
    else:
        print("No args or invalid args provided")
