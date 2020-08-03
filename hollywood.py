import sys
import random
import numpy as np
import time
import datetime
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pyqtgraph as pg


# content1 丢包率 content7 下载进度条  done!
class WorkThread1(QThread):
    # 初始化线程
    def __int__(self):
        super(WorkThread1, self).__init__()
    #线程运行函数
    def run(self):
        global content_1, content_7
        cnt = 0
        contents = []
        contents7 = []
        while True:
            if cnt == 0:
                content = "<font color='#0000FF'>----------Prepare for install package in environment FLASK36-----------</font>"
                bar = "<font color='#0000FF'>----------Prepare for install package in environment FLASK36-----------</font>"
                cnt+=1
                contents.append(content)
                contents7.append(bar)
                content_1 = (''.join([x for x in contents]))
                content_7 = (''.join([x for x in contents7]))
                time.sleep(1)
            else:
                s = random.randint(1, 1024)
                r = random.randint(0, s)
                l = s - r
                lr = '%.2f' % (l * 100 / s)
                def process_bar(percent, start_str='', end_str='', total_length=20):
                    bar = ''.join(['█'] * int(percent * total_length)) + ''
                    #  "\033[字背景颜色;字体颜色m字符串\033[0m"
                    bar = "<font color='#3300FF'>{}</font><font color='#3366FF'>{}</font></font><font color='yellow'> {:0>4.1f}%|</font><font color='white'> {}<br /></font>"\
                        .format(start_str.ljust(20),bar.ljust(total_length, '░'),percent * 100,end_str)
                    # ljust:原字符串填充左对齐,
                    return bar
                pip_lists = ['apache8-tomcat.gz','nginx5.6.tar','solr4.10-bin.tar','redis3.2','mongodb-linux-x86_6','openssl-devel']
                start_str = random.choice(pip_lists)
                bar1 = process_bar(l/s,start_str=start_str, end_str='100%')
                bar2 = process_bar((random.randint(0,1001))/1000,start_str=start_str, end_str='100%')
                bar = bar1+bar2
                content = "<font color='green'>Packets:</font> <font color='white'>Sent = <font color='yellow'>{}</font>, Received = <font color='yellow'>{}</font>, Lost =<font color='yellow'> {}</font> ({}% loss)<br /></font><br/>".format(s, r, l, lr)
                if cnt >= 5:
                    contents.pop(0)
                    contents7.pop(0)
                    cnt-=1
                else:
                    contents.append(content)
                    contents7.append(bar)
                    content_1 = (''.join([x for x in contents]))
                    content_7 = (''.join([x for x in contents7]))
                    cnt+=1
                    time.sleep(0.3)
# content3 时间+DOO content5 框 cpu done!
class WorkThread2(QThread):
    # 初始化线程
    def __int__(self):
        super(WorkThread2, self).__init__()
    # 线程运行函数
    def run(self):
        global content_3, content_5
        titl = 'PID USER'.ljust(10) + '|' + ' ' * 3 + 'PR'.ljust(7) + '|' + ' ' * 3 + 'RES'.ljust(
            7) + '|' + ' ' * 3 + '%CPU'.ljust(7) + '|' + ' ' * 3 + '%MEM'
        title = "<font color='#9900CC'>{}<br /></font>".format(titl)
        msg = "<font color='green'>****ENVIRONMENT***<br /></font>" \
              "<font color='white'>The following environment variable is utilized by script<br /></font>"
        contents=[msg,]
        contents5=[title,]
        cnt = 0
        while True:
            now = time.strftime("%Y--%m--%d %H:%M:%S", time.localtime(int(time.time())))
            if cnt >= 5:
                contents.pop(1)
                contents5.pop(1)
                cnt-=1
            else:
                msg1 = "<font color='red'>DM{}</font><font color='white'>ID:90000a{} at address</font> <font color='yellow'>100{}000{}00{}00100GX<br /></font><font color='green'>{}<br /></font>"\
                    .format(random.randint(1000, 9999),random.randint(00, 99),random.randint(0, 2),random.randint(0, 2),random.randint(0, 2),now)
                c = ['-20', '0', '20', '40', '60', '80']
                bar1 = (str(random.randint(1, 1000))).ljust(10) + '|' + ' ' * 3 + (''.join(random.choices(c))).ljust(
                    7) + '|' + ' ' * 3 + (str(random.randint(0, 99999))).ljust(7) + '|' + ' ' * 3 + (
                               str(random.randint(0, 101)) + '%').ljust(7) + '|' + ' ' * 3 + str(
                    random.randint(0, 101)) + '%'
                bar2 = (str(random.randint(1, 1000))).ljust(10) + '|' + ' ' * 3 + (''.join(random.choices(c))).ljust(
                    7) + '|' + ' ' * 3 + (str(random.randint(0, 99999))).ljust(7) + '|' + ' ' * 3 + (
                               str(random.randint(0, 101)) + '%').ljust(7) + '|' + ' ' * 3 + str(
                    random.randint(0, 101)) + '%'
                bar = "<font color='#66FFFF'>{}<br />{}<br /></font>".format(bar1,bar2)
                contents.append(msg1)
                contents5.append(bar)
                content_3 = (''.join([x for x in contents]))
                content_5 = (''.join([x for x in contents5]))
                cnt+=1
                time.sleep(0.2)
# content2 路径 content6 树状目录 done!
class WorkThread3(QThread):
    # 初始化线程
    def __int__(self):
        super(WorkThread3, self).__init__()
    # 线程运行函数
    def run(self):
        global content_2, content_6
        contents=[]
        contents6=[]
        root = ['[root@localhost local]# ~/etc/inittab',
                '[root@localhost local]# vi /etc/sysconfig/network-scripts/ifcfg-eth0',
                '[root@localhost local]# rpm -e --nodeps java-1.7.0-openjdk-1.7.0.45.el6.x86_64',
                '[root@localhost local]# tar -zxvf jdk-8u181-linux-x64.tar.gz',
                '[root@localhost local]# JAVA_HOME=/usr/local/src/jdk8/jdk1.8.0_181',
                '[root@localhost local]# export JAVA_HOME CLASSPATH PATH',
                '[root@localhost local]# MySQL-5.6.34-1.rhel5.x86_64.rpm-bundle.tar',
                '[root@localhost local]# rpm -e --nodeps  mysql-libs-5.1.71-1.el6.x86_64',
                '[root@localhost local]# rant all privileges on *.* to root @% identified by root',
                '[root@localhost local]# /sbin/iptables -I INPUT -p tcp --dport 3306 -j ACCEPT']
        path = ["<font color='#0066FF'>&lt;project</font><font color='#FF0000'>xmlns=</font><font color='#FFFFFF'>'http://maven.apache.org/POM/4.0.0' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'\
  xsi:schemaLocation='http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd'></font>\n",
                "<font color='#0066FF'>   &lt;modelVersion&gt;</font><font color='#00FF00'>4.0.0</font><font color='#0066FF'>&lt;/modelVersion&gt;</font>\n",
                "<font color='#0066FF'>   &lt;groupId&gt;</font><font color='#FFFFFF'>com.analysis.webservice</font><font color='#0066FF'>&lt;/groupId&gt;</font>\n",
                "<font color='#0066FF'>   &lt;artifactId&gt;</font><font color='#FFFFFF'>analysis-webservice</font><font color='#0066FF'>&lt;/artifactId&gt;</font>\n",
                "<font color='#0066FF'>   &lt;version&gt;</font><font color='#00FF00'>0.0.1-SNAPSHOT</font><font color='#0066FF'>&lt;/version&gt;</font>\n",
                "<font color='#0066FF'>   &lt;url&gt;</font><font color='#FFFFFF'>http://maven.apache.org</font><font color='#0066FF'>&lt;/url&gt;</font>\n",
                "<font color='#0066FF'>   &lt;properties&gt;</font>\n",
                "<font color='#0066FF'>      &lt;project.build.sourceEncoding&gt;</font><font color='#FFFFFF'>UTF-8</font><font color='#0066FF'>&lt;/project.build.sourceEncoding&gt;</font>\n",
                "<font color='#0066FF'>   &lt;/properties&gt;</font>\n",
                "<font color='#0066FF'>      &lt;snapshotRepository&gt;</font>\n",
                "<font color='#0066FF'>         &lt;id&gt;</font><font color='#FFFFFF'>snapshots</font><font color='#0066FF'>&lt;/id&gt;</font>\n",
                "<font color='#0066FF'>         &lt;name&gt;</font><font color='#FFFFFF'>Snapshots</font><font color='#0066FF'>&lt;/name&gt;</font>\n",
                "<font color='#0066FF'>      &lt;/snapshotRepository&gt;</font>\n",
                "<font color='#0066FF'>   &lt;/distributionManagement&gt;</font>\n"
                ]
        cnt = 0
        i = 0
        while True:
            if cnt >= 6:
                contents.pop(0)
                if len(contents6) >= 10:
                    contents6.pop(0)
                cnt-=1
            else:
                msg = "<font color='#CCCCFF'>{}<br /></font>".format(random.choice(root))
                if i==14:
                    i = 0
                msg6 = path[i]
                i+=1
                contents.append(msg)
                contents6.append(msg6)
                content_2 = (''.join([x for x in contents]))
                content_6 = (''.join([x for x in contents6]))
                cnt+=1
                time.sleep(0.23)
# content4 色块 content8  content9
class WorkThread4(QThread):
    # 初始化线程
    def __int__(self):
        super(WorkThread4, self).__init__()
    # 线程运行函数
    def run(self):
        global content_4, content_8,content_9
        contents4 =[]
        contents8 = ['ok']
        contents9 = ['ok']
        cnt = 0
        msg_sin4 = ["<font size='10' color='#004020'>██</font>",
                    "<font size='10' color='#006020'>██</font>",
                    "<font size='10' color='#008020'>██</font>",
                    "<font size='10' color='#00a020'>██</font>",
                    "<font size='10' color='#00c020'>██</font>",
                    "<font size='10' color='#00ff20'>██</font>"]
        msg_sin9 = [
            "<font color='#c00040'>[1930:23C0][2015-08-07T00:02:32]</font><font color='#FF0000'>e000:</font> <font color='#FFFFFF'>0x80240017: configure per-machine MSU package.<br /></font>",
            "<font color='#c00040'>[1930:23C0][2015-08-07T00:02:32]</font><font color='#FF0000'>i319:</font> <font color='#FFFFFF'>Applied execute package: crt_14.0_v6.3_x86, restart: None<br /></font>",
            "<font color='#c00040'>[1930:23C0][2015-08-07T00:02:32]</font><font color='#FF0000'>i330:</font> <font color='#FFFFFF'>Removed bundle dependency provider: {28c2d4d6-0707-99118d90b8ba}e.<br /></font>",
            "<font color='#c00040'>[1930:23C0][2015-08-07T00:02:32]</font><font color='#FF0000'>i371:</font> <font color='#FFFFFF'>Updating session, registration key: SOFTWARE\Microsoft\Windows\.<br /></font>",
            "<font color='#c00040'>[1930:23C0][2015-08-07T00:02:32]</font><font color='#FF0000'>i352:</font> <font color='#FFFFFF'>Removing cached bundle: {28c2d4d6-0707-41ac-a8b7-99118d90b8ba}.<br /></font>",
            "<font color='#c00040'>[1930:23C0][2015-08-07T00:02:32]</font><font color='#FF0000'>i399:</font> <font color='#FFFFFF'>Apply complete, result: 0x80240017, ba requested restart:  No.<br /></font>"
        ]
        msg_sin8 = [
            "<font color='#c0a0ff'>Link encap:</font><font color='#FFFFFF'>Ethernet  HWaddr</font><font color='#FFFF99'>00:0C:29:11:30:39 <br /></font>",
            "<font color='#c0a0ff'>inet addr:</font><font color='#FFFFFF'>192.168.134.129</font>  <font color='#c0a0ff'>Bcast:</font><font color='#FFFFFF'>192.168.134.255</font>  <font color='#c0a0ff'>Mask:</font><font color='#FFFFFF'>255.255.255.0<br /></font>",
            "<font color='#c0a0ff'>inet6 addr:</font> <font color='#FFFFFF'>fe80::20c:29ff:fe11:3039/64</font> <font color='#c0a0ff'>Scope:</font><font color='#FFFFFF'>Link<br /></font>",
            "<font color='#c0a0ff'>UP BROADCAST RUNNING MULTICAST  MTU:</font><font color='#FFFFFF'>1500</font>  <font color='#c0a0ff'>Metric:</font><font color='#FFFFFF'>1<br /></font>",
            "<font color='#c0a0ff'>RX packets:</font><font color='#FFFFFF'>19731</font> <font color='#c0a0ff'>errors:</font><font color='#FFFFFF'>0</font> <font color='#c0a0ff'>dropped:</font><font color='#FFFFFF'>0</font> <font color='#c0a0ff'>overruns:</font><font color='#FFFFFF'>0</font> <font color='#c0a0ff'>frame:</font><font color='#FFFFFF'>0<br /></font>",
            "<font color='#c0a0ff'>TX packets:</font><font color='#FFFFFF'>502</font> <font color='#c0a0ff'>errors:</font><font color='#FFFFFF'>0</font> <font color='#c0a0ff'>dropped:</font><font color='#FFFFFF'>0</font> <font color='#c0a0ff'>overruns:</font><font color='#FFFFFF'>0</font> <font color='#c0a0ff'>carrier:</font><font color='#FFFFFF'>0<br /></font>"
            "<font color='#c0a0ff'>collisions:</font><font color='#FFFFFF'>0</font> <font color='#c0a0ff'>txqueuelen:</font><font color='#FFFFFF'>1000 <br /></font>"
            "<font color='#c0a0ff'>RX bytes:</font><font color='#FFFFFF'>1248492 (1.1 MiB)</font>  <font color='#c0a0ff'>TX bytes:</font><font color='#FFFFFF'>58905 (57.5 KiB)<br /></font>"
        ]

        while True:
            if cnt == 0:
                contents4.append("<font size='3' color='white'>------------SYSTEM INFO---------<br /></font>"
                                 "<font size='2' color='white'>[root@S-CentOS home]# cat /proc/version<br /></font>"
                                 "<font size='2' color='white'>Linux version 2.6.32-431.el6.x86_64 (mockbuild@c6b8.bsys.dev.centos.org)<br /></font>"
                                 "<font size='2' color='white'>gcc version 4.4.7 20120313 (Red Hat 4.4.7-4) (GCC) ) #1 SMP Fri<br /></font>"
                                 "<font size='2' color='white'>Nov 22 03:15:09 UTC 2013<br /></font>")
                contents8.append("<font color='white'>Distributor ID: CentOS Description: CentOS release 6.5 (Final)<br /></font>"
                                 "<font color='white'>Release: 6.5<br /></font>"
                                 "<font color='white'>Codename: Final<br /></font>")
                contents9.append("<font color='white'>[2454:2284][2015-08-07T00:02:32]e000:0x80240017: execute MSU package.<br /></font>")
                cnt+=1
            if cnt >= 5:
                contents4.pop(1)
                contents8.pop(1)
                contents9.pop(1)
                cnt-=1
            else:
                msg4 = ''.join(random.choices(msg_sin4,k=5))
                msg8 = ''.join(random.choice(msg_sin8))
                msg9 = ''.join(random.choice(msg_sin9))
                contents4.append(msg4)
                contents8.append(msg8)
                contents9.append(msg9)
                content_4 = (''.join([x for x in contents4]))
                content_8 = (''.join([x for x in contents8]))
                content_9 = (''.join([x for x in contents9]))
                cnt+=1
                time.sleep(0.3)


# content10 代码流刷新  done!
class WorkThread5(QThread):
    # 初始化线程
    def __int__(self):
        super(WorkThread5, self).__init__()
    # 线程运行函数
    def run(self):
        global content_10
        content_10 = "<font color='green'>connecting to Zion host<br /></font>"
        def AddStr(addstr):
            content_10 = "<font color='green'>connecting to Zion host{}<br /></font>".format(addstr)
            return content_10
        time.sleep(1)
        content_10 = AddStr('.')
        time.sleep(1)
        content_10 = AddStr('..')
        time.sleep(1)
        content_10 = AddStr('...')
        time.sleep(1)
        content_10 = AddStr('... SUCCEEDED')
        time.sleep(0.5)
        content_10 = AddStr('... SUCCEEDED<br />enter username:Stark')
        time.sleep(0.2)
        content_10 = AddStr('... SUCCEEDED<br />enter username:Stark<br />enter password: ******')
        time.sleep(0.2)
        content_10 = AddStr('... SUCCEEDED<br />enter username:Stark<br />enter password: ******<br />logging in')
        time.sleep(0.2)
        content_10 = AddStr('... SUCCEEDED<br />enter username:Stark<br />enter password: ******<br />logging in.')
        time.sleep(0.2)
        content_10 = AddStr('... SUCCEEDED<br />enter username:Stark<br />enter password: ******<br />logging in..')
        time.sleep(0.2)
        content_10 = AddStr('... SUCCEEDED<br />enter username:Stark<br />enter password: ******<br />logging in...')
        time.sleep(0.2)
        content_10 = AddStr('... SUCCEEDED<br />enter username:Stark<br />enter password: ******<br />logging in... SUCCEEDED')
        time.sleep(0.2)
        content_10 = AddStr(
            '... SUCCEEDED<br />enter username:Stark<br />enter password: ******<br />logging in... SUCCEEDED<br />Hello,Stark.')
        time.sleep(1)
        charts = [*[chr(x) for x in range(65, 123) if x not in range(91, 97)], *map(str, range(10))]
        cnt = 0
        contents = []
        contents.append(content_10)
        while True:
            if cnt >= 6:
                contents.pop(0)
                cnt-=1
            else:
                msg1 = (' ' * 3).join(random.choices(charts, k=90))
                msg = "<font color='#00FF00'>{}</font>".format(msg1)
                contents.append(msg)
                content_10 = (''.join([x for x in contents]))
                cnt += 1
                time.sleep(0.02) #cont

class plotwindows(QtWidgets.QWidget):
    def __init__(self):
        super(plotwindows,self).__init__()
        grid = QGridLayout()
        self.edita1 = QTextEdit()
        self.edita2 = QTextEdit()
        self.edita3 = QTextEdit()
        self.edita4 = QTextEdit()
        self.edita5 = QTextEdit()
        self.edita6 = QTextEdit()
        self.edita7 = QTextEdit()
        self.edita8 = QTextEdit()
        self.edita9 = QTextEdit()
        self.edita10 = QTextEdit()

        self.edita1.setStyleSheet("background:black")
        self.edita2.setStyleSheet("background:black")
        self.edita3.setStyleSheet("background:black")
        self.edita4.setStyleSheet("background:black")
        self.edita5.setStyleSheet("background:black")
        self.edita6.setStyleSheet("background:black")
        self.edita7.setStyleSheet("background:black")
        self.edita8.setStyleSheet("background:black")
        self.edita9.setStyleSheet("background:black")
        self.edita10.setStyleSheet("background:black")

        grid.addWidget(self.edita1, 0,0)
        grid.addWidget(self.edita2, 0,1)
        grid.addWidget(self.edita3, 0,2)
        grid.addWidget(self.edita4, 0,3)
        grid.addWidget(self.edita5, 1,0)
        grid.addWidget(self.edita6, 1,1)
        grid.addWidget(self.edita7, 1,2,1,2)
        grid.addWidget(self.edita8, 2,0)
        grid.addWidget(self.edita9, 2,1)
        grid.addWidget(self.edita10, 2,2,1,2)
        desktop = QApplication.desktop()
        w = desktop.width()
        h = desktop.height()
        grid.setSpacing(0)
        self.setLayout(grid)
        self.resize(w,h)
        self.Mytimer()

    def Mytimer(self):
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(100)
    def update(self):
        self.edita1.setHtml(str(content_1))
        self.edita2.setHtml(str(content_2))
        self.edita3.setHtml(str(content_3))
        self.edita4.setHtml(str(content_4))
        self.edita5.setHtml(str(content_5))
        self.edita6.setHtml(str(content_6))
        self.edita7.setHtml(str(content_7))
        self.edita8.setHtml(str(content_8))
        self.edita9.setHtml(str(content_9))
        self.edita10.setHtml(str(content_10))

def mainwindows():

    app = QtWidgets.QApplication(sys.argv)
    new = plotwindows()
    # new.showFullScreen()
    new.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    workThread1 = WorkThread1()
    workThread2 = WorkThread2()
    workThread3 = WorkThread3()
    workThread4 = WorkThread4()
    workThread5 = WorkThread5()
    workThread1.start()
    workThread2.start()
    workThread3.start()
    workThread4.start()
    workThread5.start()
    mainwindows()
