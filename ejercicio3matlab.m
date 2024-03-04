syms t s tau

% Definir la función a integrar
f = exp(t) * sin(tau);

% Calcular la transformada de Laplace de e^t
laplace_exp = laplace(exp(t), t, s);

% Definir la transformada de Laplace de sin(tau)
laplace_sin_tau = laplace(sin(tau), tau, s);

% Calcular la convolución de las transformadas de Laplace
convolution = laplace_exp * laplace_sin_tau;

% Mostrar el resultado
disp("La transformada de Laplace de la integral de 0 a t de (e^t * sen(tau) dtau) es:");
disp(convolution);
