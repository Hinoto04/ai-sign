import os
import sys
from PyQt5.QtCore import QPoint, QSize, Qt
from PyQt5.QtGui import QImage, QPainter, QPen
from PyQt5.QtWidgets import QApplication, QFileDialog, QInputDialog, QMainWindow, QAction, QPushButton, qApp, QDesktopWidget

class DrawingTool(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.image = QImage(QSize(160, 80), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.brush_size = 3
        self.brush_color = Qt.black
        self.last_point = QPoint()
        self.savepath = ''
        self.username = 'Default'
        self.number = 0
        self.initUI()
        
    def initUI(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('File')

        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save)

        clear_action = QAction('Clear', self)
        clear_action.setShortcut('Ctrl+C')
        clear_action.triggered.connect(self.clear)
        
        next_action = QAction('Next', self)
        next_action.setShortcut('Ctrl+N')
        next_action.triggered.connect(self.next)

        filemenu.addAction(next_action)
        filemenu.addAction(save_action)
        filemenu.addAction(clear_action)
        
        self.btn = QPushButton('Set Username', self)
        self.btn.move(5, 5)
        self.btn.clicked.connect(self.setUsername)
        
        self.nbtn = QPushButton('Set Number', self)
        self.nbtn.move(110, 5)
        self.nbtn.clicked.connect(self.setNumber)
        
        self.setWindowTitle('Sign Drawing Tool')
        self.resize(800, 400)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def setUsername(self):
        username, ok = QInputDialog.getText(self, 'InputDialog', 'Enter Username')

        if ok:
            self.username = username
            self.number = 0
        
    def setNumber(self):
        number, ok = QInputDialog.getInt(self, 'InputDialog', 'Enter Number')
        
        if ok:
            self.number = number
    
    def pixelpos(self, x, y):
        return QPoint(int(x/(self.width()/160)), int(y/(self.height()/80)))
        
    def paintEvent(self, e):
        canvas = QPainter(self)
        canvas.drawImage(self.rect(), self.image, self.image.rect())
        
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = self.pixelpos(e.x(), e.y())
    
    def mouseMoveEvent(self, e):
        if(e.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
            painter.drawLine(self.last_point, self.pixelpos(e.x(), e.y()))
            self.last_point = self.pixelpos(e.x(), e.y())
            self.update()
    
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drawing = False
    
    def save(self):
        fpath, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if fpath:
            self.image.save(fpath)
            
    def clear(self):
        self.image.fill(Qt.white)
        self.update()
    
    def next(self):
        if self.savepath == '':
            fpath = QFileDialog.getExistingDirectory(self, "Select Directory")
            
            if fpath:
                self.savepath = fpath
        else:
            fpath = self.savepath + '/' + str(self.number) + '_' + self.username + '.png'
            self.image.save(fpath)
            self.clear()
            self.number += 1
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawingTool()
    sys.exit(app.exec_())