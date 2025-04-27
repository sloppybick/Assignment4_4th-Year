import numpy as np
import scipy as sp
from scipy.optimize import linprog

print("""Min Z = 4x₁ + 3x₂
Subject to these constraints:

Vitamins: 200x1 + 100x2 ≥ 4000
Minerals: 1x1 + 2x2 ≥ 50
Calories: 40x1 + 40x2 ≥ 1400
Non-negativity: x1 ≥ 0, x2 ≥ 0""")
c=np.array([4,3])
#converting signs of >= to<=
A_ub=np.array([[-200,-100],[-1,-2],[-40,-40]])
b_ub=np.array([-4000,-50,-1400])
bounds=((0,None),(0,None))

result=linprog(c,A_ub,b_ub,bounds=bounds,method='highs')

x1=result.x[0]
x2=result.x[1]
obj=result.fun

print(f'\nfood A: {x1}')
print(f'\nfood B: {x2}')
print(f'\nMinimumCost: {obj}')

vitamins_scipy = 200 * result.x[0] + 100 * result.x[1]
minerals_scipy = result.x[0] + 2 * result.x[1]
calories_scipy = 40 * result.x[0] + 40 * result.x[1]

print("\nConstraints Check:")
print(f"Vitamins: {vitamins_scipy:.2f} >= 4000")
print(f"Minerals: {minerals_scipy:.2f} >= 50")
print(f"Calories: {calories_scipy:.2f} >= 1400")
