import numpy as np

def north_west_corner(supply,demand,costs):
    #allocation = [[0 for _ in range(len(demand))] for _ in range(len(supply))]
    allocation=np.zeros((4,5))
    total_cost=0
    i,j=0,0
    while i<len(supply) and j<len(demand):
        quantity=min(supply[i],demand[j])
        allocation[i][j]=quantity
        total_cost += quantity*costs[i,j]

        supply[i] -= quantity
        demand[j] -= quantity

        if supply[i]==0: #move down
           i +=1
        else: #move right
           j +=1 

    return allocation,total_cost


def least_cost_maethod(supply,demand,costs):
    allocation=np.zeros((4,5))
    #allocation = [[0 for _ in range(len(demand))] for _ in range(len(supply))]
    total_cost=0
    
    while True:
        min_cost=float('inf')
        min_i,min_j=-1,-1

        for i in range(len(supply)):
            for j in range(len(demand)):
                if supply[i]>0 and demand[j]>0 and costs[i][j]<min_cost:
                    min_cost=costs[i][j]
                    min_i,min_j=i,j
        
        if min_i==-1:
          break
        quantity=min(supply[min_i],demand[min_j])
        allocation[min_i][min_j]=quantity
        total_cost += quantity*costs[min_i][min_j]

        supply[min_i] -= quantity
        demand[min_j] -= quantity
    return allocation,total_cost                
costs=np.array([[4,3,1,2,6],[5,2,3,4,5],[3,5,6,3,2],[2,4,4,5,3]])

supply=np.array([80,60,40,20])
demand=np.array([60,60,30,40,10])

print("North-West Corner Rule:")
nw_supply=supply.copy()
nw_demand=demand.copy()
nw_allocation,nw_cost=north_west_corner(nw_supply,nw_demand,costs)
for row in nw_allocation:
    print(row)
print(f"Total Cost: {nw_cost}\n")

print("Least Cost Method:")
lc_supply=supply.copy()
lc_demand=demand.copy()
lc_allocation,lc_cost=least_cost_maethod(lc_supply,lc_demand,costs)

for row in lc_allocation:
    print(row)
print(f"Total Cost: {lc_cost}\n")


if nw_cost>lc_cost:
    print('Least Cost Method is more effective')