function [] = square_volume1()
  % пример 4 oy
t = 0:0.1:4;
z = sqrt(t);
alpha = -pi:0.1:pi+0.1;
x = (cos(alpha)')*z;
y = (sin(alpha)')*z;
t = kron(ones(length(alpha), 1), t);
 
mesh(x,y,t)
q1 = 2.*pi.*quad(@final1, 0, 4);
 
hold on
axis equal
disp(q1);
endfunction

function[y]=final1(x)
y = sqrt(x).*sqrt(1+(1./(2.*sqrt(x))).^2);
end
