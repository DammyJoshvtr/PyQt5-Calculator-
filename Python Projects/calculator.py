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
        return vbox
        
        
    def buttons(self):
        hbox = QHBoxLayout()
        btn1 = QPushButton("1")
        btn1.clicked.connect(self.calculations)
        btn2 = QPushButton("2")
        btn2.clicked.connect(self.calculations)
        btn3 = QPushButton("3")
        btn3.clicked.connect(self.calculations)
        # return btn1

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        
        hbox2 = QHBoxLayout()
        btn4 = QPushButton("4")
        btn5 = QPushButton("5")
        btn6 = QPushButton("6")
        
        hbox2.addWidget(btn4)
        hbox2.addWidget(btn5)
        hbox2.addWidget(btn6)
        
        hbox3 = QHBoxLayout()
        btn7 = QPushButton("7")
        btn8 = QPushButton("8")
        btn9 = QPushButton("9")
        
        hbox3.addWidget(btn7)
        hbox3.addWidget(btn8)
        hbox3.addWidget(btn9)
        
        hbox4 = QHBoxLayout()
        btn0 = QPushButton("0")
        btn0.setFixedSize(100,50)
        hbox4.addWidget(btn0)
        
        
        # layout = self.layout()
        # layout.addLayout(hbox)
        # layout.addLayout(hbox2)
        # layout.addLayout(hbox3)
        # layout.addLayout(hbox4)


    def backspace_button(self):
        ...
    
    # def calculations(self):
    #     print("Button 1 Clicked")
    #     final_ans = self.line_ans
    #     if self.buttons().isClicked:
    #         final_ans = self.line_ans.textChanged(self.buttons())
    
    def calculations(self):
        sender_button = self.sender()
        if sender_button.text() == "1":
            current_text = self.line_ans.text()
            if current_text == "0":
                self.line_ans.setText("1")
            else:
                self.line_ans.setText(current_text + "1")
                
                
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
        
        vbox2.addWidget(add_button)
        vbox2.addWidget(minus_button)
        vbox2.addWidget(divide_button)
        vbox2.addWidget(multiply_button)
        
        # layout2 = self.layout()
        # layout2.addLayout(hbox5)
        
        
        
        # self.addLayout()
                
            
            

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())