#!/usr/bin/env python
# coding: utf-8

# In[20]:


import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


# In[27]:


def main():
    # Solicitar la función y el valor de traslación en el eje s al usuario
    expresion_str = input('Ingrese la función f(t): exp(a*s) ')
    expresion = sp.sympify(expresion_str)  # Convertir la cadena en una expresión simbólica
    a = float(input('¿Cuál es el desplazamiento de la función?: '))

    # Definir las variables simbólicas
    s, t = sp.symbols('s t')

    # Calcular la transformada de Laplace de la función original
    Ls_original = sp.laplace_transform(expresion, t, s)

    # Aplicar el desplazamiento en el dominio de Laplace
    Ls_desplazada = Ls_original[0].subs(s, s - a)

    print('La función desplazada en el dominio de Laplace es:')
    print(Ls_desplazada)

    # Convertir las expresiones simbólicas a funciones manejables
    F_original = sp.lambdify(t, expresion, 'numpy')
    F_desplazada = sp.lambdify(s, Ls_desplazada, 'numpy')

    # Evaluar las funciones en un rango de valores
    t_values = np.linspace(-10, 10, 400)
    expresion_values = F_original(t_values)
    s_values = np.linspace(-10, 10, 400)
    F_desplazada_values = F_desplazada(s_values + a)  # Agregar el desplazamiento a los valores de s

    # Obtener la función desplazada en el dominio del tiempo
    f_t_desplazada = sp.inverse_laplace_transform(Ls_desplazada, s, t)

    # Convertir la expresión simbólica a una función manejable
    F_t_desplazada = sp.lambdify(t, f_t_desplazada, 'numpy')
    f_t_desplazada_values = F_t_desplazada(t_values)

    # Graficar las funciones
    plt.figure(figsize=(12, 6))

    plt.plot(t_values, expresion_values, label='Función ingresada')
    plt.plot(t_values, f_t_desplazada_values, label='Desplazada (Transformada inversa de Laplace)', color='black')
    plt.ylim(-10, 10)
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.legend()
    plt.title('traslacion eje S')
    plt.grid(True)

    plt.tight_layout()
    plt.show()


# In[28]:


main()


# In[ ]:





# In[ ]:




