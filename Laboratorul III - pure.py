import numpy as np

matrix = np.array([
    [50, 55, 60, 65],
    [40, 45, 50, 55],
    [30, 35, 40, 45],
    [20, 25, 30, 35],
])

row_min_values = np.min(matrix, axis=1)
maxmin = np.max(row_min_values)
strategy_p1 = np.argmax(row_min_values) + 1

col_max_values = np.max(matrix, axis=0)
minimax = np.min(col_max_values)
strategy_p2 = np.argmin(col_max_values) + 1

print("Matricea de câștiguri:")
print(matrix)

print("\n--- Strategia Firmei Alpha ---")
print(f"Minim pe rânduri: {row_min_values}")
print(f"Maxmin: {maxmin}")
print(f"Strategia optimă Alpha: S{strategy_p1}")

print("\n--- Strategia Firmei Beta ---")
print(f"Maxim pe coloane: {col_max_values}")
print(f"Minimax: {minimax}")
print(f"Strategia optimă Beta: S{strategy_p2}")
