import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Ваши заметки")
        MainWindow.resize(960, 640)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(212, 234, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CompanyField = QtWidgets.QFrame(self.centralwidget)
        self.CompanyField.setGeometry(QtCore.QRect(10, 10, 941, 51))
        self.CompanyField.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 13px;")
        self.CompanyField.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CompanyField.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CompanyField.setObjectName("CompanyField")
        self.label = QtWidgets.QLabel(self.CompanyField)
        self.label.setGeometry(QtCore.QRect(640, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(70, 211, 185);\n"
                                 "background-color: rgb(255, 255, 255);\n"
                                 "color: rgb(70, 211, 185);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.CompanyField)
        self.label_2.setGeometry(QtCore.QRect(890, 0, 41, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Logo (1).png"))
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 70, 941, 561))
        self.frame_2.setStyleSheet("background-color: rgb(158, 208, 255);\n"
                                   "border-radius: 20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 921, 541))
        self.frame_3.setStyleSheet("background-color:rgba(255, 255, 255, 0.6);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setGeometry(QtCore.QRect(0, 60, 921, 4))
        self.line.setStyleSheet("background-color:rgba(158, 208, 255, 0.59);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame_3)
        self.line_2.setGeometry(QtCore.QRect(370, 0, 4, 551))
        self.line_2.setStyleSheet("background-color: rgba(158, 208, 255, 0.59);")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textHeading = QtWidgets.QTextEdit(self.frame_3)
        self.textHeading.setGeometry(QtCore.QRect(380, 70, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Days One")
        font.setPointSize(16)
        self.textHeading.setFont(font)
        self.textHeading.setStyleSheet("border-radius: 6px;")
        self.textHeading.setObjectName("textHeading")
        self.textContent = QtWidgets.QTextEdit(self.frame_3)
        self.textContent.setGeometry(QtCore.QRect(380, 120, 531, 411))
        font = QtGui.QFont()
        font.setFamily("Days One")
        font.setPointSize(14)
        self.textContent.setFont(font)
        self.textContent.setStyleSheet("border-radius: 6px;")
        self.textContent.setObjectName("textContent")
        self.saveButton = QtWidgets.QPushButton(self.frame_3)
        self.saveButton.setGeometry(QtCore.QRect(775, 495, 131, 28))
        font = QtGui.QFont()
        font.setFamily("Days One")
        font.setPointSize(8)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet("color: rgb(0, 0, 0);\n"
                                      "border-radius: 9px;\n"
                                      "background-color: rgb(182, 219, 255);")
        self.saveButton.setObjectName("saveButton")
        self.createButton = QtWidgets.QPushButton(self.frame_3)
        self.createButton.setGeometry(QtCore.QRect(5, 5, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Days One")
        font.setPointSize(10)
        self.createButton.setFont(font)
        self.createButton.setStyleSheet("color: rgb(115, 150, 217);\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 13px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("+.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.createButton.setIcon(icon)
        self.createButton.setCheckable(False)
        self.createButton.setAutoRepeat(False)
        self.createButton.setAutoExclusive(False)
        self.createButton.setAutoRepeatDelay(300)
        self.createButton.setObjectName("createButton")

        # Adding QListWidget
        # Adding QListWidget for saved notes
        self.savedNotesList = QtWidgets.QListWidget(self.frame_3)
        self.savedNotesList.setGeometry(QtCore.QRect(10, 70, 351, 415))
        self.savedNotesList.setObjectName("savedNotesList")

        # Adding Delete button
        self.deleteButton = QtWidgets.QPushButton(self.frame_3)
        self.deleteButton.setGeometry(QtCore.QRect(10, 495 , 351, 33))
        font = QtGui.QFont()
        font.setFamily("Days One")
        font.setPointSize(9)
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "border-radius: 9px;\n"
                                        "background-color: rgb(255, 71, 87);")
        self.deleteButton.setObjectName("deleteButton")
        self.deleteButton.setText("Удалить")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the create button to clear input fields
        self.createButton.clicked.connect(self.clear_fields)

        # Connect the save button to the save_note method
        self.saveButton.clicked.connect(self.save_note)

        # Connect the QListWidget item click signal to load_note method
        self.savedNotesList.itemClicked.connect(self.load_note)

        # Connect the Delete button to the delete_note method
        self.deleteButton.clicked.connect(self.delete_note)

        # Load saved notes on startup
        # Load saved notes on startup
        self.load_notes()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "To-Do Reminder"))
        self.textHeading.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.textContent.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.saveButton.setText(_translate("MainWindow", "Сохранить"))
        self.createButton.setText(_translate("MainWindow", "   Создать новую заметку"))

    def clear_fields(self):
        self.textHeading.clear()
        self.textContent.clear()
        # Deselect the currently selected item in the saved notes list
        self.savedNotesList.setCurrentItem(None)

    def save_note(self):
        heading = self.textHeading.toPlainText().strip()
        content = self.textContent.toPlainText().strip()
        if heading and content:
            current_item = self.savedNotesList.currentItem()
            if current_item:
                # Update existing note
                self.update_note_file(current_item.text(), heading, content)
                current_item.setText(heading)
            else:
                # Save new note
                with open("notes.txt", "a", encoding="utf-8") as file:
                    file.write(f"{heading}\n{content}\n---\n")
                self.savedNotesList.addItem(heading)
            self.textHeading.clear()
            self.textContent.clear()

    def load_notes(self):
        try:
            with open("notes.txt", "r", encoding="utf-8") as file:
                notes = file.read().split('---\n')
                for note in notes:
                    if note.strip():
                        heading = note.split('\n')[0]
                        self.savedNotesList.addItem(heading)
        except FileNotFoundError:
            pass

    def load_note(self, item):
        heading = item.text()
        with open("notes.txt", "r", encoding="utf-8") as file:
            notes = file.read().split('---\n')
            for note in notes:
                if note.startswith(heading):
                    content = '\n'.join(note.split('\n')[1:])
                    self.textHeading.setPlainText(heading)
                    self.textContent.setPlainText(content)
                    break

    def delete_note(self):
        current_item = self.savedNotesList.currentItem()
        if current_item:
            heading = current_item.text()
            self.savedNotesList.takeItem(self.savedNotesList.row(current_item))
            self.delete_note_from_file(heading)
            self.textHeading.clear()
            self.textContent.clear()

    def update_note_file(self, old_heading, new_heading, new_content):
        with open("notes.txt", "r", encoding="utf-8") as file:
            notes = file.read().split('---\n')
        with open("notes.txt", "w", encoding="utf-8") as file:
            for note in notes:
                if note.startswith(old_heading):
                    file.write(f"{new_heading}\n{new_content}\n---\n")
                else:
                    file.write(note + '---\n')

    def delete_note_from_file(self, heading):
        with open("notes.txt", "r", encoding="utf-8") as file:
            notes = file.read().split('---\n')
        with open("notes.txt", "w", encoding="utf-8") as file:
            for note in notes:
                if not note.startswith(heading):
                    file.write(note + '---\n')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
