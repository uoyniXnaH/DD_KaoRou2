#!/usr/bin/python3
# -*- coding: utf-8 -*-


import images
import requests
from PySide2.QtWidgets import QGridLayout, QDialog, QLabel, QApplication
from PySide2.QtCore import Qt, QUrl, QThread


def _translate(context, text, disambig):
    return QApplication.translate(context, text, disambig)


class thankToBoss(QThread):
    def __init__(self, parent=None):
        super(thankToBoss, self).__init__(parent)

    def run(self):
        print('start link')
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
        response = requests.get(r'https://github.com/jiafangjun/DD_KaoRou', headers=headers)
        print(response.text)


class pay(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('赞助和支持')
        self.resize(800, 480)
        layout = QGridLayout()
        self.setLayout(layout)
        txt = u'DD烤肉机由B站up：执鸣神君 业余时间独立开发制作。\n\
\n所有功能全部永久免费给广大烤肉man使用，无需专门找我获取授权。\n\
\n有独立经济来源的老板们如觉得烤肉机好用的话，不妨小小支持亿下\n\
\n一元也是对我继续更新烤肉机的莫大鼓励。十分感谢！\n'
        label = QLabel(txt)
        label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label, 0, 0, 1, 2)

        bilibili_url = QLabel()
        bilibili_url.setAlignment(Qt.AlignCenter)
        bilibili_url.setOpenExternalLinks(True)
        bilibili_url.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://space.bilibili.com/637783\">\
<span style=\" text-decoration: underline; color:#cccccc;\">执鸣神君B站主页: https://space.bilibili.com/637783</span></a></p></body></html>", None))
        layout.addWidget(bilibili_url, 1, 0, 1, 2)

        github_url = QLabel()
        github_url.setAlignment(Qt.AlignCenter)
        github_url.setOpenExternalLinks(True)
        github_url.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://github.com/jiafangjun/DD_KaoRou\">\
<span style=\" text-decoration: underline; color:#cccccc;\">烤肉机项目开源地址: https://github.com/jiafangjun/DD_KaoRou</span></a></p></body></html>", None))
        layout.addWidget(github_url, 2, 0, 1, 2)

        layout.addWidget(QLabel(), 3, 0, 1, 1)
        alipay = QLabel()
        alipay.setFixedSize(260, 338)
        alipay.setStyleSheet('border-image: url(:/images/0.jpg)')
        layout.addWidget(alipay, 4, 0, 1, 1)
        weixin = QLabel()
        weixin.setFixedSize(260, 338)
        weixin.setStyleSheet('border-image: url(:/images/1.jpg)')
        layout.addWidget(weixin, 4, 1, 1, 1)
        layout.addWidget(QLabel(), 5, 0, 1, 1)

        self.thankToBoss = thankToBoss()
        self.thankToBoss.start()
