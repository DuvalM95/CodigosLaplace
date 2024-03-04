import sympy as sp

# Definir símbolos y funciones
t, s, tau = sp.symbols('t s tau')
f = sp.exp(t) * sp.sin(tau)

# Calcular la transformada de Laplace de e^t
laplace_exp = sp.laplace_transform(sp.exp(t), t, s)[0]

# Calcular la transformada de Laplace de sin(tau)
laplace_sin_tau = sp.laplace_transform(sp.sin(tau), tau, s)[0]

# Calcular la convolución de las transformadas de Laplace
convolution = laplace_exp * laplace_sin_tau

# Mostrar el resultado
print("La transformada de Laplace de la integral de 0 a t de (e^t * sen(tau) dtau) es:")
print(convolution)

input("Presiona Enter para salir...")