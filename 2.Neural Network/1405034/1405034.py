# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 20:18:39 2018

@author: Raju
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import random
eps=np.finfo(float).eps


def getmaxidx(M):
    idx=0
    val=0
    for i in range(len(M)):
        if M[i]>val:
            val=M[i]
            idx=i
    return idx   
 
def Sum(M):
    sum=0;
    for i in range(len(M)):
        sum=sum+M[i]   
    return sum

def sigmoid_single(x):
     val=1/(1+math.exp(-x))
     return val

def sigmoid(M):
    m=np.empty(0)
    for i in range(len(M)):
        val=M[i]
        val=sigmoid_single(val)
        m=np.append(m,val)
        
    return m
    
def Read_data():
    
    data=pd.read_csv('trainNN.txt',sep="\t",header=None)
    data_length=len(data)
    #print(data_length)
    column=len(data.columns)
    #print(column)
    features=column-1
    class_type=set(data[len(data.columns)-1])
    #print(class_type)
    num_type=len(class_type)
    #print(num_type)
    for i in range (1,num_type):
        data[column-1+i]=0
    for i in range (data_length):
        val=data[column-1][i]
        data.iloc[[i],[column-1]] = 0
        data.iloc[[i],[column-1+val-1]]=1
        
    layer=[features,3,4,num_type]
    M=[]
    for i in range(1,len(layer)-1):
        m=[]
        for j in range(layer[i]):
            #print(layer[i])
            l=[]
            for k in range(layer[i-1]):
                #print(layer[j])
                l.append(random.randint(0,1))
            m.append(l)
        #print(m)
        mm=np.transpose(m)
        #print(mm)
        M.append(mm)
    #print(M)
    #print(M[0])
    
    
    #print(b)
    terror=100000
    loop=0
    WM=M
    MM=M
    while (loop<20):
        M=MM
        Error=0
        for p in range(data_length):
            a=np.empty(0)
            for i in range(features):
                a=np.append(a,data.iloc[p][i])
            #print(a)
            b=np.empty(0)
            for i in range(column-1,column-1+num_type):
                b=np.append(b,data.iloc[p][i]) 
            v=[]
            y=[]
            y.append(a)
            x=a
            for i in range(len(M)):
                x=np.matmul(x,M[i])
                v.append(x)
                x=sigmoid(x)
                y.append(x)
             
            xx=y[len(y)-1]
            #xx=xx*b
            v.append(xx)
            xx=sigmoid(xx)
            y.append(xx)
            #print(v)
            #print(y)
            delta=[]
            result = np.subtract(y[len(y)-1],b)
            #print(result)
            error=result*result*0.5
            error=Sum(error)
            #print(error)
            Error=Error+error
            fv=sigmoid(v[len(v)-1])*(1-sigmoid(v[len(v)-1]))
            delta_L=result*fv
            delta.append(delta_L)
            
            for i in range(len(M)):
                tem=M[len(M)-1-i]*Sum(delta[i])
                tem=Sum(tem)
                fpv=sigmoid(v[len(v)-2-i])*(1-sigmoid(v[len(v)-2-i]))
                delt=tem*fpv
                delta.append(delt)
            
            #print(MM)
            #print(len(M))
            #print(delta[1][0])
            w=[]
            for i in range(len(MM)):
                MM[i]=MM[i]+MM[i]*delta[i][0]*y[i][0]*(-0.04)
                
        loop=loop+1
        #print(Error)
        if Error<terror:
            terror=Error
            WM=M
            
    #print(terror)
    #print(WM)
    
    
    datat=pd.read_csv('testNN.txt',sep="\t",header=None)
    datat_length=len(data)
    #print(datat_length)
    columnt=len(datat.columns)
    featurest=columnt-1
    classt_type=set(datat[len(datat.columns)-1])
    #print(class_type)
    numt_type=len(classt_type)
    for i in range (1,num_type):
        datat[columnt-1+i]=0
    for i in range (datat_length):
        val=datat[columnt-1][i]
        datat.iloc[[i],[columnt-1]] = 0
        datat.iloc[[i],[columnt-1+val-1]]=1
        
    accuracy=0
    mismatch=0
    for p in range(datat_length):
        at=np.empty(0)
        for i in range(featurest):
            at=np.append(at,datat.iloc[p][i])
            
        bt=np.empty(0)
        for i in range(columnt-1,columnt-1+numt_type):
            bt=np.append(bt,datat.iloc[p][i]) 
        
        vt=[]
        yt=[]
        yt.append(at)
        xt=at
        for i in range(len(WM)):
            xt=np.matmul(xt,WM[i])
            vt.append(xt)
            xt=sigmoid(xt)
            yt.append(xt)
             
        xxt=y[len(yt)-1]
        #xxt=xxt*bt
        vt.append(xxt)
        xxt=sigmoid(xxt)
        yt.append(xxt)
        ll=yt[len(yt)-1]
        check=getmaxidx(ll)+1
        #print(check," ",datat.iloc[p][featurest])
        if(check==datat.iloc[p][featurest]):
            accuracy=accuracy+1
        else:
            mismatch=mismatch+1
    
    print("Accuracy=",(accuracy/datat_length)*100,"%")
    print("Misclassified Examples=",mismatch)
    return data


    
    
def main():
    data=Read_data()
     
     
     
     
if __name__ == "__main__":
    main()


