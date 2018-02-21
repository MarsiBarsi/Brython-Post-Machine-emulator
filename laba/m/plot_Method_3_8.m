function [] = plot_Method_3_8(x_low, x_high, Tolerance)

n = 2;
m = 1;

h = (x_high - x_low)/n;
Integral_previous = 0;

Vector_x = [];
Vector_y = [];

while (1)
  S = 0;
  for k = 1:1:m
    x = x_low + 2*(k - 1)*h;
    S = S + f(x) + 4*f(x + h) + f(x + 2*h);
    Vector_x = [Vector_x, x];
    Vector_y = [Vector_y, f(x)];
  end
Integral = S*h/3;
  if (abs(Integral - Integral_previous) < Tolerance)
    break;
  else
  m = n;
  n = n*2;
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
end
