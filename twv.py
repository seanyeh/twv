#!/usr/bin/env python3

import PyQt5
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

import sys

app = QApplication("twv")
view = QWebEngineView()
view.setUrl(QUrl(sys.argv[1]))
view.showMaximized()
app.exec_()
