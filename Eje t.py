#!/usr/bin/env python
# coding: utf-8

# ## eje t

# In[30]:


import sympy as sp
import matplotlib.pyplot as plt
import numpy as np


# In[48]:


def main():
    # Solicitar la función y el valor de traslación en el eje t al usuario
    f_t_str = input('Ingrese la función f(t): ')
    f_t = sp.sympify(f_t_str)  # Convertir la cadena en una expresión simbólica
    b = float(input('Ingrese el valor de traslación en el eje t: '))

    # Definir las variables simbólicas
    s, t = sp.symbols('s t')

    # Realizar la traslación en el eje t
    f_t_desplazada = sp.Heaviside(t - b) * f_t.subs(t, t - b)

    # Calcular la transformada de Laplace de la función original y la desplazada
    F_s = sp.laplace_transform(f_t, t, s)
    F_s_desplazada = sp.laplace_transform(f_t_desplazada, t, s)

    # Convertir las expresiones simbólicas a funciones manejables
    F_original = sp.lambdify(s, F_s[0], 'numpy')
    F_desplazada = sp.lambdify(t, f_t_desplazada, 'numpy')

    # Evaluar la función original en un rango de valores de t
    t_values = np.linspace(-10, 10, 400)
    f_t_values = sp.lambdify(t, f_t, 'numpy')(t_values)

    # Evaluar las transformadas de Laplace en un rango de valores de s
    s_values = np.linspace(-10, 10, 400)
    F_original_values = F_original(s_values)
    F_desplazada_values = F_desplazada(t_values)

    # Graficar las transformadas de Laplace y la función desplazada
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 2)
    plt.plot(t_values, f_t_values, label='Función f(t)', linestyle='--', color='black')
    plt.plot(t_values, F_desplazada_values, label='Función desplazada f(t)', color='blue')  # Función desplazada
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.title('Función desplazada f(t)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

    print('La función desplazada en el dominio de Laplace es:')
    print(F_s_desplazada[0])


# In[49]:



    main()


# In[ ]:




