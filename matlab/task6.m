function [] = task6 ()
t = -log(2):0.1:0;
z = 2 + t*0;
alpha = -pi:0.1:pi+0.1;
x = (cos(alpha)')*z;
y = (sin(alpha)')*z;
t = kron(ones(length(alpha), 1), t);
 
mesh(x,y,t)
q1 = pi*quad(@myf, -log(2),0);
 
hold on
 
t = -log(2):0.1:0;
z = exp(-t);
alpha = -pi:0.1:pi+0.1;
x = (cos(alpha)')*z;
y = (sin(alpha)')*z;
t = kron(ones(length(alpha), 1), t);
 
mesh(x,y,t)
q2 = pi*quad(@myf2, -log(2),0);
disp(q1-q2)

t = 0:0.1:2;
z = 0 + t*0;
alpha = -pi:0.1:pi+0.1;
x = (cos(alpha)')*z;
y = (sin(alpha)')*z;
t = kron(ones(length(alpha), 1), t);
 
mesh(x,y,t)
end
 

function[x]=myf();
x = (2).^2;
end
 
function[y] = myf2(x)
y = (exp(-x)).^2;
end
