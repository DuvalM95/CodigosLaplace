% Definición de la función Heaviside
function y = Heaviside(t)
    y = piecewise(t >= 0, 1, 0);
end

% Definición de parámetros
syms L q t s

% Ecuación diferencial en el dominio del tiempo
eqn = 160*L*diff(q, t) + L*diff(q, t, 2) + 104*L*q == 20*L*Heaviside(t);

% Transformada de Laplace de la ecuación
eqn_laplace = laplace(eqn, t, s);

% Resolución para Q(s)
Q_s = solve(eqn_laplace, q);

% Simplificación de la expresión
Q_s = simplify(Q_s);

% Transformada inversa de Laplace para obtener q(t)
q_t = ilaplace(Q_s, s, t);

% Visualización de la solución
disp(['La solución de la ecuación diferencial es:']);
disp(q_t);

% Evaluación de la solución en t = 1
t_eval = 1;
q_eval = subs(q_t, t, t_eval);

% Visualización del valor de la solución en t = 1
disp(['El valor de la solución en t = 1 es:']);
disp(q_eval);
