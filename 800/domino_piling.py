#PROBLEM - Return how many 2x1 domino pieces can fit perfectly into a board of M x N squares.


m,n = map(int, input().split())

m_n_parameter = m*n

max_dominos = m_n_parameter // 2

print(max_dominos)