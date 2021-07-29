#!/usr/bin/env python
#coding = utf-8
#导入模块
import os
import sys
import time
import math
import datetime
import glob
import p
#随机数模块
class K :
    def __init__ (self,zz,ff=1):
        self.Seed=zz
        self.Mode=ff
    def Ran (self,rs=0,fs=False):
        data=self.Seed*1+2*3-456/7+8-9*self.Mode**1**0.75//8
        self.Float=data
        self.Int=int(data-(data%1))
        if fs==True:
            return int(0-self.Int)
        elif fs==False:
            if rs==0:
                return int(self.Int)
            elif rs==1:
                return float(data)
            elif rs==-1:
                return float(0-data)
            else:
                pass
    def Res (self,zz,ff):
        self.Seed=zz
        self.Mode=ff
#译码器
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
print(FY())
print('decoder')
