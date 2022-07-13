# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from math import sin, cos, tan, pi, e, log, asin, acos, atan
from numpy import linspace, array
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import scipy.integrate as integ
from scipy.misc import derivative
shift = 0
Ans = 'undefined'
A = 0
B = 0
C = 0
D = 0
X = 0
Y = 0
Z = 0
STO_press = 0
def prime(n):
    if (n < 2): return 0
    else:
        count = 0
        i = 2
        while (i <= n):
            if (n % i == 0): count += 1
            else: pass
            i += 1
            if (count > 1): break
        if count == 1: return 1
        else: return 0

def prime_list(n): 
    t = []
    for i in range(2, n + 1):
        if (prime(i) == 1): t.append(i)
    return t

def FACT(n):
    if ((type(n)!=int) or (n < 0)):
        t = 'Invalid value for FACT function! \nPress AC to continue!'
        return t
    elif (n == 0): return 0
    elif (n == 1): return 1
    else:
        basedata = []
        powerdata = []
        l = prime_list(n)
        i = 0
        while (n > 1):
            if (n % l[i] != 0): i += 1
            else:
                count = 0
                while (n % l[i] == 0):
                    count += 1
                    n = n/l[i]
                basedata.append(l[i])
                powerdata.append(count)
        s = str(basedata[0]) + '^' + str(powerdata[0])
        for i in range(1, len(basedata)):
            s = s + '*'+ str(basedata[i]) + '^' + str(powerdata[i])
        return s

def ln(a):
    if (a<=0): return 'Invalid value for ln function! \nPress AC to return!'
    else: return log(a,e)

def root(a,n):
    try:
        return a**(1/n)
    except:
        return 'Invalid value for power function! \nPress AC to return!'

def factorial(n):
    if ((type(n) != int) or (n < 0)):
        return 'Invalid value for factorial function! \nPress AC to return!'
    else:
        if (n == 0): return 1
        elif (n == 1): return 1
        else: return factorial(n - 1)*n

def inte(f,a,b):
    t = integ.quad(f,a,b)
    out = t[0]
    return out
def deriv(f,n):
    out = derivative(f,n)
    return out

def sigma(f,a,b):
    s = 0
    if ((a > b) or (type(a) != int) or (type(b) != int)): 
        return '''Insufficient value for sigma function! \nPress AC to continue!'''
    else:
        x = linspace(a,b,b-a+1)
        for i in range(len(x)):
            s = s + f(x[i])
        return s

