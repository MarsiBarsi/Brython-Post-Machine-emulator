function [] = Monte_Karlo (a,b,n)
test_x=a:1/1000:b;
test_y=f(test_x);

x=a+(b-a).*rand(n,1);

min_v=min(f(a:1/n:b));
max_v=max(f(a:1/n:b));

y=min_v+(max_v-min_v).*rand(n,1);

S=(b-a)/n;
counter=0;

hold on;
grid on;
plot (test_x, test_y,'k');

for i=1:1:n
  if (y(i)<f(x(i)))
    if (f(x(i))>0)
      if (y(i)>0)
      plot (x(i),y(i),'*g');
      else
      plot (x(i),y(i),'*r');
      end
      else plot (x(i),y(i),'*r');
    end
      counter=counter+1;

      else
      if f(x(i)<0)
        if (y(i)<0)
         plot (x(i),y(i),'*g');
        else
         plot (x(i),y(i),'*r');
        end
      else
       plot (x(i),y(i),'*r');
      end
  end
end
Fn=S*counter/n;
sum=0;
for i=1:1:n
sum=sum+f(x(i));
end

  Fn2=sum*(b-a)*n;
  % final out
  fprintf("\n Final Integral: %d\n",Fn2*10.^(-6));
  fprintf(" point amount: %d \n", n);
  legend('f(x)=1./(3+cos(x))')

  xlabel('X axis')
  ylabel('Y axis')
endfunction
