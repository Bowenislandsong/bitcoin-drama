clear
close all

intrerw = load('interval_width.mat');
intrerd = load('interval_dep.mat');

histogram(intrerw.x/60,48,'Normalization','probability')
hold on
histogram(intrerd.x/60,48,'Normalization','probability')
