clc;
clear; 
syms s t;
expresion = input('Ingrese la función f(t): exp(a*s)');
Ls = laplace(expresion, t, s);
a = input('¿Cuál es el desplazamiento de la función?: ');

respuesta = subs(Ls, s, s - a);

disp('La función desplazada en el dominio de Laplace es:');
disp(respuesta);

% Convertir las expresiones simbólicas a funciones manejables
figure(1);
F_original = ezplot(expresion,[-10,10]);
hold on;
F_desplazada = ezplot(ilaplace(respuesta),[-10,10]);
ylim([-10, 10]);
xlabel('s');
ylabel('F(s)');
legend('Original', 'Desplazada');
title('Transformada de Laplace');
