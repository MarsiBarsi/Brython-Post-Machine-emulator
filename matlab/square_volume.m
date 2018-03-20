function [] = square_volume()
t = 0:0.1:2*pi;
z = t - sin(t);
alpha = -pi:0.1:pi+0.1;
x = (cos(alpha)')*z;
y = (sin(alpha)')*z;
t = kron(ones(length(alpha), 1), t);
 
mesh(x,y,t)

hold on
axis equal

t = 0:0.1:2*pi;
z = 1 - cos(t);
alpha = -pi:0.1:pi+0.1;
x = (cos(alpha)')*z;
y = (sin(alpha)')*z;
t = kron(ones(length(alpha), 1), t);
 
mesh(x,y,t)

q = 2.*pi.*quad('y = (x-sin(x)).*sqrt((1-cos(x)).^2 + (sin(x)).^2)', 0, 2*pi);
disp(q);
draw
endfunction

function[y]=pr1(x)
y = (1-cos(x)).^2;
end
function[y]=pr2(x)
y = (sin(x)).^2;
end
function[y]=final(x)
y = (@pr1+@pr2).^(1./2);
end
function[y] = final1(x)
y = (x-sin(x)).*@final;
end
function[]=draw()
figure
t = 0:0.1:2*pi;
z = t - sin(t);
plot(t, z, 'b')
hold on
t = 0:0.1:2*pi;
z = 1 - cos(t);
plot(t,z,'r')
end