function [] = plot_Method_Sympson (a, b, m)
n=2*m;
h=(b-a)/n;
s=0;
for k=1:1:m
x1=a+2*h*(k-1);
x2=x1+h;
x3=a+2*h*k;
f_x1=f(x1);
f_x2=f(x2);
f_x3=f(x3);
p=polyfit([x1 x2 x3], [f_x1 f_x2 f_x3],2);
t=polyval (p,x1:abs(x3-x1)/40:x3);
hold on;
plot (x1:abs(x3-x1)/40:x3,t,'r');
plot([x1 x1], [0 f_x1], 'b');
plot([x3 x3], [0 f_x3], 'b');
legend('f(x)=2sin(2x)')
title("Sympsons' Method")
xlabel('X axis')
ylabel('Y axis')
s=s+h/3*(f_x1+4*f_x2+f_x3);
end
