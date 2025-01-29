from pulp import *

fabrics = ["F1", "F2", "F3", "F4", "F5"]
supply = {"F1": 800, "F2": 1000, "F3": 700, "F4": 800, "F5": 400}

deposits = ["D1", "D2", "D3", "D4", "D5", "D6"]
demand = {"D1": 500, "D2": 700, "D3": 600, "D4": 800, "D5": 600, "D6": 500}

costs = [
    [8, 6, 10, 9, 7, 8],
    [9, 7, 8, 5, 6, 9],
    [7, 9, 11, 8, 6, 10],
    [6, 8, 9, 7, 5, 3],
    [5, 7, 8, 6, 4, 2],
]

costs = makeDict([fabrics, deposits], costs, 0)
prob = LpProblem("Fabric Distribution Problem", LpMinimize)
Routes = [(w, b) for w in fabrics for b in deposits]
vars = LpVariable.dicts("Route", (fabrics, deposits), 0, None, LpInteger)
prob += (
    lpSum([vars[w][b] * costs[w][b] for (w, b) in Routes]),
    "Sum_of_Transporting_Costs",
)
for w in fabrics:
    prob += (
        lpSum([vars[w][b] for b in deposits]) <= supply[w],
        f"Sum_of_Products_out_of_Fabric_{w}",
    )

# The demand minimum constraints are added to prob for each demand node (bar)
for b in deposits:
    prob += (
        lpSum([vars[w][b] for w in fabrics]) >= demand[b],
        f"Sum_of_Products_into_Deposit{b}",
    )

print(prob)
print(prob.solve())
