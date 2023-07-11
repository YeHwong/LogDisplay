#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023-07-11 17:53
# @File: main.py
# @Author: YeHwong
# @Email: 598318610@qq.com
# @Version ：1.0.0
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QObject, pyqtSlot, QMetaObject


class LogDisplayApp(QObject):
    def __init__(self):
        super().__init__()
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("my_icon.png"))
        # self.tray_icon.activated.connect(self.on_tray_icon_activated)

        self.menu = QMenu()
        self.restore_action = self.menu.addAction("Restore")
        self.restore_action.triggered.connect(self.restore_app)

        self.quit_action = self.menu.addAction("Quit")
        self.quit_action.triggered.connect(QApplication.instance().quit)

        self.tray_icon.setContextMenu(self.menu)
        self.tray_icon.show()
        QMetaObject.connectSlotsByName(self)

    @pyqtSlot()
    def on_tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.restore_app()

    @pyqtSlot()
    def on_restore_action_triggered(self):
        self.restore_app()

    def restore_app(self):
        self.tray_icon.hide()
        print("reason")
        # restore the application
        # ...


if __name__ == '__main__':
    app = QApplication([])
    my_app = LogDisplayApp()
    app.exec_()
