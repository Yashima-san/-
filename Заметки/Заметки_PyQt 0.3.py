import sys
import os
import threading
import time
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QDateTimeEdit, QFrame
from PyQt5.QtCore import QDateTime, Qt
from plyer import notification


class NotificationDialog(QDialog):
    def __init__(self, parent=None):
        super(NotificationDialog, self).__init__(parent)
        self.setWindowTitle("Уведомление")
        self.resize(300, 120)

        # Установить флаг для удаления верхней части окна
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.setStyleSheet("background-color: rgb(212, 234, 255);")  # Set the background color

        # Create and style the outer frame
        self.outerFrame = QFrame(self)
        self.outerFrame.setGeometry(QtCore.QRect(10, 10, 280, 100))
        self.outerFrame.setStyleSheet("background-color: rgb(158, 208, 255);"
                                      "border-radius: 10px;")

        # Create and style the inner frame
        self.innerFrame = QFrame(self.outerFrame)
        self.innerFrame.setGeometry(QtCore.QRect(10, 10, 260, 80))
        self.innerFrame.setStyleSheet("background-color: rgba(255, 255, 255, 0.6);"
                                      "border-radius: 10px;")

        # Create the dateTimeEdit and set its style
        self.dateTimeEdit = QDateTimeEdit(self.innerFrame)
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.dateTimeEdit.setGeometry(QtCore.QRect(10, 15, 240, 30))
        self.dateTimeEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1,"
                                        " stop:0 rgba(225, 225, 225, 1), stop:1 rgba(249, 249, 249, 1));"
                                        "border-radius: 12px;")

        # Create the setButton and set its style
        self.setButton = QtWidgets.QPushButton(self.innerFrame)
        self.setButton.setGeometry(QtCore.QRect(175, 55, 80, 20))
        self.setButton.setText("задать")
        font = QtGui.QFont("Days One", 12)
        self.setButton.setFont(font)
        self.setButton.setStyleSheet("background-color: rgba(105, 255, 201, 1);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-radius: 10px;")
        self.setButton.clicked.connect(self.accept)

        # Create the cancelButton and set its style
        self.cancelButton = QtWidgets.QPushButton(self.innerFrame)
        self.cancelButton.setGeometry(QtCore.QRect(85, 55, 80, 20))
        self.cancelButton.setText("отмена")
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("background-color: rgba(255, 0, 0, 1);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px;")
        self.cancelButton.clicked.connect(self.reject)

    def getDateTime(self):
        return self.dateTimeEdit.dateTime()


def schedule_notification(notification_time, note_title):
    def notification_worker():
        while True:
            current_time = time.localtime()

            # Корректное сравнение времени
            if time.mktime(current_time) >= time.mktime(notification_time.timetuple()):
                notification.notify(
                    title="Напоминание",
                    message=note_title,
                    app_name="Заметки"
                )
                break
            time.sleep(10)

    threading.Thread(target=notification_worker, daemon=True).start()


def load_reminders_json():
    if not os.path.exists("reminders.json"):
        return []
    with open("reminders.json", "r") as file:
        return json.load(file)


