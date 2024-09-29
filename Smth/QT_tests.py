import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog, QLineEdit


# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        inp = QInputDialog()
        default_window_size = QSize(500, 300)
        self.resize(default_window_size)
        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(button)
        self.setCentralWidget(inp)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()