#!/usr/bin/env python
#coding = utf-8
#导入模块
import os
import sys
import time
import math
import datetime
import glob
def FY (path_a='Dw.dw',path_b='Yw.yw'):
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
            Data.append(Ym[int(path)])
        return Data
    except:
        return None
def te (a):
    return a
class ID:
    '''
    This is a procedure due to household registration.
    ================
    
    '''
    def __init__ (self):
        self.__lst={}
        self.__cache=0
        self.ids=[]
        self.num=0
        self.i=0
    def __del__ (self):
        del self.__cache;del self.__lst
        del self.ids
        del self.num;del self.i
        print('The empire died.')
    def __str__ (self):
        return 'Have '+str(self.num)+' people.'
    def __int__ (self):
        return int(self.num)
    def __float__ (self):
        return float(self.num)
    def __len__ (self):
        self.num=len(self.__lst)
        return int(self.num)
    def __bool__ (self):
        if self.num!=0:
            return True
        else:
            return False
    def __gt__ (self,other):
        if self.num>other:
            return True
        else:
            return False
    def __ge__ (self,other):
        if self.num>=other:
            return True
        else:
            return False
    def __lt__ (self,other):
        if self.num<other:
            return True
        else:
            return False
    def __le__ (self,other):
        if self.num<=other:
            return True
        else:
            return False
    def __ep__ (self,other):
        if self.num==other:
            return True
        else:
            return False
    def __ne__ (self,other):
        if self.num!=other:
            return True
        else:
            return False
    def __getitem__ (self,key):
        try:
            return self.__lst[key]
        except:
            s={'name':'Diannaojun-Liu','dob':['1.01.01','00.00.00'],'in':['1.01.01','00.00.00'],'id':'0000.10101.000.0:3'}
            return s
    def __cmp__ (self,dst):
        if self.num==dst:
            return dst
        elif self.num!=dst:
            return 0-dst
        elif self.num>dst:
            return dst+1
        elif self.num>=dst:
            return dst+0.5
        elif self.num<dst:
            return dst-1
        elif self.num<=dst:
            return dst-0.5
        else:
            return False
    def __add__ (self,other):
        if type(other)==tuple and len(other)==2:
            if type(other[1])==dict and type(other[0])==str:
                if len(other[0])==18 or len(other[0])==19:
                    if len(other[1]['dob'][0])==7 or len(other[1]['dob'][0])==8:
                        if len(other[1]['dob'][1])==8 and len(other[1]['in'][1])==8:
                            if len(other[1]['in'][0])==7 or len(other[1]['in'][0])==8:
                                if len(other[1]['id'])==18 or len(other[1]['id'])==19:
                                    if len(other[1])==4 and type(other[1]['name'])==str:
                                        self.__lst[str(other[0])]=other[1]
                                        self.num=len(self.__lst)
                                        self.ids.append(str(other[0]))
        return self.__getitem__(str(other[0]))
    def __sub__ (self,other):
        if type(other)==str:
            if len(other)==19 or len(other)==18:
                try:
                    del self.__lst[str(other)]
                    return self.__lst
                    self.num=len(self.__lst)
                    self.ids.pop(self.ids.index(other))
                except:
                    pass
    def __mul__ (self,other):
        if type(other)==int and other>-1 and other<len(self.__lst)+1:
            self.__cache=self.__lst[self.ids[other]]
            return self.__cache
    def add (self,other):
        if type(other)==tuple and len(other)==2:
            if type(other[1])==dict and type(other[0])==str:
                if len(other[0])==18 or len(other[0])==19:
                    if len(other[1]['dob'][0])==7 or len(other[1]['dob'][0])==8:
                        if len(other[1]['dob'][1])==8 and len(other[1]['in'][1])==8:
                            if len(other[1]['in'][0])==7 or len(other[1]['in'][0])==8:
                                if len(other[1]['id'])==18 or len(other[1]['id'])==19:
                                    if len(other[1])==4 and type(other[1]['name'])==str:
                                        self.__lst[str(other[0])]=other[1]
                                        self.num=len(self.__lst)
                                        self.ids.append(str(other[0]))
        return self.__getitem__(str(other[0]))
    def sub (self,other):
        if type(other)==str:
            if len(other)==19 or len(other)==18:
                try:
                    del self.__lst[str(other)]
                    return self.__lst
                    self.num=len(self.__lst)
                    self.ids.pop(self.ids.index(other))
                except:
                    pass
    def out (self):
        return self.__lst
        self.num=len(self.__lst)
    pass
t=ID()
print(t+('0000.10101.000.0:3',{'name':'Diannaojun-Liu','dob':['1.01.01','00.00.00'],'in':['1.01.01','00.00.00'],'id':'0000.10101.000.1:3'}))
print(t['0000.10101.000.0:3'])
print(len(t))
print(dir(t))
print(t-'0000.10101.000.0:3')
print(t['0000.10101.000.0:3'])
print(len(t))
print()
del t