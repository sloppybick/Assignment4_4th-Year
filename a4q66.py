import pulp

# Create the model
model = pulp.LpProblem(name="Factory_Warehouse_Transportation", sense=pulp.LpMinimize)

# Define sets
factories = ["F1", "F2", "F3"]
warehouses = ["W1", "W2", "W3"]

# Supply capacity for each factory
supply = {
    "F1": 200,
    "F2": 160,
    "F3": 90
}

# Demand at each warehouse
demand = {
    "W1": 180,
    "W2": 120,
    "W3": 150
}

# Shipping costs from factories to warehouses
costs = {
    ("F1", "W1"): 16, ("F1", "W2"): 20, ("F1", "W3"): 12,
    ("F2", "W1"): 14, ("F2", "W2"): 8,  ("F2", "W3"): 18,
    ("F3", "W1"): 26, ("F3", "W2"): 24, ("F3", "W3"): 16
}

# Decision variables - how many units to ship from each factory to each warehouse
shipments = {}
for f in factories:
    for w in warehouses:
        shipments[(f, w)] = pulp.LpVariable(name=f"{f}_to_{w}", lowBound=0, cat=pulp.LpInteger)

# Objective function: minimize total shipping cost
model += pulp.lpSum(shipments[(f, w)] * costs[(f, w)] for f in factories for w in warehouses)

# Constraint 1: Supply constraint - can't ship more than each factory's capacity
for f in factories:
    model += pulp.lpSum(shipments[(f, w)] for w in warehouses) <= supply[f], f"Supply_constraint_{f}"

# Constraint 2: Demand constraint - each warehouse's demand must be met
for w in warehouses:
    model += pulp.lpSum(shipments[(f, w)] for f in factories) >= demand[w], f"Demand_constraint_{w}"

# Solve the model
model.solve()

# Print the status of the solution
print(f"Status: {pulp.LpStatus[model.status]}")

# Display the optimal solution
print("\nOptimal shipping plan:")
for f in factories:
    for w in warehouses:
        if shipments[(f, w)].value() > 0:
            print(f"Ship {int(shipments[(f, w)].value())} units from {f} to {w}")

# Calculate the total shipping cost
total_cost = pulp.value(model.objective)
print(f"\nTotal shipping cost: {int(total_cost)} BDT")

# Print the optimal solution in a more structured format
print("\nOptimal Solution Table:")
print("-" * 50)
print(f"{'From/To':<10} | {'W1':<10} | {'W2':<10} | {'W3':<10} | {'Total':<10}")
print("-" * 50)
for f in factories:
    row = f"{f:<10} | "
    row_total = 0
    for w in warehouses:
        units = int(shipments[(f, w)].value())
        row += f"{units:<10} | "
        row_total += units
    row += f"{row_total:<10}"
    print(row)
print("-" * 50)
print(f"{'Demand':<10} | {'180':<10} | {'120':<10} | {'150':<10} | {sum(demand.values()):<10}")
print("-" * 50)

# Check if the problem is balanced
total_supply = sum(supply.values())
total_demand = sum(demand.values())
print(f"\nTotal Supply: {total_supply}")
print(f"Total Demand: {total_demand}")
if total_supply == total_demand:
    print("The problem is balanced.")
else:
    print(f"The problem is unbalanced with excess supply of {total_supply - total_demand} units.")