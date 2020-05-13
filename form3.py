from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from tkinter.messagebox import showinfo



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setWindowIcon(QtGui.QIcon('icon.png'))
        Form.setObjectName("Form")
        Form.resize(812, 479)
        Form.setStyleSheet("#Form\n"
"{\n"
"background-image:url(C:/Users/Python/Desktop/New folder (2)/bg.jpg);\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, -1, 821, 481))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"background-color:white;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"border-radius:10px;\n"
"border:1px solid black;\n"
"\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(480, 0, 350, 490))
        self.frame_2.setStyleSheet("QFrame\n"
"{\n"
"background-color:#5845b0;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(110, 120, 141, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"background-color:transparent;\n"
"color:white;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(110, 140, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"background-color:transparent;\n"
"color:white;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(80, 20, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"background-color:transparent;\n"
"color:white;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(110, 170, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{\n"
"background-color:transparent;\n"
"color:white;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 10, 260, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"color:#5845b0;\n"
"}")
        self.label.setObjectName("label")
        self.pushButton_facebook = QtWidgets.QPushButton(self.frame)
        self.pushButton_facebook.setGeometry(QtCore.QRect(120, 80, 40, 40))
        self.pushButton_facebook.setStyleSheet("QPushButton{\n"
"image: url(:/newPrefix/fb.png);\n"
"border-radius:10px;\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_facebook.setText("")
        self.pushButton_facebook.setObjectName("pushButton_facebook")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(160, 130, 170, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"color:#5845b0;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"color:black;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.lineEditusername = QtWidgets.QLineEdit(self.frame)
        self.lineEditusername.setGeometry(QtCore.QRect(120, 200, 250, 30))
        self.lineEditusername.setPlaceholderText("Username") 
        self.lineEditusername.setObjectName("lineEditusername")
        self.lineEdit_2_passwd = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2_passwd.setGeometry(QtCore.QRect(120, 260, 250, 30))
        self.lineEdit_2_passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2_passwd.setObjectName("lineEdit_2_passwd")
        self.lineEdit_2_passwd.setPlaceholderText("Password") 
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(140, 420, 160, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"color:#5845b0;\n"
"}\n"
"\n"
"QLabel:hover\n"
"{\n"
"color:black;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.pushButtonsignin = QtWidgets.QPushButton(self.frame)
        self.pushButtonsignin.setGeometry(QtCore.QRect(160, 360, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonsignin.setFont(font)
        self.pushButtonsignin.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"background-color:#5845b0;\n"
"border:2px solid white;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"background-color:white;\n"
"border:1px solid black;\n"
"\n"
"}")
        self.pushButtonsignin.setObjectName("pushButtonsignin")
        self.pushButtonsignup = QtWidgets.QPushButton(self.frame)
        self.pushButtonsignup.setGeometry(QtCore.QRect(600, 250, 110, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonsignup.setFont(font)
        self.pushButtonsignup.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"background-color:#5845b0;\n"
"border:2px solid white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"background-color:white;\n"
"border:1px solid black;\n"
"\n"
"}")
        self.pushButtonsignup.setObjectName("pushButtonsignup")
        self.pushButton_insta = QtWidgets.QPushButton(self.frame)
        self.pushButton_insta.setGeometry(QtCore.QRect(210, 80, 40, 40))
        self.pushButton_insta.setStyleSheet("QPushButton{\n"
"image: url(:/newPrefix/instadd.png);\n"
"border-radius:10px;\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_insta.setText("")
        self.pushButton_insta.setObjectName("pushButton_insta")
        self.pushButton_youtube = QtWidgets.QPushButton(self.frame)
        self.pushButton_youtube.setGeometry(QtCore.QRect(300, 80, 40, 40))
        self.pushButton_youtube.setStyleSheet("QPushButton{\n"
"image: url(:/newPrefix/yo.png);\n"
"border-radius:10px;\n"
"background-color:transparent;\n"
"\n"
"}")
        self.pushButton_youtube.setText("")
        self.pushButton_youtube.setObjectName("pushButton_youtube")
        self.pushButtonsignin.clicked.connect(self.show1)
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(150, 310, 190, 18))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        
       
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

       

    
    def show1(self):
        showinfo("LogIn","You Are Successfully Login" )

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
       
        self.label_5.setText(_translate("Form", "Enter Your  Details And"))
        self.label_6.setText(_translate("Form", "Start Amazing Journe"))
        self.label_4.setText(_translate("Form", "Hello Friend!!"))
        self.label_7.setText(_translate("Form", " With Us."))
        self.label.setText(_translate("Form", "Sign In To Cyber World"))
        self.label_2.setText(_translate("Form", "Or Use Email Account"))
        self.label_3.setText(_translate("Form", "Forget Your Password"))
        self.pushButtonsignin.setText(_translate("Form", "Sign In"))
        self.pushButtonsignup.setText(_translate("Form", "Sign Up"))
        self.checkBox.setText(_translate("Form", "Remeber Password"))
        
        

        
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
