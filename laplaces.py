import sympy as sp

# Definir variables simbólicas
s, k = sp.symbols('s k')

# Definir la expresión obtenida en Python
expression = (sp.I / (2 * (sp.I * k + s)**2)) - (sp.I / (2 * (-sp.I * k + s)**2))

# Simplificar la expresión
simplified_expression = sp.simplify(expression)

print("La expresión simplificada es:")
print(simplified_expression)



input("Presiona Enter para salir...")