def load_notes_json():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as fail:
            notes = json.load(fail)
        return notes
    else:
        return []


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 640)

        # Set window icon
        icon_path = "icon.png"
        if os.path.exists(icon_path):
            icon = QtGui.QIcon(icon_path)
            MainWindow.setWindowIcon(icon)
        else:
            print(f"Icon file {icon_path} not found")

        font_path = "./fonts/DaysOne-Regular.ttf"
        if os.path.exists(font_path):
            QtGui.QFontDatabase.addApplicationFont(font_path)
            font = QtGui.QFont("Days One", 8)
        else:
            print(f"Font file {font_path} not found")
            font = QtGui.QFont("Arial", 8)

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
        self.label.setGeometry(QtCore.QRect(630, 10, 311, 31))
        font = QtGui.QFont("Arial", 25)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(70, 211, 185);\n"
                                 "background-color: rgb(255, 255, 255);\n"
                                 "color: rgb(70, 211, 185);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.CompanyField)
        self.label_2.setGeometry(QtCore.QRect(890, 0, 41, 51))
        self.label_2.setPixmap(QtGui.QPixmap("Logo.png"))
        self.label_2.setObjectName("label_2")
        self.guideButton = QtWidgets.QPushButton(self.centralwidget)
        self.guideButton.setGeometry(QtCore.QRect(30, 20, 31, 31))
        icon = QtGui.QIcon("guide.png")
        self.guideButton.setIcon(icon)
        self.guideButton.setStyleSheet("background-color: rgb(255, 255, 255);border-radius: 20px")
        self.guideButton.setObjectName("guideButton")
        self.guideButton.clicked.connect(self.guide_frame)
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
        font = QtGui.QFont("Days One", 12)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet("color: rgb(0, 0, 0);\n"
                                      "border-radius: 9px;\n"
                                      "background-color: rgb(182, 219, 255);")
        self.saveButton.setObjectName("saveButton")
        self.createButton = QtWidgets.QPushButton(self.frame_3)
        self.createButton.setGeometry(QtCore.QRect(5, 5, 361, 51))
        font = QtGui.QFont("Days One", 16)
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
        self.savedNotesList.setFont(QtGui.QFont("Days One", 14))
        self.savedNotesList.itemClicked.connect(self.load_note_for_editing)

        # Adding Delete button
        self.deleteButton = QtWidgets.QPushButton(self.frame_3)
        self.deleteButton.setGeometry(QtCore.QRect(10, 495, 351, 33))
        font = QtGui.QFont("Days One", 15)
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
        self.notificationButton.setGeometry(QtCore.QRect(860, 5, 51, 51))
        font = QtGui.QFont("Days One", 9)
        self.notificationButton.setFont(font)
        self.notificationButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "border-radius: 13px;")
        self.notificationButton.setObjectName("notificationButton")
        self.notificationButton.setIcon(QtGui.QIcon("Uvedoml.png"))
        self.notificationButton.clicked.connect(self.show_notification_dialog)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To-Do Reminder"))
        self.label.setText(_translate("MainWindow", "To-Do Reminder"))
        self.saveButton.setText(_translate("MainWindow", "Сохранить"))
        self.createButton.setText(_translate("MainWindow", "Создать новую заметку"))

    def clear_fields(self):
        self.textHeading.clear()
        self.textContent.clear()
        self.savedNotesList.clearSelection()

    def save_note(self):
        title = self.textHeading.toPlainText()
        content = self.textContent.toPlainText()
        if title:
            notes = load_notes_json()
            existing_note = None
            for note in notes:
                if note["title"] == title:
                    existing_note = note
                    break
            if existing_note:
                # Обновление существующей заметки
                existing_note["content"] = content
            else:
                # Создание новой заметки, если заметка с таким заголовком не найдена
                notes.append({"title": title, "content": content})
            with open("notes.json", "w") as fail:
                json.dump(notes, fail, indent=4)
            self.load_notes()

    def load_note_for_editing(self, item):
        title = item.text()
        notes = load_notes_json()
        for note in notes:
            if note["title"] == title:
                self.textHeading.setText(note["title"])
                self.textContent.setText(note["content"])
                break

    def load_notes(self):
        self.savedNotesList.clear()
        notes = load_notes_json()
        for note in notes:
            self.savedNotesList.addItem(note["title"])

    def load_note(self, item):
        title = item.text()
        notes = load_notes_json()
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
        notes = load_notes_json()
        updated_notes = [note for note in notes]
        updated_notes = [note for note in notes if note["title"] != title_to_delete]
        with open("notes.json", "w") as fail:
            json.dump(updated_notes, fail, indent=4)
        self.load_notes()
        self.clear_fields()

    def show_notification_dialog(self):
        dialog = NotificationDialog()
        if dialog.exec_() == QDialog.Accepted:
            selected_date_time = dialog.getDateTime().toPyDateTime()
            note_title = self.textHeading.toPlainText()
            note_content = self.textContent.toPlainText()
            if note_title:
                reminders = load_reminders_json()
                reminders.append(
                    {"datetime": selected_date_time.isoformat(), "title": note_title, "content": note_content})
                with open("reminders.json", "w") as fail:
                    json.dump(reminders, fail, indent=4)
                schedule_notification(selected_date_time, note_title)

    def guide_frame(self):
        # Создание и отображение фрейма
        self.additionalFrame = QtWidgets.QFrame(self.centralwidget)
        self.additionalFrame.setGeometry(QtCore.QRect(100, 10, 770, 600))
        self.additionalFrame.setStyleSheet("background-color: rgba(158, 208, 255, 0.7);")

        scroll_area = QtWidgets.QScrollArea(self.additionalFrame)
        scroll_area.setGeometry(QtCore.QRect(0, 0, 770, 600))  # Размер и положение виджета со скроллом
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        # Создание виджета для отображения текста
        self.textLabel = QtWidgets.QLabel(self.additionalFrame)
        self.textLabel.setGeometry(QtCore.QRect(0, 0, 750, 2000))  # Размер и положение текста внутри фрейма
        font = QtGui.QFont("Days One", 10)
        self.textLabel.setFont(font)
        self.textLabel.setText("<html>"
                               "<body>"
                               "<div align='center'>"
                               "<h1>To-Do Reminder: Ваше руководство по использованию</h1>"
                               "<p><i>Это бета-версия приложения! Так что возможны некоторые ошибки!</i></p>"
                               "<br>"
                               "<p>Добро пожаловать в To-Do Reminder!</p>"
                               "<p>Это приложение поможет вам организовать свои задачи и не забыть о важных делах.</p>"
                               "<p>Помните, что приложение находится на стадии бета-тестирования, поэтому возможны некоторые ошибки. "
                               "Если вы столкнетесь с проблемами, пожалуйста, сообщите нам.</p>"
                               "<br>"
                               "<p><b>Основные функции:</b></p>"
                               "<ul>"
                               "<li>Создание заметки:</li>"
                               "<p>Введите текст в заголовок и описание заметки в поле ввода.</p>"
                               "<p>Нажмите кнопку \"Создать новую заметку\", чтобы создать заметку</p>"
                               "<br>"
                               "<li>Просмотр заметок:</li>"
                               "<p>В списке заметок с левой стороны отображаются все созданные вами заметки.</p>"
                               "<p>Вы можете нажать на заметку, чтобы просмотреть её детали.</p>"
                               "<br>"
                               "<li>Редактирование задач:</li>"
                               "<p>Выберите заметку из списка.</p>"
                               "<p>Внесите изменения в поле ввода.</p>"
                               "<p>Нажмите кнопку \"Сохранить\", чтобы обновить заметку.</p>"
                               "<br>"
                               "<li>Удаление задач:</li>"
                               "<p>Выберите заметку из списка.</p>"
                               "<p>Нажмите кнопку \"Удалить\", чтобы удалить заметку.</p>"
                               "<br>"
                               "<li>Уведомления:</li>"
                               "<p>Нажмите кнопку \"Уведомление\".</p>"
                               "<p>Установите дату, месяц, год и время уведомления, а также когда хотите, чтобы приходило напоминание.</p>"
                               "<p>Нажмите кнопку \"Задать\", чтобы создать уведомление.</p>"
                               "<p>Приложение будет напоминать вам о задаче в заданное время.</p>"
                               "<br>"
                               "<p><b>Дополнительные советы:</b></p>"
                               "<p>В бета-версии приложение может сохранять задачи только в течение сеанса работы.</p>"
                               "<p>Приложение будет работать стабильнее, если вы будете закрывать и открывать его только при необходимости.</p>"
                               "<p>Мы работаем над улучшением приложения и добавлением новых функций. "
                               "Если вы столкнетесь с ошибками, пожалуйста, сообщите нам об этом!</p>"
                               "<br>"
                               "<p>Спасибо за использование To-Do Reminder!</p>"
                               "<br>"
                               "<p><b>Контакты для связи с нами:</b></p>"
                               "<p>E-mail → alirkotiaaaa@gmail.com , dibikovd@mail.com</p>"
                               "<p><b>Телеграмм канал U-fad Company</b></p>"
                               "<p>Переходите по Qr-коду!</p>"
                               "<br>"
                               "<img src='qr_kod.png' alt='image'/>"  # Путь к изображению и его альтернативный текст
                               "</div>"
                               "</body>"
                               "</html>")

        self.textLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)  # Выравнивание текста
        self.textLabel.setWordWrap(True)  # Перенос текста на новую строку при необходимости

        scroll_area.setWidget(self.textLabel)

        self.additionalFrame.show()

    def mousePressEvent(self, event):
        # Проверка, был ли клик выполнен в пределах additionalFrame
        if hasattr(self, 'additionalFrame') and not self.additionalFrame.geometry().contains(event.pos()):
            self.additionalFrame.close()


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

