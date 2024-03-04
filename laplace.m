syms t s k;

% Definir la función t * sin(kt)
f_t = t * sin(k*t);

% Calcular la transformada de Laplace de f(t)
F_s = laplace(f_t, t, s);

disp('La transformada de Laplace de t * sin(kt) es:');
disp(F_s);
