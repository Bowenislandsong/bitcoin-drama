%% multiple transactions occrences

o = 2;
p = 0.95;
q = 0.05;
ni = 5;


% prob(ni,1,q,o,0)

figure(1)
g = []
for p = 0.4:0.05:1
g = [g,prob(ni,p,q,o,1)]
end
plot(0.4:0.05:1,g,'LineWidth',4)
xlabel("Probability of L's True Positive")
ylabel("Probability")
set(gca,'FontSize', 42);


o = 2;
p = 0.95;
ni = 5;

figure(2)
h = []
for q = 0:0.05:0.5
h = [h,prob(ni,p,q,o,1)]
end
plot(0:0.05:0.5,h,'LineWidth',4)
set(gca,'FontSize', 42);
xlabel("Probability of L's False Positive")
ylabel("Probability")

o = 2;
p = 0.95;
q = 0.05;

figure(3)
h = []
for ni = 2:10
h = [h,prob(ni,p,q,o,1)]
end
plot(2:10,h,'LineWidth',4)
set(gca,'FontSize', 42);
% title("Average Number of Transactions in Each Observation")
xlabel("Avg. # of Trans. in Each Observation")
ylabel("Probability")


o = 2;
p = 0.95;
q = 0.05;
ni = 5;

figure(4)
h = []
for ctp = 0:0.05:0.9
h = [h,prob(ni,p,q,o,ctp)]
end
plot(0:0.05:0.9,h,'LineWidth',4)
% title("Percentage of |C_T| Over |C|")
set(gca,'FontSize', 42);
xlabel("Ratio of |C_T| Over |C|")
ylabel("Probability")







function res = prob(ni,p,q,o,ctp)

n = (ni^o);
% q = (q^(o-1));
if ctp == 1
    ct = 0;
else
    ct = floor(ctp*n);
end

cf = n-1-ct;

res = 0;
for k = 1:n
    res1 = 0;
    if ct>0
        for i = max([0,k-1-cf]):min([ct,k-1])
            res1 = res1+nchoosek(ct,i)*p^i*(1-p)^(ct-i)*nchoosek(cf,k-1-i)*q^(k-1-i)*(1-q)^(cf+i-k+1);
        end
    else
        res1 = nchoosek(cf,k-1)*q^(k-1)*(1-q)^(cf-k+1);
    end
        
    res = res + res1/k;
end

res = res*p;

end
