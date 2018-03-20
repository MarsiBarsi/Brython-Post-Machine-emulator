function [] = task4 ()
t = 0:0.1:((2.^(1./2))./2); 
z = 2.*asin(t);

alpha = -pi:0.1:pi+0.1;
x = (cos(alpha)').*z;
y = (sin(alpha)').*z;
t = kron(ones(length(alpha), 1), t);

mesh(x,y,t)
q1 = pi*quad('y = (2.*asin(x)).^2',0,((2.^(1./2))./2))

hold on

t = ((2.^(1./2))./2):0.1:1;
z = 2.*acos(t);

alpha = -pi:0.1:pi+0.1;
x = (cos(alpha)').*z;
y = (sin(alpha)').*z;
t = kron(ones(length(alpha), 1), t);

mesh(x,y,t)
q2 = pi*quad('y = (2.*acos(x)).^2',((2.^(1./2))./2),1)
disp(q1+q2)
endfunction