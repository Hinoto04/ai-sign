import sys
from PyQt5.QtCore import QPoint, QSize, Qt
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QAction, qApp, QDesktopWidget

class DrawingTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image = QImage(QSize(160, 80), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.brush_size = 5
        self.brush_color = Qt.black
        self.last_point = QPoint()
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

        filemenu.addAction(save_action)
        filemenu.addAction(clear_action)
        
        self.setWindowTitle('Sign Drawing Tool')
        self.resize(800, 400)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def save(self):
        fpath, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if fpath:
            self.image.save(fpath)
            
    def clear(self):
        self.image.fill(Qt.white)
        self.update()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawingTool()
    sys.exit(app.exec_())