function [] = plot_trap_m (x_low, x_high, Tolerance)

n = 2;
h = (x_high - x_low)/n;

Iteration_stop_flag = false;
Integral_previous = 0;

Vx=[];
Vy=[];

while (Iteration_stop_flag != true)
  S = (f(x_low) + f(x_high))/2;
  for k=1:1:n-1
    x = x_low + k*h;
    S = S + f(x);
    Vx=[Vx,x];
         Vy=[Vy,f(x)];
         hold on;
  end
  Integral = S*h;
  if (abs(Integral-Integral_previous) < Tolerance)
  else
    n = n*2;
    h = h/2;
    Integral_previous = Integral;
    Iteration_stop_flag = true;
    Vx=[];
    Vy=[];
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

    picture(x_low,x_high,10);
    xlabel('X axis')
    ylabel('Y axis')
    hold on
endfunction

% draw
  function [] = picture(x_low,x_high,n)
      h = (x_high - x_low)./n;
      x = x_low;
      Px=[];
      Py=[];
      Vx=[];
      Vy=[];
      Vx=[Vx,x];
      Vy=[Vy,f(x)];
      for i=1:n
          i=i+1;
          Px=[x x];
          Py=[0 f(x)];
          x = x+h;
          Vx=[Vx,x];
          Vy=[Vy,f(x)];
          plot(Px,Py,'r',Vx,Vy,'r');
      end
   end
