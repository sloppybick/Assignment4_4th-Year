import numpy as np
import matplotlib.pyplot as plt
from pulp import *

prob=LpProblem("Minimize Cost",LpMinimize)

x1=LpVariable("x1",0,None,LpContinuous)
x2=LpVariable("x2",0,None,LpContinuous)
x3=LpVariable("x3",0,None,LpContinuous)
x4=LpVariable("x4",0,None,LpContinuous)

prob += 45*x1+40*x2+85*x3+65*x4,"objective"

prob += 3*x1+4*x2+8*x3+6*x4>=800,"c1"
prob += 2*x1+2*x2+7*x3+5*x4>=200,"c2"
prob += 6*x1+4*x2+7*x3+4*x4>=700,"c3"

print('\n The Minimization problem is: ')

print("""
       Min Z: 45x1 + 40x2 + 85x3 + 65x4
       Subject to:
       3x1 + 4x2 + 8x3 + 6x4 >= 800
       2x1 + 2x2 + 7x3 + 5x4 >= 200
       6x1 + 4x2 + 7x3 + 4x4 >= 700
       and x1, x2, x3, x4 >= 0
""")
sol=prob.solve()

#print("Status:",LpStatus[prob.status])

for v in prob.variables():
    print(v.name,"=",v.varValue)

print("\nMinimum Cost= ")
print("BDT",value(prob.objective))

protein = 3*x1.varValue + 4*x2.varValue + 8*x3.varValue + 6*x4.varValue
fat = 2*x1.varValue + 2*x2.varValue + 7*x3.varValue + 5*x4.varValue
carbs = 6*x1.varValue + 4*x2.varValue + 7*x3.varValue + 4*x4.varValue

print("\nNutritional Values: ")
print("\nProtein: ",protein)
print("\nFat: ",fat)
print("\nCarbohydrate: ",carbs)
    





