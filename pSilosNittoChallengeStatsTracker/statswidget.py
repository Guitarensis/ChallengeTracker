from PyQt5 import QtWidgets, QtCore


class StatsWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.avg_rt_widget = QtWidgets.QLCDNumber(self.mainmenu)
        self.avg_rt_widget.setGeometry(QtCore.QRect(30, 70, 91, 23))
        self.avg_rt_widget.setObjectName("avg_rt_widget")

        self.avg_et_widget = QtWidgets.QLCDNumber(self.mainmenu)
        self.avg_et_widget.setGeometry(QtCore.QRect(30, 110, 91, 23))
        self.avg_et_widget.setObjectName("avg_et_widget")

        self.avg_mph_widget = QtWidgets.QLCDNumber(self.mainmenu)
        self.avg_mph_widget.setGeometry(QtCore.QRect(30, 150, 91, 23))
        self.avg_mph_widget.setObjectName("avg_mph_widget")

        self.rt_diff_widget = QtWidgets.QLCDNumber(self.mainmenu)
        self.rt_diff_widget.setGeometry(QtCore.QRect(30, 190, 91, 23))
        self.rt_diff_widget.setObjectName("rt_diff_widget")

        self.et_diff_widget = QtWidgets.QLCDNumber(self.mainmenu)
        self.et_diff_widget.setGeometry(QtCore.QRect(30, 230, 91, 23))
        self.et_diff_widget.setObjectName("et_diff_widget")

        self.et_diff_label = QtWidgets.QLabel(self.mainmenu)
        self.et_diff_label.setGeometry(QtCore.QRect(130, 230, 41, 21))
        self.et_diff_label.setObjectName("et_diff_label")

        self.rt_diff_label = QtWidgets.QLabel(self.mainmenu)
        self.rt_diff_label.setGeometry(QtCore.QRect(130, 190, 41, 31))
        self.rt_diff_label.setObjectName("rt_diff_label")

        self.avg_mph_label = QtWidgets.QLabel(self.mainmenu)
        self.avg_mph_label.setGeometry(QtCore.QRect(130, 150, 51, 21))
        self.avg_mph_label.setObjectName("avg_mph_label")

        self.avg_et_label = QtWidgets.QLabel(self.mainmenu)
        self.avg_et_label.setGeometry(QtCore.QRect(130, 110, 51, 21))
        self.avg_et_label.setObjectName("avg_et_label")

        self.avg_rt_label = QtWidgets.QLabel(self.mainmenu)
        self.avg_rt_label.setGeometry(QtCore.QRect(130, 70, 51, 21))
        self.avg_rt_label.setObjectName("avg_rt_label")

        self.total_races_widget = QtWidgets.QLCDNumber(self.mainmenu)
        self.total_races_widget.setGeometry(QtCore.QRect(30, 400, 161, 23))
        self.total_races_widget.setObjectName("total_races_widget")

        self.total_races_label = QtWidgets.QLabel(self.mainmenu)
        self.total_races_label.setGeometry(QtCore.QRect(200, 400, 91, 21))
        self.total_races_label.setObjectName("total_races_label")

        self.foul_output_widget = QtWidgets.QLCDNumber(self.mainmenu)
        self.foul_output_widget.setGeometry(QtCore.QRect(30, 350, 91, 23))
        self.foul_output_widget.setObjectName("foul_output_widget")

        self.foul_output_label = QtWidgets.QLabel(self.mainmenu)
        self.foul_output_label.setGeometry(QtCore.QRect(130, 350, 31, 21))
        self.foul_output_label.setObjectName("foul_label")
