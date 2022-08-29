import sys
from re import A
import qrcode
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
from PyQt5 import QtWidgets

class MainWindow(QMainWindow):
    QuestionTag = []
    InfoTag =  []
    def __init__(self):
        self.QuestionTag = []
        self.InfoTag = []
        QMainWindow.__init__(self)

        self.setGeometry(50,50,1280,720)
          
        self.setWindowTitle("YAML Parser") 

        self.nameLabellu = QLabel(self)
        self.nameLabellu.setText('Infoscreen')
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Etage:')
        self.nameLabel1 = QLabel(self)
        self.nameLabel1.setText('Ueberschrift: ')
        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('Text: ')
        self.nameLabel3 = QLabel(self)
        self.nameLabel3.setText('Hash: ')
        self.nameLabelinfo = QLabel(self)
        self.nameLabelinfo.setText('Normalerweiße sollte der default Hash verwendet werden. In dem Fall das dieser keine Eindeutigkeit mehr garantiert, kann dieser manuel verändert werden. \nRichtige Antworten auf jeweilige Fragen müssen durch den aktivierten Checkbox markiert werden.')

        self.linel = QLineEdit(self)
        self.linel1 = QLineEdit(self)
        self.linel2 = QLineEdit(self)
        self.linel3 = QLineEdit(self)


        self.linel.move(120, 150)
        self.linel1.move(120, 200)
        self.linel2.move(120, 250)
        self.linel3.move(120, 300)


        self.linel.resize(200, 32)
        self.linel1.resize(200, 32)
        self.linel2.resize(200, 32)
        self.linel3.resize(200, 32)

        self.nameLabellu.move(120, 100)
        self.nameLabel.move(80, 150)
        self.nameLabel1.move(40, 200)
        self.nameLabel2.move(80, 250)
        self.nameLabel3.move(80, 300)


        pybuttonl = QPushButton('Umwandeln', self)
        pybuttonl.clicked.connect(self.clickMethodl)
        pybuttonl.resize(200,32)
        pybuttonl.move(120, 350)        

        self.nameLabelru = QLabel(self)
        self.nameLabelru.setText('Fragescreen')
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Etage:')
        self.nameLabel1 = QLabel(self)
        self.nameLabel1.setText('Frage: ')
        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('Antwort 1: ')
        self.nameLabel3 = QLabel(self)
        self.nameLabel3.setText('Antwort 2: ')
        self.nameLabel4 = QLabel(self)
        self.nameLabel4.setText('Antwort 3: ')
        self.nameLabel5 = QLabel(self)
        self.nameLabel5.setText('Antwort 4: ')
        self.nameLabel6 = QLabel(self)
        self.nameLabel6.setText('Hash: ')

        self.liner = QLineEdit(self)
        self.liner1 = QLineEdit(self)
        self.liner2 = QLineEdit(self)
        self.liner3 = QLineEdit(self)
        self.liner4 = QLineEdit(self)
        self.liner5 = QLineEdit(self)
        self.liner6 = QLineEdit(self)


        self.liner.move(700, 150)
        self.liner1.move(700, 200)
        self.liner2.move(700, 250)
        self.liner3.move(700, 300)
        self.liner4.move(700, 350)
        self.liner5.move(700, 400)
        self.liner6.move(700, 450)

        

        self.liner.resize(200, 32)
        self.liner1.resize(200, 32)
        self.liner2.resize(200, 32)
        self.liner3.resize(200, 32)
        self.liner4.resize(200, 32)
        self.liner5.resize(200, 32)
        self.liner6.resize(200, 32)
        
        
        self.nameLabelru.move(700, 100)
        self.nameLabel.move(630, 150)
        self.nameLabel1.move(630, 200)
        self.nameLabel2.move(630, 250)
        self.nameLabel3.move(630, 300)
        self.nameLabel4.move(630, 350)
        self.nameLabel5.move(630, 400)
        self.nameLabel6.move(630, 450)
        self.nameLabelinfo.move(120, 50)
        self.nameLabelinfo.resize(1000,32)


        self.CheckBox1 = QCheckBox(self)
        self.CheckBox1.move(915, 250)
        self.CheckBox2 = QCheckBox(self)
        self.CheckBox2.move(915, 300)
        self.CheckBox3 = QCheckBox(self)
        self.CheckBox3.move(915, 350)
        self.CheckBox4 = QCheckBox(self)
        self.CheckBox4.move(915, 400)

        pybuttonr = QPushButton('Umwandeln', self)
        pybuttonr.clicked.connect(self.clickMethodr)
        pybuttonr.resize(200,32)
        pybuttonr.move(700, 500)  
        
    def clickMethodl(self):
        Etagel = self.linel.text()
        Ueberschriftl = self.linel1.text()
        Textl = self.linel2.text()
        Hashl = self.linel3.text()
        self.InfoTag = [Etagel, Ueberschriftl,Textl,Hashl]
        print(self.InfoTag)
        data = yamlhandling.dataGeneratorInfo(ar1 = self.InfoTag)
        yamlhandling.yamlAdd(data, self.InfoTag)
    
    def clickMethodr(self):
        Etager = self.liner.text()
        Frager = self.liner1.text()
        Antwort1r = self.liner2.text()
        Antwort2r = self.liner3.text()
        Antwort3r = self.liner4.text()
        Antwort4r = self.liner5.text()
        a1atf = self.CheckBox1.isChecked()
        a2atf = self.CheckBox2.isChecked()
        a3atf = self.CheckBox3.isChecked()
        a4atf = self.CheckBox4.isChecked()
        Hashr = self.liner6.text()
        self.QuestionTag = [Etager,Frager,Antwort1r,a1atf,Antwort2r,a2atf,Antwort3r,a3atf,Antwort4r,a4atf,Hashr]
        print(self.QuestionTag)
        data = yamlhandling.dataGeneratorFrage(self.QuestionTag)
        yamlhandling.yamlAdd(data, self.QuestionTag)
        
class yamlhandling: 
    ar1 = MainWindow.InfoTag
    ar2 = MainWindow.QuestionTag

    def dataGeneratorInfo(ar1):
        data = f"""
        - type: information
            headline: {ar1[1]}
            text: {ar1[2]}
            hash: {ar1[3]}
        """
        return data
    
    def dataGeneratorFrage(ar2):
        data = f"""
        - type: question
            frage: {ar2[1]}
                allanswers:
                - answer: {ar2[2]}
                    trueanswer: {ar2[3]}
                - answer: {ar2[4]}
                    trueanswer: {ar2[5]}
                - answer: {ar2[6]}
                    trueanswer: {ar2[7]}
                - answer: {ar2[8]}
                    trueanswer: {ar2[9]}
            hash: {ar2[10]}
        """
        return data


    def yamlAdd(dataInsert, x):
        Hash = x[len(x)-1] 
        img = qrcode.make(Hash)
        img.save("{}.png".format(Hash), "PNG")
        with open('auto.txt', mode='r') as file:
            data = file.read()
            
        with open('auto.txt', mode='w') as file:
            dataNew= data + dataInsert
            file.write(dataNew)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )

