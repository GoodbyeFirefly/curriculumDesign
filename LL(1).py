# 对应博客讲解链接
# https://blog.csdn.net/qq_41528502/article/details/103957028


# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file 'D:\testPyQt5\PyQt5_code\test2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
 
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
 
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHeaderView
 
 
class Ui_Form(object):
    generative = []  # 存放textEdit中的文法
    generative_ = {}  # 字典存放处理过的产生式(一个key对应一个list)
    input = ''  # 存放输入串
    ter_colt = []
    non = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
    non_colt = []
    ter_colt_copy = []  # 去掉空字的终结符集合
    first_set = {}  # 字典存放处理first集(一个key对应一个list)
    follow_set = {}  # 字典存放处理follow集(一个key对应一个list)
    analyze_table = []  # 预测分析表
    state = 0  # 状态，0：Null；1：Accepted；2：Error；3：产生式含有左递归
    message = '' # 记录状态框的输出信息
    judge = {}  # 用以判断间接左递归 存放"key=非终结符，value=对应产生式的首个非终结符" 以字典模拟树
    judge_list = []
    recursion_tag = -1  # 是否含左递归的标记，-1：尚未确定，0:不含 1:含直接左递归，2：含间接左递归
    directRecList = []  # 记录含直接左递归的非终结符
 
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(954, 610)
 
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(320, 10, 20, 571))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
 
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(350, 20, 571, 501))
        self.tabWidget.setObjectName("tabWidget")
 
        self.PROCESS = QtWidgets.QWidget()
        self.PROCESS.setObjectName("PROCESS")
        self.tableView_3 = QtWidgets.QTableView(self.PROCESS)
        self.tableView_3.setGeometry(QtCore.QRect(0, 0, 561, 481))
        self.tableView_3.setObjectName("tableView_3")
        self.tabWidget.addTab(self.PROCESS, "")
 
        self.FIRST = QtWidgets.QWidget()
        self.FIRST.setObjectName("FIRST")
        self.tableView = QtWidgets.QTableView(self.FIRST)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 561, 481))
        self.tableView.setObjectName("tableView")
        self.tabWidget.addTab(self.FIRST, "")
        # self.model = QStandardItemModel(20,10)
 
        self.FOLLOW = QtWidgets.QWidget()
        self.FOLLOW.setObjectName("FOLLOW")
        self.tableView_2 = QtWidgets.QTableView(self.FOLLOW)
        self.tableView_2.setGeometry(QtCore.QRect(0, 0, 561, 481))
        self.tableView_2.setObjectName("tableView_2")
        self.tabWidget.addTab(self.FOLLOW, "")
 
        self.ANALYZE = QtWidgets.QWidget()
        self.ANALYZE.setObjectName("ANALYZE")
        self.tableView_4 = QtWidgets.QTableView(self.ANALYZE)
        self.tableView_4.setGeometry(QtCore.QRect(0, 0, 561, 481))
        self.tableView_4.setObjectName("tableView_4")
        self.tabWidget.addTab(self.ANALYZE, "")
 
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 550, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btnRun_Clicked)  # 将按钮与函数 btnRun_Clicked绑定
 
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(350, 550, 54, 12))
        self.label_3.setObjectName("label_3")
 
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(400, 540, 481, 31))
        self.textBrowser.setObjectName("textBrowser")
 
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 40, 258, 481))
        self.widget.setObjectName("widget")
 
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
 
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
 
        self.verticalLayout.addWidget(self.label)
 
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
 
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
 
        self.verticalLayout.addItem(spacerItem)
 
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
 
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
 
        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
 
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PROCESS), _translate("Form", "分析过程"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FIRST), _translate("Form", "FIRST集"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.FOLLOW), _translate("Form", "FOLLOW集"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ANALYZE), _translate("Form", "分析表"))
        self.pushButton.setText(_translate("Form", "Run"))
        self.label_3.setText(_translate("Form", "State:"))
        self.label.setText(_translate("Form", "文法(相同非终结符产生式用|隔开,不要回车)："))
        self.label_2.setText(_translate("Form", "输入："))
 
    def isTerminal(self, c):  # 若c介于A-Z之间则认为是非终结符(注意添加 self参数)
        if c < 'A' or c > 'Z':
            return True
        else:
            return False
 
    def getFirstSet(self, target):  # 此函数递归调用
        for VN in self.generative_.keys():  # 遍历每个非终结符,直到找到target
            if VN == target:
                for formula in self.generative_[VN]:  # 遍历非终结符的所有产生式
                    time = 0  # 记录产生式右侧的非终结符的first集中含ε的个数，若等于右侧产生式的长度，则将ε加入产生式左侧非终结符的first集中
                    for c in formula:  # 分析产生式
                        if self.isTerminal(c):  # 若为终结符则直接加入first集
                            self.first_set.setdefault(VN, []).append(c)  # 由于set不支持索引 故使用list而不是set()
                            break
                        else:
                            self.getFirstSet(c)
                            if 'ε' in self.first_set[c]:  # self.first_set[c]其实是指一个list
                                time += 1
                            else:
                                for value in self.first_set[c]:
                                    self.first_set.setdefault(VN, []).append(value)
                    if time == len(formula):
                        self.first_set.setdefault(VN, []).append('ε')
 
    def getFollowSet(self, target):
        for VN in self.generative_.keys():
            for formula in self.generative_[VN]:
                length = len(formula)
                for i in range(len(formula)):
                    flag = 1  # 作为判断E->ABC...中 A后面的终结符的first集中是否含ε的标志 1：含有
                    if formula[i] == target and flag == 1 and i < length - 1:
                        pos = i
                        cha = formula[pos + 1]
                        if self.isTerminal(cha):  # 例如E->Ab，求A的follow集 发现A后为终结符 则直接跳过此产生式
                            self.follow_set.setdefault(target, []).append(cha)
                            break
                        else:  # 此循环用于解决E->ABCDe,类似的target后多个终结符的first集含有$的情况
                            while flag == 1 and pos < len(formula) - 1:
                                if self.isTerminal(cha):
                                    self.follow_set.setdefault(VN, []).append(cha)
                                    flag = 0
                                    break
                                else:
                                    tag = 0  # 标记当前非终结符的first集中是否含ε， 0：否
                                    for j in range(len(self.first_set[cha])):
                                        cha1 = self.first_set[cha][j]
                                        if cha1 != 'ε':
                                            self.follow_set.setdefault(target, []).append(cha1)
                                        else:
                                            tag = 1
                                    if tag == 0:  # 若当前非终结符的first集中不否含ε， 则可分析下一个产生式
                                        flag = 0
                                    pos += 1
                            if pos == len(formula) - 1 and target != VN:
                                self.getFollowSet(VN)
                                for cha2 in self.follow_set[VN]:
                                    self.follow_set.setdefault(target, []).append(cha2)
 
                    elif target != VN and formula[i] == target and flag == 1 and i == length - 1:
                        self.getFollowSet(VN)
                        for cha2 in self.follow_set[VN]:
                            self.follow_set.setdefault(target, []).append(cha2)
 
    def getAnalyzeTable(self):
        for VN in self.non_colt:
            pos_x = self.non_colt.index(VN)
            for formula in self.generative_[VN]:
                for c in formula:
                    if self.isTerminal(c) and c != 'ε':  # 分析表中的终结符无ε
                        pos_y = self.ter_colt_copy.index(c)
                        self.analyze_table[pos_x][pos_y] = formula
                        break
                    elif c != 'ε':  # c为非终结符时
                        flag = 0  # 若flag为0表明非终结符的first集中不含ε
                        for c1 in self.first_set[c]:
                            if c1 == 'ε':
                                for c2 in self.follow_set[VN]:
                                    pos_y = self.ter_colt_copy.index(c2)
                                    self.analyze_table[pos_x][pos_y] = 'ε'
                                    flag = 1
                            else:
                                pos_y = self.ter_colt_copy.index(c1)
                                self.analyze_table[pos_x][pos_y] = formula
                        if flag == 0:
                            break  # 分析下一个产生式
                    else:  # c为空字时
                        for c2 in self.follow_set[VN]:
                            pos_y = self.ter_colt_copy.index(c2)
                            self.analyze_table[pos_x][pos_y] = 'ε'
 
    def analyzeProcess(self):
        analyse_stack = []
        analyse_stack.append('#')
        analyse_stack.append(self.non_colt[0])  # 分析栈
        # print(analyse_stack)
        remain_part = list(self.input)  # 剩余输入串
        formula = ''  # 所用产生式
        action = ['初始化']  # 动作(采用列表形式)
        time = 0  # 记录步骤数
 
        self.model_3 = QStandardItemModel(30, 4)
        label_x = ['分析栈', '剩余输入串', '所用产生式', '动作']
        self.model_3.setHorizontalHeaderLabels(label_x)
 
        temp = ''.join(analyse_stack)
        item = QStandardItem(temp)
        self.model_3.setItem(0, 0, item)
        temp = ''.join(remain_part)
        item = QStandardItem(temp)
        self.model_3.setItem(0, 1, item)
        item = QStandardItem(formula)
        self.model_3.setItem(0, 2, item)
        temp = ','.join(action)
        item = QStandardItem(temp)
        self.model_3.setItem(0, 3, item)
 
        # print(analyse_stack)
 
        while not (len(analyse_stack) == 1 and len(remain_part) == 1):
            left = analyse_stack[-1]
            right = remain_part[0]
 
            if not self.isTerminal(left):
                formula = self.analyze_table[self.non_colt.index(left)][self.ter_colt_copy.index(right)]
            if left == right:
                time += 1
                del analyse_stack[-1]
                del remain_part[0]
                formula = ''
                action = ['GETNEXT']
                temp = ''.join(analyse_stack)
                item = QStandardItem(temp)
                self.model_3.setItem(time, 0, item)
                temp = ''.join(remain_part)
                item = QStandardItem(temp)
                self.model_3.setItem(time, 1, item)
                item = QStandardItem(formula)
                self.model_3.setItem(time, 2, item)
                temp = ','.join(action)
                item = QStandardItem(temp)
                self.model_3.setItem(time, 3, item)
            else:
                if formula == 0:
                    self.state = 2  # 输入串无法解析
                    self.message = 'Error: There is no way between \'' + left + '\' and \'' + right + '\''
                    break
 
                else:
                    if formula == 'ε':
                        time += 1  # 次数加一
                        del analyse_stack[-1]  # POP
                        formula = left + '->' + 'ε'
                        action = ['POP']
                        temp = ''.join(analyse_stack)
                        item = QStandardItem(temp)
                        self.model_3.setItem(time, 0, item)
                        temp = ''.join(remain_part)
                        item = QStandardItem(temp)
                        self.model_3.setItem(time, 1, item)
                        item = QStandardItem(formula)
                        self.model_3.setItem(time, 2, item)
                        temp = ','.join(action)
                        item = QStandardItem(temp)
                        self.model_3.setItem(time, 3, item)
                    else:
                        time += 1
                        del analyse_stack[-1]  # POP
                        li = list(formula)
                        li.reverse()
                        analyse_stack += li
                        formula = left + '->' + formula
                        act = 'PUSH(' + ''.join(li) + ')'
                        action = ['POP', act]
                        temp = ''.join(analyse_stack)
                        item = QStandardItem(temp)
                        self.model_3.setItem(time, 0, item)
                        temp = ''.join(remain_part)
                        item = QStandardItem(temp)
                        self.model_3.setItem(time, 1, item)
                        item = QStandardItem(formula)
                        self.model_3.setItem(time, 2, item)
                        temp = ','.join(action)
                        item = QStandardItem(temp)
                        self.model_3.setItem(time, 3, item)
 
        if len(analyse_stack) == 1 and len(remain_part) == 1:
            self.state = 1
        self.tableView_3.horizontalHeader().setStretchLastSection(True)
        self.tableView_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_3.setModel(self.model_3)
 
    def isLeftRecursion(self, target):  # 递归判断间接左递归
        self.judge_list.append(target)
        if target in self.judge and self.recursion_tag == -1:  # 是否递归还未确定
            for V in self.judge[target]:
                if self.judge_list.count(V) > 0:  # 若列表中已含有当前非终结符
                    self.judge_list.append(V)
                    self.state = 3
                    self.recursion_tag = 2
                    return
 
                self.isLeftRecursion(V)
            if self.recursion_tag == 0:
                self.judge_list.remove(target)
        elif target not in self.judge:  # 目标元素不在间接左递归的judge中 eg.S->ab|c 递归中断 即循环链条中断
            self.recursion_tag = 0
            return
 
    def getNewNon(self):  # 返回新的非终结符
        for cha in self.non:
            if cha not in self.non_colt:
                return cha
 
    def delRecursion(self):
        if 'ε' not in self.ter_colt:
            self.ter_colt.append('ε')
        if self.recursion_tag == 1:
            for cha in self.directRecList:  # 消除直接左递归
                newNon = self.getNewNon()  # 获得新标识符
                self.non_colt.append(newNon)  # 加入非终结符集合
                for formula in self.generative_[cha]:  # 遍历此非终结符的所有产生式
                    if cha == formula[0]:
                        s1 = formula[1:]  # E->E+T 提取右侧产生式中的+T
                        formula_ = s1 + newNon  # 替换原先的产生式
                        self.generative_.setdefault(newNon, []).append(formula_)  # 为新终结符创建产生式
                        self.generative_.setdefault(newNon, []).append('ε')  # 为新终结符创建产生式
                        self.generative_[cha].remove(formula)  # 删除含直接左递归因素的产生式
                        i = 0 # 由于下面循环中对循环条件generative_做出修改 迭代顺序会与想象中不同 故用i作为下标进行处理
                        for formula1 in self.generative_[cha]:  # 修改其余产生式
                            formula4 = formula1 + newNon
                            self.generative_[cha].remove(formula1)
                            self.generative_.setdefault(cha).insert(i, formula4)
                            i += 1
        if self.recursion_tag == 2:  # 间接左递归 以产生式 S->Qc|c;Q->Rb|b;R->Sa|a为例
            #print(self.generative_)
            judge_list_copy = self.judge_list.copy()
            del judge_list_copy[-1]  # 去掉[S,Q,R,S]中的S
 
            while len(judge_list_copy) > 1:
                # print(self.non_colt)
                for VN in self.non_colt:  # 遍历所有产生式 注意是所有
                    for formula2 in self.generative_[VN]:
                        flag = 0  # 判断产生式中是否含此符号
                        for cha1 in formula2:
                            if cha1 == judge_list_copy[-1]:  # 等于judge_list_copy的末尾元素 自下向上进行替换
                                flag = 1
                                break
                        if flag == 1:  # 其中一个产生式含待替换的VN 需替换的次数为VN的产生式个数
                            s2 = formula2  # 副本
                            if formula2 in self.generative_[VN]:
                                self.generative_[VN].remove(formula2)  # 删除该产生式
 
                            for formula3 in self.generative_[judge_list_copy[-1]]:  # 用R的各产生式替换
                                s3 = s2
                                s3 = s3.replace(judge_list_copy[-1], formula3)
                                self.generative_.setdefault(VN, []).append(s3)  # 插入产生式集中
                self.non_colt.remove(judge_list_copy[-1])
                del self.generative_[judge_list_copy[-1]]
                del judge_list_copy[-1]
                print(self.generative_)
 
            # 至此 会出现 S->Sabc|abc|bc|c 再消除一次直接左递归即可
            newNon = self.getNewNon()  # 获得新标识符
            self.non_colt.append(newNon)  # 加入非终结符集合
            cha = self.judge_list[0]
            for formula in self.generative_[cha]:  # 遍历此非终结符的所有产生式
                if cha == formula[0]:  # 找到含左递归因子的产生式
                    s1 = formula[1:]  # E->E+T 提取右侧产生式中的+T
                    formula_ = s1 + newNon  # 替换原先的产生式
                    self.generative_.setdefault(newNon, []).append(formula_)  # 为新终结符创建产生式
                    self.generative_.setdefault(newNon, []).append('ε')  # 为新终结符创建产生式
                    self.generative_[cha].remove(formula)  # 删除含直接左递归因素的产生式
                    print(self.generative_[cha])
                    print(123)
 
                    '''此方法不行！！！移除元素，并在末尾添加元素会使迭代过程超出预期
                    for other in self.generative_[cha]:  # 修改其余产生式
                        s4 = other + newNon
                        self.generative_[cha].remove(other)
                        self.generative_.setdefault(cha, []).append(s4)
                    print(self.generative_[cha])
                    break
                    '''
                    i = 0
                    for other in self.generative_[cha]:  # 修改其余产生式
                        s4 = other + newNon
                        self.generative_[cha].remove(other)
                        self.generative_.setdefault(cha).insert(i, s4)
                        i += 1
                    print(self.generative_[cha])
                    break
 
    # 将形如E->A|B|$的产生式处理为{'E':['A','B','$'],...}的字典形式
    def inputAndSolve(self):
        self.generative = self.textEdit.toPlainText().split('\n')
        self.input = '' + self.lineEdit.text()
        terminal = ''  # 临时存放非终结符
        # 规范化产生式
        for temp in self.generative:
            s = ''  # 临时存放产生式
            i = 0
            while i < len(temp):
                if i == 0:
                    terminal = temp[0]
                    if temp[0] not in self.non_colt:
                        self.non_colt.append(temp[0])
                    i += 3  # 跳过E->A中的->
                elif i >= 3:
                    if temp[i] == '|':
                        i += 1
                        self.generative_.setdefault(terminal, []).append(s)
                        s = ''
                        continue
                    else:
                        if self.isTerminal(temp[i]):
                            if temp[i] not in self.ter_colt:
                                self.ter_colt.append(temp[i])
                        s += temp[i]
                        i += 1
            self.generative_.setdefault(terminal, []).append(s)  # 每个非终结符的最后一个产生式需要
        self.ter_colt_copy = self.ter_colt
        if 'ε' in self.ter_colt_copy:
            self.ter_colt_copy.remove('ε')
        self.ter_colt_copy.append('#')
 
        '''RECURSION'''
        # 这里做简化处理 认为文法中只存在间接左递归或直接左递归中的一种  且间接左递归只含有一条循环链
        # 若想完善此点 可用while循环不断判断、消除 直到确认无递归出现为止
 
        for VN in self.generative_.keys():  # 寻找并判断直接左递归
            for formula in self.generative_[VN]:
                cha1 = formula[0]
 
                if not self.isTerminal(cha1):
                    self.judge.setdefault(VN, []).append(cha1)  # 记录每个非终结符的各个产生式的首个非终结符 为消除间接左递归准备
                    if VN == cha1:
                        self.directRecList.append(cha1)  # 记录含直接左递归的非终结符
                        self.recursion_tag = 1  # 确定为直接左递归
                        self.state = 3
                        self.message += 'DirectLeftRecurtion:'
                        s = VN + '->' + formula + '\n'
                        self.message += s
 
        # print(self.judge)为消除间接左递归准备
        if self.recursion_tag != 1:  # 若非直接左递归则继续
            self.isLeftRecursion(self.non_colt[0])
            if self.recursion_tag == 2:  # 若此时确定recursion_tag为2 则为间接左递归
                self.message = 'IndirectLeftRecurtion:'
                self.message += '->'.join(self.judge_list)
                # print(self.message)
        # print(self.recursion_tag)
 
        if self.recursion_tag == 1 or self.recursion_tag == 2:  # 含有左递归
            self.delRecursion()
            textEditBoxList = []  # 显示修改后的文法
            textEditBoxList.extend(self.generative)
            textEditBoxList.append(' ')
            bound = '***左递归消除后的文法为***'
            textEditBoxList.append(bound)
            textEditBoxList.append(' ')
            for VN in self.generative_:
                str = VN + '->'
                for formula in self.generative_[VN]:
                    if formula == self.generative_[VN][-1]:
                        str = str + formula
                    else:
                        str = str + formula + '|'
                textEditBoxList.append(str)
            textEditBoxStr = '\n'.join(textEditBoxList)
            self.textEdit.setText(textEditBoxStr)
 
        self.state = 0  # 若含有左递归 则已消除
        print(self.generative_)
 
        # 接下来进行过程的求解
        if self.state == 0:
            '''FIRST'''
            # 求first集
            for VN in self.generative_.keys():
                self.getFirstSet(VN)
            # 去除first集key对应的list中重复的非终结符
            for VN in self.first_set:
                test = list(set(self.first_set[VN]))
                self.first_set[VN] = test
            # 将first集作为数据源以QTableView的形式展示出来
            self.model = QStandardItemModel(len(self.non_colt), len(self.ter_colt))
            label_y = []
            for s in self.non_colt:
                label_y.append(s)
            self.model.setVerticalHeaderLabels(label_y)
            for row in range(len(self.non_colt)):
                for column in range(len(self.first_set[self.non_colt[row]])):
                    item = QStandardItem(self.first_set[self.non_colt[row]][column])
                    self.model.setItem(row, column, item)
            self.tableView.horizontalHeader().setStretchLastSection(True)
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableView.setModel(self.model)
            # print(self.first_set)
 
            '''FOLLOW'''
            # 求follow集
            for VN in self.non_colt:
                if VN == self.generative[0][0]:  # 在开始符E的follow集中加入#
                    self.follow_set.setdefault(VN, []).append('#')
                self.getFollowSet(VN)
            # 去除follow集key对应的list中重复的非终结符
            for VN in self.follow_set:
                test = list(set(self.follow_set[VN]))
                self.follow_set[VN] = test
            # 将follow集作为数据源以QTableView的形式展示出来
            self.model_2 = QStandardItemModel(len(self.non_colt), len(self.ter_colt))
            self.model_2.setVerticalHeaderLabels(label_y)
            for row in range(len(self.non_colt)):
                for column in range(len(self.follow_set[self.non_colt[row]])):
                    item = QStandardItem(self.follow_set[self.non_colt[row]][column])
                    self.model_2.setItem(row, column, item)
            self.tableView_2.horizontalHeader().setStretchLastSection(True)
            self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableView_2.setModel(self.model_2)
 
            '''ANALYZE'''
            self.analyze_table = [[0 for col in range(len(self.ter_colt))] for row in range(len(self.non_colt))]
            self.getAnalyzeTable()
            self.model_4 = QStandardItemModel(len(self.non_colt), len(self.ter_colt_copy))
            label_x = []
            label_y = []
            for s in self.ter_colt_copy:
                label_x.append(s)
            for s in self.non_colt:
                label_y.append(s)
            self.model_4.setHorizontalHeaderLabels(label_x)
            self.model_4.setVerticalHeaderLabels(label_y)
            for row in range(len(self.non_colt)):
                for column in range(len(self.ter_colt_copy)):
                    item = QStandardItem(self.analyze_table[row][column])
                    self.model_4.setItem(row, column, item)
            self.tableView_4.horizontalHeader().setStretchLastSection(True)
            self.tableView_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableView_4.setModel(self.model_4)
            print(self.analyze_table)
 
            '''PROCESS'''
            self.analyzeProcess()
 
        if self.state == 0 and self.recursion_tag == 0:
            self.message = 'Null'
        elif self.state == 1 and self.recursion_tag == 0:
            self.message = 'Accepted!\n'
        # state等于2，3的情况已经在分析过程中添加到message中
        self.textBrowser.setText(self.message)
 
    def btnRun_Clicked(self):
 
        self.inputAndSolve()
 
 
if __name__ == "__main__":
    import sys
 
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