def line(string):
    s = ''
    while (len(string) > 33):
        s = s + string[:33] +'\n'
        string = string[33:]
    s = s + string
    return s

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.setEnabled(True)
        Calculator.resize(973, 717)
        font = QtGui.QFont()
        font.setPointSize(12)
        Calculator.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.Output_Screen = QtWidgets.QLabel(self.centralwidget)
        self.Output_Screen.setGeometry(QtCore.QRect(10, 40, 480, 631))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.Output_Screen.setFont(font)
        self.Output_Screen.setMouseTracking(True)
        self.Output_Screen.setFrameShape(QtWidgets.QFrame.Panel)
        self.Output_Screen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Output_Screen.setLineWidth(1)
        self.Output_Screen.setText("")
        self.Output_Screen.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.Output_Screen.setObjectName("Output_Screen")
        self.button_0 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('0'))
        self.button_0.setGeometry(QtCore.QRect(520, 610, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_0.setFont(font)
        self.button_0.setObjectName("button_0")
        self.button_dot = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('.'))
        self.button_dot.setGeometry(QtCore.QRect(610, 611, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_dot.setFont(font)
        self.button_dot.setObjectName("button_dot")
        self.button_power10 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('*10^'))
        self.button_power10.setGeometry(QtCore.QRect(700, 611, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.button_power10.setFont(font)
        self.button_power10.setObjectName("button_power10")
        self.button_ans = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('Ans'))
        self.button_ans.setGeometry(QtCore.QRect(790, 611, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_ans.setFont(font)
        self.button_ans.setObjectName("button_ans")
        self.button_out = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('='))
        self.button_out.setGeometry(QtCore.QRect(880, 611, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_out.setFont(font)
        self.button_out.setObjectName("button_out")
        self.button_minus = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('-'))
        self.button_minus.setGeometry(QtCore.QRect(880, 520, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_minus.setFont(font)
        self.button_minus.setObjectName("button_minus")
        self.button_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('2'))
        self.button_2.setGeometry(QtCore.QRect(610, 520, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('1'))
        self.button_1.setGeometry(QtCore.QRect(520, 519, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_1.setFont(font)
        self.button_1.setObjectName("button_1")
        self.button_plus = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('+'))
        self.button_plus.setGeometry(QtCore.QRect(790, 520, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_plus.setFont(font)
        self.button_plus.setObjectName("button_plus")
        self.button_3 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('3'))
        self.button_3.setGeometry(QtCore.QRect(700, 520, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_3.setFont(font)
        self.button_3.setObjectName("button_3")
        self.button_divide = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('/'))
        self.button_divide.setGeometry(QtCore.QRect(880, 430, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_divide.setFont(font)
        self.button_divide.setObjectName("button_divide")
        self.button_5 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('5'))
        self.button_5.setGeometry(QtCore.QRect(610, 430, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_5.setFont(font)
        self.button_5.setObjectName("button_5")
        self.button_4 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('4'))
        self.button_4.setGeometry(QtCore.QRect(520, 429, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_4.setFont(font)
        self.button_4.setObjectName("button_4")
        self.button_multiply = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('*'))
        self.button_multiply.setGeometry(QtCore.QRect(790, 430, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_multiply.setFont(font)
        self.button_multiply.setObjectName("button_multiply")
        self.button_6 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('6'))
        self.button_6.setGeometry(QtCore.QRect(700, 430, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_6.setFont(font)
        self.button_6.setObjectName("button_6")
        self.button_AC = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('AC'))
        self.button_AC.setGeometry(QtCore.QRect(880, 340, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_AC.setFont(font)
        self.button_AC.setObjectName("button_AC")
        self.button_8 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('8'))
        self.button_8.setGeometry(QtCore.QRect(610, 340, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_8.setFont(font)
        self.button_8.setObjectName("button_8")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('7'))
        self.button_7.setGeometry(QtCore.QRect(520, 339, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_7.setFont(font)
        self.button_7.setObjectName("button_7")
        self.button_del = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('DEL'))
        self.button_del.setGeometry(QtCore.QRect(790, 340, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_del.setFont(font)
        self.button_del.setObjectName("button_del")
        self.button_9 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('9'))
        self.button_9.setGeometry(QtCore.QRect(700, 340, 71, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_9.setFont(font)
        self.button_9.setObjectName("button_9")
        self.button_leftparen = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('('))
        self.button_leftparen.setGeometry(QtCore.QRect(520, 250, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_leftparen.setFont(font)
        self.button_leftparen.setObjectName("button_leftparen")
        self.buttonGroup = QtWidgets.QButtonGroup(Calculator)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.button_leftparen)
        self.button_rightparen = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press(')'))
        self.button_rightparen.setGeometry(QtCore.QRect(594, 250, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_rightparen.setFont(font)
        self.button_rightparen.setObjectName("button_rightparen")
        self.buttonGroup.addButton(self.button_rightparen)
        self.button_npower = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('^'))
        self.button_npower.setGeometry(QtCore.QRect(668, 250, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_npower.setFont(font)
        self.button_npower.setObjectName("button_npower")
        self.buttonGroup.addButton(self.button_npower)
        self.button_nroot = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('root('))
        self.button_nroot.setGeometry(QtCore.QRect(742, 250, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_nroot.setFont(font)
        self.button_nroot.setObjectName("button_nroot")
        self.buttonGroup.addButton(self.button_nroot)
        self.button_logab = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('log('))
        self.button_logab.setGeometry(QtCore.QRect(816, 250, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_logab.setFont(font)
        self.button_logab.setObjectName("button_logab")
        self.buttonGroup.addButton(self.button_logab)
        self.button_ln = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('ln('))
        self.button_ln.setGeometry(QtCore.QRect(890, 250, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_ln.setFont(font)
        self.button_ln.setObjectName("button_ln")
        self.buttonGroup.addButton(self.button_ln)
        self.button_cos = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('cos('))
        self.button_cos.setGeometry(QtCore.QRect(594, 180, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_cos.setFont(font)
        self.button_cos.setObjectName("button_cos")
        self.button_tan = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('tan('))
        self.button_tan.setGeometry(QtCore.QRect(668, 180, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_tan.setFont(font)
        self.button_tan.setObjectName("button_tan")
        self.button_X = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('X'))
        self.button_X.setGeometry(QtCore.QRect(742, 180, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_X.setFont(font)
        self.button_X.setObjectName("button_X")
        self.button_Y = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('Y'))
        self.button_Y.setGeometry(QtCore.QRect(816, 180, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_Y.setFont(font)
        self.button_Y.setObjectName("button_Y")
        self.button_Z = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('Z'))
        self.button_Z.setGeometry(QtCore.QRect(890, 180, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_Z.setFont(font)
        self.button_Z.setObjectName("button_Z")
        self.button_sin = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('sin('))
        self.button_sin.setGeometry(QtCore.QRect(520, 180, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_sin.setFont(font)
        self.button_sin.setObjectName("button_sin")
        self.label_round = QtWidgets.QLabel(self.centralwidget)
        self.label_round.setGeometry(QtCore.QRect(520, 586, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_round.setFont(font)
        self.label_round.setAlignment(QtCore.Qt.AlignCenter)
        self.label_round.setObjectName("label_round")
        self.label_pi = QtWidgets.QLabel(self.centralwidget)
        self.label_pi.setGeometry(QtCore.QRect(520, 405, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_pi.setFont(font)
        self.label_pi.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pi.setObjectName("label_pi")
        self.label_e = QtWidgets.QLabel(self.centralwidget)
        self.label_e.setGeometry(QtCore.QRect(520, 495, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_e.setFont(font)
        self.label_e.setAlignment(QtCore.Qt.AlignCenter)
        self.label_e.setObjectName("label_e")
        self.button_comma = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press(','))
        self.button_comma.setGeometry(QtCore.QRect(520, 110, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_comma.setFont(font)
        self.button_comma.setObjectName("button_comma")
        self.button_integration = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('inte('))
        self.button_integration.setGeometry(QtCore.QRect(594, 110, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_integration.setFont(font)
        self.button_integration.setObjectName("button_integration")
        self.button_i_unit = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('j'))
        self.button_i_unit.setGeometry(QtCore.QRect(668, 110, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_i_unit.setFont(font)
        self.button_i_unit.setObjectName("button_i_unit")
        self.button_factorial = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('factorial('))
        self.button_factorial.setGeometry(QtCore.QRect(742, 110, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_factorial.setFont(font)
        self.button_factorial.setObjectName("button_factorial")
        self.button_calc = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('CALC'))
        self.button_calc.setGeometry(QtCore.QRect(816, 110, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_calc.setFont(font)
        self.button_calc.setObjectName("button_calc")
        self.button_fact = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('FACT('))
        self.button_fact.setGeometry(QtCore.QRect(890, 110, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_fact.setFont(font)
        self.button_fact.setObjectName("button_fact")
        self.button_STO = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('STO'))
        self.button_STO.setGeometry(QtCore.QRect(890, 40, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_STO.setFont(font)
        self.button_STO.setObjectName("button_STO")
        self.button_SHIFT = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Press('SHIFT'))
        self.button_SHIFT.setGeometry(QtCore.QRect(520, 40, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_SHIFT.setFont(font)
        self.button_SHIFT.setObjectName("button_SHIFT")
        self.label_A = QtWidgets.QLabel(self.centralwidget)
        self.label_A.setGeometry(QtCore.QRect(520, 230, 61, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_A.setFont(font)
        self.label_A.setAlignment(QtCore.Qt.AlignCenter)
        self.label_A.setObjectName("label_A")
        self.label_B = QtWidgets.QLabel(self.centralwidget)
        self.label_B.setGeometry(QtCore.QRect(594, 230, 61, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_B.setFont(font)
        self.label_B.setAlignment(QtCore.Qt.AlignCenter)
        self.label_B.setObjectName("label_B")
        self.label_C = QtWidgets.QLabel(self.centralwidget)
        self.label_C.setGeometry(QtCore.QRect(668, 230, 61, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_C.setFont(font)
        self.label_C.setAlignment(QtCore.Qt.AlignCenter)
        self.label_C.setObjectName("label_C")
        self.label_D = QtWidgets.QLabel(self.centralwidget)
        self.label_D.setGeometry(QtCore.QRect(742, 230, 61, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_D.setFont(font)
        self.label_D.setAlignment(QtCore.Qt.AlignCenter)
        self.label_D.setObjectName("label_D")
        self.label_arcsin = QtWidgets.QLabel(self.centralwidget)
        self.label_arcsin.setGeometry(QtCore.QRect(520, 160, 61, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_arcsin.setFont(font)
        self.label_arcsin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_arcsin.setObjectName("label_arcsin")
        self.label_arccos = QtWidgets.QLabel(self.centralwidget)
        self.label_arccos.setGeometry(QtCore.QRect(594, 160, 61, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_arccos.setFont(font)
        self.label_arccos.setAlignment(QtCore.Qt.AlignCenter)
        self.label_arccos.setObjectName("label_arccos")
        self.label_arctan = QtWidgets.QLabel(self.centralwidget)
        self.label_arctan.setGeometry(QtCore.QRect(668, 160, 61, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_arctan.setFont(font)
        self.label_arctan.setAlignment(QtCore.Qt.AlignCenter)
        self.label_arctan.setObjectName("label_arctan")
        self.label_derivative = QtWidgets.QLabel(self.centralwidget)
        self.label_derivative.setGeometry(QtCore.QRect(594, 90, 61, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_derivative.setFont(font)
        self.label_derivative.setAlignment(QtCore.Qt.AlignCenter)
        self.label_derivative.setObjectName("label_derivative")
        self.label_sigma = QtWidgets.QLabel(self.centralwidget)
        self.label_sigma.setGeometry(QtCore.QRect(742, 90, 61, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_sigma.setFont(font)
        self.label_sigma.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sigma.setObjectName("label_sigma")
        self.label_absolute = QtWidgets.QLabel(self.centralwidget)
        self.label_absolute.setGeometry(QtCore.QRect(668, 90, 61, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_absolute.setFont(font)
        self.label_absolute.setAlignment(QtCore.Qt.AlignCenter)
        self.label_absolute.setObjectName("label_absolute")
        self.mode_choose = QtWidgets.QComboBox(self.centralwidget)
        self.mode_choose.setGeometry(QtCore.QRect(594, 40, 283, 41))
        self.mode_choose.setEditable(False)
        self.mode_choose.setObjectName("mode_choose")
        self.mode_choose.addItem("")
        self.mode_choose.addItem("")
        self.mode_choose.addItem("")
        self.mode_choose.addItem("")
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 973, 21))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def Press(self, button):
        #Globalize variables.
        global mode, shift, A, B, C, D, X, Y, Z, STO_press, Ans
        mode = self.mode_choose.currentText()
        # For Normal Mode:
        if mode == '1: Normal':
            try:
                #For SHIFT isn't pressed:
                if shift == 0:
                    #For STO isn't pressed:
                    if STO_press == 0:
                        if button == 'AC':
                            self.Output_Screen.setText('')
                        elif button == 'DEL':
                            t = self.Output_Screen.text()
                            if len(t) == 0: pass
                            else: self.Output_Screen.setText(t[:-1])
                        elif button == 'Ans':
                            if Ans == 'undefined': pass
                            else: self.Output_Screen.setText(f'{self.Output_Screen.text()}{button}')
                        elif button == 'SHIFT': shift = 1
                        elif button == 'STO': STO_press = 1
                        elif button == '=':
                            t = self.Output_Screen.text()
                            t = t.replace('^', '**')
                            t = t.replace('inte(', 'inte( lambda X:')
                            t = t.replace('deriv(', 'deriv( lambda X:')
                            t = t.replace('sigma(', 'sigma( lambda X:')
                            Ans = eval(t)
                            self.Output_Screen.setText(line(str(Ans)))
                        elif button == 'j': pass
                        elif button == 'CALC': pass
                        else: self.Output_Screen.setText(f'{self.Output_Screen.text()}{button}')
                    #For STO is pressed:
                    else:
                        if button == 'X': X = eval('Ans')
                        elif button == 'Y': Y = eval('Ans')
                        elif button == 'Z': Z = eval('Ans')
                        elif button == '(': A = eval('Ans')
                        elif button == ')': B = eval('Ans')
                        elif button == '^': C = eval('Ans')
                        elif button == 'root(': D = eval('Ans')
                        else: pass
                        STO_press = 0 
                #For SHIFT is pressed:
                else:
                    if button == '0': self.Output_Screen.setText(f'{self.Output_Screen.text()}round(')
                    elif button == '1': self.Output_Screen.setText(f'{self.Output_Screen.text()}e')
                    elif button == '4': self.Output_Screen.setText(f'{self.Output_Screen.text()}pi')
                    elif button == '(': self.Output_Screen.setText(f'{self.Output_Screen.text()}A')
                    elif button == ')': self.Output_Screen.setText(f'{self.Output_Screen.text()}B')
                    elif button == '^': self.Output_Screen.setText(f'{self.Output_Screen.text()}C')
                    elif button == 'root(': self.Output_Screen.setText(f'{self.Output_Screen.text()}D')
                    elif button == 'sin(': self.Output_Screen.setText(f'{self.Output_Screen.text()}asin(')
                    elif button == 'cos(': self.Output_Screen.setText(f'{self.Output_Screen.text()}acos(')
                    elif button == 'tan(': self.Output_Screen.setText(f'{self.Output_Screen.text()}atan(')
                    elif button == 'inte(': self.Output_Screen.setText(f'{self.Output_Screen.text()}deriv(')
                    elif button == 'j': self.Output_Screen.setText(f'{self.Output_Screen.text()}abs(')
                    elif button == 'factorial(': self.Output_Screen.setText(f'{self.Output_Screen.text()}sigma(')
                    else: pass
                    shift = 0
            except:
                self.Output_Screen.setText('Error! \nPress AC to return!')

        #For Complex Mode:
        elif mode == '2: Complex Number':
            try:
                import cmath as cm
                if shift == 0:
                    if STO_press == 0:
                        if ((button == 'inte(')
                            or (button == 'factorial(')
                            or (button == 'FACT(')):
                            pass
                        elif button == '=':
                            t = str(self.Output_Screen.text())
                            t = t.replace('^','**')
                            t = t.replace('sin(', 'cm.sin(')
                            t = t.replace('cos(', 'cm.cos(')
                            t = t.replace('tan(', 'cm.tan(')
                            t = t.replace('log(', 'cm.log(')
                            t = t.replace('asin(', 'cm.asin(')
                            t = t.replace('acos(', 'cm.acos(')
                            t = t.replace('atan(', 'cm.atan(')
                            Ans = eval(t)
                            self.Output_Screen.setText(line(str(Ans)))
                        elif button == 'SHIFT':
                            shift = 1
                        elif button == 'Ans':
                            if Ans == 'undefined': pass
                            else: self.Output_Screen.setText(f'{self.Output_Screen.text()}Ans')
                        elif button == 'STO': STO_press = 1
                        elif button == 'CALC': pass
                        elif button == 'AC': self.Output_Screen.setText('')
                        elif button == 'DEL':
                            t = str(self.Output_Screen.text())
                            if len(t) == 0: pass
                            else: self.Output_Screen.setText(t[:-1])
                        else: self.Output_Screen.setText(f'{self.Output_Screen.text()}{button}')
                    else:
                        if button == 'X': X = eval('Ans')
                        elif button == 'Y': Y = eval('Ans')
                        elif button == 'Z': Z = eval('Ans')
                        elif button == '(': A = eval('Ans')
                        elif button == ')': B = eval('Ans')
                        elif button == '^': C = eval('Ans')
                        elif button == 'root(': D = eval('Ans')
                        else: pass
                        STO_press = 0 
                else:
                    if button == '0': self.Output_Screen.setText(f'{self.Output_Screen.text()}round(')
                    elif button == '1': self.Output_Screen.setText(f'{self.Output_Screen.text()}e')
                    elif button == '4': self.Output_Screen.setText(f'{self.Output_Screen.text()}pi')
                    elif button == '(': self.Output_Screen.setText(f'{self.Output_Screen.text()}A')
                    elif button == ')': self.Output_Screen.setText(f'{self.Output_Screen.text()}B')
                    elif button == '^': self.Output_Screen.setText(f'{self.Output_Screen.text()}C')
                    elif button == 'root(': self.Output_Screen.setText(f'{self.Output_Screen.text()}D')
                    elif button == 'j': self.Output_Screen.setText(f'{self.Output_Screen.text()}abs(')
                    elif button == 'sin(': self.Output_Screen.setText(f'{self.Output_Screen.text()}asin(')
                    elif button == 'cos(': self.Output_Screen.setText(f'{self.Output_Screen.text()}acos(')
                    elif button == 'tan(': self.Output_Screen.setText(f'{self.Output_Screen.text()}atan(')
                    else: pass
                    shift = 0
            except:
                self.Output_Screen.setText('Error! \nPress AC to return!')
        elif mode == '3: Equation Solver':
            from sympy import symbols, solve
            import sympy as sp
            try:
                def s_root(x, n):
                    x = symbols('x')
                    out = x**(1/n)
                    return out
                x = symbols('x')
                def s_ln(x):
                    x = symbols('x')
                    out = sp.log(x)
                    return out
                def s_log(x, b):
                    x = symbols('x')
                    out = sp.log(x)/sp.log(b)
                    return out 
                if shift == 0:
                    if ((button == 'inte(')
                        or (button == 'j')
                        or (button == 'factorial(')
                        or (button == 'CALC')
                        or (button == 'FACT(')
                        or (button == 'Ans')
                        or (button == 'STO')): pass
                    elif button == 'AC': self.Output_Screen.setText('solve(')
                    elif button == 'DEL':
                        t = self.Output_Screen.text()
                        if len(t) == 0: pass
                        else: self.Output_Screen.setText(t[:-1])
                    elif button == '=':
                        t = str(self.Output_Screen.text())
                        t = t.replace('^','**')
                        t = t.replace('sin(', 'sp.sin(')
                        t = t.replace('cos(', 'sp.cos(')
                        t = t.replace('tan(', 'sp.tan(')
                        t = t.replace('asin(', 'sp.asin(')
                        t = t.replace('acos(', 'sp.acos(')
                        t = t.replace('atan(', 'sp.atan(')
                        t = t.replace('log(', 's_log(')
                        t = t.replace('ln(', 's_ln(')
                        t = t.replace('root(', 's_root(')
                        t = eval(t)
                        s = ''
                        for i in t:
                            s = s + 'X = ' + line(str(i)) + '\n'
                        s = str(s)
                        self.Output_Screen.setText(s)
                    elif button == 'SHIFT': shift = 1
                    elif button == 'X': self.Output_Screen.setText(f'{self.Output_Screen.text()}x')
                    else: self.Output_Screen.setText(f'{self.Output_Screen.text()}{button}')
                else:
                    if button == '0': self.Output_Screen.setText(f'{self.Output_Screen.text()}round(')
                    elif button == '1': self.Output_Screen.setText(f'{self.Output_Screen.text()}e')
                    elif button == '4': self.Output_Screen.setText(f'{self.Output_Screen.text()}pi')
                    elif button == '(': self.Output_Screen.setText(f'{self.Output_Screen.text()}A')
                    elif button == ')': self.Output_Screen.setText(f'{self.Output_Screen.text()}B')
                    elif button == '^': self.Output_Screen.setText(f'{self.Output_Screen.text()}C')
                    elif button == 'root(': self.Output_Screen.setText(f'{self.Output_Screen.text()}D')
                    else: pass
                    shift = 0
            except:
                self.Output_Screen.setText('Error! Press AC to return!')
        else:
            def graph(f,a,b):
                try:
                    X = linspace(a,b,10000)
                    Y = []
                    i = 0
                    for x in X:
                        y = f(x)
                        Y.append(y)
                    Y = array(Y)
                    plt.figure(figsize=(4.85,6.5))
                    plt.plot(X,Y)
                    plt.xlabel('x')
                    plt.ylabel('y')
                    plt.grid()
                    plt.savefig('graph.png')
                    self.Output_Screen.setPixmap(QPixmap('graph.png'))
                except:
                    self.Output_Screen.setText('MathError! Infinite value in graph! \nPress AC to return!')
            try:
                if shift == 0:
                    if ((button == 'inte(')
                        or (button == 'j')
                        or (button == 'factorial(')
                        or (button == 'CALC')
                        or (button == 'FACT(')
                        or (button == 'Ans')
                        or (button == 'STO')): pass
                    elif button == 'AC': self.Output_Screen.setText('graph(')
                    elif button == 'DEL':
                        t = self.Output_Screen.text()
                        if len(t) == 0: pass
                        else: self.Output_Screen.setText(t[:-1])
                    elif button == '=':
                        t = str(self.Output_Screen.text())
                        t = t.replace('^','**')
                        t = t.replace('graph(', 'graph( lambda X:')
                        exec(t)
                    elif button == 'SHIFT': shift = 1
                    else: self.Output_Screen.setText(f'{self.Output_Screen.text()}{button}')
                else:
                    if button == '0': self.Output_Screen.setText(f'{self.Output_Screen.text()}round(')
                    elif button == '1': self.Output_Screen.setText(f'{self.Output_Screen.text()}e')
                    elif button == '4': self.Output_Screen.setText(f'{self.Output_Screen.text()}pi')
                    elif button == '(': self.Output_Screen.setText(f'{self.Output_Screen.text()}A')
                    elif button == ')': self.Output_Screen.setText(f'{self.Output_Screen.text()}B')
                    elif button == '^': self.Output_Screen.setText(f'{self.Output_Screen.text()}C')
                    elif button == 'root(': self.Output_Screen.setText(f'{self.Output_Screen.text()}D')
                    elif button == 'j': self.Output_Screen.setText(f'{self.Output_Screen.text()}abs(')
                    shift = 0
            except:
                self.Output_Screen.setText('MathError! Infinite value in graph! \nPress AC to return!')

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.button_0.setText(_translate("Calculator", "0"))
        self.button_dot.setText(_translate("Calculator", "."))
        self.button_power10.setText(_translate("Calculator", "x10^n"))
        self.button_ans.setText(_translate("Calculator", "Ans"))
        self.button_out.setText(_translate("Calculator", "="))
        self.button_minus.setText(_translate("Calculator", "-"))
        self.button_2.setText(_translate("Calculator", "2"))
        self.button_1.setText(_translate("Calculator", "1"))
        self.button_plus.setText(_translate("Calculator", "+"))
        self.button_3.setText(_translate("Calculator", "3"))
        self.button_divide.setText(_translate("Calculator", "/"))
        self.button_5.setText(_translate("Calculator", "5"))
        self.button_4.setText(_translate("Calculator", "4"))
        self.button_multiply.setText(_translate("Calculator", "*"))
        self.button_6.setText(_translate("Calculator", "6"))
        self.button_AC.setText(_translate("Calculator", "AC"))
        self.button_8.setText(_translate("Calculator", "8"))
        self.button_7.setText(_translate("Calculator", "7"))
        self.button_del.setText(_translate("Calculator", "DEL"))
        self.button_9.setText(_translate("Calculator", "9"))
        self.button_leftparen.setText(_translate("Calculator", "("))
        self.button_rightparen.setText(_translate("Calculator", ")"))
        self.button_npower.setText(_translate("Calculator", "x^n"))
        self.button_nroot.setText(_translate("Calculator", "n-root"))
        self.button_logab.setText(_translate("Calculator", "loga(b)"))
        self.button_ln.setText(_translate("Calculator", "ln"))
        self.button_cos.setText(_translate("Calculator", "cos"))
        self.button_tan.setText(_translate("Calculator", "tan"))
        self.button_X.setText(_translate("Calculator", "X"))
        self.button_Y.setText(_translate("Calculator", "Y"))
        self.button_Z.setText(_translate("Calculator", "Z"))
        self.button_sin.setText(_translate("Calculator", "sin"))
        self.label_round.setText(_translate("Calculator", "round"))
        self.label_pi.setText(_translate("Calculator", "pi"))
        self.label_e.setText(_translate("Calculator", "e"))
        self.button_comma.setText(_translate("Calculator", ","))
        self.button_integration.setText(_translate("Calculator", "inte()"))
        self.button_i_unit.setText(_translate("Calculator", "j"))
        self.button_factorial.setText(_translate("Calculator", "x!"))
        self.button_calc.setText(_translate("Calculator", "CALC"))
        self.button_fact.setText(_translate("Calculator", "FACT"))
        self.button_STO.setText(_translate("Calculator", "STO"))
        self.button_SHIFT.setText(_translate("Calculator", "SHIFT"))
        self.label_A.setText(_translate("Calculator", "A"))
        self.label_B.setText(_translate("Calculator", "B"))
        self.label_C.setText(_translate("Calculator", "C"))
        self.label_D.setText(_translate("Calculator", "D"))
        self.label_arcsin.setText(_translate("Calculator", "arcsin"))
        self.label_arccos.setText(_translate("Calculator", "arccos"))
        self.label_arctan.setText(_translate("Calculator", "arctan"))
        self.label_derivative.setText(_translate("Calculator", "deriv()"))
        self.label_sigma.setText(_translate("Calculator", "sigma"))
        self.label_absolute.setText(_translate("Calculator", "Abs"))
        self.mode_choose.setItemText(0, _translate("Calculator", "1: Normal"))
        self.mode_choose.setItemText(1, _translate("Calculator", "2: Complex Number"))
        self.mode_choose.setItemText(2, _translate("Calculator", "3: Equation Solver"))
        self.mode_choose.setItemText(3, _translate("Calculator", "4: Graphing Calculator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())

