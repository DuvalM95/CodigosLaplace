syms s t R C; % Definir variables simbólicas

% Valores de los componentes del circuito
R = 100; % Resistencia en ohmios
C = 0.001; % Capacitancia en faradios

% Definir la función de entrada (puedes modificarla según sea necesario)
V_t = 5 * heaviside(t); % Una entrada escalón de 5V

% Resolver la ecuación diferencial para la corriente i(t)
I_s = (5/s) / (R + 1/(s*C));

% Aplicar la transformada inversa de Laplace
i_t = ilaplace(I_s);

disp('La corriente i(t) en función del tiempo es:');
disp(i_t);
