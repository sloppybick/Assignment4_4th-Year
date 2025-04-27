import numpy as np
import scipy as sp
# Define the constraints
# 1. Total coal constraint: x₁ + x₂ + x₃ ≤ 100
# 2. Ash constraint: 3x₁ + 2x₂ + 5x₃ ≤ 3(x₁ + x₂ + x₃)
#    This simplifies to: 0x₁ - 1x₂ + 2x₃ ≤ 0 or x₂ ≥ 2x₃
# 3. Phosphorous constraint: 0.02x₁ + 0.04x₂ + 0.03x₃ ≤ 0.03(x₁ + x₂ + x₃)
#    This simplifies to: -0.01x1 + 0.01x2 + 0x3 ≤ 0 or x1 ≥ x2
# 4. Non-negativity constraints: x1,x2,x3>=0
A_ub = [
    [1, 1, 1],     # Total coal constraint
    [0, -1, 2],    # Ash constraint (rearranged as: -x₂ + 2x₃ ≤ 0)
    [-1, 1, 0]     # Phosphorous constraint (rearranged as: -x₁ + x₂ ≤ 0)
]
b_ub = [100, 0, 0]
c1 = [-12, -15, -14]
x1_bounds = (0, None)
x2_bounds = (0, None)
x3_bounds = (0, None)


from scipy.optimize import linprog
res = linprog(c1, A_ub=A_ub, b_ub=b_ub,  bounds=(x1_bounds, x2_bounds,x3_bounds), method='simplex', options={"disp": True})
x1=res.x[0]
x2=res.x[1]
x3=res.x[2]
Obj=-res.fun
print(f'x1: {x1}\nx2: {x2}\nx3: {x3}')
print(f'Objective function value:{Obj}')

print(f'Maximum Profit: {Obj}')