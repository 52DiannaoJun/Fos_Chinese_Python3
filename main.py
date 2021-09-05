# !/usr/bin/env python
#coding = utf-8
try:
    import os
    import sys
    import time
    import math
    import datetime
    import stat
    import glob
    import calendar
    import xlwt
    import mods
    import exp as p
    import mod
except:
    print('You need os, sys, time, math, datetime, stat, glod, calendar and xlwt modules.')
    print('Or,Your mods and exp modules are lost (which means you may have downloaded pirated software)')
    exit()
#导入模块

print(os.getcwd())
k = open('logs.log','a+')
g = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
k.write('{\n    \"%s\"\n' %(g))
k.write('\n')
g = '\n▄\n'
k.close()
for k in range(3):
    for k in range(3) :
        print(g)
        time.sleep(0.05)
    print()
    time.sleep(0.75)
#初始化

def log (mode,a = None):#日志系统
    o = os.open('logs.log',os.O_WRONLY|os.O_CREAT)
    os.close(o)
    OPEN = open('logs.log','a+')
    if(mode == 'open'):
        s = '    \"open\"    :'
    elif(mode == 'creat'):
        s = '    \"creat\"   :'
    elif(mode == 'sign'):
        s = '    \"Sign in\" :'
    elif(mode == 'close'):
        s = '    \"close\"   :'
    elif(mode == 'r'):
        s = '    \"r\"       :'
    elif(mode == 'exit'):
        s = '    \"exit\"    :'
    elif(mode == 'del'):
        s = '    \"del\"     :'
    s = s + '\"' + str(a) + '\"' + '\n'
    OPEN.write('%s' % (s))
    OPEN.close
def 协议 ():#协议
    print('\033[31m===========\n协议:\n    任何由\n本',
    	    '软件造成的\n计算机故障，\n本软件\033[30m不\033[31m',
    	    '负任\n何责任！！！\n===========\033[0m')
def Pass ():#密码系统
    i = 0
    s = 0
    o = 0
    if(os.access('pass.ini',os.F_OK)):
        while i == 0:
            s = open('pass.ini','r+')
            o = next(s)
            if(o == input('密码:')):
                i = 1
            else:
                print('密码错误❌！！！')
        print('密码正确✔️！！！')
        s.close()
    else:
        s = os.open('pass.ini',os.O_RDWR|os.O_CREAT)
        o = input('密码:')
        o = os.write(s,bytes(o,'UTF-8'))
        print('成功！！！')
        os.close(s)
    return(True)
def Open (Name):#打开文件函数
    if(os.access(Name,os.F_OK) and os.access(Name,os.W_OK) and os.access(Name,os.R_OK)):
        OPEN = os.open('%s' % (Name),os.O_RDWR)
        print('打开成功')
        return(OPEN)
    else:
        print('\n请检查文件是否存在或是否有读写权限')
        return(None)
def Open_Creat (Name):#创建文件函数
    OPEN = os.open('%s' % (Name),os.O_RDWR|os.O_CREAT)
    print('创建成功')
    return(OPEN)
def Write (Name,Str):#写入文件函数
    OPEN = os.write(Name,bytes(Str,'UTF-8'))
    print('写入成功')
def Open_Append_Close (Name,Str):#追加文本函数
    try:
        OPEN = open('%s' % (Name),'a+')
        OPEN.write('%s' % (Str))
        OPEN.close
    except FileNotFoundError:
        print('请检查文件是否存在或是否有读写权限')
    else:
        print('打开，写入，关闭并保存成功')
def Close (Name):#关闭文件函数
    try:
        os.close(Name)
    except OSError:
        print('你没有打开文件')
        return(None)
    else:
        print('关闭并保存成功')
        return(Name)
def Open_Read_all_Close (Name):#读出文件函数
    try:
        OPEN = open('%s' % (Name),'r+')
        r = OPEN.readlines()
        a = 0
        print('读取:')
        for a in r:
            print(a)
        OPEN.close()
    except FileNotFoundError:
        print('文件不存在')
    else:
        print('')
