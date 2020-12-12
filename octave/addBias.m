function Xbias = addBias(X)
    [rows, cols] = size(X);
    Xbias = ones(rows, cols+1);
    Xbias(:,2:cols+1) = X;
end
