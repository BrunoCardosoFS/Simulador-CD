from PySide6 import QtWidgets
from PySide6.QtCore import Qt, Slot, QSettings
from PySide6.QtGui import QIcon
from PySide6.QtSerialPort import QSerialPort

from style.style import globalStyle

from modules.tempsettings import TempSettings

from ui.widgets.leftmenu import LeftMenu
from ui.widgets.simulation import AreaSimulation

import resources.resources

# Creating the central widget
class CentralWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QMainWindow):
        super().__init__()
    
        self.setObjectName("CentralWidget")
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.settings = QSettings("BrunoCardoso", "SimuladorCircuitosDigitais")
        self.isDarkMode = self.settings.value("darkMode",defaultValue=TempSettings.get("isDarkModeSystem"), type=bool)

        self.setStyleSheet(globalStyle(self.isDarkMode))

        self.Layout = QtWidgets.QHBoxLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(0)

        self.setLayout(self.Layout)

        self.LeftMenu = LeftMenu(self)
        self.LeftMenu.toggleDarkMode.connect(self.toggleTheme)

        self.LeftMenu.selectDevice.currentIndexChanged.connect(self.connectSerial)
        self.LeftMenu.closeSerial.connect(self.closeSerial)

        self.AreaSimulation = AreaSimulation(self)

        self.Layout.addWidget(self.LeftMenu)
        self.Layout.addWidget(self.AreaSimulation)

        # Serial Manager
        self.serialPort = QSerialPort(parent=self)

    @Slot(bool)
    def toggleTheme(self, isDarkMode:bool):
        self.isDarkMode = isDarkMode
        self.setStyleSheet(globalStyle(isDarkMode))

    @Slot(int)
    def connectSerial(self, index:int):
        if index >= 0:
            port = TempSettings.get("devices")[index][0]

            TempSettings.set("currentDevice", port)

            self.serialPort.setPortName(port)
            self.serialPort.setBaudRate(QSerialPort.Baud115200)

            # self.serialPort.setDataBits(QSerialPort.Data8)
            # self.serialPort.setParity(QSerialPort.NoParity)
            # self.serialPort.setStopBits(QSerialPort.OneStop)
            # self.serialPort.setFlowControl(QSerialPort.NoFlowControl)

            messageBox = QtWidgets.QMessageBox()

            if self.serialPort.open(QSerialPort.ReadWrite):
                messageBox.setWindowTitle(f"Conectado a {port}")
                messageBox.setIcon(QtWidgets.QMessageBox.Information)
                messageBox.setText("Conexão estabelecida com sucesso.")
                messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)

                messageBox.exec()
            else:
                self.LeftMenu.updateDevices(True)
                messageBox.setWindowTitle("Não foi possível conectar")
                messageBox.setIcon(QtWidgets.QMessageBox.Critical)
                messageBox.setText("Não foi possível conectar ao dispositivo.")
                messageBox.setInformativeText("Verifique o dispositivo e tente novamente.")
                messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)

                messageBox.exec()

    @Slot()
    def closeSerial(self):
        if self.serialPort.isOpen():
            self.serialPort.close()
            messageBox = QtWidgets.QMessageBox()
            messageBox.setWindowTitle(f"Desconectado de {TempSettings.get('currentDevice')}")
            messageBox.setIcon(QtWidgets.QMessageBox.Warning)
            messageBox.setText("Conexão encerrada, escolha um dispositivo para conectar.")
            messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)

            messageBox.exec()


# Creating the main window
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Defining window parameters
        self.setWindowTitle("Simulador Circuitos Digitais")
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        self.setWindowIcon(QIcon(":/images/icons/icon.ico"))

        self.central = CentralWidget(self)
        self.setCentralWidget(self.central)

    @Slot()
    def closeEvent(self, event):
        QtWidgets.QApplication.quit()
        super().closeEvent(event)