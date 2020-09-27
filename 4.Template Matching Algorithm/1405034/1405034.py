# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 22:01:08 2019

@author: Raju
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import random
import cv2 as cv
from scipy.stats import multivariate_normal
eps=np.finfo(float).eps

ref = cv.imread('reference.jpg',0)
row,col=ref.shape
#print((img[4][6]))
#print(row,col)
#cv.imshow('image',img)
#cv.waitKey(0)
#cv.destroyAllWindows()

plt.imshow(ref, cmap = 'gray')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

cap = cv.VideoCapture('movie.mov')
fps=cap.get(cv.CAP_PROP_FPS)
ret,frame=cap.read()
fra_num=0;
while ret:
    cv.imwrite('frame %d.jpg' %fra_num,frame)
    ret,frame=cap.read()
    fra_num=fra_num+1

print(fra_num)  
# =============================================================================
# img2=cv.imread('frame 1.jpg')
# img3=cv.imread('frame 1.jpg',0)
# img2 = cv.rectangle(img2,(50,50),(100,160),(255,0,0),3)
# cv.imwrite('out.jpg',img2)
# =============================================================================
def distance(frame,ref,m,n) :
    summ=0
    M,N=ref.shape
    for i in range(m,m+M):
        for j in range(n,n+N) :
            summ=summ+(frame[i][j]-ref[i-m][j-n])*(frame[i][j]-ref[i-m][j-n])
    return summ

def Exhaustive(frame,ref,prev_x,prev_y,p) :
    fh,fw=frame.shape
    rh,rw=ref.shape
    l_x=prev_x-p
    l_y=prev_y-p
    if(l_x<0):
        l_x=0
    if(l_y<0):
        l_y=0
    r_x=prev_x+p
    r_y=prev_y+p
    if(r_x>(fh-rh)):
        r_x=fh-rh-1
    if(r_y>(fw-rw)):
        r_y=fw-rw-1
    
    com=math.inf
    #print(com)
    search=0
    for i in range(l_x,r_x) :
        for j in range(l_y,r_y) :
            search=search+1
            val=distance(frame,ref,i,j)
            if(val<com):
                com=val
                left_x=i
                left_y=j
                
    return left_x,left_y,search



"""
img2=cv.imread('frame 0.jpg')
img3=cv.imread('frame 0.jpg',0)

#a,b,c,d=Exhaustive(img3,img)
#print(a,' ',b,' ',c,' ',d)
#img2 = cv.rectangle(img2,(b,a),(d,c),(0,0,255),2)
#cv.imwrite('out.jpg',img2)
"""
# =============================================================================
# r=cv.matchTemplate(img3,img,cv.TM_CCOEFF_NORMED)
# a,b,c,d=cv.minMaxLoc(r)
# dd=d[0]
# d2=d[1]
# img2 = cv.rectangle(img2,(dd,d2),(dd+y,d2+x),(0,0,255),2)
# #cv.imwrite('out.jpg',img2)
# print(dd,' ',d2)
# =============================================================================
def D_Logarithmic(frame,ref,prev_x,prev_y,p) :
    fh,fw=frame.shape
    rh,rw=ref.shape
    search=0
    while(True):
        k=int(math.log(p,2))
        d=int(2**(k-1))
        if(d==0) :
            return prev_x,prev_y,search
        X=[]
        Y=[]
        X.append(prev_x)
        Y.append(prev_y)
        
        if((prev_x-d)<0) :
            X.append(0)
            Y.append(prev_y)
            if((prev_y+d)>(fw-rw-1)) :
                X.append(0)
                Y.append(fw-rw-1)
            else:
                X.append(0)
                Y.append(prev_y+d)
            if((prev_y-d)<0) :
                X.append(0)
                Y.append(0) 
            else:
                X.append(0)
                Y.append(prev_y-d)  
        else:
            X.append(prev_x-d)
            Y.append(prev_y)
            if((prev_y+d)>(fw-rw-1)) :
                X.append(prev_x-d)
                Y.append(fw-rw-1)
            else:
                X.append(prev_x-d)
                Y.append(prev_y+d)
            if((prev_y-d)<0) :
                X.append(prev_x-d)
                Y.append(0) 
            else:
                X.append(prev_x-d)
                Y.append(prev_y-d)
        
        if((prev_x+d)>(fh-rh-1)) :
            X.append(fh-rh-1)
            Y.append(prev_y)
            if((prev_y+d)>(fw-rw-1)) :
                X.append(fh-rh-1)
                Y.append(fw-rw-1)
            else:
                X.append(fh-rh-1)
                Y.append(prev_y+d)
            if((prev_y-d)<0) :
                X.append(fh-rh-1)
                Y.append(0) 
            else:
                X.append(fh-rh-1)
                Y.append(prev_y-d)
        else:
            X.append(prev_x+d)
            Y.append(prev_y)
            if((prev_y+d)>(fw-rw-1)) :
                X.append(prev_x+d)
                Y.append(fw-rw-1)
            else:
                X.append(prev_x+d)
                Y.append(prev_y+d)
            if((prev_y-d)<0) :
                X.append(prev_x+d)
                Y.append(0) 
            else:
                X.append(prev_x+d)
                Y.append(prev_y-d)
                
        
                
                
        if((prev_y-d)<0):
            X.append(prev_x)
            Y.append(0)
        else:
            X.append(prev_x)
            Y.append(prev_y-d)
        if((prev_y+d)>(fw-rw-1)):
            X.append(prev_x)
            Y.append(fw-rw-1)
        else:
            X.append(prev_x)
            Y.append(prev_y+d)
            
        #print(len(X))
        #print(len(Y))
        
        com=math.inf
        for i in range(len(X)) :
            search=search+1
            val=distance(frame,ref,X[i],Y[i])
            if(val<com) :
                com=val
                prev_x=X[i]
                prev_y=Y[i]
                
        p=p/2
            
            

