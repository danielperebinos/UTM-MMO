import numpy as np

companies = ['bonavb', 'eolub', 'itab', 'pon1v', 'vestum', 'vplayb']
returns = np.array([0.409860946, -0.302287824, 0.381664788, 0.020280762, 0.287166327, -0.702481474])
volatilities = np.array([0.430209592, 0.386689635, 0.558804066, 0.280308637, 0.490779029, 0.853379184])
allocation = np.array([0.4, 0.05, 0.24478677, 0.05, 0.20521323, 0.05])

covariance_matrix = np.array([
    [0.000734446, 0.00017455, 0.000170913, 3.35193E-05, 8.6087E-05, 0.000214568],
    [0.00017455, 0.000593369, 0.00012239, 4.26269E-05, 0.0001369, 0.0002366],
    [0.000170913, 0.00012239, 0.001239135, 2.55376E-05, 0.000126702, 0.000243974],
    [3.35193E-05, 4.26269E-05, 2.55376E-05, 0.000311797, - 1.88751E-05, - 3.9626E-05],
    [8.6087E-05, 0.0001369, 0.000126702, - 1.88751E-05, 0.00095581, 0.00030034],
    [0.000214568, 0.0002366, 0.000243974, - 3.9626E-05, 0.00030034, 0.002889905],
])

risk_free = 0.03

portfolio_expected_return = np.dot(allocation, returns)
portfolio_risk = np.sqrt(np.dot(np.dot(allocation, covariance_matrix), allocation.T) * 252)
sharpe_index = (portfolio_expected_return - risk_free) / portfolio_risk

print("Expected Portfolio Return:", round(portfolio_expected_return * 100, 3), "%")
print("Portfolio Risk (Standard Deviation):", round(portfolio_risk * 100, 3), "%")
print("Sharpe Ratio of the Portfolio:", round(sharpe_index, 3))
