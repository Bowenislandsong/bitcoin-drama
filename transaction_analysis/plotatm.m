clear
close all

tw = load('trend_width.mat');
ttw = timetable(datetime(tw.x),tw.y');
ttw = retime(ttw,'daily','fillwithconstant');
ttw = retime(ttw,'weekly','mean');

td = load('trend_dep.mat');
ttd = timetable(datetime(td.x),td.y');
ttd = retime(ttd,'daily','fillwithconstant');
ttd = retime(ttd,'weekly','mean');

figure(1)

plot(ttw.Time,ttw.Var1,'DisplayName','Withdraw','LineWidth',2)
hold on
plot(ttd.Time,ttd.Var1,'DisplayName','Deposit','LineWidth',2)
title("ATM Weekly Average Daily Usage")
legend('location',"NorthWest")
set(gca,'FontSize',36);
ylabel('Transactions')

todw = load('timeofday_width.mat');
todd = load('timeofday_dep.mat');
figure(2)
b=bar(todw.x,[normalize(double(todw.y),'norm',1);normalize(double(todd.y),'norm',1)]);
% hold on
% bar(todd.x,normalize(double(todd.y),'norm',1),'DisplayName','Deposit','FaceAlpha',0.6)
legend('location',"NorthWest")
set(b,{'DisplayName'},{'Withdraw',"Deposit"}')
set(gca,'FontSize',36);
xlabel("Hour of Day (Los Angeles Time)")
title("Normalized Daily Transaction Distribution")

intrerw = load('interval_width.mat');
intrerd = load('interval_dep.mat');
figure(3)
xx = [5,10,20,40,60,120,4*60,8*60,16*60,inf];
% histogram(intrerw.x/60,48,'Normalization','probability')
h = bar([normalize(sum(xx>intrerw.x'),'norm',1);normalize(sum(xx>intrerd.x'),'norm',1)]');
legend
set(h,{'DisplayName'},{'Withdraw',"Deposit"}')
set(gca,'xticklabel',{'5min','10min','20min','40min','1hr','2hr','4hr','8hr','16hr','24hr+'}')
set(gca,'FontSize',36);
title("CDF of ATM Transaction Intervals")
