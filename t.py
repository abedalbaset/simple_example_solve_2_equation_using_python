from numpy import *
from scipy.optimize import *
def f(z):
	x=z[0]
	y=z[1]
	f=empty((2))
	f[0]=2*x+3*y-8
	f[1]=x+y-3
	return f

z=fsolve(f,[1,1])
print(z)
	
