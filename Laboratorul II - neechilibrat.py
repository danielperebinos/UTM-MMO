from pulp import *

magazine = ["M1", "M2", "M3", "M4", "M5", "M6"]
supply = {"M1": 40, "M2": 50, "M3": 60, "M4": 30, "M5": 50, "M6": 40}

centre = ["C1", "C2", "C3", "C4", "C5", "Dummy"]
demand = {"C1": 40, "C2": 50, "C3": 60, "C4": 30, "C5": 50, "Dummy": 40}

costs = [
    [50, 40, 60, 30, 50, 100],
    [60, 50, 60, 30, 50, 100],
    [55, 40, 60, 30, 50, 100],
    [70, 40, 60, 30, 50, 100],
    [40, 40, 60, 30, 50, 100],
    [40, 40, 60, 30, 40, 100],
]

costs = makeDict([magazine, centre], costs, 0)
prob = LpProblem("Magazin Distribution Problem", LpMinimize)
Routes = [(w, b) for w in magazine for b in centre]
vars = LpVariable.dicts("Route", (magazine, centre), 0, None, LpInteger)
prob += (
    lpSum([vars[w][b] * costs[w][b] for (w, b) in Routes]),
    "Sum_of_Transporting_Costs",
)
for w in magazine:
    prob += (
        lpSum([vars[w][b] for b in centre]) <= supply[w],
        f"Sum_of_Products_out_of_Magazine_{w}",
    )

# The demand minimum constraints are added to prob for each demand node (bar)
for b in centre:
    prob += (
        lpSum([vars[w][b] for w in magazine]) >= demand[b],
        f"Sum_of_Products_into_Centre{b}",
    )

print(prob)
print(prob.solve())
