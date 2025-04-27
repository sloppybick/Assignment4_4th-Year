import pulp

# Create the optimization model (maximizing profit)
model = pulp.LpProblem(name="Salesman_Assignment", sense=pulp.LpMaximize)

# Define sets
salesmen = ["A", "B", "C", "D"]
cities = ["1", "2", "3", "4"]

# Profit per day for each salesman in each city
profit = {
    ("A", "1"): 16, ("A", "2"): 10, ("A", "3"): 14, ("A", "4"): 11,
    ("B", "1"): 14, ("B", "2"): 11, ("B", "3"): 15, ("B", "4"): 15,
    ("C", "1"): 15, ("C", "2"): 15, ("C", "3"): 13, ("C", "4"): 12,
    ("D", "1"): 13, ("D", "2"): 12, ("D", "3"): 14, ("D", "4"): 15
}

# Decision variables - binary variables indicating if salesman i is assigned to city j
assignment = {}
for s in salesmen:
    for c in cities:
        assignment[(s, c)] = pulp.LpVariable(name=f"{s}_{c}", cat=pulp.LpBinary)
        

# Objective function: maximize total profit
model += pulp.lpSum(assignment[(s, c)] * profit[(s, c)] for s in salesmen for c in cities)

# Constraint 1: Each salesman must be assigned to exactly one city
for s in salesmen:
    model += pulp.lpSum(assignment[(s, c)] for c in cities) == 1, f"Salesman_{s}_constraint"

# Constraint 2: Each city must have exactly one salesman
for c in cities:
    model += pulp.lpSum(assignment[(s, c)] for s in salesmen) == 1, f"City_{c}_constraint"  

# Solve the model
model.solve()

# Print the status of the solution
print(f"Status: {pulp.LpStatus[model.status]}")

# Display the optimal assignments
print("\nOptimal Assignments:")
for s in salesmen:
    for c in cities:
        if pulp.value(assignment[(s, c)]) == 1:
            print(f"Salesman {s} is assigned to City {c} with profit {profit[(s, c)]} BDT per day")

# Calculate the total profit
total_profit = pulp.value(model.objective)
print(f"\nMaximum Total Profit: {total_profit} BDT per day")

# Create a more readable assignment table
print("\nAssignment Table:")
print("-" * 50)
print(f"{'Salesman':<10} | {'City':<10} | {'Profit (BDT)':<15}")
print("-" * 50)
for s in salesmen:
    for c in cities:
        if pulp.value(assignment[(s, c)]) == 1:
            print(f"{s:<10} | {c:<10} | {profit[(s, c)]:<15}")
print("-" * 50)

# Display the complete profit matrix for reference
print("\nProfit Matrix (BDT per day):")
print("-" * 50)
print(f"{'Salesman|City':<12} | {'1':<4} | {'2':<4} | {'3':<4} | {'4':<4}")
print("-" * 50)
for s in salesmen:
    row = f"{s:<12} | "
    for c in cities:
        row += f"{profit[(s, c)]:<4} | "
    print(row[:-2])
print("-" * 50)

# Create a visual representation of the assignment
print("\nAssignment Summary:")
print("-" * 40)
city_header = "  | " + " | ".join(f"City {c}" for c in cities)
print(city_header)
print("-" * 40)
for s in salesmen:
    row = f"S {s} | "
    for c in cities:
        if pulp.value(assignment[(s, c)]) == 1:
            row += f"  X   | "
        else:
            row += f"      | "
    print(row[:-2])
print("-" * 40)