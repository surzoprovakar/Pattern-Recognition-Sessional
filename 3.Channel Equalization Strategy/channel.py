# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 13:20:02 2018

@author: Raju
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import random
from scipy.stats import multivariate_normal
eps=np.finfo(float).eps

def char(n):
    if n==0:
        return '000'
    elif n==1:
        return '001'
    elif n==2:
        return '010'
    elif n==3:
        return '011'
    elif n==4:
        return '100'
    elif n==5:
        return '101'
    elif n==6:
        return '110'
    elif n==7:
        return '111'

class Channel:
  def __init__(self, h1, h2, sd, char):
    self.h1=h1
    self.h2=h2
    self.sd=sd
    self.Ik2=float(char[0])
    self.Ik1=float(char[1])
    self.Ik=float(char[2])
    #print(char)
    #print(type(self.Ik))
    #print(self.Ik)
  def xvalue(self):
      noise=np.random.normal(0,self.sd)
      xk=self.h1*self.Ik+self.h2*self.Ik1+noise
      #print(noise)
      noise=np.random.normal(0,self.sd)
      xk1=self.h1*self.Ik1+self.h2*self.Ik2+noise
      #print(xk)
      #print("hel")
      #print(xk1)
      
      
      return xk,xk1

class Cluster:
  def __init__(self,typ):
      self.type=typ
      self.X=[]
      self.count=0
      self.prior=0
      self.mean=[]
      self.cov=[]
      self.parent=[]
        
in_file=open("input.txt","r")
h1=float(in_file.readline());
h2=float(in_file.readline());
sd=float(in_file.readline());
in_file.close()
#print(var)
#z=Channel(h1,h2,nos,'110')
#x,y=z.xvalue()


train_file=open("train_mod.txt","r")
string=train_file.read()
train_file.close()

#print(string[2:5])
#tmp=string[0:3]
C0=Cluster('000')
C0.parent.append(0)
C0.parent.append(4)

C1=Cluster('001')
C1.parent.append(0)
C1.parent.append(4)

C2=Cluster('010')
C2.parent.append(1)
C2.parent.append(5)

C3=Cluster('011')
C3.parent.append(1)
C3.parent.append(5)

C4=Cluster('100')
C4.parent.append(2)
C4.parent.append(6)

C5=Cluster('101')
C5.parent.append(2)
C5.parent.append(6)

C6=Cluster('110')
C6.parent.append(3)
C6.parent.append(7)

C7=Cluster('111')
C7.parent.append(3)
C7.parent.append(7)

#print(C0.type)  
for i in range(len(string)-2):
    tmp=string[i:i+3]
    cl=Channel(h1,h2,sd,tmp)
    xk,xk1=cl.xvalue()
    p=[]
    p.append(xk)
    p.append(xk1)
    if (tmp=='000'):
        C0.X.append(p)
        C0.count=C0.count+1 
    elif (tmp=='001'):
        C1.X.append(p)
        C1.count=C1.count+1
    elif (tmp=='010'):
        C2.X.append(p)
        C2.count=C2.count+1
    elif (tmp=='011'):
        C3.X.append(p)
        C3.count=C3.count+1
    elif (tmp=='100'):
        C4.X.append(p)
        C4.count=C4.count+1
    elif (tmp=='101'):
        C5.X.append(p)
        C5.count=C5.count+1
    elif (tmp=='110'):
        C6.X.append(p)
        C6.count=C6.count+1
    elif (tmp=='111'):
        C7.X.append(p)
        C7.count=C7.count+1
        
        
clist=[]
clist.append(C0)
clist.append(C1)
clist.append(C2)
clist.append(C3)
clist.append(C4)
clist.append(C5)
clist.append(C6)
clist.append(C7)  
#print(len(clist))
for i in range(len(clist)):
    clist[i].prior=clist[i].count/(len(string)-2)
    
    x,y=[sum(a) for a in zip(*clist[i].X)] 
    x=x/clist[i].count
    clist[i].mean.append(x)
    y=y/clist[i].count
    clist[i].mean.append(y)
    #print(clist[0].mean)
    
    ar=clist[i].X
    arr=np.transpose(ar)
    clist[i].cov=np.cov(arr)

