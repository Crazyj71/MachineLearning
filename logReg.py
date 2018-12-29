#Author: Jamie Wyatt
#Date: 9/30/2018
#Project 3 : MACHINE LEARNING
#LOGISTIC REGRESSION PROGRAM

from math import exp

vectorUpdates = 0

def hypothesis(X, W):
	h = W[0]
	d = len(X)-1
	for i in range(d):
		h += W[i + 1] * X[i]
		
	return 1.0 / (1.0 + exp(-h))

def logistic_reg(dataset, learnRate, loop_total):
	W = [0.0 for i in range(len(dataset[0]))] #INITITAL CHOICE OF WEIGHTS
	noChangeInError = 0
	for increment in range(loop_total):
		errorTotal = 0.0
		prevErrorTotal = 0.0
		for X in dataset:
			global vectorUpdates
			vectorUpdates += 1 #Update Weights
			h = hypothesis(X, W)
			d = len(X)-1
			y = X[1] #0 or 1
			error = (y - h)
			prevErrorTotal = errorTotal
			errorTotal += error**2
			derivativeH = h * (1.0 - h)
			W[0] = W[0] + learnRate * error * derivativeH
			for i in range(d):
				W[i + 1] = W[i + 1] + learnRate * error * derivativeH* X[i]
		if(int(errorTotal*100) == int(prevErrorTotal*100)):
			noChangeInError += 1
		else:
			noChangeInError = 0
		if (noChangeInError == 20):
			return W
		
	return W


dataset = [[1.0, 0],[2.0,1],[3.0,0],[4.0,1],[5.0,0],[6.0,1],[7.0,1],[8.0,1]]
learnRate = 0.3 #LEARNING RATE CONSTANT
loop_total = 1000
 
W = logistic_reg(dataset, learnRate, loop_total)
print("W's: " + str(W))
print("Vector Updates: " + str(vectorUpdates))
