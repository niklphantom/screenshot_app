from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
import sys
import os
import json
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QGuiApplication


class MyWindow(QMainWindow):

    save_dir = "/home/lab5017/Datacastle/develop/datasets_ft/classify_autmated_test/"
    title = "mlp"
    episode = ""
    index = 0
    screenshot_list = []
    index_list = []
    new_session = True
    save_width = 1000
    save_height = 1000

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(50, 50, 1650, 1200)
        self.setWindowTitle("ScreenApp")
        self.initUI()

    def initUI(self):

        self.label1 = QLabel('PyQt5', self)
        self.label1.setGeometry(QtCore.QRect(1410, 380, 512, 288))
        pixmap = QtGui.QPixmap("")
        pixmap = pixmap.scaled(512,288)
        self.label1.setPixmap(pixmap)
        self.label2 = QLabel('Prev', self)
        self.label2.setGeometry(QtCore.QRect(1480, 340, 30, 50))

        self.label3 = QLabel('PyQt5', self)
        self.label3.setGeometry(QtCore.QRect(1410, 695, 512, 288))
        pixmap = QtGui.QPixmap("")
        pixmap = pixmap.scaled(512,288)
        self.label3.setPixmap(pixmap)
        self.label4 = QLabel('Prev prev', self)
        self.label4.setGeometry(QtCore.QRect(1480, 655, 60, 50))


        self.imageView = QtWidgets.QGraphicsView(self)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.imageView.setGeometry(QtCore.QRect(0, 60, 1410, 810))
        self.imageView.setScene(self.scene)
        self.imageView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.imageView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.imageView.setObjectName("imageView")

        self.predictLab = QtWidgets.QLabel(self)
        self.predictLab.setGeometry(100, 10, 200, 50)
        self.predictLab.setObjectName("predictLab")

        self.deleteImageBut = QtWidgets.QPushButton(self)
        self.deleteImageBut.setGeometry(QtCore.QRect(1440, 330, 93, 28))
        self.deleteImageBut.setObjectName("deleteImageBut")

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1440, 20, 160, 310))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.saveDirBut = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.saveDirBut.setObjectName("saveDirBut")
        self.verticalLayout.addWidget(self.saveDirBut)
        self.saveDirLab = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.saveDirLab.setObjectName("saveDirLab")
        self.verticalLayout.addWidget(self.saveDirLab)

        self.titleLab = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.titleLab.setObjectName("titleLab")
        self.verticalLayout.addWidget(self.titleLab)
        self.titleEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.titleEdit.setObjectName("titleEdit")
        self.verticalLayout.addWidget(self.titleEdit)
        self.titleEdit.setText(str(self.title))

        self.episodeLab = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.episodeLab.setObjectName("episodeLab")
        self.verticalLayout.addWidget(self.episodeLab)
        self.episodeEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.episodeEdit.setObjectName("episodeEdit")
        self.verticalLayout.addWidget(self.episodeEdit)
        self.episodeEdit.setText(str(self.episode))

        self.save_widthLab = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.save_widthLab.setObjectName("save_widthLab")
        self.verticalLayout.addWidget(self.save_widthLab)
        self.save_widthEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.save_widthEdit.setObjectName("save_widthEdit")
        self.verticalLayout.addWidget(self.save_widthEdit)
        self.save_widthEdit.setText(str(self.save_width))

        self.save_heightLab = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.save_heightLab.setObjectName("save_heightLab")
        self.verticalLayout.addWidget(self.save_heightLab)
        self.save_heightEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.save_heightEdit.setObjectName("save_heightEdit")
        self.verticalLayout.addWidget(self.save_heightEdit)
        self.save_heightEdit.setText(str(self.save_height))

        self.automatic = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.automatic.setObjectName("check it if you are stupid C:")
        self.verticalLayout.addWidget(self.automatic)

        self.file_format_combo = QComboBox()
        self.file_format_combo.addItems(["png", "jpg"])
        self.verticalLayout.addWidget(self.file_format_combo)

        self.two_screen_info = QLabel('Settings for usage with 2 monitors', self)
        self.verticalLayout.addWidget(self.two_screen_info)

        self.combo_box = QComboBox()
        self.combo_box.addItems(["Save whole screenshot", "Save bottom half of img",
                                 "Save upper half of img", "Save left half of img",
                                 "Save right part of img",
                                 "Capture primary monitor", "Capture second monitor"])
        self.verticalLayout.addWidget(self.combo_box)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        if os.path.isfile("last_session_data.json"):
            with open("last_session_data.json", "r") as read_file:
                data = json.load(read_file)
            self.save_dir = data["save_dir"]
            self.saveDirLab.setText(self.save_dir)
            self.title = data["title"]
            self.titleEdit.setText(str(self.title))
            self.episode = data["episode"]
            self.episodeEdit.setText(str(self.episode))
            self.save_width = data["save_width"]
            self.save_widthEdit.setText(str(self.save_width))
            self.save_height = data["save_height"]
            self.save_heightEdit.setText(str(self.save_height))
            index = self.combo_box.findText(data["two_monitors_settings"], Qt.MatchFixedString)
            if index >= 0:
                self.combo_box.setCurrentIndex(index)
            index_f = self.file_format_combo.findText(data["file_format"], Qt.MatchFixedString)
            if index_f >= 0:
                self.file_format_combo.setCurrentIndex(index_f)



        # actions, changes and clicks
        self.saveDirBut.clicked.connect(self.changeSaveDir)
        self.automatic.stateChanged.connect(self.changeMode)
        self.deleteImageBut.clicked.connect(self.deleteImg)

        self.instantScreenshotCheckbox = QtWidgets.QCheckBox("Instant screenshot by 'S' button", self.verticalLayoutWidget)
        self.instantScreenshotCheckbox.setObjectName("instantScreenshotCheckbox")
        self.verticalLayout.addWidget(self.instantScreenshotCheckbox)

        # Connect the new checkbox signal
        self.instant_screenshot_enabled = False
        self.instantScreenshotCheckbox.stateChanged.connect(self.toggleInstantScreenshot)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def toggleInstantScreenshot(self, state):
        """Enable or disable instant screenshot functionality."""
        self.instant_screenshot_enabled = state == Qt.Checked


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.deleteImageBut.setText(_translate("MainWindow", "delete"))
        self.saveDirBut.setText(_translate("MainWindow", "Save directory"))
        self.saveDirLab.setText(_translate("MainWindow", "save"))
        self.titleLab.setText(_translate("MainWindow", "title"))
        self.episodeLab.setText(_translate("MainWindow", "episode"))
        self.save_widthLab.setText(_translate("MainWindow", "adjust screenshot save width"))
        self.save_heightLab.setText(_translate("MainWindow", "adjust screenshot save height"))
        self.automatic.setText(_translate("MainWindow", "check it if you are stupid C:"))

    def deleteImg(self):
        self.screenshot_list.pop()
        self.scene.clear()
        self.index = self.index - 1
        # pixmap = QtGui.QPixmap(os.path.join(self.save_dir, self.screenshot_list[-1]))
        # newSceneWidth = pixmap.width()
        # newSceneHeight = pixmap.height()
        # self.scene.setSceneRect(0,0, newSceneWidth, newSceneHeight)
        # self.scene.addPixmap(QtGui.QPixmap(pixmap))
        # # and also refresh prevs
        # self.refresh_prev_screenshots()

    def changeMode(self, state):
        pass

    def start_new_session(self):
        self.index = 0
        self.screenshot_list = []
        self.index_list = []
        file_list = os.listdir(self.save_dir)
        file_list.sort()
        for file_name in file_list:
            print(file_name)
            ext = file_name[file_name.rfind(".") + 1:]
            if ext == "jpg" or ext == "png" or ext == "jpeg":
                relevance = file_name.rfind(self.title + "_" + self.episode + "_")
                # find only relevant to current session images, and determine max last saved index
                if relevance != -1:
                    prefix_len = len(self.title + "_" + self.episode + "_")
                    self.screenshot_list.append(file_name)
                    current_index = int(file_name[relevance + prefix_len: file_name.rfind(".")])
                    self.index_list.append(current_index)
        self.screenshot_list.sort(key=lambda elem: int(elem[len(self.title + "_" + self.episode + "_"): elem.rfind(".")]))
        if self.index_list:
            self.index = max(self.index_list) + 1
        # save file about current session to load delete time
        session_data = {"save_dir": self.save_dir, "title": self.title, "episode": self.episode, "save_width": self.save_width, "save_height": self.save_height,
                        "two_monitors_settings": self.combo_box.currentText(), "file_format": self.file_format_combo.currentText()}
        with open("last_session_data.json", "w") as write_file:
            json.dump(session_data, write_file)

    def refresh_prev_screenshots(self):
        if len(self.screenshot_list) > 1:
            pixmap = QtGui.QPixmap(os.path.join(self.save_dir, self.screenshot_list[-2]))
            print(self.screenshot_list[-2])
            pixmap = pixmap.scaled(512,288)
            self.label1.setPixmap(pixmap)
        if len(self.screenshot_list) > 2:
            pixmap = QtGui.QPixmap(os.path.join(self.save_dir, self.screenshot_list[-3]))
            pixmap = pixmap.scaled(512,288)
            self.label3.setPixmap(pixmap)

    def changeSaveDir(self):
        self.save_dir = QtWidgets.QFileDialog.getExistingDirectory()
        self.saveDirLab.setText(self.save_dir)

    def keyPressEvent(self, e: QtGui.QKeyEvent):
        if e.key() == QtCore.Qt.Key_V:
            self.copyImg()
        if e.key() == QtCore.Qt.Key_Delete:
            self.deleteImg()
        elif e.key() == QtCore.Qt.Key_S:
            if self.instant_screenshot_enabled:
                self.copyImg(paste_mode=False)
            else:
                QMessageBox.warning(self, "Instant Screenshot Disabled",
                                    "Please enable 'Instant screenshot by S button' in the UI to use this feature.")

    def copyImg(self, paste_mode=True):
        temp_episode = self.episodeEdit.text()
        temp_title = self.titleEdit.text()
        temp_save_width = int(self.save_widthEdit.text())
        temp_save_height = int(self.save_heightEdit.text())
        if self.title != temp_title or self.episode != temp_episode or \
                self.save_height != temp_save_height or self.save_width != temp_save_width:
            self.title = temp_title
            self.episode = temp_episode
            self.save_width = temp_save_width
            self.save_height = temp_save_height
            self.new_session = True
        if self.title == "" and self.episode == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Not so fast")
            msg.setInformativeText('Please fill some info in title or episode fields')
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        if int(self.save_width) < int(self.save_height):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Not so fast")
            msg.setInformativeText('Width is smaller than height, are you sure?')
            msg.setWindowTitle("Error")
            msg.exec_()
        if int(self.save_width) > 4000 or int(self.save_height) > 4000:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Not so fast")
            msg.setInformativeText('Image dimension exceeds 4000 pixels, are you sure?')
            msg.setWindowTitle("Error")
            msg.exec_()

        self.scene.clear()

        screen_idx = self.combo_box.currentIndex()
        if screen_idx == 5:  # Capture primary monitor
            screen = QGuiApplication.primaryScreen()
        elif screen_idx == 6:  # Capture second monitor
            screens = QGuiApplication.screens()
            if len(screens) > 1:
                screen = screens[1]  # Secondary monitor
            else:
                QMessageBox.warning(self, "Error", "Only one monitor detected.")
                return
        else:  # Fallback to whole screenshot
            screen = QGuiApplication.primaryScreen()

        # Automatic screenshot capture for instant mode
        if not paste_mode:
            if screen is None:
                return
            p = screen.grabWindow(0)  # Capture the entire screen or all screens
        else:
            # Original behavior for 'V' key: paste from clipboard
            clip = QApplication.clipboard()
            mimeData = clip.mimeData()
            try:
                p = QtGui.QPixmap(mimeData.imageData())
            except:
                return

        current_width = p.width()
        current_height = p.height()
        combo_idx = self.combo_box.currentIndex()

        # Crop based on combo_idx
        if combo_idx == 1:
            p = p.copy(0, current_height // 2, current_width, current_height // 2)  # Crop bottom half
        elif combo_idx == 2:
            p = p.copy(0, 0, current_width, current_height // 2)  # Crop upper half
        elif combo_idx == 3:
            p = p.copy(0, 0, current_width // 2, current_height)  # Crop left half
        elif combo_idx == 4:
            p = p.copy(current_width // 2, 0, current_width // 2, current_height)  # Crop right half

        self.scene.addPixmap(p)
        if self.new_session:
            self.start_new_session()
            self.new_session = False

        self.save_img(p)
        self.refresh_prev_screenshots()

    def save_img(self, img):
        """Saves the image as a file."""
        current_width = img.width()
        current_height = img.height()

        if current_width != self.save_width or current_height != self.save_height:
            img = img.scaled(self.save_width, self.save_height, transformMode=Qt.SmoothTransformation)

        img_path = os.path.join(
            self.save_dir,
            f"{self.title}_{self.episode}_{self.index}.{self.file_format_combo.currentText()}"
        )
        img.save(img_path, self.file_format_combo.currentText().upper())
        self.screenshot_list.append(
            f"{self.title}_{self.episode}_{self.index}.{self.file_format_combo.currentText()}"
        )
        self.index += 1


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