def Hierarchical(frame,ref,prev_x,prev_y,p,level) :
    Level=[]
    Img=[]
    Img.append(frame)
    Img.append(ref)
    Level.append(Img)
    for i in range(1,level+1) :
        arr=[]
        sframe=cv.resize(Level[i-1][0],None,fx=0.5,fy=0.5)
        arr.append(sframe)
        sref=cv.resize(Level[i-1][1],None,fx=0.5,fy=0.5)
        arr.append(sref)
        Level.append(arr)
    
    #print(len(Img))
    search=0
    x=0
    y=0
    l=2**level
    
    for i in range(level,-1,-1) :
        if(i==level) :
            x,y,s=D_Logarithmic(Level[i][0],Level[i][1],int(prev_x/l),int(prev_y/l),int(p/l))
            x=x-int(prev_x/l)
            y=y-int(prev_y/l)
            search=search+1
        else:
            X=int(prev_x/l)+2*x
            Y=int(prev_y/l)+2*y
            x,y,s=D_Logarithmic(Level[i][0],Level[i][1],X,Y,p/2)
            x=x-int(prev_x/l)
            y=y-int(prev_y/l)
            search=search+1
            
        l=l/2
    return x+prev_x,y+prev_y,search
 
        
    
           
    
img_array =[]
search=0
p=4
for i in range(fra_num) :
    
    if(i==0):
        img=cv.imread('frame 0.jpg',0)
        height,width=img.shape
        size=(width,height)
        match=cv.matchTemplate(img,ref,cv.TM_CCOEFF_NORMED)
        minVal, maxVal, minLoc, maxLoc=cv.minMaxLoc(match)
        fit_y=maxLoc[0]
        fit_x=maxLoc[1]
        #print(fit_x,' ',fit_x)
        img=cv.imread('frame 0.jpg')
        cv.rectangle(img,(fit_y,fit_x),(fit_y+col,fit_x+row),(0,0,255),2)
        cv.imwrite('out 0.jpg',img)
        img_array.append(img)
        
    else:
        img=cv.imread('frame %d.jpg' %i,0)
        #fit_x,fit_y,s=Exhaustive(img,ref,fit_x,fit_y,p)
        #fit_x,fit_y,s=D_Logarithmic(img,ref,fit_x,fit_y,p)
        fit_x,fit_y,s=Hierarchical(img,ref,fit_x,fit_y,p,2)
        img=cv.imread('frame %d.jpg' %i)
        cv.rectangle(img,(fit_y,fit_x),(fit_y+col,fit_x+row),(0,0,255),2)
        cv.imwrite('out %d.jpg' %i,img)
        img_array.append(img)
        search=search+s
        
    print('frame %d' %i)
         
"""
imgg=cv.imread('frame 0.jpg',0)
h,w=imgg.shape
size=(h,w)
img_array = []
for i in range(fra_num) :
    img2=cv.imread('frame %d.jpg' %i)
    #print(img2.shape)
    img_array.append(img2)
    
 
out = cv.VideoWriter("p.mov",cv.VideoWriter_fourcc(*'DIVX'), fps, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
cv.destroyAllWindows()
"""           
out = cv.VideoWriter("output.mov",cv.VideoWriter_fourcc(*'DIVX'), fps, size)       
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
cv.destroyAllWindows()

search_num=search/(fra_num-1)
print(search_num)


