import sys
import os
import threading
import time
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QHBoxLayout, QDateTimeEdit, QPushButton, QMessageBox
from PyQt5.QtCore import QDateTime
from plyer import notification


# Окно с уведомлением
class NotificationDialog(QDialog):
    def __init__(self, parent=None):
        super(NotificationDialog, self).__init__(parent)
        self.setWindowTitle("Уведомление")
        self.resize(300, 150)
        layout = QVBoxLayout(self)

        self.dateTimeEdit = QDateTimeEdit(self)
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.dateTimeEdit)

        buttonBox = QHBoxLayout()
        self.setButton = QPushButton("Задать", self)
        self.setButton.clicked.connect(self.accept)
        buttonBox.addWidget(self.setButton)

        layout.addLayout(buttonBox)

    def getDateTime(self):
        return self.dateTimeEdit.dateTime()


# Главное окно с заметками
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 640)
        font_path = "./fonts/DaysOne-Regular.ttf"
        if os.path.exists(font_path):
            QtGui.QFontDatabase.addApplicationFont(font_path)
            font = QtGui.QFont("Days One", 8)
        else:
            print(f"Font file {font_path} not found")
            font = QtGui.QFont("Arial", 8)  # Fallback to a default font

        font = QtGui.QFont("Days One", 8)
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
        font = QtGui.QFont("Arial", 20)
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
        self.frame_notice = QtWidgets.QFrame(self.frame_2)
        self.frame_notice.setGeometry(QtCore.QRect(170, 90, 600, 380))
        self.frame_notice.setStyleSheet("\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.5, y1:1,"
                                        "x2:0.5, y2:0, stop:0 rgba(255, 255, 255, 0.7),"
                                        " stop:0.810945 rgba(255, 255, 255, 0.8),"
                                        " stop:0.825871 rgba(146, 255, 216, 1));")
        self.frame_notice.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_notice.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_notice.setObjectName("frame_notice")
        self.frame_notice.setVisible(False)
        self.label_notice = QtWidgets.QLabel(self.frame_notice)
        self.label_notice.setEnabled(True)
        self.label_notice.setGeometry(QtCore.QRect(135, 0, 400, 60))
        font = QtGui.QFont("Days One", 20)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_notice.setFont(font)
        self.label_notice.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_notice.setMouseTracking(True)
        self.label_notice.setTabletTracking(False)
        self.label_notice.setAcceptDrops(False)
        self.label_notice.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
                                        "color: rgba(25, 108, 93, 1);")
        self.label_notice.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_notice.setTextFormat(QtCore.Qt.AutoText)
        self.label_notice.setScaledContents(False)
        self.label_notice.setObjectName("label_notice")
        self.button_cencel_2 = QtWidgets.QPushButton(self.frame_notice)
        self.button_cencel_2.setGeometry(QtCore.QRect(300, 320, 130, 40))
        font = QtGui.QFont("Days One", 12)
        self.button_cencel_2.setFont(font)
        self.button_cencel_2.setStyleSheet("background-color: rgba(167, 212, 255, 1);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "border-radius: 10px;")
        self.button_cencel_2.setObjectName("button_cencel_2")
        self.button_cencel_2.clicked.connect(self.hide_frame)
        self.button_del_2 = QtWidgets.QPushButton(self.frame_notice)
        self.button_del_2.setGeometry(QtCore.QRect(460, 320, 130, 40))
        font = QtGui.QFont("Days One", 12)
        self.button_del_2.setFont(font)
        self.button_del_2.setStyleSheet("background-color: rgba(105, 255, 201, 1);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px;")
        self.button_del_2.setObjectName("button_del_2")
        self.notice_week = QtWidgets.QCheckBox(self.frame_notice)
        self.notice_week.setGeometry(QtCore.QRect(30, 300, 260, 60))
        font = QtGui.QFont("Days One", 15)
        self.notice_week.setFont(font)
        self.notice_week.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.notice_week.setObjectName("notice_week")
        self.notice_day = QtWidgets.QCheckBox(self.frame_notice)
        self.notice_day.setGeometry(QtCore.QRect(30, 240, 270, 40))
        font = QtGui.QFont("Days One", 15)
        self.notice_day.setFont(font)
        self.notice_day.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                      "\n"
                                      "color: rgb(0, 0, 0);")
        self.notice_day.setObjectName("notice_day")
        self.notice_year = QtWidgets.QCheckBox(self.frame_notice)
        self.notice_year.setGeometry(QtCore.QRect(300, 225, 280, 70))
        font = QtGui.QFont("Days One", 15)
        self.notice_year.setFont(font)
        self.notice_year.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.notice_year.setObjectName("notice_year")
        self.textEdit_day = QtWidgets.QTextEdit(self.frame_notice)
        self.textEdit_day.setGeometry(QtCore.QRect(130, 80, 290, 40))
        font = QtGui.QFont("Days One", 14)
        self.textEdit_day.setFont(font)
        self.textEdit_day.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(225, 225, 225, 1), "
            "stop:1 rgba(249, 249, 249, 1));")
        self.textEdit_day.setObjectName("textEdit_day")
        self.textEdit_month = QtWidgets.QTextEdit(self.frame_notice)
        self.textEdit_month.setGeometry(QtCore.QRect(130, 130, 290, 40))
        font = QtGui.QFont("Days One", 14)
        self.textEdit_month.setFont(font)
        self.textEdit_month.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(225, 225, 225, 1), "
            "stop:1 rgba(249, 249, 249, 1));")
        self.textEdit_month.setObjectName("textEdit_month")
        self.textEdit_year = QtWidgets.QTextEdit(self.frame_notice)
        self.textEdit_year.setGeometry(QtCore.QRect(130, 180, 290, 40))
        font = QtGui.QFont("Days One", 14)
        self.textEdit_year.setFont(font)
        self.textEdit_year.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(225, 225, 225, 1), "
            "stop:1 rgba(249, 249, 249, 1));")
        self.textEdit_year.setObjectName("textEdit_year")
        self.label_day = QtWidgets.QLabel(self.frame_notice)
        self.label_day.setGeometry(QtCore.QRect(30, 80, 90, 40))
        font = QtGui.QFont("Days One", 20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_day.setFont(font)
        self.label_day.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
                                     "color: rgba(88, 203, 182, 1);")
        self.label_day.setObjectName("label_day")
        self.label_month = QtWidgets.QLabel(self.frame_notice)
        self.label_month.setGeometry(QtCore.QRect(30, 130, 101, 40))
        font = QtGui.QFont("Days One", 20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_month.setFont(font)
        self.label_month.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
                                       "color: rgba(88, 203, 182, 1);")
        self.label_month.setObjectName("label_month")
        self.label_year = QtWidgets.QLabel(self.frame_notice)
        self.label_year.setGeometry(QtCore.QRect(30, 180, 71, 40))
        font = QtGui.QFont("Days One", 20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_year.setFont(font)
        self.label_year.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
                                      "color: rgba(88, 203, 182, 1);")
        self.label_year.setObjectName("label_year")
        self.timeEdit = QtWidgets.QTimeEdit(self.frame_notice)
        self.timeEdit.setGeometry(QtCore.QRect(430, 130, 161, 41))
        font = QtGui.QFont("Days One", 12)
        self.timeEdit.setFont(font)
        self.timeEdit.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(225, 225, 225, 1), stop:1 rgba(249, 249, 249, 1));")
        self.timeEdit.setObjectName("timeEdit")
        self.label_team = QtWidgets.QLabel(self.frame_notice)
        self.label_team.setGeometry(QtCore.QRect(430, 80, 101, 40))
        font = QtGui.QFont("Days One", 20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_team.setFont(font)
        self.label_team.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
                                      "color: rgba(88, 203, 182, 1);")
        self.label_team.setObjectName("label_year_2")
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
        font = QtGui.QFont("Days One", 16)
        self.textHeading.setFont(font)
        self.textHeading.setStyleSheet("border-radius: 6px;")
        self.textHeading.setObjectName("textHeading")
        self.textContent = QtWidgets.QTextEdit(self.frame_3)
        self.textContent.setGeometry(QtCore.QRect(380, 120, 531, 411))
        font = QtGui.QFont("Days One", 14)
        self.textContent.setFont(font)
        self.textContent.setStyleSheet("border-radius: 6px;")
        self.textContent.setObjectName("textContent")
        self.saveButton = QtWidgets.QPushButton(self.frame_3)
        self.saveButton.setGeometry(QtCore.QRect(775, 495, 131, 28))
        font = QtGui.QFont("Days One", 9)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet("color: rgb(0, 0, 0);\n"
                                      "border-radius: 9px;\n"
                                      "background-color: rgb(182, 219, 255);")
        self.saveButton.setObjectName("saveButton")
        self.createButton = QtWidgets.QPushButton(self.frame_3)
        self.createButton.setGeometry(QtCore.QRect(5, 5, 361, 51))
        font = QtGui.QFont("Days One", 12)
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
        self.deleteButton.setGeometry(QtCore.QRect(10, 495, 351, 33))
        font = QtGui.QFont("Days One", 9)
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
        self.load_notes()

        # Notification button setup
        self.notificationButton = QtWidgets.QPushButton(self.frame_3)
        self.notificationButton.setGeometry(QtCore.QRect(490, 15, 351, 33))
        font = QtGui.QFont("Days One", 9)
        self.notificationButton.setFont(font)
        self.notificationButton.setStyleSheet("background-color: rgb(0, 255, 127);\n"
                                              "border-radius: 9px;")
        self.notificationButton.setObjectName("notificationButton")
        self.notificationButton.setText("Уведомление")
        self.notificationButton.clicked.connect(self.toggle_frame)
        #self.notificationButton.clicked.connect(self.show_notification_dialog)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Заметки"))
        self.label.setText(_translate("MainWindow", "To-Do Reminder"))
        self.saveButton.setText(_translate("MainWindow", "Сохранить"))
        self.createButton.setText(_translate("MainWindow", "Создать новую заметку"))
        self.label_notice.setText(_translate("MainWindow", "Настройка о напоминании"))
        self.button_cencel_2.setText(_translate("MainWindow", "Отменить"))
        self.button_del_2.setText(_translate("MainWindow", "Удалить"))
        self.notice_week.setText(_translate("MainWindow", "Уведомить за \nнеделю"))
        self.notice_day.setText(_translate("MainWindow", "Уведомить за 3 дня"))
        self.notice_year.setText(_translate("MainWindow", "Повторять каждый \nгод"))
        self.label_day.setText(_translate("MainWindow", "День"))
        self.label_month.setText(_translate("MainWindow", "Месяц"))
        self.label_year.setText(_translate("MainWindow", "Год"))
        self.timeEdit.setWhatsThis(_translate("MainWindow", ""))
        self.label_team.setText(_translate("MainWindow", "Время"))


    def clear_fields(self):
        self.textHeading.clear()
        self.textContent.clear()
        self.savedNotesList.clearSelection()

    def save_note(self):
        title = self.textHeading.toPlainText()
        content = self.textContent.toPlainText()
        if title:
            notes = self.load_notes_json()
            notes.append({"title": title, "content": content})
            with open("notes.json", "w") as file:
                json.dump(notes, file, indent=4)
            self.load_notes()

    def load_notes_json(self):
        if not os.path.exists("notes.json"):
            return []
        with open("notes.json", "r") as file:
            return json.load(file)

    def load_notes(self):
        self.savedNotesList.clear()
        notes = self.load_notes_json()
        for note in notes:
            self.savedNotesList.addItem(note["title"])

    def load_note(self, item):
        title = item.text()
        notes = self.load_notes_json()
        for note in notes:
            if note["title"] == title:
                self.textHeading.setText(note["title"])
                self.textContent.setText(note["content"])
                break

    def delete_note(self):
        selected_items = self.savedNotesList.selectedItems()
        if not selected_items:
            return
        selected_item = selected_items[0]
        title_to_delete = selected_item.text()
        notes = self.load_notes_json()
        updated_notes = [note for note in notes]
        updated_notes = [note for note in notes if note["title"] != title_to_delete]
        with open("notes.json", "w") as file:
            json.dump(updated_notes, file, indent=4)
        self.load_notes()
        self.clear_fields()

    def show_notification_dialog(self):
        dialog = NotificationDialog()
        if dialog.exec_() == QDialog.Accepted:
            selected_date_time = dialog.getDateTime().toPyDateTime()
            note_title = self.textHeading.toPlainText()
            note_content = self.textContent.toPlainText()
            if note_title:
                reminders = self.load_reminders_json()
                reminders.append(
                    {"datetime": selected_date_time.isoformat(), "title": note_title, "content": note_content})
                with open("reminders.json", "w") as file:
                    json.dump(reminders, file, indent=4)
                self.schedule_notification(selected_date_time, note_title)

    def load_reminders_json(self):
        if not os.path.exists("reminders.json"):
            return []
        with open("reminders.json", "r") as file:
            return json.load(file)

    def schedule_notification(self, notification_time, note_title):
        def notification_worker():
            while True:
                current_time = time.localtime()
                if current_time >= notification_time.timetuple():
                    notification.notify(
                        title="Напоминание",
                        message=note_title,
                        app_name="Заметки"
                    )
                    break
                time.sleep(10)

        threading.Thread(target=notification_worker, daemon=True).start()

    def toggle_frame(self):
        if not self.frame_notice.isVisible():
            self.notificationButton.setEnabled(False)
        else:
            self.notificationButton.setEnabled(True)
        self.frame_notice.setVisible(not self.frame_notice.isVisible())

    def hide_frame(self):
        self.frame_notice.setVisible(False)
        self.notificationButton.setEnabled(True)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Check if the file exists and create it if not
    if not os.path.exists("notes.json"):
        with open("notes.json", "w") as file:
            json.dump([], file)

    # Check if the file exists and create it if not
    if not os.path.exists("reminders.json"):
        with open("reminders.json", "w") as file:
            json.dump([], file)

    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
