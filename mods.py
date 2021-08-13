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