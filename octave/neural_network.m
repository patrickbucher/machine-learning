% train.csv contains data about male athletes. Columns:
% 1) height in meters
% 2) weight in kilograms
% 3) sport as label
%   0: Cycling
%   1: Swiss Wrestling
%   2: Alpine Skiing
%   3: Sumo Wrestling
%   4: Long-Distance Running
data = csvread('train.csv');
X = data(:,[1,2]);
Y = data(:,3);

% normalize input data
X(:,1) = (X(:,1) - mean(X(:,1))) / std(X(:,1));
X(:,2) = (X(:,2) - mean(X(:,2))) / std(X(:,2));

% dimension information
m = length(X);
n = length(unique(Y));

% one-hot encode labels
y = zeros(m, n)
for i = 1:(max(Y)+1)
    y(:,i) = (Y == (i-1));
end

X
y
