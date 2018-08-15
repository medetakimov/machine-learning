U = np.random.randn(M, K) / K
V = np.random.randn(K, N) / K
B = np.zeros(M)
C = np.zeros(N)

for t in xrange(T):

  # update B
  for i in xrange(M):
  if i in ratings_by_i:
    accum = 0
    for j, r in ratings_by_i[i]:
      accum += (r - U[i,:].dot(V[:,j]) - C[j] - mu)
    B[i] = accum / (1 + reg) / len(ratings_by_i[i])

  # update U
  for i in xrange(M):
    if i in ratings_by_i:
      matrix = np.zeros((K, K)) + reg*np.eye(K)
      vector = np.zeros(K)
      for j, r in ratings_by_i[i]:
        matrix += np.outer(V[:,j], V[:,j])
        vector += (r - B[i] - C[j] - mu)*V[:,j]
      U[i,:] = np.linalg.solve(matrix, vector)

  # update C
  for j in xrange(N):
    if j in ratings_by_j:
      accum = 0
      for i, r in ratings_by_j[j]:
        accum += (r - U[i,:].dot(V[:,j]) - B[i] - mu)
      C[j] = accum / (1 + reg) / len(ratings_by_j[j])

  # update V
  for j in xrange(N):
    if j in ratings_by_j:
      matrix = np.zeros((K, K)) + reg*np.eye(K)
      vector = np.zeros(K)
      for i, r in ratings_by_j[j]:
        matrix += np.outer(U[i,:], U[i,:])
        vector += (r - B[i] - C[j] - mu)*U[i,:]
      V[:,j] = np.linalg.solve(matrix, vector)
