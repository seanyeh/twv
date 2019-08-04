#!/usr/bin/env python3

import PyQt5
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebKitWidgets import QWebView

import sys

app = QApplication(sys.argv)
view = QWebView()
view.setUrl(QUrl(sys.argv[1]))
view.showMaximized()
app.exec_()
