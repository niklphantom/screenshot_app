from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
import sys
#from classify_automated_not_ide import *

class MyWindow(QMainWindow):
    automatic_cond = False  # automated mode if false

    source_dir = "/home/lab5017/Datacastle/develop/datasets_ft/classify_autmated_test/src/"
    save_dir = "/home/lab5017/Datacastle/develop/datasets_ft/classify_autmated_test/"
    weights_path = "/home/lab5017/Datacastle/develop/datasets_ft/eleron/SN_eleron_4_EPS_acc091.h5"
    height = 224
    width = 224
    channels = 3
    number_of_classes = 4
    classes_file = ""
    classes = ["background", "car", "groups", "people"]
    pred = None
    img_name = None
    imgs_names = None
    counter = 0


    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(50, 50, 1650, 1200)
        self.setWindowTitle("Autorazmetka")
        self.initUI()

    def initUI(self):

        self.width = 224
        # self.centralwidget = QtWidgets.QWidget()
        # self.centralwidget.setObjectName("centralwidget")
        # self.photo = QtWidgets.QLabel(self.centralwidget)
        # self.photo.setGeometry(QtCore.QRect(1500, 1200, 841, 511))
        # self.photo.setText("")
        # self.photo.setPixmap(QtGui.QPixmap("filenam.png"))
        # self.photo.setScaledContents(True)
        # self.photo.setObjectName("photo")

        # pixmap = QtGui.QPixmap("filenam.png")
        # sceneItem = self.addItem(pixmap)
        # sceneItem.setPos(1500,1500)

        self.label2 = QLabel('PyQt5', self)
        self.label2.setGeometry(QtCore.QRect(1410, 530, 512, 288))
        #label2.move(20,0)
        #label2.setGeometry(QtCore.QRect(0, 0, 841, 511))
        pixmap = QtGui.QPixmap("filenam.png")
        pixmap = pixmap.scaled(512,288)
        self.label2.setPixmap(pixmap)
        self.label3 = QLabel('PyQt5', self)
        self.label3.setGeometry(QtCore.QRect(1570, 530, 30, 50))


        self.imageView = QtWidgets.QGraphicsView(self)
        self.scene = QtWidgets.QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 1400, 800)
        self.imageView.setGeometry(QtCore.QRect(0, 60, 1410, 810))
        self.imageView.setScene(self.scene)
        self.imageView.setObjectName("imageView")

        self.predictLab = QtWidgets.QLabel(self)
        self.predictLab.setGeometry(100, 10, 200, 50)
        self.predictLab.setObjectName("predictLab")

        self.nextImageBut = QtWidgets.QPushButton(self)
        self.nextImageBut.setGeometry(QtCore.QRect(1450, 500, 93, 28))
        self.nextImageBut.setObjectName("nextImageBut")

        self.startAutoClassBut = QtWidgets.QPushButton(self)
        self.startAutoClassBut.setGeometry(QtCore.QRect(1450, 450, 94, 28))
        self.startAutoClassBut.setObjectName("startAutoClassBut")

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1440, 20, 160, 406))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.sourceDirBut = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sourceDirBut.setObjectName("sourceDirBut")
        self.verticalLayout.addWidget(self.sourceDirBut)
        self.sourceDirLab = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sourceDirLab.setObjectName("sourceDirLab")
        self.verticalLayout.addWidget(self.sourceDirLab)

        self.saveDirBut = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.saveDirBut.setObjectName("saveDirBut")
        self.verticalLayout.addWidget(self.saveDirBut)
        self.saveDirLab = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.saveDirLab.setObjectName("saveDirLab")
        self.verticalLayout.addWidget(self.saveDirLab)

        self.weightsBut = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.weightsBut.setObjectName("weightsBut")
        self.verticalLayout.addWidget(self.weightsBut)
        self.weightsLab = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.weightsLab.setObjectName("weightsLab")
        self.verticalLayout.addWidget(self.weightsLab)

        self.heightLab = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.heightLab.setObjectName("heightLab")
        self.verticalLayout.addWidget(self.heightLab)
        self.heidhtEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.heidhtEdit.setObjectName("heidhtEdit")
        self.verticalLayout.addWidget(self.heidhtEdit)

        self.widthLab = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.widthLab.setObjectName("widthLab")
        self.verticalLayout.addWidget(self.widthLab)
        self.widthEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.widthEdit.setObjectName("widthEdit")
        self.verticalLayout.addWidget(self.widthEdit)
        self.widthEdit.setText(str(self.width))

        self.classesBut = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.classesBut.setObjectName("classesBut")
        self.verticalLayout.addWidget(self.classesBut)
        self.classesLab = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.classesLab.setObjectName("classesLab")

        self.verticalLayout.addWidget(self.classesLab)
        self.automatic = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.automatic.setObjectName("automatic")
        self.verticalLayout.addWidget(self.automatic)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        # actions, changes and clicks
        self.sourceDirBut.clicked.connect(self.changeSourceDir)
        self.saveDirBut.clicked.connect(self.changeSaveDir)
        self.weightsBut.clicked.connect(self.changeWeightsFile)
        self.classesBut.clicked.connect(self.changeClassFile)
        self.automatic.stateChanged.connect(self.changeMode)
        self.startAutoClassBut.clicked.connect(self.startClassify)
        self.nextImageBut.clicked.connect(self.nextImg)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nextImageBut.setText(_translate("MainWindow", "Next"))
        self.startAutoClassBut.setText(_translate("MainWindow", "Start autoclass"))
        self.sourceDirBut.setText(_translate("MainWindow", "Source directory"))
        self.sourceDirLab.setText(_translate("MainWindow", "source"))
        self.saveDirBut.setText(_translate("MainWindow", "Save directory"))
        self.saveDirLab.setText(_translate("MainWindow", "save"))
        self.weightsBut.setText(_translate("MainWindow", "Weights path"))
        self.weightsLab.setText(_translate("MainWindow", "weights"))
        self.heightLab.setText(_translate("MainWindow", "height"))
        self.widthLab.setText(_translate("MainWindow", "width"))
        self.classesBut.setText(_translate("MainWindow", "Classes"))
        self.classesLab.setText(_translate("MainWindow", "classes"))
        self.automatic.setText(_translate("MainWindow", "automatic"))

    def nextImg(self):
        self.scene.clear()
        self.scene.addPixmap(QtGui.QPixmap(self.img_name))
        self.counter += 1
        newfont = QtGui.QFont("Times", 14, QtGui.QFont.Bold)
        self.predictLab.setText(self.pred)
        self.predictLab.setFont(newfont)
        if self.counter < len(self.imgs_names):
            self._predict()

    def changeMode(self, state):
        self.automatic_cond = state == QtCore.Qt.Checked

    def changeSourceDir(self):
        self.source_dir = QtWidgets.QFileDialog.getExistingDirectory()
        self.sourceDirLab.setText(self.source_dir)

    def changeSaveDir(self):
        self.save_dir = QtWidgets.QFileDialog.getExistingDirectory()
        self.saveDirLab.setText(self.save_dir)

    def changeWeightsFile(self):
        self.weights_path = QtWidgets.QFileDialog.getOpenFileName()[0]
        self.weightsLab.setText(self.weights_path)

    def changeClassFile(self):
        self.classes_file = QtWidgets.QFileDialog.getOpenFileName()[0]
        self.classesLab.setText(self.classes_file)

    def startClassify(self):
        self.width = self.widthEdit.text()
        self.height = self.heidhtEdit.text()

        with open(self.classes_file, 'r') as f:
            self.classes = f.readlines()
            self.number_of_classes = len(self.classes)
            for i in range(self.number_of_classes):
                self.classes[i] = self.classes[i].replace('\n', '').replace(' ', '')
        print(self.classes)

        if self.automatic_cond:
            start_classify(source_dir=self.source_dir,
                           save_dir=self.save_dir,
                           weights_path=self.weights_path,
                           classes=self.classes,
                           num_classes=self.number_of_classes,
                           height=self.height,
                           width=self.width)
        else:
            self.imgs_names = os.listdir(self.source_dir)
            for i in range(len(self.imgs_names)):
                self.imgs_names[i] = os.path.join(self.source_dir, self.imgs_names[i])
            self._predict()

    def _predict(self):
        img_name = self.imgs_names[self.counter]
        self.img_name, self.pred = predict(img_name=img_name,
                save_dir=self.save_dir,
                weights_path=self.weights_path,
                classes=self.classes,
                num_classes=self.number_of_classes,
                height=self.height,
                width=self.width)

    def keyPressEvent(self, e: QtGui.QKeyEvent):
        if e.key() == QtCore.Qt.Key_V:
            self.copyImg()

    def copyImg(self):
        self.scene.clear()
        clip = QApplication.clipboard()
        mimeData = clip.mimeData()
        newSceneWidth = mimeData.imageData().width()
        newSceneHeight = mimeData.imageData().height()
        self.scene.setSceneRect(0,0, newSceneWidth, newSceneHeight)
        self.scene.addPixmap(QtGui.QPixmap(mimeData.imageData()))
        #self.scene.setScaledContents(False)
        p = QtGui.QPixmap(mimeData.imageData())
        p.save("filenam.png","PNG")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