def Mdrd (Name):#创建目录函数
    try:
        os.mkdir(Name)
    except OSError:
        print('目录已有或无法创建')
    else:
        print('文件夹创建成功')
def Rename (Old,New):#重命名目录函数
    try:
        os.rename('%s' % (Old),'%s' % (New))
    except OSError:
        print('目录不存在，或新名称已有')
    else:
        print('目录重命名成功')
def Renames (old,new):#重命名文件函数
    try:
        os.renames('%s' % (old),'%s' % (new))
    except OSError:
        print('文件不存在，或新名称已有')
    else:
        print('文件重命名成功')
def Dels (Name):#删除文件函数
    try:
        os.rmdir('%s' % (Name))
    except OSError:
        print('文件夹不存在，或者不是空目录')
    else:
        print('文件夹删除成功')
    return('e5-'+Name)
def Del (name):#删除目录函数
    if(os.access(name,os.F_OK)):
        os.remove('%s' % (name))
        print('文件删除成功')
        return(name)
    else:
        print('文件不存在')
def Su_shu (i,a):#素数计算器
    print('欢迎使用质数计算器')
    s = []    
    while(i < a):
        j = 2
        while(j <= (i/j)):
            if(not(i%j)):
                break
            j = j + 1
        if(j > (i/j)):
            print(i)
            s.append(i)
        i = i + 1
    print(s,'\n计算完成')
def List (I,Mode,Name,Var):#记事本函数
    if(Mode == 'ae'):
        I[Name] = Var
        return(I)
    elif(Mode == 'c'):
        del I[Name]
        return(I)
    elif(Mode == 'r'):
        i = '列表内容如下:'
        print(i)
        for i in I:
            print(i,':',I[i])
        return(I)
    elif(Mode != 'r' and Mode != 'ae' and Mode != 'c'):
        print('    3not   Mode not\n  ' + Mode + '<<<\n  Help')
        return(I)
def Var (Mode,I,i):#变量函数
    if(Mode == 'e'):
        i = I
    elif(Mode == 'r'):
        print(i)
    return(i)
