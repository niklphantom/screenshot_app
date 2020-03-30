from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
import sys
import os
import json
from PyQt5.QtWidgets import QMessageBox



class MyWindow(QMainWindow):

    save_dir = "/home/lab5017/Datacastle/develop/datasets_ft/classify_autmated_test/"
    title = "mlp"
    episode = ""
    index = 0
    screenshot_list = []
    index_list = []
    new_session = True

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
        self.scene.setSceneRect(0, 0, 1400, 800)
        self.imageView.setGeometry(QtCore.QRect(0, 60, 1410, 810))
        self.imageView.setScene(self.scene)
        self.imageView.setObjectName("imageView")

        self.predictLab = QtWidgets.QLabel(self)
        self.predictLab.setGeometry(100, 10, 200, 50)
        self.predictLab.setObjectName("predictLab")

        self.deleteImageBut = QtWidgets.QPushButton(self)
        self.deleteImageBut.setGeometry(QtCore.QRect(1450, 300, 93, 28))
        self.deleteImageBut.setObjectName("deleteImageBut")

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1440, 20, 160, 260))
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

        self.automatic = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.automatic.setObjectName("check it if you are stupid C:")
        self.verticalLayout.addWidget(self.automatic)

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

        # actions, changes and clicks
        self.saveDirBut.clicked.connect(self.changeSaveDir)
        self.automatic.stateChanged.connect(self.changeMode)
        self.deleteImageBut.clicked.connect(self.deleteImg)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.deleteImageBut.setText(_translate("MainWindow", "delete"))
        self.saveDirBut.setText(_translate("MainWindow", "Save directory"))
        self.saveDirLab.setText(_translate("MainWindow", "save"))
        self.titleLab.setText(_translate("MainWindow", "title"))
        self.episodeLab.setText(_translate("MainWindow", "episode"))
        self.automatic.setText(_translate("MainWindow", "check it if you are stupid C:"))

    def deleteImg(self):
        self.screenshot_list.pop()
        self.scene.clear()
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
        session_data = {"save_dir": self.save_dir, "title": self.title, "episode": self.episode}
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

    def copyImg(self):
        temp_episode = self.episodeEdit.text()
        temp_title = self.titleEdit.text()
        if self.title != temp_title or self.episode != temp_episode:
            self.title = temp_title
            self.episode = temp_episode
            self.new_session = True
        if self.title == "" and self.episode == "":
            #print("uuuu nelza tak")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Not so fast")
            msg.setInformativeText('Please fill some info in title or episode fields')
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        self.scene.clear()
        clip = QApplication.clipboard()
        mimeData = clip.mimeData()
        try:
            newSceneWidth = mimeData.imageData().width()
        except:
            return
        newSceneHeight = mimeData.imageData().height()
        self.scene.setSceneRect(0,0, newSceneWidth, newSceneHeight)
        self.scene.addPixmap(QtGui.QPixmap(mimeData.imageData()))
        #self.scene.setScaledContents(False)
        if self.new_session:
            self.start_new_session()
            self.new_session = False

        p = QtGui.QPixmap(mimeData.imageData())
        self.save_img(p)
        self.refresh_prev_screenshots()
        # p.save("filenam.png","PNG")

    def save_img(self, img):
        # accepts input of image as a pyqt pixmap
        img_path = os.path.join(self.save_dir, self.title + "_" + self.episode + "_" + str(self.index) + ".png")
        img.save(img_path, "PNG")
        self.screenshot_list.append(self.title + "_" + self.episode + "_" + str(self.index) + ".png")
        self.index = self.index + 1


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
