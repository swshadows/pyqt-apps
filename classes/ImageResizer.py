import os
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from .qt_designer.Window import Ui_MainWindow


class ImageResizer(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnChooseFile.clicked.connect(self.open_image)
        self.btnResize.clicked.connect(self.resize_image)
        self.btnSave.clicked.connect(self.save_image)

    def open_image(self):
        init_path = os.path.expanduser("~")
        image, _ = QFileDialog.getOpenFileName(self.centralwidget, "Abrir imagem", init_path)
        self.inputOpenFile.setText(image)
        self.originalImage = QPixmap(image)
        self.imgLabel.setPixmap(self.originalImage)
        self.inputWidth.setText(str(self.originalImage.width()))
        self.inputHeight.setText(str(self.originalImage.height()))

    def resize_image(self):
        try:
            width = int(self.inputWidth.text())
            self.newImage = self.originalImage.scaledToWidth(width)
            self.imgLabel.setPixmap(self.newImage)
            self.inputWidth.setText(str(self.newImage.width()))
            self.inputHeight.setText(str(self.newImage.height()))
        except Exception as err:
            print(f"Erro: {err}")

    def save_image(self):
        os_desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        image, _ = QFileDialog.getSaveFileName(self.centralwidget, "Salvar imagem", os_desktop)
        try:
            self.newImage.save(image, "png")
        except Exception as err:
            print(f"Erro: {err}")
