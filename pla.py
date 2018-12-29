from itertools import product
import random

dataset = []

for x in range(1, 26, 1):
	tempset = [random.randint(50,100), random.randint(0,50), -1]
	dataset.append(tempset)
	tempset = [random.randint(0,49), random.randint(50,100), 1]
	dataset.append(tempset)


for x in range(0,50,1):
	print("Point " + str(x) + ": \t(" +  str(dataset[x][0]) + ",\t " + str(dataset[x][1]) + ")")

c=.2
k=.2
w0 = random.randint(-10,10)
w1 = random.randint(-10,10)
w2 = random.randint(-10,10)

loopcount = 0
loop_bound = 10000

while(loopcount < loop_bound):
	loopcount = loopcount + 1
	for x in range(0,50,1):
		d = dataset[x][2]
		D = w0 + w1*dataset[x][0] + w2*dataset[x][1]
		if D < 0:
			D = -1
		else: 
			D = 1
		if D > d or D < d:
			w0 = w0 + c*d*k
			w1 = w1 + c*d*dataset[x][0]
			w2 = w2 + c*d*dataset[x][1]

total = 50
error = 0
for x in range(0,50,1):
	D = w0 + w1*dataset[x][0] + w2*dataset[x][1]
	if D<0:
		D=-1
	else:
		D=1
	d = dataset[x][2]
	if D > d or D < d:
		error = error + 1

print("")
PercentError = float(error)/float(total)
print("Percent Error: " + str(PercentError) + "%")
print("Soln: W0= " + str(w0) + " W1= " + str(w1) + " W2= " + str(w2))
print("y=" + str(-w1/w2) + "x + " + str(-w0/w2))

############################################################################################2nd Part

try:
	next = raw_input("Press enter to continue...")

except SyntaxError:
	next = ""

dataset = []

for x in range(1, 26, 1):
	tempset = [random.randint(0,100), random.randint(0,100), -1]
	dataset.append(tempset)
	tempset = [random.randint(0,100), random.randint(0,100), 1]
	dataset.append(tempset)

for x in range(0,50,1):
	print("Point " + str(x) + ": \t(" +  str(dataset[x][0]) + ",\t " + str(dataset[x][1]) + ")  " + str(dataset[x][2]))

c=.2
k=.2
w0 = random.randint(-10,10)
w1 = random.randint(-10,10)
w2 = random.randint(-10,10)

loopcount = 0
loop_bound = 10000

while(loopcount < loop_bound):
	loopcount = loopcount + 1
	for x in range(0,50,1):
		d = dataset[x][2]
		D = w0 + w1*dataset[x][0] + w2*dataset[x][1]
		if D < 0:
			D = -1
		else:
			D = 1
		if D > d or D < d:
			w0 = w0 + c*d*k
			w1 = w1 + c*d*dataset[x][0]
			w2 = w2 + c*d*dataset[x][1]

total = 50
error = 0
for x in range(0,50,1):
	D = w0 + w1*dataset[x][0] + w2*dataset[x][1]
	d = dataset[x][2]
	if D<0:
		D=-1
	else:
		D=1
	if D > d or D < d:
		error = error + 1

print("")
PercentError = (float(error)/float(total))*100.0
print("Percent Error: " + str(PercentError) + "%")
print("Soln: W0= " + str(w0) + " W1= " + str(w1) + " W2= " + str(w2))
print("y=" + str(-w1/w2) + "x + " + str(-w0/w2))

