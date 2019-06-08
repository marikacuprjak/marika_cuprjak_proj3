# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:14:25 2019

@author: XX
"""

import numpy as np
import sys
import matplotlib.pyplot as plt
from math import *

def dlugosc(fia,fib,lama,lamb):
    fiA=fia*pi/180
    fiB=fib*pi/180
    lamA=lama*pi/180
    lamB=lamb*pi/180
    a= 6378137
    e2=0.00669438002290

    b=a*sqrt(1-e2)
    f=1-(b/a);
    dell=lamB-lamA;
    UA=atan((1-f)*tan(fiA));
    UB=atan((1-f)*tan(fiB));
    L1=dell
    w=(0.000001/3600)*pi/180
    L=0
    while abs(L-L1)>w:
        L=L1
        sinsig=sqrt((cos(UB)*sin(L1))**2+(cos(UA)*sin(UB)-sin(UA)*cos(UB)*cos(L1))**2);
        cossig= sin(UA)*sin(UB)+cos(UA)*cos(UB)*cos(L1);
        sig=atan2(sinsig,cossig);
        sina=(cos(UA)*cos(UB)*sin(L1))/(sinsig); 
        cos2a=1-(sina)**2;
        cos2sigm=cossig-((2*sin(UA)*sin(UB))/cos2a);
        C=(f/16)*cos2a*(4+f*(4-3*cos2a));
        L1=dell+(1-C)*f*sina*(sig+C*sinsig*(cos2sigm+C*cossig*(-1+2*(cos2sigm)**2)));
    u2=(a**2-b**2)*cos2a/(b**2)
    A=1+(u2/16384)*(4096+u2*(-768+u2*(320-175*u2)));
    B=(u2/1024)*(256+u2*(-128+u2*(74-47*u2)));
    delt=B*sinsig*(cos2sigm+(1/4)*B*(cossig*(-1+2*(cos2sigm)**2)-(1/6)*B*cos2sigm*(-3+4*(sin(sig))**2)*(-3+4*(cos2sigm)**2)));
    s=b*A*(sig-delt)*0.001
    return(s)

