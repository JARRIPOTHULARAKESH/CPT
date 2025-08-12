# from sklearn.linear_model import Lasso
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error
# from sklearn.datasets import make_regression
# import numpy as np

# np.random.seed(42)
# x,y=make_regression(n_samples=100, n_features=10, noise=10.0,random_state=42)
# x_train,y_train,x_test,y_test= train_test_split(x,y,test_size=0.2, random_state=42)
# lasso= Lasso(alpha=1.0)
# lasso.fit(x_train, y_train)
# y_pred= lasso.predict(x_test)
# print("Lasso Regression Coefficients:", lasso.coef_)
# print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import make_regression
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(42)

# Generate sample regression data
X, y = make_regression(n_samples=100, n_features=10, noise=15, random_state=42)

# Split into train & test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Lasso regression
lasso = Lasso(alpha=1.0)
lasso.fit(X_train, y_train)

# Predictions
y_pred = lasso.predict(X_test)

# Results
print("Lasso Regression Coefficients:", lasso.coef_)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Extract first two features for visualization
x1_test = X_test[:, 0]
x2_test = X_test[:, 1]

# 3D Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter actual vs predicted
ax.scatter(x1_test, x2_test, y_test, color='blue', label='Actual', alpha=0.8)
ax.scatter(x1_test, x2_test, y_pred, color='red', label='Predicted', alpha=0.8)

# Create a grid for surface
x1_range = np.linspace(x1_test.min(), x1_test.max(), 100)
x2_range = np.linspace(x2_test.min(), x2_test.max(), 100)
x1_grid, x2_grid = np.meshgrid(x1_range, x2_range)

# Fill remaining features with mean values
x_grid = np.zeros((x1_grid.size, X.shape[1]))
x_grid[:, 0] = x1_grid.ravel()
x_grid[:, 1] = x2_grid.ravel()
for i in range(2, X.shape[1]):
    x_grid[:, i] = np.mean(X_test[:, i])

# Predict for the grid
y_grid = lasso.predict(x_grid).reshape(x1_grid.shape)

# Plot surface
ax.plot_surface(x1_grid, x2_grid, y_grid, color='yellow', alpha=0.5)

# Labels and title
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Target Variable')
ax.set_title('Lasso Regression 3D Visualization')
plt.legend()
plt.show()
