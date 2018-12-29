#Author: Jamie Wyatt
#Date: 11/21/2018
#Project 4 : MACHINE LEARNING
#Page 75, Question 2.24

import random
from math import exp

#GLOBALS
gBar = [0,0] #[slope,y-intercept]
Bias = 0
Variance = 0
Eout = 0
A = []
B = []


def hypothesis(Dataset):
    #y=slopeX+b
    slope = (Dataset[1][1]-Dataset[0][1])/(Dataset[1][0]-Dataset[0][0])
    b = (-Dataset[0][0])*slope + Dataset[0][1]
    h = [slope, b]
    return h

def getGbar():
    random.seed(1)
    global gBar
    global A
    global B
    sampleSize = 10000
    for i in range(0,sampleSize,1):
        x1 = random.uniform(-1,1)
        x2 = random.uniform(-1,1)
        y1 = x1*x1
        y2 = x2*x2      
        Dataset = [[x1,y1],[x2,y2]]
        h = hypothesis(Dataset)         #g(D)x(i)
        gBar[0] += h[0]
        gBar[1] += h[1]
        A.append(h[0])
        B.append(h[1])
    gBar[0] = gBar[0] / sampleSize
    gBar[1] = gBar[1] / sampleSize
    
def CalculateError():
    random.seed(1)
    global Bias
    global Variance
    global Eout
    global A
    global B
    sampleSize = 10000
    for i in range(0,sampleSize,1):
        x = random.uniform(-1,1)
        fX = x*x
        gBarOfX = gBar[0]*x + gBar[1]                       #average function from all functions
        gDX = (A[i]*x + B[i])                               #specific hypothesis for one given X within distribution (-1 to 1)
        Eout += (((gDX - gBarOfX)**2) + ((gBarOfX-fX)**2))  #Total Error
        Variance += (gDX - gBarOfX)**2                      #Squared error of current hypothesis minus mean hypothesis
        Bias += (gBarOfX-fX)**2                             #Squared error of mean hypothesis minus target function
    Variance = Variance / sampleSize
    Bias = Bias / sampleSize
    Eout = Eout / sampleSize
    
getGbar()
CalculateError()
print("y= " + str(gBar[0]) + "x + " + str(gBar[1]))
print("Variance= " + str(Variance))
print("Bias= " + str(Bias))
print("Eout= " + str(Eout))
