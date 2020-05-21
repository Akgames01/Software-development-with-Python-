from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QApplication,QDialog,QWidget,QVBoxLayout,QLabel,QLineEdit,QPushButton,QProgressBar,QMessageBox,QFileDialog)
import sys
#from fbs_runtime.application_context.PyQt5 import ApplicationContext
import urllib.request as urequest
class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        layout = QVBoxLayout()
        self.url = QLineEdit()
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        download = QPushButton('Download')
        browse = QPushButton('Browse')
        #adding placeholder 
        self.url.setPlaceholderText('URL')
        self.save_location.setPlaceholderText('File Save location')
        #making progress bar value 
        self.progress.setValue(float(0))
        self.progress.setAlignment(Qt.AlignHCenter)
        layout.addWidget(self.url)        
        layout.addWidget(self.save_location)
        layout.addWidget(browse)
        layout.addWidget(self.progress)
        layout.addWidget(download)
        self.setLayout(layout)
        #changing look
        self.setWindowTitle('PyDownloader')
        download.clicked.connect(self.download)
        browse.clicked.connect(self.browse_file)
        #adding browse buttons
    #adding functionality 
    def browse_file(self):
        save_file = QFileDialog.getSaveFileName(self,caption='Save File as',directory='.',filter='All Files (*.*)')
        print(save_file)
        self.save_location.setText(QDir.toNativeSeparators(save_file[0]))
    def download(self):
        #event handler 
        url = self.url.text()
        save_location = self.save_location.text()
        #retrieving url and save on the disk 
        try:
            urequest.urlretrieve(url,save_location,self.report)
            
        except Exception:
            QMessageBox.warning(self,'Warning','Download unsucessfull')
            return
        QMessageBox.information(self,'Information','Download is Complete')#self is parent Q widget 2nd argument is title of the box 
            #pass
        self.progress.setValue(float(0))
        self.url.setText('')
        self.save_location.setText('')
    def report(self,blocknum,blocksize,totalsize):#for reporting info about download and update the progress bar
        readsofar = blocknum*blocksize
        if totalsize > 0:
            percent = (readsofar*100)/totalsize
            self.progress.setValue(percent)


app = QApplication(sys.argv)
dialog = Downloader()
dialog.show()
app.exec_()