# =============================================================================
# for i in range(len(clist)):
#     print(clist[i].prior)
#     print(clist[i].mean)
#     print(clist[i].cov)
#     print()
# =============================================================================
#print(clist[4].cov)
#t=np.transpose(clist[4].cov)
#print(t)
############Test Data##############
class Track:
  def __init__(self):
      self.value=0
      self.parent=-1
      
test_file=open("test.txt","r")
test=test_file.read()
test_file.close()

#print(len(test))
TX=[]
for i in range(len(test)-2):
    tmp=test[i:i+3]
    cl=Channel(h1,h2,sd,tmp)
    xk,xk1=cl.xvalue()
    p=[]
    p.append(xk)
    p.append(xk1)
    TX.append(p)
    
#print(len(TX))
Vit=[]
c1=[]
#print(type(clist[0].mean))
#print(type(TX[0]))

# =============================================================================
# for i in range(len(clist)):
#     temp=np.empty((0,2))
#     temp=np.vstack([temp,clist[i].mean])
#     
#     temp1=np.empty((0,2))
#     temp1=np.vstack([temp1,TX[0]])
#     sub=temp1-temp
#     subT=np.transpose(sub)
#     #print(sub)
#     #print(subT)
#     inv=np.linalg.inv(clist[i].cov)
#     res=np.matmul(sub,inv)
#     res=np.matmul(res,subT)
#     c1.append(res)
# Vit.append(c1)
# =============================================================================
#print(Vit[0])
for i in range(len(clist)):
    mean=np.empty((0))
    mean=np.append(mean,clist[i].mean[0])
    mean=np.append(mean,clist[i].mean[1])
    
    cov=np.empty((0,2))
    cov=np.vstack([cov,clist[i].cov[0]])
    cov=np.vstack([cov,clist[i].cov[1]])
    
    temp=np.empty((0,2))
    temp=np.vstack([temp,TX[0]])
    
    gaus=multivariate_normal.pdf(temp,mean=mean,cov=cov)
    val=clist[i].prior*gaus+eps
    val=np.log(val)
    obj=Track()
    obj.value=val
    c1.append(obj)
Vit.append(c1)
#print(c1)
for i in range (1,len(TX)):
    c=[]
    for j in range(len(clist)):
        mean=np.empty((0))
        mean=np.append(mean,clist[j].mean[0])
        mean=np.append(mean,clist[j].mean[1])
        
        cov=np.empty((0,2))
        cov=np.vstack([cov,clist[j].cov[0]])
        cov=np.vstack([cov,clist[j].cov[1]])
        
        temp=np.empty((0,2))
        temp=np.vstack([temp,TX[i]])
        
        gaus=multivariate_normal.pdf(temp,mean=mean,cov=cov)
        val=clist[j].prior*gaus+eps
        val=np.log(val)
        
        x=clist[j].parent[0]
        y=clist[j].parent[1]
        num1=Vit[i-1][x].value
        num2=Vit[i-1][y].value
        obj=Track()
        if (num1>=num2):
            value=val+num1
            obj.value=value
            obj.parent=x
        else:
            value=val+num2
            obj.value=value
            obj.parent=y
        c.append(obj)
    Vit.append(c)

#print(len(Vit[4]))
channel=[]
maxx=Vit[len(Vit)-1][0].value
trk=0
for i in range(1,8):
    if(Vit[len(Vit)-1][i].value>maxx):
        maxx=Vit[len(Vit)-1][i].value
        trk=i
        
channel.append(trk)
j=len(Vit)-1
parent=-2
while j>0:
    parent=Vit[j][trk].parent
    channel.append(parent)
    trk=parent
    j=j-1
#print(len(channel))
#print(channel)
channel.reverse()
#print(channel)
final=''
for i in range(len(channel)):
    st=char(channel[i])
    if i==0:
        final=final+st
    else:
        final=final+st[2]
        
#print(len(final))
#print(final)
accu=0
for i in range(len(final)):
    if final[i]==test[i]:
        accu=accu+1
accu=accu/len(test)*100
print(final)
print("Accuracy:",accu,"%")

out=open("out.txt","w")
out.write(final)
out.close()

