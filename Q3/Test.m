clearvars
clc
f = @(x) x.^5-6*x.^4+5;
n=10^(5);
root=0;
v=0:.1:10;
xroot=0:length(v)-1;
for j=1:length(v)-1
a=v(j);
b=v(j+1);
[x,e,root,xroot]=Unknown(f,a,b,n,root,xroot);
disp('--------------------')
disp(a) 
disp('      to')
disp(' ')
disp(b)
x
e
end
disp('--------------------')
root
disp('--------------------')
c=xroot;
xroot=1:root;
for t=1:root
   xroot(t)=c(t);
end
for t=1:root
   x=xroot(t)
end
fileroot = fopen('example.txt', 'w');
fprintf(fileroot,'%10.5f',root,xroot);
fclose(fileroot);