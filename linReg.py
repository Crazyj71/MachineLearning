#Author: Jamie Wyatt
#Date: 9/24/2018
#PROJECT 2 : MACHINE LEARNING

X = [1.0,2.0,3.0,4.0,5.0,10.0,11.0,12.0,13.0]
Y = [0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0]
E = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

Sum_X = 0.0
Sum_Y = 0.0
Sum_Squares_X = 0.0

for i in range(0,len(X),1):
    Sum_X = Sum_X + X[i]
    Sum_Y = Sum_Y + Y[i]

Mean_X = Sum_X/len(X)
Mean_Y = Sum_Y/len(Y)

Sum_of_Products = 0;
for i in range(0,len(X),1):
    Sum_of_Products = Sum_of_Products + (X[i]-Mean_X)*(Y[i]-Mean_Y)
    E[i] = (Mean_X-X[i])**2
    Sum_Squares_X = Sum_Squares_X + E[i]

b = Sum_of_Products/Sum_Squares_X
a = Mean_Y - (b*Mean_X)



print("a=" + str(a))
print("b=" + str(b))
print("Sum of X=" + str(Sum_X))
print("Sum of Y=" + str(Sum_Y))
print("Mean of X=" + str(Mean_X))
print("Mean of Y=" + str(Mean_Y))
print("Sum Squares X=" + str(Sum_Squares_X))
print("Sum Products X=" + str(Sum_of_Products))
print("Equation: y=" + str(b) + "x + " + str(a))
