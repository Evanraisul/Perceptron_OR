### Author: Md. Raisul Islam Evan
### MBSTU CSE



import numpy as np
import matplotlib.pyplot as plt

w=np.round(np.random.rand(3)*10,1)
print("Random value: ",w)
w1=w[0]
w2=w[1]
bias=w[2]
input=np.array([[0,0],[0,1],[1,0],[1,1]])
print("Input: \n",input)

plt.plot([1,.1],[.1,1])
plt.plot([0,0,1,1],[0,1,0,1],'o')
plt.show()

targetOutput=input[:,0] | input[:,1]
print("Target output:\n",targetOutput)
#step function
def step(n):
    if n>=0:
        return 1
    return 0
error=np.array([0,0,0,1])

e=np.sum(error)
maxIteration=100
t=0
learningRate=.8
value=[[w1,w2,bias]]

while(t<maxIteration and e!=0):
    for i in range(len(input)):
        actualOutput=step(np.dot(np.array([w1,w2]),input[i])+bias)
        err=targetOutput[i]-actualOutput
        error[i]=abs(err)   
        w1=round(w1+learningRate*err*input[i][0],1)
        w2=round(w2+learningRate*err*input[i][1],1)
        bias=round(bias+learningRate*err,1)
        value.append([w1,w2,bias])
    e=np.sum(error)
    t+=1

print(value)
print("Iteration: ",t)
print(error)
