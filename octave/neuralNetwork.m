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
y = zeros(m, n);
for i = 1:(max(Y)+1)
    y(:,i) = (Y == (i-1));
end

% neural network: L=3, K=5
% input   hidden  output
%         (+1)
%         (a2_1)    (  )
% (+1)    (a2_2)    (  )
% (x1)    (a2_3)    (  )
% (x2)    (a2_4)    (  )
%         (a2_5)    (  )
%         (a2_6)

% input -> hidden: 3 inputs, 6 outputs; symmetric
Theta1 = rand(6, 3);
Theta1 = Theta1 * 2 - 1;

% hidden -> output: 7 inputs, 5 outputs; symmetric
Theta2 = rand(5, 7);
Theta2 = Theta2 * 2 - 1;

% first activation: input with bias unit
a1 = addBias(X);

% second activation: hidden layer
z2 = a1 * Theta1';
a2 = sigmoid(z2);

a2bias = addBias(a2);
z3 = a2bias * Theta2';
a3 = sigmoid(z3);

% delta3: difference of last activation to labels
delta3 = a3 - y;

% delta2: back propagation, discard delta for bias unit
delta2 = delta3 * Theta2 .* a2bias .* (1 - a2bias);
delta2 = delta2(:,2:size(delta2)(2));

% no delta for input -> no d1

% capital Deltas
Delta2 = a2' * delta3;
Delta3 = a1' * delta2;

D2 = zeros(size(Delta2));
D3 = zeros(size(Delta3));

[rows, cols] = size(Delta3);
for i = 1:rows
    for j = 1:cols
        % no regularization
        D3(i,j) = (1/m) .* Delta3(i,j);
    end
end
D3

% TODO: implement gradient checking
