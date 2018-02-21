function [] = plot_Left_r(x_low, x_high, Tolerance)
n = 2;
h = (x_high - x_low )/n;
Iteration_stop_flag = false;
Integral_previous = 0;
Vector_x = [];
Vector_y = [];
while (Iteration_stop_flag != true)
  S=0;
  for k=1:1:n
    x = x_low + (k-1)*h;
    S = S + f(x);
    Vector_x = [Vector_x, x];
    Vector_y = [Vector_y, f(x)];
  end
  Integral = S*h;
  if (abs(Integral - Integral_previous) < Tolerance)
    Iteration_stop_flag = true;
  else
    n = n *2;
    h = h/2;
    Integral_previous = Integral;
    Vector_x = [];
    Vector_y = [];
  end
end
 % out:
  fprintf("\n Final integral: %d \n", Integral);
  fprintf(" value of n: %d \n", n);
  fprintf(" Step amount: %d \n", h);
   % graph:
  a = [pi/3:0.05:pi/2];
  plot(a, f(a), 'r')
  legend('f(x)=1./(3+cos(x))')
  xlabel('X axis')
  ylabel('Y axis')
  hold on
  bar(Vector_x, Vector_y, 'y')
endfunction
