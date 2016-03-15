#coding: utf8
import sys
import matplotlib

matplotlib.use("Qt5Agg", force=True)

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUiType
from custom_canvas import StaticCanvas
from play import calc_for_plot

import numpy as np

app = QApplication(sys.argv)
app.setApplicationName('Lab 2')
form_class, base_class = loadUiType('main_form.ui')


class MainWindow(QDialog, form_class):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)
        self.setupUi(self)
        self.x_t = StaticCanvas(self.x_t_tab,'$x(t)$')
        self.x_dx = StaticCanvas(self.x_dx_tab,'$\dot{x}(x)$')
        self.x_t_layout.addWidget(self.x_t)
        self.x_dx_layout.addWidget(self.x_dx)
        self.r = 0.1
        self.l = 0.1 #not 0
        self.c = 0.1 #not 0
        self.m = 0
        self.s = 0
        self.a = 0
        self.left_bound = 0
        self.right_bound = 1
        self.step = 0.00001
        self.x0 = 0
        self.dx0 = 0
        self.update_coefficients()

    @pyqtSlot()
    def build_graph(self):
        try:
            self.x_t.clear()
            self.x_dx.clear()
            self.r = np.float64(self.r_input.text())
            self.l = np.float64(self.l_input.text())
            self.c = np.float64(self.c_input.text())
            self.m = np.float64(self.m_input.text())
            self.s = np.float64(self.s_input.text())
            self.a = np.float64(self.a_input.text())

        except:
            return
        try:
            x, y= calc_for_plot(self.right_bound, self.step, self.x0, self.dx0, self.r,self.l, self.c, self.m,
                                    self.s, self.a)
            self.x_t.plot(x[0], x[1])
            self.x_dx.plot(y[0], y[1])
        except Exception as e:
            print(e)

    @pyqtSlot()
    def template_selected(self):
        sender = self.sender().objectName()
        # if sender == 'harmonic_rad':
        #     self.delta = 0
        #     self.w0 = 20
        #     self.f0 = 0
        #     self.w = 0
        #     self.update_coefficients()
        # elif sender == 'dying_rad':
        #     self.delta = 10
        #     self.w0 = 1
        #     self.f0 = 0
        #     self.w = 0
        #     self.update_coefficients()
        # elif sender == 'forced_rad':
        #     self.delta = 5
        #     self.w0 = 80
        #     self.f0 = 3
        #     self.w = 10
        #     self.update_coefficients()

    @pyqtSlot(int)
    def limit_change(self, value):
        self.right_bound = value

    @pyqtSlot('double')
    def step_change(self, value):
        self.step = value

    @pyqtSlot('QString')
    def initval_change(self, value):
        sender = self.sender().objectName()
        try:
            value = np.float64(value)
        except:
            return
        if sender == 'x0_input':
            self.x0 = value
        elif sender == 'dx0_input':
            self.dx0 = value

    def update_coefficients(self):
        self.r_input.setText(str(self.r))
        self.l_input.setText(str(self.l))
        self.c_input.setText(str(self.c))
        self.m_input.setText(str(self.m))
        self.s_input.setText(str(self.s))
        self.a_input.setText(str(self.a))


    @pyqtSlot('QString')
    def coef_edited(self, value):
        self.other_rad.setChecked(True)



#-----------------------------------------------------#
form = MainWindow()
form.setWindowTitle('Лабораторна робота №2 - МСС')
form.show()
sys.exit(app.exec_())