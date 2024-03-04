clc;
clear;
syms s t;

% Función original en el dominio del tiempo
f_t = input('Ingrese la función f(t): ');

% Valor de la traslación en el eje t
b = input('Ingrese el valor de traslación en el eje t: ');

% Realizar la traslación en el eje t
f_t_desplazada = heaviside(t - b) * subs(f_t, t, t - b);

disp(f_t_desplazada);

% Calcular la transformada de Laplace de la función original y la desplazada
F_s = laplace(f_t, t, s);
F_s_desplazada = laplace(f_t_desplazada, t, s);

% Convertir las expresiones simbólicas a funciones manejables
figure(1);
F_original = ezplot(f_t,[-10,10]);
hold on;
F_desplazada = ezplot(ilaplace(F_s_desplazada),[-10,10]);
ylim([-10, 10]);
xlabel('s');
ylabel('F(s)');
legend('Original', 'Desplazada');
title('Transformada de Laplace');

% Mostrar la función desplazada
disp('La función desplazada en el dominio de Laplace es:');
disp(F_s_desplazada); 
