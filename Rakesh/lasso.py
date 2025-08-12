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

np.random.seed(42)

# Generate sample regression data
X, y = make_regression(n_samples=100, n_features=10, noise=10.0, random_state=42)

# Correct unpacking order
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit Lasso model
lasso = Lasso(alpha=1.0)
lasso.fit(X_train, y_train)

# Predictions
y_pred = lasso.predict(X_test)

# Results
print("Lasso Regression Coefficients:", lasso.coef_)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
