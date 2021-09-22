import sys
from PyQt5.QtCore import QPoint, QSize, Qt
from PyQt5.QtGui import QImage, QIntValidator, QPainter, QPen
from PyQt5.QtWidgets import QApplication, QCheckBox, QFileDialog, QFormLayout, QInputDialog, QLineEdit, QMainWindow, QAction, QPushButton, qApp, QDesktopWidget

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
        self.username = '테스트'
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
        
        self.e1 = QLineEdit(self)
        self.e1.setValidator(QIntValidator())
        self.e1.setMaxLength(4)
        self.e1.setAlignment(Qt.AlignRight)
        self.e1.move(5, 5)
        self.e1.returnPressed.connect(self.setNumber)
        self.e1.setText('1')
        
        self.e2 = QLineEdit(self)
        self.e2.setMaxLength(4)
        self.e2.setAlignment(Qt.AlignRight)
        self.e2.move(110, 5)
        self.e2.returnPressed.connect(self.setUsername)
        self.e2.setText('테스트')
        
        self.e3 = QCheckBox(self)
        self.e3.move(220, 5)
        
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
        username = self.e2.text()
        
        if username == '':
            self.username = '테스트'
            self.e2.setText(self.username)
        else:
            self.username = username
            self.number = 0
            self.e1.setText('0')
        
    def setNumber(self):
        number = self.e1.text()
        self.number = int(number)
    
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
                fpath = self.savepath + '/' + str(self.number) + '_' + self.username + '_' + str(self.e3.isChecked()) + '.png'
                self.image.save(fpath)
                self.clear()
                self.number += 1
                self.e1.setText(str(self.number))
        else:
            fpath = self.savepath + '/' + str(self.number) + '_' + self.username + '_' + str(self.e3.isChecked()) + '.png'
            self.image.save(fpath)
            self.clear()
            self.number += 1
            self.e1.setText(str(self.number))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawingTool()
    sys.exit(app.exec_())