from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import pandas as pd

import cv2
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5 import QtWidgets, uic
from matplotlib.figure import Figure
from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtWidgets, uic


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # Load the UI Page
        uic.loadUi('test.ui', self)
        self.Run.clicked.connect(self.CameraRun)
        self.bt_fig.clicked.connect(self.ShowFig)

    @pyqtSlot()
    def CameraRun(self):
        camera = cv2.VideoCapture(0)
        while (camera.isOpened()):
            ret, frame = camera.read()
            if ret == True:
                self.displayImage(frame, 1)
                cv2.waitKey()
        camera.release()
        cv2.destroyAllWindows()

    def displayImage(self, img, window=1):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if (img.shape[2]) == 4:
                qformat = QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        self.cam.setPixmap(QPixmap.fromImage(img))
        self.cam.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def ShowFig(self):
        df = pd.read_excel(r'reddotCo.xlsx')
        X = df['X']
        Y = df['Y']
        self.fig.plot(X, Y)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
