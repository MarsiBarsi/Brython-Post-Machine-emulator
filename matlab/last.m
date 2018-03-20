function [res] = last ()
f = @(x) x.^(3./2);
pr = @(x) sqrt(1 + ((3./2)*sqrt(x)).^2);
res = (quad(pr, 0, 1));

x=0:0.01:3;
y = f(x);

plot(x,y);
axis equal

 
endfunction
