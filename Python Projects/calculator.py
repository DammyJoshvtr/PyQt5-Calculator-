import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QLCDNumber, QLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(200,200, 500,300)
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon('icon.png'))
        self.setStyleSheet('font-size:30px')
        
        self.ans()
        self.buttons()
        self.arith_signs()
        
        self.layout()
        # self.on_button_clicked()
        
        
    def layout_window(self):
        main_container = QVBoxLayout()
        main_container.addLayout(button())
        main_container.addLayout(backspace_button())
        main_container.addLayout(arith_signs())
        main_container.addLayout(ans())
        self.setLayout(main_container)
        
    def ans(self):
        vbox = QVBoxLayout()
        self.line_ans = QLineEdit()
        self.line_ans.setText("0")
        
        vbox.addWidget(self.line_ans)
        self.setLayout(vbox)
        return vbox
        
        
    def buttons(self):
        hbox = QHBoxLayout()
        btn1 = QPushButton("1")
        btn1.clicked.connect(self.calculations)
        btn2 = QPushButton("2")
        btn2.clicked.connect(self.calculations)
        btn3 = QPushButton("3")
        btn3.clicked.connect(self.calculations)
        btn14 = QPushButton("+")
        btn14.clicked.connect(self.calculations)
        # return btn1

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn14)
        
        hbox2 = QHBoxLayout()
        btn4 = QPushButton("4")
        btn4.clicked.connect(self.calculations)
        btn5 = QPushButton("5")
        btn5.clicked.connect(self.calculations)
        btn6 = QPushButton("6")
        btn6.clicked.connect(self.calculations)
        btn15 = QPushButton("-")
        btn14.clicked.connect(self.calculations)
        
        hbox2.addWidget(btn4)
        hbox2.addWidget(btn5)
        hbox2.addWidget(btn6)
        hbox2.addWidget(btn15)
        
        hbox3 = QHBoxLayout()
        btn7 = QPushButton("7")
        btn7.clicked.connect(self.calculations)
        btn8 = QPushButton("8")
        btn8.clicked.connect(self.calculations)
        btn9 = QPushButton("9")
        btn9.clicked.connect(self.calculations)
        btn16 = QPushButton("/")
        btn16.clicked.connect(self.calculations)
        
        hbox3.addWidget(btn7)
        hbox3.addWidget(btn8)
        hbox3.addWidget(btn9)
        hbox3.addWidget(btn16)
        
        hbox4 = QHBoxLayout()
        btn0 = QPushButton("0")
        btn0.setFixedSize(100,50)
        btn0.clicked.connect(self.calculations)
        btn17 = QPushButton("*")
        btn17.setFixedSize(100,50)
        btn17.clicked.connect(self.calculations)

        
        hbox4.addWidget(btn0)
        hbox4.addWidget(btn17)
        
        
        self.setLayout(hbox)
        
        
        layout = self.layout()
        layout.addLayout(hbox)
        layout.addLayout(hbox2)
        layout.addLayout(hbox3)
        layout.addLayout(hbox4)


    def backspace_button(self):
        ...
    
    
    def calculations(self):
        sender_button = self.sender()
        if sender_button.text() == "1":
            current_text = self.line_ans.text()
            if current_text == "0":
                self.line_ans.setText("1")
            else:
                self.line_ans.setText(current_text + "1")
        elif sender_button.text() == "2":
            current_text = self.line_ans.text()
            if current_text == "0":
                self.line_ans.setText("2")
            else:
                self.line_ans.setText(f"{current_text}2")
        elif sender_button.text() == "3":
            current_text = self.line_ans.text()
            if current_text == "0":
                self.line_ans.setText("3")
            else:
                self.line_ans.setText(f"{current_text}3")
        elif sender_button.text() == "4":
            current_text = self.line_ans.text()
            if current_text == "0":
                self.line_ans.setText("4")
            else:
                self.line_ans.setText(f"{current_text}4")
        elif sender_button.text() == "5":
            current_text = self.line_ans.text()
            if current_text == "0":
                self.line_ans.setText("5")
            else:
                self.line_ans.setText(f"{current_text}5")
        elif sender_button.text() == "6":
            current_text = self.line_ans.text()
            if current_text == "0":
                self.line_ans.setText("6")
            else:
                self.line_ans.setText(f"{current_text}6")
        elif sender_button.text() == "7":
            current_text = self.line_ans.text()
            if current_text == "0":
                self.line_ans.setText("7")
            else:
                self.line_ans.setText(f"{current_text}7")
        elif sender_button.text() == "8":
            current_text = self.line_ans.text()
            if current_text == "0":
                self.line_ans.setText("8")
            else:
                self.line_ans.setText(f"{current_text}8")
        elif sender_button.text() == "0":
            current_text = self.line_ans.text()
            if current_text == "0":
                self.line_ans.setText("0")
            else:
                self.line_ans.setText(f"{current_text}0")
        elif sender_button.text() == "9":
            current_text = self.line_ans.text()
            if current_text == "0":
                self.line_ans.setText("9")
            else:
                self.line_ans.setText(f"{current_text}9")
        elif sender_button.text() == "+":
            current_text = self.line_ans.text()
            if current_text == "0":
                self.line_ans.setText("+")
            else:
                self.line_ans.setText(f"{current_text}+")
        elif sender_button.text() == "-":
            current_text = self.line_ans.text()
            if current_text == "0":
                self.line_ans.setText("-")
            else:
                self.line_ans.setText(f"{current_text}-")
        elif sender_button.text() == "/":
            current_text = self.line_ans.text()
            if current_text == "0":
                pass

        elif sender_button.text() == "*":
            current_text = self.line_ans.text()
            if current_text == "0":
                self.line_ans.setText("*")
            else:
                self.line_ans.setText(f"{current_text}*")
                

    
    
    
    def arith_signs(self):
        vbox2 = QVBoxLayout()
        add_button = QPushButton("+")
        add_button.clicked.connect(self.calculations)
        minus_button = QPushButton("-")
        minus_button.clicked.connect(self.calculations)
        divide_button = QPushButton("/")
        divide_button.clicked.connect(self.calculations)
        multiply_button = QPushButton("*")
        multiply_button.clicked.connect(self.calculations)
                
            
        
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
