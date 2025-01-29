from scipy.optimize import linprog

c = [2000, 1200, 2200, 1300, 2500]
A = [
    [-1, -0.5,  0,  0,  0],
    [ 0,  0, -1, -0.5,  0],
    [ 0,  0,  0,  0, -1],
    [ 1,  1,  1,  1,  1],
]
b = [-10, -12, -5, 30]
x_bounds = [(0, None) for _ in range(5)]
result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method="simplex")

if result.success:
    print("Soluție optimă găsită:")
    print(f"x1 (Dimineață, Full-time): {result.x[0]:.2f} angajați")
    print(f"x2 (Dimineață, Part-time): {result.x[1]:.2f} angajați")
    print(f"x3 (După-amiază, Full-time): {result.x[2]:.2f} angajați")
    print(f"x4 (După-amiază, Part-time): {result.x[3]:.2f} angajați")
    print(f"x5 (Noapte, Full-time): {result.x[4]:.2f} angajați")
    print(f"Cost total minim: {result.fun:.2f} RON")
else:
    print("Nu s-a găsit o soluție optimă.")
