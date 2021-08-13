import time
import xlwt
import os
class FOS (Exception):
    def _init_ (self,value):
        self.value = value
    def _str_ (self):
        return(self.value)
def fose ():
    raise FOS
class MONG (Exception):
    def _init_ (self,value):
        self.value = value
    def _str_ (self):
        return(self.value)
def monge ():
    raise MONG
def hi ():
    图标 = ['■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■',
        '',
        '□■■■□  □□□  ■□□□□  ■■■■■  ■□□□■  ■■■■■',
        '□□■□□  □□□  ■□□□□  ■□□□■  ■□□□■  ■□□□□',
        '□□■□□  □□□  ■□□□□  ■□□□■  □■□■□  ■■■■■',
        '□□■□□  □□□  ■□□□□  ■□□□■  □■□■□  ■□□□□',
        '□■■■□  □□□  ■■■■■  ■■■■■  □□■□□  ■■■■■',
        '',
        '■■■■■  ■■■■■  ■■■■■  □□■□□',
        '■□□□□  ■□□□■  ■□□□□  □□■□□',
        '■■■■■  ■□□□■  ■■■■■  □□■□□',
        '■□□□□  ■□□□■  □□□□■  □□□□□',
        '■□□□□  ■■■■■  ■■■■■  □□■□□',
        '',
        '■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■']
    i = 0
    print('欢迎使用FOS中文版！')
    time.sleep(2)
    for i in 图标 :
        time.sleep(0.15)
        print(i)
    I = ['加载中，请稍候']
    s = 0
    for s in range(3*4) :
        for i in I :
            print(i, end = '')
            i = s % 4
            print('•' * i)
            time.sleep(0.25)
    print('加载成功！！！')
    time.sleep(1)
    print('\f\r\t\v\n'*1000)
    print('\033[31m自打开本软件之时起，便默认同意本《协议》\n输入“协议”         以阅读并确认\033[0m')
    for i in 图标 :
        print(i)
def Help ():
    HElp = ['\033[34;1m===============',
        'Open打开一个文件',
        'Write向一个文件写入文本',
        'Creat创建一个文件并打开',
        'Close关闭并保存一个文件',
        'Open_Append_Close以追加的方式打开文件，写入文本并保存(简称Oac)',
        'Read打开并读取所有文本（简称Orac）',
        'Mdrd创建一个文件夹(简称md)',
        'Rename重命名文件夹',
        'Renames重命名文件',
        'Dels删除文件夹',
        'Del删除文件',
        'Chdir更改工作目录',
        'Word按照fos标准码编译字符串',
        'Fosw批量按照fos码编译字符串',
        'Decode译码器',
        'tree -0查看目录下所有文件(目录)',
        'Tree 查看目录下所有文件(目录)(包括子目录下的文件和子目录的目录。。。)',
        'Mong打开并查看.mong图片',
        'Calculator 计算器(简称Jsq)',
        'Su_shu计算Min到Max之间的所以质数or素数(简称Ss)',
        'Var定义值',
        'List定义列表(简称Lis)',
        'Time获取并显示当前时间',
        'Cdt倒计时',
        'Hex转十六进制',
        'Oct转八进制',
        'Bin转二进制',
        'Clean up the screen清屏(简称Cls或Clear)',
        'Help帮助',
        'Exit退出',
        '===============\033[0m']
    HELp = 0
    for HELp in HElp :
        print(HELp)
def x_xl (x_name='x.x',xl_name='xl.xls'):
    with open(str(x_name),'r') as fo:
        z=fo.readlines()
        lits=[]
        lists=[]
        for i in z:
            i=i.replace('\n','')
            i=i.replace('\r','')
            i=i.replace('\t','    ')
            lits=i.split('//')
            lists.append(lits)
        fo.close()
        fo=xlwt.Workbook(encoding='utf-8')
        table=fo.add_sheet('main', cell_overwrite_ok=True)
        style=xlwt.XFStyle()
        font=xlwt.Font()
        font.name='Times New Roman'
        font.bold=True
        font.underline=False
        font.italic=False
        style.font=font
        x=0;y=0
        for y in range(256):
            for x in range(256):
                try:
                    text=lists[y][x]
                except:
                    text=''
                if '&&'in text:
                    table.write(y,x,text,style)
                else:
                    table.write(y,x,text)
        fo.save(str(xl_name))
    return True
def x_list (x_name='x.x'):
    with open(str(x_name),'r') as fo:
        z=fo.readlines()
        lits=[]
        lists=[]
        for i in z:
            i=i.replace('\n','')
            i=i.replace('\r','')
            i=i.replace('\t','    ')
            lits=i.split('//')
            lists.append(lits)
        fo.close()
        return lists
def x_str (x_name='x.x'):
    with open(str(x_name),'r') as fo:
        z=fo.readlines()
        lits=[]
        lists=[]
        for i in z:
            i=i.replace('\n','')
            i=i.replace('\r','')
            i=i.replace('\t','    ')
            lits=i.split('//')
            lists.append(lits)
        fo.close()
        texts=''
        for x in lists:
            texts=texts+'\n '+'*-----'*len(x)+'\n'
            for y in x:
                text=y
                if '&&'in text:
                    texts+=' | \033[51m%s\033[0m'%(text)
                else:
                    texts+=' | %s'%(text)
            texts+='|'
        texts=texts+'\n '+'*-----'*len(x)+'\n'
        return texts
true,false=True,False;null,none=None