def cdt ():#倒计时函数
    I = ['■■■■■','■□□□■','■□□□■','■■■■■','□□□□■','□□□□■','■■■■■',
        '■■■■■','■□□□■','■□□□■','■■■■■','■□□□■','■□□□■','■■■■■',
        '■■■■■','□□□□■','□□□□■','□□□□■','□□□□■','□□□□■','□□□□■',
        '■■■■■','■□□□□','■□□□□','■■■■■','■□□□■','■□□□■','■■■■■',
        '■■■■■','■□□□□','■□□□□','■■■■■','□□□□■','□□□□■','■■■■■',
        '■□□■□','■□□■□','■□□■□','■■■■■','□□□■□','□□□■□','□□□■□',
        '■■■■■','□□□□■','□□□□■','■■■■■','□□□□■','□□□□■','■■■■■',
        '■■■■■','□□□□■','□□□□■','■■■■■','■□□□□','■□□□□','■■■■■',
        '□□■□□','□□■□□','□□■□□','□□■□□','□□■□□','□□■□□','□□■□□',
        '■■■■■','■□□□■','■□□□■','■□□□■','■□□□■','■□□□■','■■■■■']
    s = -1
    i = ''
    for i in I:
        s += 1
        if(s%7 == 0):
            print((70-s)//7-1)
        print(i)
        time.sleep(1/7)
def Chdir (Path):#切换工作目录函数
    try:
        os.chdir(Path)
    except FileNotFoundError:
        print('目录不存在或无法进入')
def User (a = 0):#用户名函数
    if(os.access('name.ini',os.F_OK)):
        o = open('name.ini','r+',-1,'UTF-8')
        Name = next(o)
        print('hi！\033[36m%s\033[0m！' %(Name))
        o.close
        return(Name)
    else:
        o = os.open('name.ini',os.O_WRONLY|os.O_CREAT)
        Name = input('用户名:')
        O = os.write(o,bytes('%s' %(Name), 'UTF-8'))
        print('Ok！')
        time.sleep(0.5)
        print('你是第一次使用这个软件吧')
        time.sleep(2)
        print('没关系！跟着我慢慢来！')
        time.sleep(2)
        print('你应该看得懂这个吧！')
        time.sleep(1)
        p.Help()
        time.sleep(2)
        print('如果你看不懂，那你就没救了！💩💩💩')
        time.sleep(2)
        print('如果你还看不懂，那你就加作者QQ:')
        time.sleep(0.5)
        print('3014469240')
        time.sleep(5)
        os.close(o)
def Usr ():#用户名函数
    o = open('name.ini','r+',-1,'UTF-8')
    Name = next(o)
    o.close
    return(Name)
def Get_cwd ():#返回目录函数
    for i in os.getcwd :
        print(i)
def Sys ():#系统配置函数
    if(os.access('sys.ini',os.F_OK)):
        o = open('sys.ini','r')
        s = next(o)
        i = next(o)
        print('\033[33m%sV-%s\033[0m' %(s,i))
        o.close
        print('')
    else:
        o = os.open('sys.ini',os.O_WRONLY|os.O_CREAT)
        Name = 'FOS' + '\n' + '0.2'
        O = os.write(o,bytes('%s' %(Name), 'UTF-8'))
        os.close(o)
        Sys()
    o = open('sys.ini','r')
    a = Name = next(o)
    a = r'%s' %(a)
    i = Name = next(o)
    if(i != '0.2' or a != 'FOS'):
        os.remove('sys.ini')
        o.close
        o = os.open('sys.ini',os.O_WRONLY|os.O_CREAT)
        Name = 'FOS' + '\n' + '0.2'
        O = os.write(o,bytes('%s' %(Name), 'UTF-8'))
        os.close(o)
def Rn ():#重命名函数
    if(os.access('name.ini',os.F_OK)):
        os.remove('name.ini')
        o = os.open('name.ini',os.O_WRONLY|os.O_CREAT)
        Name = input('用户名:')
        o = os.write(o,bytes('%s' %(Name), 'UTF-8'))
    else:
        o = os.open('name.ini',os.O_WRONLY|os.O_CREAT)
        Name = input('用户名:')
        O = os.write(o,bytes('%s' %(Name), 'UTF-8'))
    return(Name)
def Pw ():#密码重置函数
    if(os.access('pass.ini',os.F_OK)):
        o = open('pass.ini','r+')
        i = next(o)
        s = input('原密码:')
        if(i == s):
            o.close()
            os.remove('pass.ini')
            n = input('新密码:')
            o = os.open('pass.ini',os.O_WRONLY|os.O_CREAT)
            o = os.write(o,bytes('%s' %(n), 'UTF-8'))
        else:
            print('密码错误')
    else:
        o = os.open('pass.ini',os.O_WRONLY|os.O_CREAT)
        n = input('密码:')
        O = os.write(o,bytes('%s' %(n), 'UTF-8'))
    return(n)
def Ver ():#版本函数
    o = open('sys.ini','r+')
    i = next(o)
    s = i
    i = next(o)
    s = s + ' v-' + i
    print(s)
def Hex (i,a='0'):#进制转换
    if(a=='0'):
        i = str(hex(int(i)))
    else:
        i = str(int(i,16))
    return(i)
def Oct (i,a='0'):#进制转换
    if(a=='0'):
        i = str(oct(int(i)))
    else:
        i = str(int(i,8))
    return(i)
def Bin (i,a='0'):#进制转换
    if(a=='0'):
        i = str(bin(int(i)))
    else:
        i = str(int(i,2))
    return(i)
def Cal ():#日历函数
    y = int(time.strftime("%Y", time.localtime()))
    m = int(time.strftime('%m', time.localtime()))
    d = int(time.strftime("%d", time.localtime()))
    z = time.strftime('%Z',time.localtime())
    i = calendar.month(y,m)
    i = r'%s' %(i)
    i = i.replace('%s'%(d),'\033[91m%s\033[0m'%(d))
    i = i.replace('\n','|\n|')
    print('当前时区:',z)
    t = time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime())
    print('西欧标准时间(0时区):',t)
    print('当前时间(%s时间):' %(z),time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(datetime.datetime.now())
    print()
    print('calendar:')
    print(i)
def tree (l):#返回目录文件函数
    print()
    k = 0
    g = glob.glob('*')
    for k in g:
        a = '~'*(l//3)
        a = a + '-'*((l%3)//2)
        a = a + '_'*(((l%3)%2)//1)
        a = a+k
        if(os.path.isfile('%s'%(k))):
            print(a)
        elif(os.path.isdir('%s'%(k))):
            if(k == 'system'):
                print('pp'h)
            else:
                a = a+'-(文件夹):'
                print(a)
                os.chdir('%s'%(k))
                tree(l + 1)
    i = '..'
    os.chdir(i)
    print()
def treea (l):#装B函数
    print('\033[32m')
    k = 0
    g = glob.glob('*')
    for k in g:
        a = '￣'*(l//3)
        a = a + '—'*((l%3)//2)
        a = a + '＿'*(((l%3)%2)//1)
        a = a+k
        if(os.path.isfile('%s'%(k))):
            print(a)
            time.sleep(0.1)
        elif(os.path.isdir('%s'%(k))):
            if(k == 'system'):
                print('pp')
                time.sleep(0.1)
            else:
                a = a+'-(文件夹):'
                print(a)
                time.sleep(0.1)
                os.chdir('%s'%(k))
                tree(l + 1)
    i = '..'
    os.chdir(i)
    print()
    time.sleep(0.5)
def word (s):#FOS字符编码
    d = {'0000':'A','0001':'B','0002':'C','0003':'D',
        '0004':'E','0005':'F','0006':'G','0007':'H',
        '0008':'I','0009':'J','0010':'K','0011':'L',
        '0012':'M','0013':'N','0014':'O','0015':'P',
        '0016':'Q','0017':'R','0018':'S','0019':'T',
        '0020':'U','0021':'V','0022':'W','0023':'X',
        '0024':'Y','0025':'Z','0026':'a','0027':'b',
        '0028':'c','0029':'d','0030':'e','0031':'f',
        '0032':'g','0033':'h','0034':'i','0035':'j',
        '0036':'k','0037':'l','0038':'m','0039':'n',
        '0040':'o','0041':'p','0042':'q','0043':'r',
        '0044':'s','0045':'t','0046':'u','0047':'v',
        '0048':'w','0049':'x','0050':'y','0051':'z',
        '0052':'.','0053':',','0054':'?','0055':'!',
        '0056':':','0057':'/','0058':'@','0059':'\"',
        '0060':'...','0061':'......','0087':';','0062':'\'',
        '0063':'~','0064':'(','0065':')','0066':'<',
        '0067':'>','0068':'[','0069':']','0070':'*',
        '0071':'&','0072':'\\','0073':'`','0074':'#',
        '0075':'$','0076':'%','0077':'^','0078':'_',
        '0079':'+','0080':'-','0081':'=','0082':'{',
        '0083':'}','0084':'|','0085':'\n','0086':'\t',
        '0087':' ','0088':'  ','0089':'    ','0090':'',
        '0091':True,'0092':False,'0093':None,'0094':'\f',
        '0095':'\000','0096':'\v','0097':'┌','0098':'┐',
        '0099':'─','0100':'├','0101':'│','0102':'┬',
        '0103':'┼','0104':'└','0105':'┘','0106':'┤',
        '0107':'┴','0108':'´','0109':'ˆ','0110':'`',
        '0111':'̃','0112':'̄','0113':'̆','0114':'\'',
        '0115':' ͜','0016':' ͡','0117':'̍','0119':'\033[0m',
        '0118':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        '0120':'\033[1m','0121':'\033[2m','0122':'\033[3m',
        '0130':'0','0131':'1','0132':'2','0133':'3',
        '0134':'4','0135':'5','0136':'6','0137':'7',
        '0138':'8','0139':'9',
        }
    i = 0
    for i in s:
        i = d.get('%s' %(i))
        print(i,end = '')
    print()
def jsq (m):#计算器函数
    if(m=='jttl'):
        h = int(input('头数(个数):'))
        f = int(input('脚数:'))
        fa = int(input('鸡腿数(小):'))
        fb = int(input('兔腿数(大):'))
        r = int((f-h*fa)/(fb-fa))
        c = int(h-r)
        d = '兔:%s，鸡%s'%(r,c)
        return(d)
    if(m!='jttl'):
        na = int(input('数字1:'))
        nb = int(input('数字2:'))
        n = {'+':na+nb,'-':na-nb,'*':na*nb,'×':na*nb,
            '/':na/nb,'÷':na/nb,'%':na%nb,'^':na**nb,
            ';':na//nb,'|':na//nb,'//':na**(1/nb)}
        d = n.get(m)
        return(d)
def mong (a):#FOS图片格式
    if('.mong' in a):
        try:
            a = open('%s'%(a),'r')
        except FileNotFoundError:
            print('没有这个图片')
        try:
            b = next(a)
        except StopIteration:
            print('图片被损坏')
            b = ''
        except TypeError:
            b = ''
        c = 0
        for c in b:
            if(c == '0'):
                print('\033[0m□',end='')
            if(c == '1'):
                print('\033[37m■',end='')
            if(c == '2'):
                print('\033[97m■',end='')
            if(c == '3'):
                print('\033[31m■',end='')
            if(c == '4'):
                print('\033[91m■',end='')
            if(c == '5'):
                print('\033[33m■',end='')
            if(c == '6'):
                print('\033[93m■',end='')
            if(c == '7'):
                print('\033[32m■',end='')
            if(c == '8'):
                print('\033[92m■',end='')
            if(c == '9'):
                print('\033[36m■',end='')
            if(c == 'a'):
                print('\033[96m■',end='')
            if(c == 'b'):
                print('\033[34m■',end='')
            if(c == 'c'):
                print('\033[94m■',end='')
            if(c == 'd'):
                print('\033[35m■',end='')
            if(c == 'e'):
                print('\033[95m■',end='')
            if(c == 'f'):
                print('\033[30m■',end='')
            if(c == 'g'):
                print('\033[90m■',end='')
            if(c == ':'):
                print()
            if(c == ' '):
                print(' ',end='')                
        print('\033[0m')
        try:
            a.close()
        except AttributeError:
            pass
    else:
        print('请打开.mong文件')
def FY (path_a='Dw.dw',path_b='Yw.yw'):#译码器
    try:
        path=0
        Dm=[]
        Dw=open('%s'%(path_a))
        D=Dw.readlines()
        for path in D:
            Dm.append(path.strip())
        Dw.close()
    except:
        pass
    try:
        Ym=[]
        Yw=open('%s'%(path_b),'r')
        Y=Yw.readlines()
        for path in Y:
            Ym.append(path.strip())
        Yw.close()
    except:
        pass
    try:
        Data=[]
        for path in Dm:
            if path=='CR':
                Data.append('\r')
            elif path=='LF':
                Data.append('\n')
            elif path=='HT':
                Data.append('\t')
            elif path=='VT':
                Data.append('\v')
            elif path=='BA':
                Data.append('\b')
            elif path=='NL':
                Data.append('\000')
            else:
                Data.append(Ym[int(path)])
        return Data
    except:
        return None
#函数配置

p.hi()
A = 0
b = 0
i = 0
mong('test.mong')
mong('help.mong')
VAR = None
LIS = {}
i = 0
y=[]
time.sleep(0.1)
Sys()
Pass()
f = User()
time.sleep(0.1)
print(datetime.datetime.now())
time.sleep(0.5)
p.Help()
time.sleep(0.5)
log('sign',time.asctime())
Cal()
A = Open_Creat('mc.mong')
Write(A,'33333333:77777777:77777777:77777777')
Close(A)
#变量配置
#主程序:
while b == 0 :
    h = '[Fos0_2.py:' + f + ']' + os.getcwd()
    c = input('\033[36m%s\033[33m>>>\033[0m' %(h))
    if(c == 'Help' or c == 'help'):
        p.Help()
    elif(c=='Ymq' or c=='Decode'):
        print(FY(input('密文文件名：'),input('母版文件名：')))
    elif(c == 'Exit' or c == 'exit'):
        b = 1
    elif(c == 'tree -0' or c == 'Tree'):
        k = os.getcwd()
        print('当前目录:',k)
        print('\n'*2,k)
        print('┏┌ start:')
        g = glob.glob('*')
        for k in g:
            if(os.path.isfile('%s'%(k))):
                print('││',k)
            elif(os.path.isdir('%s'%(k))):
                print('┠┝',k,'-(catalog)')
        print('┗└ end:')
    elif(c == 'tree' or c == 'TREE'):
        k = os.getcwd()
        print('当前目录:',k)
        tree(0)
        os.chdir(k)
    elif(c == 'Open' or c == 'open'):
        print('当前目录所有文件:')
        k = os.getcwd()
        print(k)
        g = glob.glob('*')
        for k in g:
            if(os.path.isfile('%s'%(k))):
                print('-',k)
            elif(os.path.isdir('%s'%(k))):
                print('-',k,'-(文件夹)')
        A = Open(input('文件名'))
        log('open',A)
    elif(c == 'Creat' or c == 'creat'):
        A = Open_Creat(input('文件名'))
        log('creat',A)
    elif(c == 'Write' or c == 'write'):
        Write(A,input('文本内容'))
    elif(c == 'Close' or c == 'close'):
        Close(A)
        log('close',A)
    elif(c == 'Open_Append_Close' or c == 'Oac' or c == 'oac'):
        Open_Append_Close(input('文件名'),input('文本内容'))
        log('open')
        log('close')
    elif(c == 'Read' or c == 'read' or c == 'orac'):
        Open_Read_all_Close(input('文件名'))
        log('open')
        log('close')
    elif(c == 'Mdrd' or c == 'mdrd' or c == 'Md' or c == 'md'):
        Mdrd(input('目录名称'))
    elif(c == 'Rename' or c == 'rename'):
        Rename(input('目录名称'),input('新名称'))
    elif(c == 'Renames' or c == 'renames'):
        Renames(input('文件名'),input('新名称'))
    elif(c == 'Dels' or c == 'dels'):
        log('del',Dels(input('目录名称')))
    elif(c == 'Del' or c == 'del'):
        log('del',Del(input('文件名')))
    elif(c == 'Su_shu' or c == 'Ss' or c == 'ss'):
        try:
            Su_shu(int(input('从:')),int(input('到:')))
        except ValueError:
            print('请输入数字')
    elif(c == 'Clean up the screen' or c == 'Cls' or c == 'cls' or c == 'clear' or c == 'Clear'):
        print('\f\r\t\v\n'*8000)
    elif(c == 'cccp' or c == 'CCCP' or c == 'Cccp' or c == '苏联' or c == '苏维埃'):
        print('\033[43;31m########    ########    ########    ########',
        	    '\n#           #           #           #      #',
        	    '\n#           #           #           #      #',
        	    '\n#           #           #           ########',
        	    '\n#           #           #           #       ',
        	    '\n#           #           #           #       ',
        	    '\n#           #           #           #       ',
        	    '\n#######     ########    ########    #       \033[0m')
        print('\033[33m★\033[0m'*48)
        cccp = ['\033[41;33mСоюз нерушимый республик свободныхСплотила навеки Великая Русь.',
            'Да здравствует созданный волей народовЕдиный, могучий Советский Союз!',
            'Славься, Отечество наше свободное,Дружбы народов надёжный оплот!',
            'Знамя советское, знамя народноеПусть от победы к победе ведёт!',
            'Сквозь грозы сияло нам солнце свободы,И Ленин великий нам путь озарил:',
            'Нас вырастил Сталин — на верность народу,На труд и на подвиги нас вдохновил!',
            'Славься, Отечество наше свободное,Счастья народов надёжный оплот!',
            'Знамя советское, знамя народноеПусть от победы к победе ведёт!',
            'Мы армию нашу растили в сраженьях.',
            'Захватчиков подлых с дороги сметём!',
            'Мы в битвах решаем судьбу поколений,Мы к славе Отчизну свою поведём!',
            'Славься, Отечество наше свободное,Славы народов надёжный оплот!',
            'Знамя советское, знамя народноеПусть от победы к победе ведет!\033[0m']
        CCCP = 0
        for CCCP in cccp :
            print(CCCP)
            time.sleep(1)
    elif(c == 'mc' or c == 'Mc' or c == 'minecraft' or 
    	    c == 'Minecraft'):
        word(['0012','0034','0039','0030','0028','0043',
            '0026','0031','0045'])
        
    elif(c == 'Lis' or c == 'List' or c == 'list'):
        LIS = List(LIS,input('模式(r是显示列表，\nae是添加或编辑列表的值，\nc是删除列表的值。\n输入:'),input('项目名(显示列表可不填):'),input('内容(显示列表和删除列表可不填):'))
    elif(c == 'Var' or c == 'Variable' or c == 'var'):
        VAR = Var(input('模式(r是显示，\ne是更改。)\n输入:'),input('值(显示可不填)'),VAR)
    elif(c == 'Cdt' or c == 'cdt'):
        cdt()
    elif(c == 'Time' or c == 'time' or c == 'gettime'):
        Cal()
    elif(c == 'Chdir' or c == 'Cd' or c == 'cd' or c == 'chdir'):
        k = os.getcwd()
        g = os.path.join(k, os.pardir)
        g = os.path.abspath(g)
        print('父目录:',g)
        print('当前目录:',k)
        Chdir(input('工作目录'))
    elif(c == 'Getcwd' or c == 'Gc' or c == 'Get_cwd' or c == 'getcwd' or c == 'gcd'):
        Get_cwd()
    elif(c == '协议'):
        协议()
    elif(c == 'name'):
        log('r',Rn())
        f = Usr()
    elif(c == 'pass'):
        log('r',Pw())
    elif(c == 'ver' or c == 'Ver'):
        Ver()
    elif(c == 'hex' or c == 'Hex'):
        print(Hex(input('数:'),input('(十进制转十六进制(0)十六进制转十进制(1))\n输入:')))
    elif(c == 'oct' or c == 'Oct'):
        print(Oct(input('数:'),input('(十进制转八进制(0)十八进制转十进制(1))\n输入:')))
    elif(c == 'bin' or c == 'Bin'):
        print(Bin(input('数:'),input('(十进制转十二进制(0)二进制转十进制(1))\n输入:')))
    elif(c == 'try' or c == 'tree -1'):
        input('\033[32m')
        k = os.getcwd()
        treea(0)
        print(k)
        time.sleep(0.5)
        treea(0)
        print(k)
        time.sleep(0.5)
        treea(0)
        print(k)
        time.sleep(0.5)
        treea(0)
        print(k)
        time.sleep(0.5)
        treea(0)
        print(k)
        time.sleep(0.5)
        treea(0)
        print(k)
        time.sleep(0.5)
        os.chdir(k)
        print(k)
        time.sleep(0.5)
    elif(c == 'mong' or c == 'Mong'):
        for k in glob.glob('*.mong'):
            print(k)
        mong(input('文件名:'))
    elif(c == 'word' or c == 'Word'):
        word(input('按,分割:').split(','))
    elif(c == 'fosw' or c == 'Fosw'):
        for k in glob.glob('*.fosw'):
            print(k)
        for k in glob.glob('*.wong'):
            print(k)
        k = open(input('文件名'),'r')
        k = next(k)
        word(k.split(','))
        k.close
    elif(c == 'jsq' or c == 'Jsq' or c =='Calculator'):
        print(jsq(input('模式(符号，jttl(鸡兔同笼)):')))
    elif(c == ""):
        pass
    else:
        print('    0not   Function not\n   %s <<<\n  Help' % (c))
#退出
Sys()
print(random.randint(0,1))
print()
print()
print('正在关闭程序')
log('exit',time.asctime())
time.sleep(3);print('成功关闭！')
k = open('logs.log','a+')
k.write('}\n')
time.sleep(0.5)
sys.exit()
exit()
#完。。。
pass