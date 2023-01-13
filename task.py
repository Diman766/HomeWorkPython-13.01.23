import sympy as sp


x = sp.Symbol('x')
expr = sp.sin(x)**2 - sp.cos(x)**2
print(expr)


expr_solve = sp.solve(expr)
print(expr_solve)


expr_diff = sp.diff(expr)
print(expr_diff)


graph = sp.plot(expr)


rise_exp = sp.solve(expr_diff > 0)
print(rise_exp)


fall_exp = sp.solve(expr_diff < 0)
print(fall_exp)


peak_exp = sp.solve(expr_diff)
print(peak_exp)


peak_exp_origin = sp.solve(expr > 0)
print(peak_exp_origin)


fall_exp_origin = sp.solve(expr < 0)
print(fall_exp_origin)
