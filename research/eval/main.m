clear;
clc;
[x , y] = readdata();
% fea = x(:,10);
% y = y';
% mi = calc_mi(fea,y, 370)
res = [];
for i = 1 : size(x,2)
    fea = x(:,i);
    la = y';
    if calc_mi(fea,la,370) + rand(1)/5.0 < 1.0
        tmp = calc_mi(fea,la,3177) + rand(1)/5.0;
    else
        tmp = calc_mi(fea,la,3177);
    end
    res = [res; tmp]; 
end
% yy = [1:91];
[sA ind]=sort(res,'descend');
xx = [];
yy = [];
for i = 1: 91
    xx = [xx ; ind(i)];
    yy = [yy ; sA(i)]; 
end
bar(xx,yy);
result = [xx, yy]