#Author: Jamie Wyatt
#Date: 11/30/2018
#PROJECT 5 : MACHINE LEARNING

import random
from math import exp
from operator import sub
import numpy as np

random.seed(50000)

X = []
Y = []

def f(x):
    return ((x*x) + 10)

def GetData():
    for i in range(0,12,1):
        X.append(random.uniform(-2,10))
        Y.append(f(X[i]))
        print(str(X[i]) + "\t" + str(Y[i]))

def RidgeReg(X_Data, Y_Data, Lambda):
    SampleSize = len(X_Data)
    X = np.array(X_Data)
    W0 = np.ones(len(X))
    X = np.column_stack((W0,X))
    Xt = np.transpose(X)
    Y = np.array(Y_Data)
    Yt = np.transpose(Y)
    LambdaIdentity = Lambda * np.identity(2)
    Wreg = np.linalg.inv(np.dot(Xt, X) + LambdaIdentity)
    h_lambda = np.dot(np.dot(X,Wreg), Xt)
    y_reg = np.dot(X.transpose(), Y)
    w = np.dot(Wreg,y_reg)
    return w

def CrossV(X,Y, Lambda):
    Ecv = 0
    counter =0
    print("Cross Val using " + str(Lambda));
    for i in range(0,9,4):
        counter += 1
        ecv =0
        Ein = 0
        TrainSetX = []
        TrainSetY = []
        if(i==8):
            TrainSetY = Y[:i]
            TrainSetX = X[:i]
            TestSetX= X[i:]
            TestSetY= Y[i:]
        if(i==4):
            TrainSetY = Y[:i]
            TrainSetX = X[:i]
            TrainSetX.extend(X[i+4:])
            TrainSetY.extend(Y[i+4:])
            TestSetX = X[i:i+4]
            TestSetY = X[i:i+4]
        if(i==0):
            TrainSetX = X[i+4:]
            TrainSetY = Y[i+4:]
            TestSetX= X[:i+4]
            TestSetY= Y[:i+4]
            
        wTrain = RidgeReg(TrainSetX, TrainSetY, Lambda)
        #wTest = RidgeReg(TestSetX, TestSetY, Lambda)
        for j in range(len(TestSetX)):
            yHat = wTrain[0] + wTrain[1]*TestSetX[j]
            ecv += (yHat - TestSetY[j])**2
        ecv = ecv / len(TestSetX)
        Ecv += ecv
        for j in range(len(X)):
            yHat = wTrain[0] + wTrain[1]*X[j]
            Ein += (yHat - Y[j])**2
        Ein = Ein / len(X)
        print("\tEin (D-"+ str(counter) + ") :" + str(Ein))
    Ecv = Ecv / 3
    print("\tEcv: " + str(Ecv))
        
print("Dataset:")
GetData()
print("")
h = RidgeReg(X,Y,0)
print("RESULTS:")
print("a=\t\t\t" + str(h[1]))
print("b=\t\t\t" + str(h[0]))
print("Lin Reg Equation: \ty=" + str(h[1]) + "x + " + str(h[0]))

CrossV(X,Y,.1)
CrossV(X,Y,1)
CrossV(X,Y,10)
CrossV(X,Y,100)

#ABOVE WAS RAN AND LAMBDA=100 was found to be the lowest ECV
print("\nChose 100 for Lambda")
EinFinal = 0
wFinal = RidgeReg(X, Y, 100)
print("Ridge Reg Equation: \ty=" + str(wFinal[1]) + "x + " + str(wFinal[0]))

for j in range(len(X)):
    yHat = wFinal[0] + wFinal[1]*X[j]
    EinFinal += (yHat - Y[j])**2
EinFinal = EinFinal / len(X)
print("Final Ein: " + str(EinFinal))


