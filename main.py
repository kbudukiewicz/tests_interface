import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np


class AnotherWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test")
        self.setWindowIcon(QIcon('896689.png'))

        self.score = 0

        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
        self.startWatch = False

        self.label = QLabel(self)
        self.label.setGeometry(30, 20, 150, 70)

        self.Start()

        self.start = QPushButton("Koniec testu", self)
        self.start.setGeometry(200, 30, 150, 50)
        self.start.pressed.connect(self.reset)

        self.label_score = QLabel(self)
        self.label_score.setGeometry(400, 30, 80, 50)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showCounter)
        self.timer.start(100)

        self.label1 = QLabel('1. Jaka jest stolica Czech?', self)
        self.label1.setGeometry(30, 100, 441, 21)
        self.radioButton1 = QRadioButton('Praga', self)
        self.radioButton1.setGeometry(30, 130, 95, 20)
        self.radioButton2 = QRadioButton('Bratyslawa', self)
        self.radioButton2.setGeometry(160, 130, 95, 20)
        self.radioButton3 = QRadioButton('Berlin', self)
        self.radioButton3.setGeometry(270, 130, 95, 20)
        self.radioButton1.clicked.connect(self.check)

        self.label2 = QLabel('2. Ktore miasto nie nalezy do USA?', self)
        self.label2.setFont(QFont('Arial', 10))
        self.label2.setGeometry(30, 160, 441, 21)
        self.radioButton4 = QRadioButton('Los Angeles', self)
        self.radioButton4.setGeometry(30, 190, 95, 20)
        self.radioButton5 = QRadioButton('Califormia', self)
        self.radioButton5.setGeometry(160, 190, 95, 20)
        self.radioButton6 = QRadioButton('Waszyngton', self)
        self.radioButton6.setGeometry(270, 190, 95, 20)
        self.radioButton5.clicked.connect(self.check)

        self.label3 = QLabel('3. Jaka jest najdluzsza rzeka w Polsce?', self)
        self.label3.setGeometry(30, 220, 441, 21)
        self.radioButton7 = QRadioButton('Wisla', self)
        self.radioButton7.setGeometry(30, 250, 95, 20)
        self.radioButton8 = QRadioButton('Odra', self)
        self.radioButton8.setGeometry(160, 250, 95, 20)
        self.radioButton9 = QRadioButton('Warta', self)
        self.radioButton9.setGeometry(270, 250, 95, 20)
        self.radioButton7.clicked.connect(self.check)

        self.label4 = QLabel('4. Jaka byla pierwsza stolica Polski?', self)
        self.label4.setFont(QFont('Arial', 10))
        self.label4.setGeometry(30, 280, 441, 21)
        self.radioButton10 = QRadioButton('Warszawa', self)
        self.radioButton10.setGeometry(30, 310, 95, 20)
        self.radioButton11 = QRadioButton('Krakow', self)
        self.radioButton11.setGeometry(160, 310, 95, 20)
        self.radioButton12 = QRadioButton('Gniezno', self)
        self.radioButton12.setGeometry(270, 310, 95, 20)
        self.radioButton12.clicked.connect(self.check)

        self.label5 = QLabel('5. Ktore miasto jest najwieksze?', self)
        self.label5.setFont(QFont('Arial', 10))
        self.label5.setGeometry(30, 340, 441, 21)
        self.radioButton13 = QRadioButton('Lodz', self)
        self.radioButton13.setGeometry(30, 370, 95, 20)
        self.radioButton14 = QRadioButton('Poznan', self)
        self.radioButton14.setGeometry(160, 370, 95, 20)
        self.radioButton15 = QRadioButton('Wroclaw', self)
        self.radioButton15.setGeometry(270, 370, 95, 20)
        self.radioButton13.clicked.connect(self.check)

        self.label6 = QLabel('6. Jaka jest stolica Niemiec?', self)
        self.label6.setFont(QFont('Times', 10))
        self.label6.setGeometry(30, 400, 441, 21)
        self.radioButton16 = QRadioButton('Berlin', self)
        self.radioButton16.setGeometry(30, 430, 95, 20)
        self.radioButton17 = QRadioButton('Paryz', self)
        self.radioButton17.setGeometry(160, 430, 95, 20)
        self.radioButton18 = QRadioButton('Londyn', self)
        self.radioButton18.setGeometry(270, 430, 95, 20)
        self.radioButton16.clicked.connect(self.check)

        self.label7 = QLabel('7. Ktore panstwo jest najmniejsze?', self)
        self.label7.setGeometry(30, 460, 441, 21)
        self.radioButton19 = QRadioButton('Polska', self)
        self.radioButton19.setGeometry(30, 490, 95, 20)
        self.radioButton20 = QRadioButton('Czechy', self)
        self.radioButton20.setGeometry(160, 490, 95, 20)
        self.radioButton21 = QRadioButton('Litwa', self)
        self.radioButton21.setGeometry(270, 490, 95, 20)
        self.radioButton21.clicked.connect(self.check)

        self.label8 = QLabel('8. Jakie miasto jest najwieksze z Trojmiasta?', self)
        self.label8.setGeometry(30, 520, 441, 21)
        self.radioButton22 = QRadioButton('Sopot', self)
        self.radioButton22.setGeometry(30, 550, 95, 20)
        self.radioButton23 = QRadioButton('Gdynia', self)
        self.radioButton23.setGeometry(160, 550, 95, 20)
        self.radioButton24 = QRadioButton('Gdansk', self)
        self.radioButton24.setGeometry(270, 550, 95, 20)
        self.radioButton24.clicked.connect(self.check)

        self.label9 = QLabel('9. Jaki kraj nie jest w Europie?', self)
        self.label9.setGeometry(30, 580, 441, 21)
        self.radioButton25 = QRadioButton('Polska', self)
        self.radioButton25.setGeometry(30, 610, 95, 20)
        self.radioButton26 = QRadioButton('Egipt', self)
        self.radioButton26.setGeometry(160, 610, 95, 20)
        self.radioButton27 = QRadioButton('Portugalia', self)
        self.radioButton27.setGeometry(270, 610, 95, 20)
        self.radioButton26.clicked.connect(self.check)

        self.label10 = QLabel('10. Ile jest kontynentow?', self)
        self.label10.setGeometry(30, 640, 441, 21)
        self.radioButton28 = QRadioButton('5', self)
        self.radioButton28.setGeometry(30, 670, 95, 20)
        self.radioButton29 = QRadioButton('6', self)
        self.radioButton29.setGeometry(160, 670, 95, 20)
        self.radioButton30 = QRadioButton('7', self)
        self.radioButton30.setGeometry(270, 670, 95, 20)
        self.radioButton30.clicked.connect(self.check)

    def showCounter(self):
        list_time1 = np.arange(1, 9999, 2)
        list_time2 = np.arange(0, 10000, 2)
        if self.startWatch:
            self.counter += 1

            if self.counter == 0:
                self.counter_activity.stop()
            elif self.counter in list_time1:
                self.setStyleSheet("background-color: yellow;")
                self.label1.setStyleSheet("background-color: darkgreen")
                self.label2.setStyleSheet("border :5px solid ;"
                                          "border-top-color : green; "
                                          "border-left-color : blue;"
                                          "border-right-color : blue;"
                                          "border-bottom-color : green")
                self.label3.setStyleSheet("background-color: orange")
                self.label4.setStyleSheet("background-color: blue")
                self.label5.setStyleSheet("background-color: white")
                self.label6.setStyleSheet("background-color: orange")
                self.label7.setStyleSheet("background-color: green")
                self.label8.setStyleSheet("background-color: yellow")
                self.label9.setStyleSheet("background-color: red")
                self.label10.setStyleSheet("border :5px solid ;"
                                           "border-top-color : red; "
                                           "border-left-color : pink;"
                                           "border-right-color : green;"
                                           "border-bottom-color : yellow")

                self.radioButton1.setStyleSheet("background-color: orange")
                self.radioButton2.setStyleSheet("background-color: red")
                self.radioButton5.setStyleSheet("background-color: orange")
                self.radioButton6.setStyleSheet("background-color: orange")
                self.radioButton7.setStyleSheet("background-color: yellow")
                self.radioButton8.setStyleSheet("background-color: orange")
                self.radioButton9.setStyleSheet("background-color: red")
                self.radioButton12.setStyleSheet("background-color: green")
                self.radioButton14.setStyleSheet("background-color: lightblue")
                self.radioButton16.setStyleSheet("background-color: pink")
                self.radioButton17.setStyleSheet("background-color: white")
                self.radioButton18.setStyleSheet("background-color: blue")
                self.radioButton21.setStyleSheet("background-color: pink")
                self.radioButton23.setStyleSheet("background-color: lightred")
                self.radioButton24.setStyleSheet("background-color: yellow")
                self.radioButton25.setStyleSheet("background-color: lightgreen")
                self.radioButton28.setStyleSheet("background-color: green")
                self.radioButton30.setStyleSheet("background-color: black")

            elif self.counter in list_time2:
                self.setStyleSheet("background-color: white;")
                self.label1.setStyleSheet("background-color: lightgreen")
                self.label2.setStyleSheet("border :5px solid ;"
                                          "border-top-color : blue; "
                                          "border-left-color : green;"
                                          "border-right-color : green;"
                                          "border-bottom-color : blue")
                self.label3.setStyleSheet("background-color: green")
                self.label4.setStyleSheet("background-color: red")
                self.label5.setStyleSheet("background-color: red")
                self.label6.setStyleSheet("background-color: green")
                self.label7.setStyleSheet("background-color: white")
                self.label8.setStyleSheet("background-color: lightblue")
                self.label9.setStyleSheet("background-color: pink")
                self.label10.setStyleSheet("border :5px solid ;"
                                           "border-top-color : pink; "
                                           "border-left-color : red;"
                                           "border-right-color : yellow;"
                                           "border-bottom-color : green")

                self.radioButton1.setStyleSheet("background-color: yellow")
                self.radioButton2.setStyleSheet("background-color: yellow")
                self.radioButton5.setStyleSheet("background-color: blue")
                self.radioButton6.setStyleSheet("background-color: red")
                self.radioButton7.setStyleSheet("background-color: yellow")
                self.radioButton8.setStyleSheet("background-color: orange")
                self.radioButton9.setStyleSheet("background-color: red")
                self.radioButton12.setStyleSheet("background-color: orange")
                self.radioButton14.setStyleSheet("background-color: lightgreen")
                self.radioButton16.setStyleSheet("background-color: lightblue")
                self.radioButton17.setStyleSheet("background-color: blue")
                self.radioButton18.setStyleSheet("background-color: green")
                self.radioButton21.setStyleSheet("background-color: white")
                self.radioButton23.setStyleSheet("background-color: lightblue")
                self.radioButton24.setStyleSheet("background-color: lightblue")
                self.radioButton25.setStyleSheet("background-color: lightblue")
                self.radioButton26.setStyleSheet("background-color: white")
                self.radioButton27.setStyleSheet("background-color: white")
                self.radioButton28.setStyleSheet("background-color: blue")
                self.radioButton30.setStyleSheet("background-color: orange")

            cnt = int((self.counter / 10 - int(self.counter / 10)) * 10)
            self.count = '0' + str(cnt)

            if int(self.counter / 10) < 10:
                self.second = '0' + str(int(self.counter / 10))
            else:
                self.second = str(int(self.counter / 10))
                if self.counter / 10 == 60.0:
                    self.second == '00'
                    self.counter = 0
                    min = int(self.minute) + 1
                    if min < 10:
                        self.minute = '0' + str(min)
                    else:
                        self.minute = str(min)

        text = self.minute + ':' + self.second + ':' + self.count
        self.label.setText('<h1 style="color:blue">' + text + '</h1>')

    def check(self):
        self.score += 1

    def check_score(self):
        self.label_score.setText('<h1 style="color:blue">' + str(self.score) + '/10' +'</h1>')

    def Start(self):
        if w is not None:
            self.startWatch = True

    def reset(self):
        if self.start.text() == 'Koniec testu':
            self.check_score()
            self.startWatch = False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 200, 300)
        self.setWindowTitle('Test geograficzny')
        self.setWindowIcon(QIcon('896689.png'))

        self.w = None
        layout = QVBoxLayout()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_probny)

        self.button1 = QPushButton("Informacje o tescie probnym", self)
        self.button1.clicked.connect(self.show_info_prob)
        layout.addWidget(self.button1)

        self.button2 = QPushButton("Informacje o tescie wlasciwym", self)
        self.button2.clicked.connect(self.show_info_wlasciwy)
        layout.addWidget(self.button2)

        self.button3 = QPushButton("Test wlasciwy", self)
        self.button3.clicked.connect(self.show_new_window)
        layout.addWidget(self.button3)

        self.label1 = QLabel("Pytania testowe:", self)
        layout.addWidget(self.label1)

        self.pytanie1 = QLabel("1. Jaki kraj nie jest w Europie?.:", self)
        layout.addWidget(self.pytanie1)
        self.radioButton1 = QRadioButton('Polska', self)
        self.radioButton2 = QRadioButton('Egipt', self)
        self.radioButton3 = QRadioButton('Portugalia', self)
        layout.addWidget(self.radioButton1)
        layout.addWidget(self.radioButton2)
        layout.addWidget(self.radioButton3)

        self.pytanie2 = QLabel("2. Jaka jest stolica Niemiec?:", self)
        layout.addWidget(self.pytanie2)
        self.radioButton4 = QRadioButton('Praga', self)
        self.radioButton5 = QRadioButton('Dortmund', self)
        self.radioButton6 = QRadioButton('Berlin', self)
        layout.addWidget(self.radioButton4)
        layout.addWidget(self.radioButton5)
        layout.addWidget(self.radioButton6)

        self.pytanie3 = QLabel("3. Ktore panstwo jest najmniejsze?:", self)
        layout.addWidget(self.pytanie3)
        self.radioButton7 = QRadioButton('Estonia', self)
        self.radioButton8 = QRadioButton('Polska', self)
        self.radioButton9 = QRadioButton('Niemcy', self)
        self.radioButton7.clicked.connect(self.info)
        layout.addWidget(self.radioButton7)
        layout.addWidget(self.radioButton8)
        layout.addWidget(self.radioButton9)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

    def info(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Super Ci poszlo, powodzenia na tescie wlasciwym!")
        msgBox.setWindowTitle("Informacja")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()

    def show_info_prob(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Test sprawdza Twoja sprawnosc oraz wiedze geograficzna. Jest to proba przed ocena koncowa "
                       "we wlasciwym sprawdzianie. Test sklada sie z 3 pytan. "
                       "Po klikniecia przycisku OK zaczyna wizualizacja testu probnego. "
                       "W kazdym pytaniu jest tylko jedna prawidlowa odpowiedz. "
                       "Powodzenia!")
        msgBox.setWindowTitle("Informacja")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.counter = 0
            self.timer.start(100)

    def show_info_wlasciwy(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Test sprawdza Twoja sprawnosc oraz wiedze geograficzna.Test sklada sie z 10 pytan. "
                       "Od klikniecia przycisku START TEST zaczyna odmierzac sie czas. "
                       "W kazdym pytaniu jest tylko jedna prawidlowa odpowiedz. "
                       "Za kazda poprawna odpowiedz masz 1pkt, a za zla 0. Po odpowiedzeniu na wsyzstkie pytania "
                       "zakoncz test przyciskiem KONIEC TESTU. "
                       "W lewym gornym rogu jest czas rowziazania, a w prawym wynik."
                       " Powodzenia!")
        msgBox.setWindowTitle("Informacja")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()

    def show_probny(self):
        list_time1 = np.arange(1, 9999, 2)
        list_time2 = np.arange(0, 10000, 2)
        self.counter += 1
        if self.counter in list_time1:
            self.pytanie1.setStyleSheet("background-color: lightgreen")
            self.pytanie2.setStyleSheet("border :5px solid ;"
                                        "border-top-color : blue; "
                                        "border-left-color : green;"
                                        "border-right-color : green;"
                                        "border-bottom-color : blue")
            self.pytanie3.setStyleSheet("background-color: green")
            self.radioButton1.setStyleSheet("background-color: orange")
            self.radioButton2.setStyleSheet("background-color: red")
            self.radioButton5.setStyleSheet("background-color: orange")
            self.radioButton6.setStyleSheet("background-color: orange")
            self.radioButton7.setStyleSheet("background-color: yellow")
            self.radioButton8.setStyleSheet("background-color: orange")
            self.radioButton9.setStyleSheet("background-color: red")

        elif self.counter in list_time2:
            self.pytanie1.setStyleSheet("background-color: lightgreen")
            self.pytanie2.setStyleSheet("border :5px solid ;"
                                        "border-top-color : blue; "
                                        "border-left-color : green;"
                                        "border-right-color : green;"
                                        "border-bottom-color : blue")
            self.pytanie3.setStyleSheet("background-color: green")
            self.radioButton1.setStyleSheet("background-color: blue")
            self.radioButton2.setStyleSheet("background-color: white")
            self.radioButton5.setStyleSheet("background-color: red")
            self.radioButton6.setStyleSheet("background-color: blue")
            self.radioButton7.setStyleSheet("background-color: green")
            self.radioButton8.setStyleSheet("background-color: green")
            self.radioButton9.setStyleSheet("background-color: orange")

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
        self.w.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
