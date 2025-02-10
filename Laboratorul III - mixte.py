from pulp import LpMaximize, LpProblem, LpVariable, LpStatus

problem = LpProblem(name="optimizare_preturi", sense=LpMaximize)

Electro = LpVariable(name="Electro", lowBound=0)
Tehno = LpVariable(name="Tehno", lowBound=0)
Rezerva = LpVariable(name="Rezerva", lowBound=0)
Profit = LpVariable(name="Profit", lowBound=0)

problem += Profit, "Maximizarea_Profitului_Mediu_Asteptat"

problem += 10 * Electro + 12 * Tehno + 5 * Rezerva - Profit >= 0, "Rezultatul_1"
problem += 15 * Electro + 18 * Tehno - 10 * Rezerva - Profit >= 0, "Rezultatul_2"
problem += 20 * Electro + 22 * Tehno - 15 * Rezerva - Profit >= 0, "Rezultatul_3"
problem += 1 * Electro + 1 * Tehno + 1 * Rezerva - Profit == 1, "Rezultatul_4"

problem += Electro + Tehno + Rezerva == 1, "Suma_Probabilitatilor"

status = problem.solve()

print(f"Status: {LpStatus[problem.status]}")
print("\nProbabilitățile optime:")
print(f"Electro (Probabilitatea pentru strategia Electro): {Electro.value():.4f}")
print(f"Tehno (Probabilitatea pentru strategia Tehno): {Tehno.value():.4f}")
print(f"Rezerva (Probabilitatea pentru strategia de rezervă): {Rezerva.value():.4f}")
print(f"Profitul mediu așteptat: {Profit.value():.4f}")
print(f"\nProfitul maxim mediu (Profit): {problem.objective.value():.4f}")
