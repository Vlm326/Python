import pyttsx3
import random
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QFileDialog
)
from PyQt6.QtCore import Qt
import sys

engine = pyttsx3.init()

def delete_bad_signes_from_words(word: str) -> str:
    for i in '!"#$%&()*+,-./:;<]^_`|~':
        word = word.replace(i, '')
    return word

def reading_file():
    while True:
        path, _ = QFileDialog.getOpenFileName(caption='Введите путь к файлу', filter="Text Files (*.txt);;All Files (*)")
        if not path:
            return [], None
        
        try:
            with open(path, encoding="utf-8") as f:
                content = []
                for line in f:
                    if len(line.split()) > 1:
                        for word in line.split():
                            content.append(delete_bad_signes_from_words(word.lower()))
                    else:
                        content.append(delete_bad_signes_from_words(line.lower()))
                return content, path
        except FileNotFoundError:
            return [], path
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return [], path

def input_processing(words: list, index: int, inp: str, errors: list, correct_word_display: QLabel) -> bool:
    if inp == words[index]:
        engine.say('Правильно!')
        correct_word_display.setText('Правильно!')
    elif inp == 'след':
        return True
    elif inp == 'остановить':
        return False
    else:
        engine.say('Неправильно!')
        errors.append(words[index])
        correct_word_display.setText(f'Неправильно! Верное слово: {words[index]}')

    engine.runAndWait()
    return True

class WordCheckerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Проверка слов")
        self.setGeometry(300, 300, 400, 400)
        self.words = []
        self.errors = []
        self.count = 0
        self.word_index = 0
        self.path = ""
        
        self.init_ui()
    
    def init_ui(self):
        pass