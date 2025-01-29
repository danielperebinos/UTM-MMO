from scipy.optimize import linprog

c = [-500, -300, -150, -100, -80]
A = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0.1, 0.1, 0.1, -0.9, 0.1]
]
b = [1000, 100, 200, 0]
x_bounds = [(0, None) for _ in range(5)]
result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method="simplex")

if result.success:
    print("Soluție optimă găsită:")
    print(f"x1 (VIP): {result.x[0]:.2f} bilete")
    print(f"x2 (Premium): {result.x[1]:.2f} bilete")
    print(f"x3 (Standard): {result.x[2]:.2f} bilete")
    print(f"x4 (Reducere Studenți): {result.x[3]:.2f} bilete")
    print(f"x5 (Acces General): {result.x[4]:.2f} bilete")
    print(f"Venit total maxim: {-result.fun:.2f} RON")
else:
    print("Nu s-a găsit o soluție optimă.")
