import numpy as np
from scipy import linalg


set.seed (1)
m = 10000
n =  5000
A = np.random.rand(m,n)

  # Matrix multiply
%timeit B = crossprod(A)
B = A.T.dot(A)



# Cholesky Factorization
%timeit C = linalg.cho_factor(B)
C = linalg.cho_factor(A)

# Singular Value Decomposition
m = 10000
n = 2000
A = np.random.rand(m,n)

%timeit linalg.svd(a=A, compute_uv=False)


# Principal Components Analysis
m = 10000
n = 2000
A = matrix (runif (m*n),m,n)
system.time (P = prcomp(A))

# Linear Discriminant Analysis
library('MASS')
g = 5
k = round (m/2)
A = data.frame (A, fac=sample (LETTERS[1:g],m,replace=TRUE))
train = sample(1:m, k)
system.time (L = lda(fac ~., data=A, prior=rep(1,g)/g, subset=train))







