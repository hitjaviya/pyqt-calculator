from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
from UI.main_ui import Ui_Form
import sys

 
import sys

class MyWindow(QtWidgets.QWidget):
    MAX_FONT_SIZE = 100
    MIN_FONT_SIZE = 30
    FONT_SIZE_THRESHOLDS = [item for item in enumerate(range(90,30,-5),9)]
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.output=self.ui.lineEdit
        self.ans_line=self.ui.Ans_LineEdit
        self.ans=0
        self.operator_list=["+","-","*","/"]
        self.initialize_ui()
    def initialize_ui(self):
        self.setup_window()
        self.setup_buttons()
        self.init_singnal_slot()
    def setup_window(self):
        self.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
    def setup_buttons(self):
        self.ui.plus_minus_btn.setCheckable(True)
        self.ui.plus_minus_btn.setChecked(False)
    def init_singnal_slot(self):
        self.ui.ans_btn.clicked.connect(self.action_ans)
        self.ui.claer_btn.clicked.connect(self.action_clear)
        self.ui.plus_minus_btn.clicked.connect(self.action_chnage_value)
        self.ui.division_btn.clicked.connect(self.action_div)
        self.ui.dot_btn.clicked.connect(self.action_point)
        self.ui.percentage_btn.clicked.connect(self.action_percentage)
        self.ui.multi_btn.clicked.connect(self.action_mul)
        self.ui.plus_btn.clicked.connect(self.action_plus)
        self.ui.minus_btn.clicked.connect(self.action_minus)
        self.ui.equal_btn.clicked.connect(self.action_equal)
        self.ui.one_btn.clicked.connect(self.action1)
        self.ui.two_btn.clicked.connect(self.action2)
        self.ui.three_btn.clicked.connect(self.action3)
        self.ui.four_btn.clicked.connect(self.action4)
        self.ui.five_btn.clicked.connect(self.action5)
        self.ui.six_btn.clicked.connect(self.action6)
        self.ui.seven_btn.clicked.connect(self.action7)
        self.ui.eight_btn.clicked.connect(self.action8)
        self.ui.nine_btn.clicked.connect(self.action9)
        self.ui.zero_btn.clicked.connect(self.action0)

    def calculate(self,equation):
        result = eval(equation)
        self.ans=result 
        return result
    
    def action_equal(self):

        equation = self.output.text()
 
        try:
            result=self.calculate(equation)
            if str(result).__contains__("."):
                self.ans_line.setText("="+str(round(result,4))) 
            else:
                self.ans_line.setText("="+str(int(result)))
            self.action_clear()
        except:
            self.output.setText("Wrong Input")
    # def update_font_size(self):
    #     text_length=len(self.output.text())
    #     for threshold,size in self.FONT_SIZE_THRESHOLDS:
    #         if threshold== text_length:
    #             self.output.setStyleSheet(f"font-size:{size}px")
    #             return
    #     if text_length>16:
    #         self.output.setStyleSheet(f"font-size:{self.MIN_FONT_SIZE}px")

    #     else:
    #         self.output.setStyleSheet(f"font-size:{self.MAX_FONT_SIZE}px")

    def action_percentage(self):
        text=""
        if self.output.text() =="":

            text=str(self.ans)+text
            self.output.setText(str(float(self.output.text()+text)/100))
        else:
            for i in self.operator_list:
                if self.output.text().__contains__(i):
                    answer=self.calculate(self.output.text())
                    self.output.setText(str(float(answer)/100))
                    break


    def action_chnage_value(self):
        text="" 
        if self.output.text() =="":
            text=str(self.ans)+text
            self.output.setText("-"+text)
        else:
            if self.output.text().__contains__("-"):
                self.output.setText(self.output.text()[1:])
            else:
                self.output.setText("-"+self.output.text())


    def action_plus(self):
        text = self.output.text()
        if self.output.text() =="":
                text=str(self.ans)+text
                self.output.setText(text + " + ")
        else:
            if text[-2] in self.operator_list:
                self.output.setText(text[0:-3] + " + ")
            else:
                self.output.setText(text + " + ")
                
                
 

    def action_minus(self):

        text = self.output.text()
        if self.output.text() =="":
                text=str(self.ans)+text
                self.output.setText(text + " - ")
        else:
            if text[-2] in self.operator_list:
                self.output.setText(text[0:-3] + " - ")
            else:
                self.output.setText(text + " - ")

    def action_div(self):

        text = self.output.text()
        if self.output.text() =="":
                text=str(self.ans)+text
                self.output.setText(text + " / ")
        else:
            if text[-2] in self.operator_list:
                self.output.setText(text[0:-3] + " / ")
            else:
                self.output.setText(text + " / ")
 

    def action_mul(self):

        text = self.output.text()
        if self.output.text() =="":
                text=str(self.ans)+text
                self.output.setText(text + " * ")
        else:
            if text[-2] in self.operator_list:
                self.output.setText(text[0:-3] + " * ")
            else:
                self.output.setText(text + " * ")
 
 
    def action_point(self):
        text = self.output.text()
        if text.__contains__("."):
            self.output.setText(text)
        else:
            if self.output.text() =="":
                text=str(self.ans)+text
            self.output.setText(text + ".")


    def action_ans(self):
        if self.output.text() !="":
            pass
        text = self.output.text()
        self.output.setText(text + f"{self.ans}")


    def action_clear(self):
        self.output.setText("")
 

    def action0(self):
        text = self.output.text()
        self.output.setText(text + "0")
 

    def action1(self):
        text = self.output.text()
        self.output.setText(text + "1")
   
 
    def action2(self):
        text = self.output.text()
        self.output.setText(text + "2")
 

    def action3(self):
        text = self.output.text()
        self.output.setText(text + "3")
 

    def action4(self):
        text = self.output.text()
        self.output.setText(text + "4")
 

    def action5(self):
        text = self.output.text()
        self.output.setText(text + "5")
 

    def action6(self):
        text = self.output.text()
        self.output.setText(text + "6")
 

    def action7(self):
        text = self.output.text()
        self.output.setText(text + "7")
 

    def action8(self):
        text = self.output.text()
        self.output.setText(text + "8")
 
 
    def action9(self):
        text = self.output.text()
        self.output.setText(text + "9")
 
   
       


if __name__=='__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.setWindowTitle("Calculator")
    win.setWindowIcon(QtGui.QIcon("Images\Calculator_logo.png"))
    win.show()
    # to exit on close button click
    sys.exit(app.exec_())
