# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 06:56:20 2019

@author: shinnkun
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 22:58:40 2019

@author: shinnkun
"""


import os
import matplotlib
import cv2
import numpy as np

i1=[255,3,45]
i2=[240,0,124]
i3=[255,0,219]
i4=[141,0,235]
i5=[0,3,255]
i6=[3,74,255]
i7=[0,112,240]
i8=[0,162,255]
i9=[0,179,235]
i10=[0,227,255]



def changer(pic,exname):
    
    a=cv2.imread()
    lx=[]
    for x in range(0,1080):
        ly=[]
        for y in range(0,1920):
            color=a[x][y]
            if color<25:
                ly.append(i1)
            else:    
                    if 26<color<51:
                        ly.append(i2)                
                    else:              
                        if 52<color<76:
                            ly.append(i3)                    
                        else:                  
                            if 77<color<102:
                                ly.append(i4)                        
                            else:                      
                                if 103<color<128:
                                    ly.append(i5)                            
                                else:                      
                                    if 129<color<154:
                                        ly.append(i6) 
                                    else:
                                        if 155<color<180:
                                            ly.append(i7) 
                                        else:
                                            if 181<color<206:
                                                ly.append(i8)                                        
                                            else:    
                                                if 207<color<232:
                                                    ly.append(i9)                                            
                                                else:
                                                    ly.append(i10)                                            
      
        lx.append(ly)
    aaa = np.array(lx)
    cv2.imwrite(exname,aaa)





a=cv2.imread("img//le.006.jpg",0)
lx=[]
for x in range(0,1080):
    ly=[]
    for y in range(0,1920):
        color=a[x][y]
        if color<25:
            ly.append(i1)
        else:    
            if 26<color<51:
                ly.append(i2)                
            else:              
                if 52<color<76:
                    ly.append(i3)                    
                else:                  
                    if 77<color<102:
                        ly.append(i4)                        
                    else:                      
                        if 103<color<128:
                            ly.append(i5)                            
                        else:                      
                            if 129<color<154:
                                ly.append(i6) 
                            else:
                                if 155<color<180:
                                    ly.append(i7) 
                                else:
                                    if 181<color<206:
                                        ly.append(i8)                                        
                                    else:    
                                        if 207<color<232:
                                            ly.append(i9)                                            
                                        else:
                                            ly.append(i10)                                            
            

       
    lx.append(ly)
aaa = np.array(lx)


cv2.imwrite("res//6.jpg",aaa)
